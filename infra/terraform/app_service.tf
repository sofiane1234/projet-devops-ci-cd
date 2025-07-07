resource "azurerm_app_service_plan" "app_service_plan" {
  name                = "asp-sosso-devops-ci-cd"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Basic"
    size = "B1"
  }
}
