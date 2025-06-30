# Preparação, Orquestração e Fluxos de Dados | Data Preparation, Orchestration and Data Flows

##  Visão Geral | Overview

Esta disciplina aborda os fundamentos e práticas avançadas para preparação, orquestração e gerenciamento de fluxos de dados em ambientes corporativos. Com foco em aplicações práticas, os alunos desenvolverão habilidades essenciais para manipular dados em grande escala, implementar pipelines eficientes e garantir a qualidade dos dados em ambientes de produção.

*This course covers the fundamentals and advanced practices for data preparation, orchestration, and management of data flows in corporate environments. With a focus on practical applications, students will develop essential skills to manipulate large-scale data, implement efficient pipelines, and ensure data quality in production environments.*

##  O que iremos estudar? | What will we study?

### 1. Montagem do conjunto de dados | Dataset Assembly
- Identificação de fontes de dados
- Estratégias de coleta e amostragem
- Validação inicial de dados
- Desafios comuns na montagem de datasets

### 2. Tipos de dados | Data Types
- Dados estruturados, semi-estruturados e não-estruturados
- Formatos de armazenamento (CSV, JSON, Parquet, Avro, ORC)
- Esquemas e evolução de esquemas
- Tipagem e conversões seguras

### 3. Melhoramento e enriquecimento | Enhancement and Enrichment
- Técnicas de data augmentation
- Fontes de dados complementares
- Enriquecimento semântico e contextual
- Geração de metadados

### 4. Preparação | Preparation

#### 4.1 Eliminação de dados irrelevantes | Irrelevant Data Elimination
- Identificação de outliers e anomalias
- Filtragem baseada em regras de negócio
- Tratamento de valores nulos e inconsistentes

#### 4.2 Granulação e agregação | Granulation and Aggregation
- Níveis de granularidade e hierarquias
- Funções de agregação e sumarização
- Técnicas de roll-up e drill-down
- Agregações temporais e espaciais

#### 4.3 Consistência e concordância | Consistency and Concordance
- Padronização de formatos e unidades
- Normalização de valores e escalas
- Harmonização entre diferentes fontes
- Verificação de regras de integridade

#### 4.4 Duplicação e redundância | Duplication and Redundancy
- Algoritmos de detecção de duplicatas
- Estratégias de deduplicação
- Merge de registros similares
- Redundância controlada vs. não-controlada

#### 4.5 Análise de domínios de atributos | Attribute Domain Analysis
- Validação de ranges e valores permitidos
- Distribuição estatística de atributos
- Detecção de valores atípicos
- Domínios dinâmicos e estáticos

#### 4.6 Integridade dos dados | Data Integrity
- Regras de validação estrutural
- Integridade referencial
- Completude e acurácia
- Auditoria de qualidade de dados

### 5. Feature Engineering | Feature Engineering
- Transformação de variáveis brutas em features
- Técnicas de encoding para variáveis categóricas
- Normalização e padronização
- Derivação de atributos
- Redução de dimensionalidade
- Seleção de features relevantes

### 6. Combinando dados de múltiplas fontes | Combining Data from Multiple Sources
- Operações de join e merge
- Reconciliação de identidades
- Resolução de conflitos
- Integração temporal de dados
- Desafios em dados heterogêneos

### 7. ELT x ETL | ELT vs ETL
- Paradigmas de processamento de dados
- Trade-offs de performance vs. flexibilidade
- Aplicações ideais para cada abordagem
- Arquiteturas híbridas

#### 7.1 Ferramentas para preparação de dados | Data Preparation Tools
- Apache Spark
- Pandas e Dask
- PySpark
- Databricks
- dbt (data build tool)
- Google DataPrep
- Talend Open Studio

#### 7.2 Ferramentas de orquestração | Orchestration Tools

##### 7.2.1 Orquestradores open-source | Open-source Orchestrators
- Apache Airflow
- Luigi
- Prefect
- Dagster
- Argo Workflows

##### 7.2.2 Orquestradores baseados em Cloud | Cloud-based Orchestrators
- AWS Step Functions
- Google Cloud Composer
- Azure Data Factory
- Databricks Workflows
- Google Cloud Dataflow

#### 7.3 Ferramentas para transformação e transferência de dados | Data Transformation and Transfer Tools
- Apache NiFi
- Kafka Connect
- Spark Streaming
- Fivetran
- Stitch
- AWS Glue
- Informatica

#### 7.4 Escalonamento de jobs baseados em eventos | Event-based Job Scaling
- Arquiteturas orientadas a eventos
- Sistemas de mensageria (Kafka, RabbitMQ)
- Auto-scaling baseado em carga
- Triggers e listeners
- Padrões de notificação e fanout

### 8. Reprocessamento em serviços de migração | Reprocessing in Migration Services
- Estratégias de backfill
- Janelas de processamento
- Versionamento de pipelines
- Rastreabilidade de execuções
- Reparo de dados históricos

### 9. Resiliência em migração | Resilience in Migration
- Tolerância a falhas
- Retry policies
- Circuit breakers
- Checkpoints e snapshots
- Rollback e recovery
- Monitoramento e alertas

### 10. Implementação de fluxos de correção de dados em expurgo | Implementation of Data Correction Flows in Purging
- Políticas de retenção de dados
- Expurgo seletivo
- Anonimização e pseudonimização
- Compliance com regulações de dados
- Auditoria de limpeza

##  Laboratórios Práticos | Practical Labs

Durante o curso, serão realizados laboratórios práticos abordando:

1. **Setup de ambiente de desenvolvimento**
   - Configuração de ambientes locais e cloud
   - Ferramentas necessárias

2. **Implementação de pipelines ETL/ELT**
   - Desenvolvimento de fluxos completos
   - Integração com diferentes fontes de dados

3. **Orquestração com Apache Airflow**
   - Criação de DAGs
   - Monitoramento e troubleshooting

4. **Feature Engineering avançado**
   - Técnicas para diferentes tipos de dados
   - Otimização de features para ML

5. **Resiliência e teste de falhas**
   - Implementação de mecanismos de recuperação
   - Simulação de cenários de erro



## ⚠️ Observações Importantes | Important Notes

- **Desenvolvimento em aula**: TODOS os exercícios são desenvolvidos durante a aula e a entrega é garantida se ficarem até o final da aula. As gravações ficam disponíveis no Canvas e podem ajudá-los com dúvidas.

- **Integridade acadêmica**: Cópias de trabalhos não serão aceitas. Caso tenha dúvidas, não hesite em procurar o professor.

- **Plataforma de entrega**: TODAS as atividades devem ser entregues EXCLUSIVAMENTE através do CANVAS. Atividades entregues por e-mail NÃO SERÃO CONSIDERADAS.

- **Prazos**: Caso não possa entregar a atividade no prazo, entre em contato com o professor com antecedência. O professor entende a rotina de trabalho dos alunos e é compreensível, mas pede que respeitem os prazos de entrega. O adiamento do prazo de entrega impactará diretamente no lançamento das notas.

- **Canal de comunicação**: O contato com o professor para dúvidas deve ser feito pelo CANVAS (as notificações são enviadas diretamente para o celular do professor). O professor utiliza o Microsoft Teams durante o dia no trabalho, então não fica com ele aberto e não vê mensagens fora das aulas.

##  Bibliografia Recomendada | Recommended Bibliography

### Bibliografia Básica | Basic Bibliography
- KLEPPMANN, Martin. **Designing Data-Intensive Applications**. O'Reilly Media, 2017.
- HOFFMAN, Ted; JOHNSON, Tim. **Teaching an Elephant to Dance: Intentional Evolution Across Teams, Process, and Applications**. O'Reilly Media, 2018.
- NORONHA, Rafael; FERREIRA, Fabiano. **Engenharia de Dados: Princípios e práticas para dados confiáveis**. Casa do Código, 2022.

### Bibliografia Complementar | Complementary Bibliography
- MARZ, Nathan; WARREN, James. **Big Data: Principles and best practices of scalable realtime data systems**. Manning Publications, 2015.
- DAMA International. **DMBOK: Data Management Body of Knowledge** (2ª edição). Technics Publications, 2017.
- WHITE, Tom. **Hadoop: The Definitive Guide** (4ª edição). O'Reilly Media, 2015.
- REIS, Eduardo. **Data Science do zero à produção: Como colocar projetos de dados para rodar no mundo real**. Casa do Código, 2023.
- RAMALHO, Luciano. **Fluent Python: Clear, Concise, and Effective Programming**. O'Reilly Media, 2015.

