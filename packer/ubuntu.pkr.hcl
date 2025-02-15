variable "CLIENT_ID" {
  type = string
}
variable "CLIENT_SECRET" {
  type = string
}
variable "SUBSCRIPTION_ID" {
  type = string
}
variable "TENANT_ID" {
  type = string
}
variable "AZURE_DEVOPS_PAT" {
  type = string
}

source "azure-arm" "autogenerated_1" {
  azure_tags = {
    task = "Image deployment"
  }

  client_id       = var.CLIENT_ID
  client_secret   = var.CLIENT_SECRET
  subscription_id = var.SUBSCRIPTION_ID
  tenant_id       = var.TENANT_ID

  image_offer                       = "UbuntuServer"
  image_publisher                   = "Canonical"
  image_sku                         = "18.04-LTS"
  location                          = "East US"
  managed_image_name                = "azuredevops"
  managed_image_resource_group_name = "Azuredevops"
  os_type                           = "Linux"
  vm_size                           = "Standard_DS1_v2"
}

build {
  sources = ["source.azure-arm.autogenerated_1"]

  provisioner "shell" {
    script = "azure-devops.sh"

    environment_vars = [
      "AZURE_DEVOPS_PAT=${var.AZURE_DEVOPS_PAT}"
    ]
  }

}