# 🔵 Blue    = config.yaml     → User-defined inputs (raw config)
# 🟢 Green   = locals.tf       → Decodes YAML and makes values usable in Terraform
# 🔴 Red     = providers.tf    → Initializes the Azure provider
# 🟡 Yellow  = landing-zones.tf     → Creates resources using values from locals

locals {
  vnets = { for k, v in local.config.landing_zones : k => v if local.config.landing_zones[k].virtual_network.address != null } 
  # 🟢 Filters landing zones that have a non-null VNET address and stores them for VNET creation

  subnets = { for k, v in local.config.landing_zones : k => v if local.config.landing_zones[k].virtual_network.subnet.address != null } 
  # 🟢 Filters landing zones that have a non-null subnet address and stores them for subnet creation
}

resource "azurerm_resource_group" "rgs" {
  for_each = local.config.landing_zones  
  # 🟢 Loops through each landing zone defined in 🔵 config.yaml (platform, app_alpha, app_beta)

  name = format("RG-%s-%s-%s", upper(local.config.global.location), local.config.landing_zones[each.key].id, local.config.landing_zones[each.key].sequence_no)
  # 🟢 Builds RG name using 🔵 global.location (uppercased), landing zone ID, and sequence number
  # Example: RG-SWEDENCENTRAL-PLATFORM-1

  location = local.config.global.location  
  # 🟢 Uses region from 🔵 config.yaml → global.location
}

resource "azurerm_log_analytics_workspace" "platform" {
  count = local.config.landing_zones.platform.log_analytics == true ? 1 : 0 
  # 🟢 Creates the workspace only if 🔵 config.yaml → landing_zones.platform.log_analytics is true

  name = format("LAW-%s-%s-%s", upper(local.config.global.location), local.config.landing_zones["platform"].id, local.config.landing_zones["platform"].sequence_no)
  # 🟡 Constructs workspace name using location, ID, and sequence number

  location            = azurerm_resource_group.rgs["platform"].location  
  # 🟡 Gets location from platform RG created above

  resource_group_name = azurerm_resource_group.rgs["platform"].name  
  # 🟡 Assigns workspace to platform RG

  sku               = "PerGB2018"  
  # Defines the pricing tier for the workspace

  retention_in_days = 30  
  # Specifies log retention period
}

# NSG
resource "azurerm_network_security_group" "nsgs" {
  for_each = local.config.landing_zones
  # 🟡 Creates one NSG per landing zone

  name = format("NSG-%s-%s-%s", upper(local.config.global.location), local.config.landing_zones[each.key].id, local.config.landing_zones[each.key].sequence_no)
  # 🟡 Constructs NSG name similarly to RGs

  location            = local.config.global.location   
  # 🟡 Uses shared location

  resource_group_name = azurerm_resource_group.rgs[each.key].name
  # 🟡 Places NSG in corresponding RG
}

# VNET
resource "azurerm_virtual_network" "vnets" {
  for_each = local.vnets
  # 🟡 Only creates VNETs for landing zones with valid address

  name = format("VNET-%s-%s-%s", upper(local.config.global.location), local.vnets[each.key].id, local.vnets[each.key].sequence_no)
  # 🟡 Naming convention for VNETs

  address_space       = [local.vnets[each.key].virtual_network.address]
  # 🟡 Uses address space from config.yaml

  dns_servers         = ["10.0.0.4", "10.0.0.5"]
  # 🟡 Optional static DNS servers

  location            = local.config.global.location
  # 🟡 Sets location for VNET

  resource_group_name = azurerm_resource_group.rgs[each.key].name
  # 🟡 Associates VNET with corresponding RG
}

resource "azurerm_subnet" "subnets" {
  for_each = local.subnets
  # 🟡 Only creates subnets for entries with non-empty subnet address

  name = format("SN-%s-%s-%s", upper(local.config.global.location), local.subnets[each.key].id, local.subnets[each.key].sequence_no)
  # 🟡 Naming pattern for subnets

  virtual_network_name = azurerm_virtual_network.vnets[each.key].name
  # 🟡 Subnet is linked to VNET created above

  address_prefixes     = [local.subnets[each.key].virtual_network.subnet.address]
  # 🟡 Subnet CIDR block from YAML config

  resource_group_name  = azurerm_resource_group.rgs[each.key].name
  # 🟡 Subnet resides in the corresponding RG
}

/*
# enable global peering between the two virtual network
resource "azurerm_virtual_network_peering" "peering" {
  count                        = length(var.location)
  name                         = "peering-to-${element(azurerm_virtual_network.vnet.*.name, 1 - count.index)}"
  resource_group_name          = element(azurerm_resource_group.example.*.name, count.index)
  virtual_network_name         = element(azurerm_virtual_network.vnet.*.name, count.index)
  remote_virtual_network_id    = element(azurerm_virtual_network.vnet.*.id, 1 - count.index)
  allow_virtual_network_access = true
  allow_forwarded_traffic      = true

  # `allow_gateway_transit` must be set to false for vnet Global Peering
  allow_gateway_transit = false
}
*/