# Arquitetura de Dados, Data Lake e Data Warehouse | Data Architecture, Data Lake and Data Warehouse

## Ementa | Course Description

Esta disciplina apresenta os principais conceitos e tecnologias associados às arquiteturas modernas de dados, com ênfase em Data Lakes e Data Warehouses. O curso explora fundamentos essenciais para o desenvolvimento e implementação de soluções de dados escaláveis em ambientes corporativos modernos.

### Principais Tópicos

#### Fundamentos de Arquitetura de Dados
* **Conceitos de Data Lake e Data Warehouse**
  * Definições, diferenças e casos de uso
  * Evolução histórica das arquiteturas de dados
  * Benefícios e desafios de implementação

* **Natureza dos Dados**
  * Dados estruturados vs. semi-estruturados vs. não estruturados
  * Formatos de armazenamento (Parquet, ORC, Avro, JSON, CSV)
  * Metadados e catálogos de dados

* **Ecossistema de Dados**
  * Produtores e consumidores de dados
  * Fluxos de ingestão e consumo
  * Governança e qualidade de dados

#### Arquiteturas Avançadas
* **Data Lake**
  * Logical Data Lake e conceito de Data Ponds
  * Arquitetura Lambda vs. Arquitetura Kappa
  * Data Lakehouse e abordagens híbridas

* **Blocos Funcionais**
  * Componentes essenciais em uma arquitetura moderna de dados
  * Interfaces entre sistemas
  * Integração com fontes externas e internas

* **Abordagens de Schema**
  * Schema on-write vs. schema on-read
  * Evolução de schemas e compatibilidade
  * Técnicas de validação e conformidade

#### Arquiteturas Corporativas
* **Enterprise Data Hub**
  * Centralização e descentralização de dados
  * Modelos de acesso e compartilhamento
  * Plataformas unificadas de dados

* **Data Mesh**
  * Domínios e produtos de dados
  * Arquitetura federada e descentralizada
  * Implementação e desafios organizacionais

* **Sincronização de Fluxos**
  * Fluxos independentes e dependentes
  * Estratégias de processamento batch e streaming
  * Consistência e integridade em fluxos complexos

#### Implementação e Infraestrutura
* **Alta Disponibilidade (HA)**
  * Princípios de resiliência em arquiteturas de dados
  * Redundância e recuperação de desastres
  * Balanceamento de carga e escalonamento

* **Data Warehousing**
  * Modelagem multidimensional (Star Schema, Snowflake)
  * Construção e gerenciamento de dimensões
  * Tabelas de fatos e métricas

* **Engines e Plataformas**
  * Engines modernas de Data Warehousing (Snowflake, Redshift, BigQuery, Synapse)
  * Tecnologias de processamento distribuído (Spark, Presto, Trino)
  * Integrações com ferramentas de BI e Analytics

#### Orquestração e Organização
* **Transformações em Data Warehouse**
  * ETL vs. ELT
  * Orquestração de pipelines de dados
  * Ferramentas de transformação e processamento

* **Estruturação de Data Lakes**
  * Organização em camadas (Raw, Trusted, Refined)
  * Zonas funcionais e níveis de processamento
  * Delta Lake e implementações de transações ACID

* **Implementações On-premise vs. Cloud**
  * Comparativo de arquiteturas locais e em nuvem
  * Modelos híbridos e multi-cloud
  * Considerações de custo, performance e segurança

## Objetivos da Disciplina | Course Objectives

### Objetivo Geral | General Objective

Esta disciplina visa capacitar os alunos a dominarem os conceitos fundamentais e avançados relacionados às arquiteturas modernas de dados, permitindo:

* Compreender profundamente os fundamentos teóricos e práticos de arquiteturas de dados
* Diferenciar e aplicar corretamente os conceitos de Data Lake e Data Warehouse conforme necessidades organizacionais específicas
* Analisar criticamente a organização dos dados corporativos e propor soluções baseadas em arquiteturas escaláveis e resilientes
* Projetar ambientes de dados robustos que respondam adequadamente aos desafios de volume, variedade e velocidade (3Vs do Big Data)
* Avaliar tecnologias emergentes, técnicas de modelagem e estratégias de orquestração para ambientes analíticos modernos

### Objetivos Específicos | Specific Objectives

Ao concluir esta disciplina, o aluno será capaz de:

* **Compreender o Ecossistema de Dados**
  * Identificar produtores e consumidores de dados e suas funções nos processos decisórios
  * Mapear fluxos de informação dentro de uma organização
  * Distinguir diferentes tipos e estruturas de dados

* **Dominar Conceitos Arquiteturais**
  * Compreender os conceitos de dados estruturados, semi-estruturados e não estruturados
  * Conhecer os principais elementos arquiteturais de Data Lake e Data Warehouse
  * Aplicar princípios de arquitetura de dados para resolver problemas organizacionais

* **Implementar Processos de Dados**
  * Utilizar conceitos de ETL/ELT, modelagem dimensional e orquestração de processos
  * Avaliar criteriosamente cenários para aplicação de schema on-read e schema on-write
  * Implementar pipelines de dados eficientes e escaláveis

* **Projetar Soluções Robustas**
  * Desenhar soluções baseadas em arquiteturas com alta disponibilidade
  * Comparar abordagens de armazenamento on-premise e em nuvem
  * Selecionar tecnologias apropriadas para requisitos específicos de negócio

## Metodologia | Methodology

O curso utiliza uma abordagem teórico-prática, combinando:

* Aulas expositivas sobre conceitos fundamentais e avançados
* Estudos de caso de implementações reais em diferentes setores
* Laboratórios práticos com ferramentas e tecnologias de mercado
* Projetos em grupo para design e implementação de arquiteturas de dados
* Discussões sobre tendências e desafios da indústria

## Bibliografia | Bibliography

### Bibliografia Básica | Essential Reading

1. INMON, W. H. **Building the Data Warehouse**. 4ª Ed. Indianapolis: Wiley, 2005.
2. KIMBALL, R.; ROSS, M. **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. 3ª Ed. Indianapolis: Wiley, 2013.
3. SAWADOGO, P.; DARMONT, J. **On Data Lake Architectures and Metadata Management**. Journal of Intelligent Information Systems, v. 56, p. 97-120, 2021.

### Bibliografia Complementar | Supplementary Reading

1. DEHGHANI, Z. **Data Mesh: Delivering Data-Driven Value at Scale**. O'Reilly Media, 2022.
2. SHARMA, T.; GANDHI, G. **Data Lakes: Purposes, Practices, Patterns, and Platforms**. O'Reilly Media, 2020. 
3. PATHAK, P. **Modern Data Architecture with Delta Lake: Lakehouse Fundamentals with Databricks**. Packt Publishing, 2022.
4. KLEPPMANN, M. **Designing Data-Intensive Applications**. O'Reilly Media, 2017.
5. DREMIO. **Definitive Guide to Data Lakehouse**. Disponível em: [https://www.dremio.com/resources/guides/definitive-guide-to-data-lakehouse/](https://www.dremio.com/resources/guides/definitive-guide-to-data-lakehouse/)


---

