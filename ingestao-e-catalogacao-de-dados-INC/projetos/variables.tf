# Arquivo de variáveis de apoio
variable tags {
    default = {
        Aluno = "Tassio Luiz Dantas do Carmo" # Coloque seu nome completo
        Disciplina = "INGESTÃO E CATALOGAÇÃO DE DADOS" # Insira o nome da disciplina
        Matrícula = "1568439" # Coloque o número que aparece no seu e-mail "XXXXXXX@sga.pucminas.br"
        Email = "-----@sga.pucminas.br" # Insira o seu e-mail "XXXXXX@sga.pucminas.br"
        Professor = "Victor Sales Silva" # Nome do professor
    }
}

# LEIA OS COMENTÁRIOS ABAIXO, SÃO IMPORTANTES PARA O DECORRER DAS ATIVIDADES E EVITAR CUSTOS / DIFICULDADES COM AS PRÁTICAS!
# CERTIFIQUE-SE DE QUE O TERRAFORM ESTÁ CONFIGURADO CORRETAMENTE. ABRA O TERMINAL E ACESSE A PASTA COM OS SCRIPTS .tf PARA EXECUTAR OS PASSOS A SEGUIR

# 1. EXECUTE O terraform init
# 2. EXECUTE O terraform (plan > apply)

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
        virtualmachineAirflowDbt = "virtualmachineAirflowDbt${var.tags["Matrícula"]}" # Nome da máquina virtual onde Airflow e DataHub serão configurados (Não modificar o padrão!)
        virtualmachineDremio = "VmLinuxDremio${var.tags["Matrícula"]}" # Nome da máquina virtual onde o Dremio será configurado (Não modificar o padrão!)
        virtualMachineKafka = "VmLinuxKafa${var.tags["Matrícula"]}" # Nome da máquina virtual onde o Kafka será configurado (Não modificar o padrão!)
        instancetype1 = "Standard_E2as_v4" # Tipo de instância com 2 VCPUs e 16 GB de RAM (usada pelo AIRFLOW/DATAHUB e DREMIO)
        instancetype2 = "Standard_D2s_v3" # Tipo de instância com 2 VCPUs e 8 GB de RAM (usada pelo KAFKA)
        ippessoal = "---.--.---.---" # Substitua pelo IP do seu roteador. Utilize o site https://whatismyip.com.br/ para descobrir seu endereço IP (coloque ["XXX.XXX.XXX.XXX", "YYY.YYY.YYY.YYY"] se quiser passar uma lista de IPs)
        nomeusuariovm = "azureuser" # Nome do usuário para conectar-se as máquinas virtuais. Substituir (se quiser) por um nome de seu conhecimento
        senhausuariovm = "Xa1234@54?2" # Senha associada ao usuário para conectar-se as máquinas virtuais. Substituir (se quiser) por uma senha forte (mínimo de 12 dígitos), letras maiúsculas e minúsculas, caracteres especiais e números"
    }
}

# Variável com a instrução para instalar o Docker e Docker Compose em todas as máquinas virtuais
locals {
    install_docker = [
      "sudo usermod -aG sudo ${local.tags["nomeusuariovm"]}",
      "sudo apt-get update -y",
      "sudo apt-get install -y ca-certificates curl gnupg lsb-release",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository -y 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'",
      "sudo apt-get update -y",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin",
      "sudo apt install -y docker-compose",
      "sudo usermod -aG docker ${local.tags["nomeusuariovm"]}",
      "exit"
    ]
}