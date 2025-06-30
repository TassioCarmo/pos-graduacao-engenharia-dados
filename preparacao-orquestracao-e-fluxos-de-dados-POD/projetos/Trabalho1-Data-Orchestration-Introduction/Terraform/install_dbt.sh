#!/bin/bash

# Atualizar os pacotes do sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências
sudo apt install -y python3-pip python3-venv

# Criar um diretório para o projeto DBT
mkdir -p ~/dbt_project
cd ~/dbt_project

# Criar um ambiente virtual Python
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Atualizar o pip no ambiente virtual
pip install --upgrade pip

# Instalar o DBT e o plugin dbt-dremio
pip install dbt-core dbt-spark dbt-databricks

# Verificar a instalação do DBT
dbt --version

# Mensagem final
echo "Instalação concluída. O DBT está pronto para ser utilizado com o Azure Databricks e PySpark."