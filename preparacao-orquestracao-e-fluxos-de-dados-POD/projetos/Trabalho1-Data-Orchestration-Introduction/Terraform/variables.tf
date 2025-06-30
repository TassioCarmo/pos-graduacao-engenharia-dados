# Arquivo de variáveis de apoio
variable tags {
    default = {
        Aluno = "Tassio Luiz Dantas do Carmo" # Coloque seu nome completo
        Disciplina = "Preparação, Orquestração e Fluxos de Dados" # Insira o nome da disciplina
        Matrícula = "15xx439" # Coloque o número que aparece no seu e-mail "XXXXXXX@sga.pucminas.br"
        Email = "15xx439@sga.pucminas.br" # Insira o seu e-mail "XXXXXX@sga.pucminas.br"
        Professor = "Victor Sales Silva" # Nome do professor
    }
}

# LEIA OS COMENTÁRIOS ABAIXO, SÃO IMPORTANTES PARA O DECORRER DAS ATIVIDADES E EVITAR CUSTOS / DIFICULDADES COM AS PRÁTICAS!
# CERTIFIQUE-SE DE QUE O TERRAFORM ESTÁ CONFIGURADO CORRETAMENTE. ABRA O TERMINAL E ACESSE A PASTA COM OS SCRIPTS .tf PARA EXECUTAR OS PASSOS A SEGUIR

# 1. EXECUTE O terraform init
# 2. DEFINA O VALOR DAS VARIÁVEIS "vm_ip_allocated" = "Static" e "change_ip" = 0 (necessário para o script instalar o Docker)
# 3. EXECUTE O terraform (plan > apply)
# 4. APÓS A CRIAÇÃO DAS MÁQUINAS VIRTUAIS, DEFINA O VALOR DA VARIÁVEL "change_ip" = 1
# 5. EXECUTE O terraform (plan > apply)
# 6. APÓS A EXECUÇÃO DO PASSO 5, ALTERE O VALOR DA VARIÁVEL vm_ip_allocated para "Dynamic" e da variável "change_ip" para 0
# 7. EXECUTE NOVAMENTE O terraform (plan > apply)

# A variável abaixo usa interpolação de valores da variável tags para definir os recursos que serão criados.
locals {
    descripiton = "Nome dos serviços que serão criados na nuvem. Não modificar (estão parametrizados)"
    tags = {
        azureregion = "CanadaCentral" # Região onde os recursos serão criados - Substitua pela região onde as VM's a serem utilizadas em aula são compatíveis!
        resourcegroup = "rg-${var.tags["Matrícula"]}" # Nome do grupo de recursos (Não modificar o padrão!)
        storageaccount = "stgaccount${var.tags["Matrícula"]}" # Nome da conta de armazenamento (Não modificar o padrão!)
        datalake = "datalake-${var.tags["Matrícula"]}" # Nome do datalake (Não modificar o padrão!)
        vnet = "vnet-${var.tags["Matrícula"]}" # Nome da rede virtual (Não modificar o padrão!)
        subnet = "subnet-${var.tags["Matrícula"]}" # Nome da subrede virtual (Não modificar o padrão!)
        securitygroup = "securitygroup-${var.tags["Matrícula"]}" # Nome do grupo de segurança (Não modificar o padrão!)
        vmPrepOrqDados = "vmPrepOrqDados${var.tags["Matrícula"]}" # Nome da máquina virtual onde Airflow e DataHub serão configurados (Não modificar o padrão!)
        instancetype = "Standard_E2as_v4" # Tipo de instância com 2 VCPUs e 16 GB de RAM (usada pelo AIRFLOW/DATAHUB e DREMIO)
        ippessoal = "1xx.33.171.104" # Substitua pelo IP do seu roteador. Utilize o site https://whatismyip.com.br/ para descobrir seu endereço IP (coloque ["XXX.XXX.XXX.XXX", "YYY.YYY.YYY.YYY"] se quiser passar uma lista de IPs)
        nomeusuariovm = "azureuser" # Nome do usuário para conectar-se as máquinas virtuais. Substituir (se quiser) por um nome de seu conhecimento
        senhausuariovm = "Xa1234@54?2" # Senha associada ao usuário para conectar-se as máquinas virtuais. Substituir (se quiser) por uma senha forte (mínimo de 12 dígitos), letras maiúsculas e minúsculas, caracteres especiais e números"
        vm_ip_allocated = "Static" # Mantenha como "Static" e crie as máquinas virtuais. Após executar o terraform apply pela primeira vez e configurar as máquinas, troque o valor para "Dynamic" e execute o terraform novamente
        change_ip = 0 # (Use APENAS 0 ou 1). Modifique o valor dessa variável quando precisar trocar o tipo de alocação de IP (Dinâmico <> Estático)
    }
}

# Variável com a instrução para instalar o Docker e Docker Compose em todas as máquinas virtuais
locals {
    install_resources = [
      "echo 'Configurando os recursos...'",
      "sudo usermod -aG sudo ${local.tags["nomeusuariovm"]}",
      "sudo apt-get update -y",
      "sudo apt-get install -y ca-certificates curl gnupg lsb-release",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository -y 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'",
      "sudo apt-get update -y",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin",
      "sudo apt install -y docker-compose",
      "sudo usermod -aG docker ${local.tags["nomeusuariovm"]}",
      "sudo apt update && sudo apt upgrade -y",
      "sudo apt install -y python3-pip python3-venv",
      "sudo pip install --upgrade pip",
      "echo 'Instalando o DBT e seus conectores...'",
      "sudo pip install dbt-core dbt-spark dbt-databricks",
      "dbt --version",
      "echo 'Instalação concluída. O DBT está pronto para ser utilizado com o Azure Databricks e PySpark.'",
      "echo 'Instalando o PySpark...'",
      "docker pull jupyter/pyspark-notebook",
      "sudo docker network create rede_aula",
      "sudo docker run -p 8888:8888 --network my_network -v /home/${local.tags["nomeusuariovm"]}/",
      "echo 'Instalação concluída. O PySpark foi configurado e está pronto para uso.'",
      "exit"
    ]
}

