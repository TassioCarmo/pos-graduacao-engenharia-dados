# Glossário de Business Intelligence e Data Warehouse

## Sumário (Summary)
- [Introdução ao Business Intelligence](#introdução-ao-business-intelligence)
- [Data Warehouse: Conceitos Fundamentais](#data-warehouse-conceitos-fundamentais)
- [Silos de Dados](#silos-de-dados)
- [ETL: Extract, Transform, Load](#etl-extract-transform-load)
- [OLAP: Online Analytical Processing](#olap-online-analytical-processing)
- [Modelagem Multidimensional](#modelagem-multidimensional)
- [Modelagem Moderna de Dados](#modelagem-moderna-de-dados)
- [Dimensões em Data Warehouse](#dimensões-em-data-warehouse)
- [Tabelas Fato](#tabelas-fato)
- [Engines de Data Warehousing](#engines-de-data-warehousing)
- [Orquestração de Transformações em DW](#orquestração-de-transformações-em-dw)

## Introdução ao Business Intelligence
**Business Intelligence (BI) / Inteligência de Negócios**

Business Intelligence abrange os processos, ferramentas e tecnologias necessárias para transformar dados corporativos em informações e conhecimento acionável. O BI permite que as organizações tomem decisões mais informadas com base em evidências concretas em vez de intuição.

### O que é BI?
- Sistema que permite transformar dados em informações e informações em conhecimento
- Ferramenta para identificar anomalias, tendências e padrões nos dados de negócio
- Plataforma que suporta relatórios, análises e tomada de decisão baseada em fatos

### Usos do BI
O BI pode ser utilizado para obter:

- **Insights táticos**: Otimização de processos de negócios através da identificação de tendências, anomalias e comportamentos que requerem ação gerencial
- **Visão estratégica**: Alinhamento de diversos processos de negócios aos objetivos principais através de gerenciamento e análise integrada de desempenho

### Fluxo de valor dos dados
1. **Dados**: Provenientes de diversas fontes como planilhas, ERPs, CRMs e outros sistemas
2. **Informação**: Transformação dos dados em relatórios, gráficos e cruzamentos que respondem "O que está acontecendo?"
3. **Conhecimento**: Conversão das informações em estratégias e insights acionáveis

### Perspectivas temporais no BI
- **Passado**: O que e por que aconteceu? (Análises diversas)
- **Presente**: O que está acontecendo agora? (Performance, Indicadores, Balanced Scorecard)
- **Futuro**: Qual a minha estratégia? (Planejamento estratégico)

## Data Warehouse: Conceitos Fundamentais
**Data Warehouse (DW) / Armazém de Dados**

Um Data Warehouse é um repositório central que armazena dados históricos e atuais de múltiplas fontes em um formato estruturado para facilitar análises, relatórios e tomada de decisões.

### Características essenciais
- **Orientado por assuntos**: Organizado em torno dos principais temas do negócio
- **Integrado**: Combina dados de diferentes fontes em um formato consistente
- **Não volátil**: Uma vez carregados, os dados não são modificados (read-only)
- **Variável com o tempo**: Mantém histórico de dados para análise temporal

### Componentes básicos
Todos os Data Warehouses compartilham um design básico que inclui:
- Repositório central de dados
- Metadados (dados sobre os dados)
- Dados de resumo
- Dados brutos
- Camadas de extração e carregamento de fontes de dados
- Interfaces para usuários finais

### Data Mart
**Data Mart / Mercado de Dados**

Um Data Mart é uma subdivisão ou subconjunto de um DW:
- Focado em uma área específica do negócio ou departamento
- Contém dados relevantes apenas para um segmento da organização
- Funciona como uma "fatia" do Data Warehouse completo

### Abordagens de implementação

#### Abordagem Top-Down (Bill Inmon)
- Desenvolvimento de cima para baixo
- Criação inicial de um DW corporativo completo
- Adaptação de ferramentas tradicionais de banco de dados relacional
- Foco na integração de dados de toda a empresa

#### Abordagem Bottom-Up (Ralph Kimball)
- Desenvolvimento de baixo para cima
- Criação de data marts por processo de negócio
- Uso de modelagem dimensional
- Construção incremental do DW a partir de data marts individuais

## Silos de Dados
**Data Silos / Silos de Dados**

Silos de dados são repositórios isolados de dados que não são compartilhados com outros sistemas ou departamentos na organização.

### Problemas causados pelos silos de dados
- Visão fragmentada da informação
- Duplicação desnecessária de dados
- Inconsistências entre fontes de dados
- Dificuldade em obter uma "visão única" do negócio
- Barreira para análises integradas

Um dos principais objetivos do DW é justamente quebrar esses silos, integrando as informações em um único repositório centralizado.

## ETL: Extract, Transform, Load
**Extract, Transform, Load / Extrair, Transformar, Carregar**

O processo ETL é fundamental para a construção e manutenção de um Data Warehouse, sendo responsável por coletar, processar e carregar os dados no DW.

### Componentes do ETL
1. **Extração (Extract)**: Coleta de dados das fontes originais
2. **Transformação (Transform)**: Aplicação de regras de negócio, limpeza e padronização dos dados
3. **Carregamento (Load)**: Inserção dos dados transformados no Data Warehouse

### Importância do ETL
O processo ETL é uma das fases mais críticas na construção de um sistema DW:
- Processa grandes volumes de dados
- Implementa regras e fórmulas dos indicadores que comporão as tabelas de Fato
- Cria a "ponte" entre os sistemas operacionais e o DW
- Pode consumir até 80% do tempo de desenvolvimento de um projeto de DW
- Representa aproximadamente 55% do tempo total de execução de um projeto de DW

### Ferramentas de ETL em Nuvem
O ETL evoluiu para soluções na nuvem, como:
- Hevo Data
- AWS Glue
- AWS Data Pipeline
- Stitch Data
- Talend

### ODS (Operational Data Store)
**Operational Data Store / Repositório Operacional de Dados**

- Repositório intermediário onde os dados são colocados para consulta por outros sistemas ou áreas de inteligência
- Reúne dados de várias aplicações
- Diferente de um DW, não tem compromisso com armazenamento histórico ou auditoria de dados
- Geralmente utilizado como passo intermediário no processo ETL

## OLAP: Online Analytical Processing
**Online Analytical Processing / Processamento Analítico Online**

OLAP é uma tecnologia que permite explorar dados multidimensionais de forma interativa e em tempo real, facilitando a análise de grandes volumes de informações sob diferentes perspectivas.

### Funções básicas do OLAP
- Visualização multidimensional dos dados
- Exploração dinâmica das informações
- Rotação (mudar a perspectiva da análise)
- Múltiplos modos de visualização dos dados

### Relação com o Data Warehouse
OLAP e Data Warehouse são tecnologias complementares:
- O DW armazena as informações de forma eficiente
- O OLAP recupera essas informações com rapidez para análise

### Cubo OLAP
Um cubo OLAP é uma estrutura de dados multidimensional que:
- Proporciona rápida análise de valores quantitativos (medidas)
- Permite visualizar os dados sob diversas perspectivas ou dimensões
- Facilita operações como slice, dice, drill-down, roll-up e pivot

### Ferramentas de OLAP
**Power BI / Tableau**

São líderes no mercado de Business Intelligence:
- Power BI: Desenvolvido pela Microsoft, inicialmente como "Project Crescent" em 2010 e lançado oficialmente em 2013
- Tableau: Outra ferramenta popular para visualização de dados e análises OLAP

Essas ferramentas permitem criar dashboards interativos, relatórios dinâmicos e visualizações avançadas dos dados armazenados no DW.

## Modelagem Multidimensional
**Multidimensional Modeling / Modelagem Multidimensional**

A Modelagem Multidimensional é uma técnica de estruturação de dados otimizada para Data Warehouses, desenvolvida pelo professor Ralph Kimball. O objetivo é otimizar a recuperação rápida e segura das informações.

### Conceito do "cubo de dados"
A modelagem multidimensional pode ser metaforicamente representada como um cubo, onde:
- As arestas do cubo representam dimensões (ex: tempo, produto, localização)
- Os pontos dentro do cubo representam fatos ou medidas (ex: vendas, lucro)
- As intersecções permitem analisar medidas específicas sob múltiplas dimensões

### Elementos fundamentais
Toda modelagem dimensional possui dois componentes essenciais:
1. **Tabelas Fato**: Contêm as métricas quantitativas do negócio
2. **Tabelas Dimensão**: Contêm os descritores qualitativos dos dados

### Métricas no Data Warehouse
- Também chamadas de quantificadores ou medidas
- Podem ser consideradas KPIs (Key Performance Indicators) 
- São sempre valores numéricos provenientes de transações da empresa
- Utilizadas para quantificar aspectos do negócio que precisam ser monitorados

### Modelos de Esquema

#### Star Schema (Esquema Estrela)
- Modelo mais comum e simples
- Uma tabela Fato central conectada diretamente a várias tabelas Dimensão
- Dimensões desnormalizadas (atributos em uma única tabela)

**Exemplo:** Em um DW de vendas, uma tabela Fato "Vendas" conectada diretamente às dimensões "Tempo", "Produto", "Loja" e "Cliente".

#### Snowflake Schema (Esquema Floco de Neve)
- Modelo mais normalizado
- Tabela Fato central conectada a dimensões que, por sua vez, se conectam a outras dimensões
- Hierarquias mantidas através de relacionamentos entre dimensões

**Exemplo:** A dimensão "Produto" se conecta a outra dimensão "Categoria", que se conecta a "Departamento".

### Comparação entre Star Schema e Snowflake

**Star Schema (mais usado):**
- Dimensões desnormalizadas
- Otimizado para performance de consulta
- Hierarquias achatadas em uma única tabela
- Navegação mais simples e intuitiva
- Utiliza mais espaço de armazenamento por repetir descrições

**Snowflake Schema:**
- Dimensões normalizadas
- Mantém hierarquias em tabelas separadas
- Múltiplas tabelas geram mais junções (joins)
- Economiza espaço de armazenamento
- Acesso mais lento devido às múltiplas junções
- Maior complexidade nas consultas

## Modelagem Moderna de Dados
**Modern Data Modeling / Modelagem Moderna de Dados**

A modelagem moderna de dados evoluiu para atender às necessidades contemporâneas de análise de big data, combinando técnicas tradicionais com abordagens inovadoras.

### Abordagens modernas
- **Modelo Dimensional**: Star Schema e Snowflake (tradicional)
- **Data Vault 2.0**: Arquitetura flexível baseada em HUBs, LINKs e SATELLITEs
- **One-Big-Table (OBT)**: Desnormalização extrema em uma única tabela grande

### One-Big-Table (OBT)
**One-Big-Table / Tabela Única Grande**

Uma grande tabela que inclui a maioria dos atributos dimensionais como colunas adicionais.

#### Vantagens (Prós):
- Simplifica consultas ao reduzir a necessidade de múltiplas junções
- Melhora o tempo de resposta, especialmente com codificação de coluna
- Otimiza a performance para leitura de dados

#### Desvantagens (Contras):
- Desafios no gerenciamento de dimensões em mudança
- Difícil decisão entre usar valores de dimensão mais recentes ou valores point-in-time
- Adicionar novos atributos dimensionais requer preenchimento de dados históricos

## Dimensões em Data Warehouse
**Dimensions / Dimensões**

Dimensões são elementos estruturais que contextualizam os fatos e métricas em um Data Warehouse, permitindo analisar os dados sob diferentes perspectivas.

### Função das dimensões
- Identificam um indicador de análise sobre um empreendimento, negócio ou ação
- Permitem identificar quando (tempo), onde (geografia) e com quem (cliente, produto) ocorreu um fato
- Fornecem o contexto para interpretar as métricas

### Estrutura das tabelas dimensão
Uma tabela dimensão tipicamente armazena:
- **Surrogate Key**: Chave artificial usada para identificação
- **Natural Key**: Chave original do sistema fonte
- **Atributos**: Informações descritivas e hierarquias

### Surrogate Key em Dimensões
**Surrogate Key / Chave Substituta**

Em um Data Warehouse, a Surrogate Key é uma chave artificial utilizada nas dimensões para conectá-las às tabelas Fato.

#### Características:
- É a Primary Key (chave primária) da dimensão
- Artificial e autoincremental (1, 2, 3...)
- Criada durante o processo ETL
- Na tabela Fato, funciona como Foreign Key (chave estrangeira)
- Não existe no sistema transacional de origem
- Não pode se repetir

#### Vantagens:
- Melhora a performance das consultas
- Independente das chaves do sistema fonte
- Facilita o gerenciamento de mudanças nas dimensões
- Simplifica junções entre tabelas

## Tabelas Fato
**Fact Tables / Tabelas Fato**

As tabelas Fato são o elemento central do Data Warehouse, contendo as métricas quantitativas do negócio e as referências às dimensões relacionadas.

### Características principais
- Principal tabela do Data Warehouse
- Conecta-se às dimensões através de chaves estrangeiras
- Podem existir múltiplas tabelas Fato em um DW
- Geralmente contém grande volume de dados

### Conteúdo das tabelas Fato
As tabelas Fato armazenam principalmente:
- **Métricas**: Valores numéricos que representam os fatos do negócio (vendas, quantidade, valor)
- **Foreign Keys**: Chaves estrangeiras que relacionam a tabela Fato às dimensões

### Relação com as dimensões
- A tabela Fato possui muitas linhas (alta cardinalidade)
- Representa eventos ou transações do negócio
- Conecta-se às dimensões através de relacionamentos muitos-para-um (N:1)
- As dimensões fornecem contexto para interpretar as métricas da tabela Fato

## Engines de Data Warehousing
**Data Warehousing Engines / Motores de Data Warehousing**

As engines ou motores de Data Warehousing são sistemas otimizados para cargas de trabalho analíticas, que exigem consultas complexas em grandes volumes de dados.

### Características
- Otimizados para consultas analíticas (em contraste com bancos transacionais)
- Projetados para processar grandes volumes de dados
- Focados em leituras complexas e menos frequentes

### C-Store
O C-Store é um sistema de gerenciamento de banco de dados orientado a colunas desenvolvido por uma equipe de universidades americanas, incluindo MIT e Brown University.

#### Inovações:
- Armazenamento por coluna (não por linha)
- Otimizado para leitura de dados
- Base para as modernas engines de Data Warehouse em nuvem

### Engines modernas em nuvem
Atualmente, existem três opções dominantes para engines de Data Warehouse baseadas em nuvem:

#### Amazon Redshift
- Integração completa com serviços AWS
- Geralmente mais econômico
- Sintaxe SQL similar ao PostgreSQL
- Simples de configurar e dimensionar

#### Google BigQuery
- Sem limitação por capacidade de cluster
- Escala bem com demandas crescentes de simultaneidade
- Integração com produtos Google (Drive, Analytics)
- Preço baseado em dados processados

#### Snowflake
- Arquitetura que separa computação do armazenamento
- Altamente escalável para volume e simultaneidade
- Preço baseado no tempo de uso dos bancos de dados virtuais
- Não requer ajustes manuais de índices ou chaves de distribuição

## Orquestração de Transformações em DW
**Data Transformation Orchestration / Orquestração de Transformações de Dados**

A orquestração de transformações de dados é o processo de obter dados de múltiplas fontes, combiná-los, organizá-los e disponibilizá-los para ferramentas de análise.

### Benefícios
- Automação de fluxos de dados
- Simplificação da tomada de decisões orientada por dados
- Controle centralizado dos processos ETL
- Monitoramento e gerenciamento de dependências entre tarefas

### Apache Airflow
O Apache Airflow é uma plataforma criada pela comunidade para criar, agendar e monitorar fluxos de trabalho de forma programática.

#### Componentes principais:
- **DAG (Directed Acyclic Graph)**: Grafos de tarefas sem ciclos
- **Operator**: Etapas de transformação, divididas em:
  - **Sensor**: Realiza função de polling com frequência/timeout
  - **Executor**: Realiza operações de trigger (ex: HiveOperator, PigOperator)
- **Task**: Instância de tarefa a ser executada em um ponto específico do tempo
- **Hook**: Interface para sistemas externos (ex: JDBC, HTTP)

#### Funcionamento do DAG
- Na teoria dos grafos, um grafo é um conjunto de vértices conectados por arestas
- Em um grafo direcionado, cada aresta tem uma direção de um vértice inicial a um vértice final
- Um DAG não possui ciclos direcionados (não forma loops fechados)
- No Airflow, os DAGs representam as dependências entre tarefas de processamento de dados

### Pentaho
O Pentaho é outra ferramenta popular para orquestração de processos ETL, oferecendo interface gráfica para desenho de fluxos de transformação.

### Zonas de dados
Em arquiteturas modernas de Data Warehouse, os dados geralmente passam por diferentes zonas:
- **Bronze (Transient + Raw Zone)**: Dados brutos ingeridos das fontes originais
- **Silver**: Dados com algum tipo de tratamento inicial
- **Gold**: Dados finais prontos para consumo por ferramentas analíticas

