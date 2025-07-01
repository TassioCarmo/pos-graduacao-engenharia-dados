##  Arquitetura de Recursos e Serviços em Nuvem

### Camadas da Arquitetura
```
Data Visualization
       ↑
Governança + Consumo
       ↑
    Data Lake
       ↑
Batch + Orquestração ← Streaming
       ↑
      OLTP
```

### Descrição das Camadas
- **OLTP**: Camada de dados transacionais para sistemas e produtos
- **Batch + Orquestração**: Gerencia processos ETL/ELT e agendamento de tarefas
- **Streaming**: Processa dados em tempo real
- **Data Lake**: Armazenamento de objetos em diversos formatos
- **Governança + Consumo**: Acesso padronizado aos dados via SQL
- **Data Visualization**: Ferramentas de visualização e dashboards

## Principais Tecnologias e Ferramentas

### Infraestrutura
- **Máquinas Virtuais Azure**: Computação sob demanda
- **Docker**: Containerização para garantir conformidade
- **Azure Data Lake Storage Gen**: Armazenamento escalável de objetos

### Orquestração e Processamento
- **Apache Airflow**: Orquestração de tarefas (Open-Source)
- **Python**: Linguagem principal para projetos de dados
- **DBT (Data Build Tool)**: Transformação e modelagem de dados

### Análise e Governança
- **Dremio**: Plataforma de unificação e catalogação (Open-Source)
- **SQL**: Linguagem universal para consulta de dados

### Visualização
- **Power BI**: Dashboards interativos da Microsoft
- **Tableau**: Plataforma de análise visual
- **Qlik**: Ferramentas de análise (QlikView e QlikSense)

## Tipos de Dados e Armazenamento

### Classificação dos Dados
- **Estruturados**: Organizados em tabelas (bancos relacionais, planilhas)
- **Semiestruturados**: Com alguma estrutura (XML, JSON)
- **Não estruturados**: Sem estrutura definida (textos, imagens, vídeos, áudio, IoT)

### Estratégia de Organização - Arquitetura Medalhão
- **Bronze (Raw)**: Dados brutos sem tratamento
- **Silver (Staging/Refined)**: Dados em processamento
- **Gold (Consume/Trusted)**: Dados prontos para consumo

##  Recursos Azure Utilizados

### Estrutura Principal
| Recurso | Nome | Quantidade |
|---------|------|------------|
| Conta de Armazenamento | stgaccountXXXXX | 1 |
| Container de Blob | datalake-XXXXXX | 1 |
| Máquinas Virtuais | vmlinuxAirflow, vmlinuxDremio, vmlinuxKafka | 3 |
| Adaptador de Rede | cardinterface-airflow/dremio/kafka | 3 |
| IP Público | ippublico-airflow/dremio/kafka | 3 |
| Disco | discosistema-Airflow/Dremio/Kafka | 3 |
| Grupo de Segurança | securitygroup-XXXXXX | 1 |
| Rede Virtual | vnet-XXXXXX | 1 |

### Tipos de Armazenamento na Conta Azure
- **Contêineres (Blobs)**: Data Lake para qualquer tipo de objeto
- **Compartilhamento de Arquivos**: Protocolos SMB e NFS
- **Filas**: Armazenamento de mensagens
- **Tabelas**: Estrutura NoSQL chave-valor

## Implementação Prática

### Ingestão de Dados com Python
Utilização das bibliotecas:
- `azure-storage-blob`: Manipulação do Azure Storage Blob
- `os`: Interface de sistema

### Estrutura do Projeto
```python
def carrega_arquivo_datalake(diretorio_local, diretorio_datalake, arquivo, container, conexao):
    # Função para upload de arquivos no Data Lake
    
# Configuração
container = 'datalake-XXXXXX'
cadeia_conexao = 'CONNECTION_STRING'
diretorio_datalake = 'bronze'
```

### Datasets Utilizados
- DADOS_ESTUDANTES.json
- DADOS_VOOS.parquet
- DADOS_EXAMES.csv
- DADOS_ALUNOS.xml
- DADOS_BANCARIOS.xml

## Aspectos de Segurança e Governança

### Vantagens do Data Lake Organizado
- Flexibilidade para dados estruturados e não estruturados
- Escalabilidade eficiente
- Suporte para análise em larga escala
- Integração com ferramentas de big data e ML
- Redução de custos

### Problemas Sem Governança
- **Data Swamp**: Dados inutilizáveis
- Dificuldade de localização e uso
- Riscos de segurança
- Performance degradada
- Dificuldades de compliance

## Gestão de Custos
- Monitoramento através do portal Azure Education
- Análise detalhada por serviço
- Controle de budget e créditos
- Relatórios de custos acumulados

## Conexão SSH para Máquinas Virtuais
```bash
ssh nomeusuariovm@ip_maquina
```

## Tecnologias Complementares
- **Google Colab**: Ambiente de desenvolvimento Python
- **MobaXTerm**: Cliente SSH para Windows
- **Terraform**: Infraestrutura como código
- **WSL**: Subsistema Linux para Windows

---

## Materiais de Estudo
- Notebooks Jupyter para ingestão de dados
- Scripts Python para automação
- Configurações Docker para serviços
- Documentação de APIs Azure
