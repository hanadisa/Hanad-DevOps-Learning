terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.24.0"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = "39a8c69a-5382-4661-92eb-477ede9f2639"
}

