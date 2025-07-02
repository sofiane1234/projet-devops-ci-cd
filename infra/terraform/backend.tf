terraform {
  backend "azurerm" {
    resource_group_name  = "rg-sosso-devops-ci-cd"
    storage_account_name = "stdevopssosso"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}
