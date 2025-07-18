# 🔵 Blue    = config.yaml     → User-defined inputs (raw config)
# 🟢 Green   = locals.tf       → Decodes YAML and makes values usable in Terraform
# 🔴 Red     = providers.tf    → Initializes the Azure provider
# 🟡 Yellow  = platform.tf     → Creates resources using values from locals

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.36.0"                         # Specifies required AzureRM provider version
    }
  }
}

provider "azurerm" {
  features {}                                     # Required block, even if empty
  subscription_id = local.subscription_id        # 🟢 Pulled from locals.tf → 🔵 from config.yaml
}
