#!/bin/bash

# Diretório base do usuário
USER_HOME="/home/azureuser"

# Caminho completo para o diretório airflow
AIRFLOW_DIR="$USER_HOME/airflow"

# Pré processamento
if [ -d ~/airflow ]; then
    echo "Removendo diretorio existente airflow..."
    sudo rm -rf ~/airflow
fi

# Criar diretórios necessários com permissões adequadas
sudo mkdir -p ~/airflow/{dags,plugins,logs,scripts,datasets}
sudo chmod -R 777 "$AIRFLOW_DIR"/{dags,plugins,logs,scripts,datasets}

echo "Diretorio Airflow e subpastas criadas com sucesso."

# Concede permissões elevadas
sudo echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env;

# Entrar no diretório airflow
cd "$AIRFLOW_DIR"
echo "Acessando a pasta a seguir: "
echo $AIRFLOW_DIR

# Baixar o docker-compose.yaml do Apache Airflow
sudo curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.3/docker-compose.yaml';
sudo chmod 777 docker-compose.yaml;

# Criar arquivo requirements.txt com as bibliotecas necessárias
sudo touch "$AIRFLOW_DIR/requirements.txt"

# Adicionar bibliotecas ao arquivo requirements.txt
sudo sh -c "echo 'azure-storage-blob' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'pytz' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'faker' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'requests' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'pandas' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'pyspark' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'kafka-python' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'ksql' >> $AIRFLOW_DIR/requirements.txt"
sudo sh -c "echo 'kaggle' >> $AIRFLOW_DIR/requirements.txt"

echo "Arquivo requirements.txt criado com sucesso."

# Modificar o docker-compose.yaml para adicionar volumes scripts e datasets
sudo sed -i '/^  volumes:/a \ \ \ \ \- ${AIRFLOW_PROJ_DIR:-.}\/scripts:\/usr\/local\/airflow\/scripts\n    - ${AIRFLOW_PROJ_DIR:-.}\/datasets:\/usr\/local\/datasets' "$AIRFLOW_DIR/docker-compose.yaml"

echo "Volumes scripts e datasets adicionados ao docker-compose.yaml com sucesso."

# Desabilitar os DAGs de exemplo
sudo sed -i "s/.*AIRFLOW__CORE__LOAD_EXAMPLES.*$/    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'/" docker-compose.yaml
echo "Dags de exemplo desabilitadas no docker-compose.yaml com sucesso."

# Modificar o docker-compose.yaml para utilizar a imagem Docker local
sudo sed -i 's/image: ${AIRFLOW_IMAGE_NAME:-apache\/airflow:2.5.3}/image: ${AIRFLOW_IMAGE_NAME:-airflow-aula:2.5.3}/' docker-compose.yaml
echo "Imagem Docker airflow-aula:2.5.3 configurada no docker-compose.yaml."

# Criar arquivo Dockerfile e adicionar conteúdo
sudo touch "$AIRFLOW_DIR/Dockerfile"
sudo tee "$AIRFLOW_DIR/Dockerfile" >/dev/null <<EOF
FROM apache/airflow:2.5.3

USER root

RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        freetds-dev \\
        libkrb5-dev \\
        libsasl2-dev \\
        libssl-dev \\
        libffi-dev \\
        libpq-dev \\
        build-essential \\
        python3.9 \\
        python3-pip \\
    && apt-get install -y openjdk-11-jdk \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

# Configurar a variável de ambiente JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Definindo a versão do Python a ser usada
ENV PYTHON_VERSION=3.9

USER airflow
WORKDIR /home/airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --upgrade pip
EOF

echo "Arquivo Dockerfile criado com sucesso em $AIRFLOW_DIR."

# Construir a imagem Docker
sudo docker build -t airflow-aula:2.5.3 .

echo "Imagem Docker 'airflow-aula:2.5.3' criada com sucesso."

# Subindo o Apache Airflow
sudo docker-compose up -d;

echo "Servico inicializado com sucesso. Aguarde alguns instantes para conectar-se ao Apache Airflow."

IP_PUBLICO=$(curl -s ifconfig.me/ip | grep -oE '[0-9.]+')

echo "Para acessar, em um navegador WEB de sua preferencia (Microsoft Edge, Google Chrome, Mozilla Firefox e outros), digite http://$IP_PUBLICO:8080"
echo "Na tela de login, insira as credenciais a seguir..."
echo "Usuario: airflow"
echo "Senha: airflow"