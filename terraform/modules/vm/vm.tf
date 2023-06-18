resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  size                = "Standard_DS2_v2"
  admin_username      = var.vm_admin_username
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDO2r4UuEpQI1y4jsgPrDlPoV/o97Y+qBzzcEoKcYutsqBiruM6OrKCWpbh1FICRt6V8qWHcGHv0rqai+a72kdOLoDeITBHuy2WrkkfWDjcF1zQC1p/MnFaYL/LTNbkknfrNiEelM6qmnIMkmFVLR4FWQ/gd8a4i7MWCyTEm8hh9d0FOwpliQhAiOhITPww3+GxTRamfGzdATyU56Fq+2QIbFxdqcm3HF6bd3NKihWihDmE1s1N0cG3OlKGvMmMBo9PuUWS2pRIamo/H6kuVRsKdqw5I8CnsfbNUt1MxMebdk2O5LnwtLvVo4KiXRMo4WcKYrXIU0OOkcqLgnBLPXBPJ9p+0zVJ0bTyHXgVTzEYj0F3nUDdwvKnaOa9TS1C0e6KtYSxKCFpS2V/zWAZ/3VKUX6q6CLfOOGnEN9hNqBMEDNOjKp7Lib02Is0yzVy71gIrB590zTO4qmjO842XhBsz/trKKOjWD0W99mKdaBcq8vrER1VdVKJ5SIZEsdzaFVripH92iDmVfVvMsmLlCdAiHSEWumdU8GOva08UfPzNhcgvc555nJW5XVXcbPrAeOwFdOxpZjVtGuh+w0o8rJSYJVlZvlhS1dZFnVZnPeWqr22m2olp65YKffvSB+aPgRx7T1D1LlnTCinu9ZZbGAWPFyH0GhyqrcECLudUXml8w== rujinwong@cc-9a436514-848dd567cc-9rfqz"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
