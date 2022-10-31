provider "azurerm" {
  tenant_id       = var.tenant_id
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  features {}
}
terraform {
  backend "azurerm" {
    storage_account_name = "tfstate2998947"
    container_name       = "tfstate"
    key                  = "tfstate"
    sas_token            = "?sv=2021-06-08&ss=b&srt=co&sp=rwdlaciytfx&se=2023-10-31T10:58:43Z&st=2022-10-31T02:58:43Z&spr=https&sig=qQzr0O4eJEncKAZ8IcLYZMjD4DGTyenrzzjZyhlbOFI%3D"
  }
}
module "resource_group" {
  source         = "../../modules/resource_group"
  resource_group = var.resource_group
  location       = var.location
}
module "network" {
  source                = "../../modules/network"
  address_space         = var.address_space
  location              = var.location
  virtual_network_name  = var.virtual_network_name
  application_type      = var.application_type
  resource_type         = "NET"
  resource_group        = module.resource_group.resource_group_name
  address_prefixes_test = var.address_prefixes_test
}

module "nsg-test" {
  source              = "../../modules/networksecuritygroup"
  location            = var.location
  application_type    = var.application_type
  resource_type       = "NSG"
  resource_group      = module.resource_group.resource_group_name
  subnet_id           = module.network.subnet_id_test
  address_prefix_test = var.address_prefix_test
}
module "appservice" {
  source           = "../../modules/appservice"
  location         = var.location
  application_type = var.application_type
  resource_type    = "AppService"
  resource_group   = module.resource_group.resource_group_name
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = var.location
  application_type = var.application_type
  resource_type    = "publicip"
  resource_group   = module.resource_group.resource_group_name
}
module "vm" {
  source           = "../../modules/vm"
  location         = var.location
  application_type = var.application_type
  resource_group   = module.resource_group.resource_group_name
  subnet_id        = module.network.subnet_id_test
  vm_public_ip     = module.publicip.vm_public_ip_address_id
}