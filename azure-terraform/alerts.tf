resource "azurerm_monitor_action_group" "costs" {
  name                = "cost-alerts"
  resource_group_name = azurerm_resource_group.rgs["platform"].name
  short_name          = "cost-alerts"

  email_receiver {
    name                    = "sendtoArtiom"
    email_address           = "artiom.kocharov@gmail.com"
    use_common_alert_schema = true
  }

}

resource "azurerm_consumption_budget_subscription" "example" {
  name            = "budget-alert"
  subscription_id = format("/subscriptions/%s",local.config.global.subscription.id)

  amount     = 15
  time_grain = "Monthly"

  time_period {
    start_date = "2025-07-01T00:00:00Z"
    end_date   = "2026-07-01T00:00:00Z"
  }

  notification {
    enabled   = true
    threshold = 90.0
    operator  = "EqualTo"

   contact_groups = [
      azurerm_monitor_action_group.costs.id,
    ]
  }
}

resource "azurerm_cost_anomaly_alert" "costs" {
  name            = "cost-anomaly"
  display_name    = "Alert Costs Anomaly"
  subscription_id = format("/subscriptions/%s",local.config.global.subscription.id)
  email_subject   = "Alert Costs Anomaly"
  email_addresses = ["artiom.kocharov@gmail.com"]
}