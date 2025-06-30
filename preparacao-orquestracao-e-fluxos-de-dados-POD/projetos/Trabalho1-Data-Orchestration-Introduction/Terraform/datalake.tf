# Criar um Cointêiner de dados
resource "azurerm_storage_container" "containerdatalake" {
  name                  = "${local.tags["datalake"]}"
  storage_account_name  = azurerm_storage_account.storageaccount_aulas.name
  container_access_type = "blob"
  depends_on = [azurerm_storage_account.storageaccount_aulas]
}
