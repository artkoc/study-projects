# 🔵 Blue    = config.yaml     → User-defined inputs (raw config)
# 🟢 Green   = locals.tf       → Decodes YAML and makes values usable in Terraform
# 🔴 Red     = providers.tf    → Initializes the Azure provider
# 🟡 Yellow  = platform.tf     → Creates resources using values from locals

locals {
  config = yamldecode(file("./config.yaml"))       # 🔵 Reads your config.yaml and decodes it to a structured object
  subscription_id = local.config.global.subscription.id   # 🔵 Extracts subscription ID → 🔴 Used by the provider
}
