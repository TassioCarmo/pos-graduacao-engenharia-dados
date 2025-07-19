## O que é ingestão de dados

- A ingestão de dados é a etapa de coleta e armazenamento de dados. Os registros de uma ou mais fontes de dados são extraídos através de diversas formas (ferramentas open source ou proprietárias, scripts criados em diversas linguagens de programação) e armazenados em algum ambiente que permita analisar seu conteúdo (bancos de dados / data lakes / sistemas de arquivos et. al).
- Para a ingestão de dados, diversos métodos devem ser considerados para identificar a melhor estratégia de carga dos dados.
Algumas perguntas podem ajudar a identificar a melhor forma de realizar a ingestão dos dados
- Que tipo de dado será manipulado?
- Em quanto tempo será necessário ter acesso aos dados?
- Os dados sofrem atualizações? Existem campos de controle de alteração?
- Quem poderá visualizar os dados?
- Por quanto tempo esses dados deverão ser armazenados?
- Como garantir segurança dos dados?
- Como garantir escalabilidade no processo de ingestão de dados?

- A etapa de ingestão de dados requer a escolha de uma arquitetura que seja resiliente e escalável, pois é um dos processos mais importantes da análise dos dados e impactará diretamente na visualização dos consumidores de informações.
-  As metodologias desenvolvidas para a coleta, transformação, limpeza e armazenamento de dados entre sistemas transacionais e analíticos mais utilizadas no mercado são BATCH e STREAMING



### Tecnologias de ingestão em Batch


- BATCH é o processo de carga de dados em lotes (blocos de dados). Historicamente, grande parte das ferramentas existentes no mercado fazem a ingestão de dados usando essa metodologia e, normalmente, são relacionadas como a etapa de ingestão de um projeto de Business Intelligence.
- Na abordagem BATCH, os dados são "amontoados" em blocos que podem ser agrupados por fatores temporais, segmentações de grupos e outras coisa mais. Em seguida, uma rotina definida pelo usuário processa esses blocos de acordo com os horários agendados e definidos com os consumidores/técnicos
- Processos em BATCH são indicados em ambientes onde o usuário não tem necessidade de visualizar os dados em tempo real (dados quentes – exatamente quando são gerados), quando grandes volumes de dados estão sendo executados por algoritmos complexos (agregações, cursores e por assim vai), quando é necessário analisar todo o volume de dados e quando os dados são formados através de junções de tabelas.

- Atualmente, são utilizadas duas abordagens para executar carga de dados utilizando a metodologia BATCH:
CARGA INCREMENTAL:
- São utilizadas técnicas para coletas de informações que não foram previamente carregadas para ambientes analíticos. Normalmente, essa metodologia é utilizada para carga histórica de informações que não sofrem alterações no decorrer do tempo.
CARGA COMPLETA:
- Nessa metodologia, os dados são carregados sempre que o processo é executado, sobrescrevendo dados já existentes ou, se for um novo objeto, dando novas visões. Esse processo normalmente é aplicado em ambientes com grande atualização de dados e que não tenham mecanismos simples de identificar a alteração de itens.

## Tecnologias de ingestão em Streaming

- STREAMING é o processo de carga de dados em real-time (processamento dos dados no exato momento que são gerados no sistema transacional). O delay está em prazo de milissegundos, o que permite que o usuário acesse os dados praticamente em tempo real.
- É indicado em ambientes de missão crítica (onde os dados são cruciais para detecção de anomalias – sensores, aviação, fábricas, fraudes), e-commerce, análises médicas, monitoramento do clima e outros cenários.
Atualmente, são utilizadas duas abordagens para executar carga de dados utilizando a metodologia STREAMING
**LOGS**:
- Armazenam eventos de forma ordenada e imutável, onde novos dados são sempre anexados ao final. Consumidores podem ler os eventos no ritmo que quiserem, respeitando a ordem de chegada, permitindo reprocessamento e recuperação de dados históricos (exemplo: Kafka). Ideal para cenários de auditoria e análise retroativa de dados.
**PUB/SUB (MENSAGERIA)**:
- Publicadores enviam mensagens a um canal, e assinantes consomem essas mensagens em tempo real. Cada mensagem pode ser entregue a múltiplos assinantes, facilitando a entrega simultânea para diferentes consumidores. Usado em sistemas que exigem baixa latência e entrega em tempo real (exemplo: Google Pub/Sub).


## Infraestrutura como Código

- Infraestrutura como código (ou IaC) é uma metodologia de automação de infraestrutura de TI usada inicialmente por equipes de DevOps (desenvolvedores e operação conjunta) para gerenciar e provisionar recursos por meio de código.
- Essa abordagem pode ser utilizada tanto em recursos físicos, virtuais ou em Cloud. Ela é uma abordagem de entrega ágil de infraestrutura, usando de codificação simples e objetiva.
- A tecnologia é similar aos scripts de programação que são usados para automatizar processos. Porém, nessa modalidade, são usados para automatizar etapas de configuração que devem (ou podem) ser repetidas várias vezes em vários servidores.



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
