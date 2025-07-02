data "azurerm_key_vault" "kv" {
  name                = "kv-sosso-devops-ci-cd"
  resource_group_name = "rg-sosso-devops-ci-cd"
}

data "azurerm_key_vault_secret" "postgres_password" {
  name         = "PostgresPassword"
  key_vault_id = data.azurerm_key_vault.kv.id
}

resource "azurerm_postgresql_flexible_server" "pg" {
  name                   = "pg-sosso-devops-ci-cd"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = azurerm_resource_group.rg.location
  version                = "13"
  sku_name               = "GP_Standard_D2s_v3" 
  storage_mb             = 32768
  backup_retention_days  = 7
  administrator_login    = "adminuser"
  administrator_password = data.azurerm_key_vault_secret.postgres_password.value
  zone = "1"
}
