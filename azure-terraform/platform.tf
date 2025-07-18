# 🔵 Blue    = config.yaml     → User-defined inputs (raw config)
# 🟢 Green   = locals.tf       → Decodes YAML and makes values usable in Terraform
# 🔴 Red     = providers.tf    → Initializes the Azure provider
# 🟡 Yellow  = platform.tf     → Creates resources using values from locals

resource "azurerm_resource_group" "rgs" {
  for_each= local.config.landing_zones  # 🟢 Loops through each landing zone defined in 🔵 config.yaml (platform, app_alpha, app_beta)

  name     = format("RG-%s-%s-%s",upper(local.config.global.location),local.config.landing_zones[each.key].id, local.config.landing_zones[each.key].sequence_no)
  # 🟢 Builds RG name using 🔵 global.location (uppercased), landing zone ID, and sequence number
  # Example: RG-SWEDENCENTRAL-PLATFORM-1

  location = local.config.global.location  # 🟢 Uses region from 🔵 config.yaml → global.location
}

resource "azurerm_log_analytics_workspace" "platform" {
  count = local.config.landing_zones.platform.log_analytics == true ? 1 : 0 # 🟢 Creates the workspace only if 🔵 config.yaml → landing_zones.platform.log_analytics is true
  
  name     = format("LAW-%s-%s-%s",upper(local.config.global.location),local.config.landing_zones["platform"].id, local.config.landing_zones["platform"].sequence_no)

  location            = azurerm_resource_group.rgs["platform"].location  # 🟡 Gets location from platform RG created above
  resource_group_name = azurerm_resource_group.rgs["platform"].name  # 🟡 Assigns to the platform RG
  sku                 = "PerGB2018"  # Pricing tier for Log Analytics workspace
  retention_in_days   = 30  # Retains log data for 30 days
}
