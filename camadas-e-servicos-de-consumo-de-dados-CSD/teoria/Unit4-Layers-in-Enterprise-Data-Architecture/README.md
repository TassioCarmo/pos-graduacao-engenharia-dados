
# Arquitetura de Dados / Data Architecture

## Sumário
- [Introdução à Arquitetura de Dados](#introdução-à-arquitetura-de-dados)
- [Camadas em uma Arquitetura de Dados](#camadas-em-uma-arquitetura-de-dados)
  - [Camada de Ingestão/Coleta de Dados](#camada-de-ingestãocoleta-de-dados)
  - [Processamento Batch e Stream](#processamento-batch-e-stream)
  - [Camada de Armazenamento e Integração de Dados](#camada-de-armazenamento-e-integração-de-dados)
  - [Camada de Processamento de Dados](#camada-de-processamento-de-dados)
  - [Camada de Análise e Interface do Usuário](#camada-de-análise-e-interface-do-usuário)
  - [Camada de Pipeline de Dados](#camada-de-pipeline-de-dados)
- [Barramentos de Mensageria de Dados](#barramentos-de-mensageria-de-dados)
  - [Apache Kafka](#apache-kafka)
  - [Caso de Uso Real](#caso-de-uso-real-com-apache-kafka)
- [Armazenamento em Cache](#armazenamento-em-cache)
- [Processamento Analítico OLAP](#processamento-analítico-olap)
- [Camadas de Consumo por Serviços](#camadas-de-consumo-por-serviços)
  - [GraphQL](#graphql)
- [Plataformas Self-Service](#plataformas-self-service)
- [Design Convergente para Dados](#design-convergente-para-dados)

## Introdução à Arquitetura de Dados

Arquitetura de dados é uma disciplina fundamental para organizações que desejam aproveitar o valor estratégico de seus dados. Ela pode ser definida como:

> "...a prática de examinar a estratégia empresarial e identificar os principais pontos de integração de dados que precisam ser ativados para executar essa estratégia, estabelecendo um roteiro para criar os recursos essenciais para entregar essas integrações, permitindo que as empresas aproveitem os dados como um ativo estratégico."

> "...a ciência de avaliar onde estão os dados da sua empresa e a arte de projetar a melhor maneira futura de armazenar dados em toda a empresa."

> "...a disciplina para ajudar as empresas a gerenciar seus dados da maneira mais eficaz, segura, compatível e lucrativa."

Uma arquitetura de dados eficiente garante que:
- As informações sejam precisas e disponíveis para facilitar propósitos comerciais válidos
- Os requisitos de dados estratégicos sejam definidos e integrados aos ativos de dados
- Os investimentos em dados estejam alinhados com a estratégia de negócio
- Todo o ciclo de vida dos dados seja governado adequadamente

### Principais responsabilidades da Arquitetura de Dados:

1. Dados e documentação de requisitos para sistemas
2. Projeto de banco de dados e modelagem
3. Documentação, gestão e disseminação/acesso de metadados
4. Coleta, uso e integração de dados em toda a empresa
5. Qualidade dos dados, definição e aplicação da Governança de Dados
6. Conformidade e retenção de arquivamento de dados (como LGPD)
7. Gerenciamento de Dados Mestres

## Camadas em uma Arquitetura de Dados

Uma arquitetura de dados moderna é tipicamente composta por várias camadas distintas, cada uma com responsabilidades específicas:

- **Camada de ingestão de dados** (Data Ingestion Layer)
- **Camada de armazenamento de dados** (Data Storage Layer)
- **Camada de processamento e análise de dados** (Data Processing and Analysis Layer)
- **Camada de interface do usuário** (UI Layer)
- **Camada de pipeline de dados** (Data Pipeline Layer)

Vamos examinar cada uma dessas camadas em detalhe.

### Camada de Ingestão/Coleta de Dados

Esta é a primeira camada da arquitetura da plataforma de dados. Como o nome sugere, é responsável por conectar-se aos sistemas de origem e trazer dados para a plataforma de dados de maneira periódica.

#### Principais responsabilidades:
- Conectar-se com as diversas fontes de dados
- Transferir dados das fontes para a plataforma em modo streaming, batch ou ambos
- Manter informações sobre os dados coletados no repositório de metadados (ex: volume de dados coletados e outras informações descritivas)

#### Ferramentas populares para ingestão de dados:
- **Google Cloud Data Flow**
- **IBM Streams**
- **Amazon Kinesis**
- **Apache Kafka**

Estas ferramentas suportam os modos batch e streaming de ingestão de dados, proporcionando flexibilidade conforme as necessidades do negócio.

### Processamento Batch e Stream

#### Diferença entre Batch e Stream

**Processamento em Batch (Lote):**
- Lida com grupos de dados agrupados em intervalos de tempo específicos 
- Também conhecido como "janela de dados"
- Ideal quando não há necessidade de análises em tempo real
- As equipes de TI frequentemente precisam esperar que todos os dados sejam carregados antes de iniciar a análise

**Processamento em Stream (Fluxo contínuo):**
- Lida com dados contínuos em tempo real
- Processa dados em lotes menores conforme são recebidos
- Gera resultados quase instantâneos
- Essencial para transformar dados grandes em informações rápidas

#### Quando escolher entre Batch e Stream

A escolha entre Batch e Stream depende dos requisitos específicos do caso de uso:

**Quando usar Stream:**
- Quando dados são gerados continuamente sem interrupção (como sensores IoT)
- Quando são necessárias decisões em tempo real
- Para responder rapidamente a eventos ou ameaças
- Para processar dados com alta variabilidade ou velocidade

**Quando usar Batch:**
- Para processamento de grandes volumes de dados sem urgência
- Quando a análise histórica é mais importante que dados em tempo real
- Para processamentos que exigem recursos computacionais intensivos
- Quando a economia de recursos é prioridade sobre a velocidade

**Exemplo prático:** Uma turbina eólica com sensores sempre ligados gera um fluxo contínuo de dados ininterrupto. Uma abordagem em batch seria obsoleta neste caso, pois não há início ou fim do fluxo de dados, tornando o processamento em stream a escolha mais adequada.

É importante ressaltar que não se trata de escolher um modelo sobre o outro, mas de determinar qual é o mais adequado para cada caso de uso específico.

### Camada de Armazenamento e Integração de Dados

Após a coleta, os dados precisam ser armazenados e integrados. Esta camada é responsável por:

- Armazenar dados para processamento e uso a longo prazo
- Disponibilizar os dados para processamento nos modos streaming e batch
- Garantir que o armazenamento seja confiável, escalável, de alto desempenho e econômico

#### Tecnologias de armazenamento:

**Bancos de dados relacionais:**
- IBM DB2
- Microsoft SQL Server
- MySQL
- Oracle Database
- PostgreSQL

**Bancos de dados relacionais na nuvem:**
- IBM DB2 Cloud
- Google Cloud SQL
- Azure SQL

**Bancos de dados NoSQL:**
- MongoDB
- Cassandra
- Redis
- Neo4J
- IBM Cloudant

#### Ferramentas de integração:

- **IBM Cloud Pak for Integration** - Uma plataforma cloud impulsionada por IA que oferece:
  - Interações de eventos em tempo real
  - Transferência de dados entre diferentes ambientes de nuvem
  - Implementação e escalabilidade com arquitetura nativa em nuvem
  - Serviços básicos compartilhados com segurança e criptografia corporativa

Esta plataforma utiliza serviços e recursos como Amazon VPC, zonas de disponibilidade, grupos de segurança, Amazon EBS, Amazon EC2 e Elastic Load Balancing para criar uma infraestrutura de nuvem confiável e escalável.

### Camada de Processamento de Dados

Esta camada é responsável por tarefas de processamento como:
- Validações de dados
- Transformações
- Aplicação de lógica de negócios

#### Principais capacidades:
- Ler dados em batch ou streaming a partir do armazenamento e aplicar transformações
- Suportar ferramentas de consulta e linguagens de programação populares
- Escalar para atender às demandas de processamento de conjuntos de dados crescentes
- Fornecer ambiente para analistas e cientistas de dados trabalharem com os dados

#### Tarefas de transformação comuns:

1. **Estruturação:** Alterações na estrutura dos dados, desde simples reorganizações de campos até combinações complexas usando junções e uniões
2. **Normalização:** Redução de redundância e inconsistência, eliminando dados não utilizados
3. **Desnormalização:** Combinação de dados de múltiplas tabelas em uma única tabela para consultas mais eficientes
4. **Limpeza de dados:** Correção de irregularidades para fornecer dados confiáveis para aplicações

#### Ferramentas para processamento de dados:

- Planilhas eletrônicas
- OpenRefine
- Google DataPrep
- Watson Studio Refinery
- Trifacta Wrangler
- Bibliotecas Python e R (como Pandas, dplyr)

É importante observar que o armazenamento e processamento nem sempre ocorrem em camadas separadas. Em bancos de dados relacionais, ambas as funções acontecem na mesma camada, enquanto em sistemas de big data, os dados são primeiro armazenados (ex: no HDFS - Hadoop Distributed File System) e depois processados (ex: com Apache Spark).

### Camada de Análise e Interface do Usuário

Esta camada é responsável por fornecer os dados processados aos usuários finais, incluindo:
- Analistas de BI (Business Intelligence)
- Stakeholders de negócio
- Cientistas de dados e analistas de dados

A camada deve suportar:
- Ferramentas de consulta SQL e NoSQL
- Linguagens de programação como Python, R e Java
- APIs para execução de relatórios sobre dados para processamento online e offline

#### Ferramentas de visualização e análise:

**Tableau**
- Fundada em 2003 por Chris Stolte, Pat Hanrahan e Christian Chabot
- Foco em facilitar a visualização de dados com foco na compreensão visual
- Permite que usuários com conhecimento básico de Excel criem análises complexas
- Desenvolvido com inspiração em tecnologias de computação gráfica (um dos fundadores foi membro da Pixar)

**Power BI**
- Desenvolvido pela Microsoft, inicialmente como "Project Crescent" em 2010
- Lançado em 2013 como Microsoft Power BI para Office 365
- Evoluiu de extensões do Excel (PowerView, PowerQuery, Power Pivot) para uma plataforma completa
- Oferece solução completa de BI, incluindo visualização, criação de DW (Data Warehouse), ETL e cubos OLAP

Estas ferramentas democratizam o acesso aos dados, permitindo que profissionais com diferentes níveis de conhecimento técnico possam extrair insights valiosos.

### Camada de Pipeline de Dados

Esta é a camada responsável por implementar e manter um fluxo contínuo de dados através de todo o pipeline. Ela oferece capacidades de:
- Extração
- Transformação
- Carregamento de dados (ETL)

#### Apache Airflow

O Apache Airflow é uma das soluções de pipeline de dados mais populares, com as seguintes características:

- Plataforma criada pela comunidade para criar, agendar e monitorar fluxos de trabalho
- Arquitetura modular que usa fila de mensagens para orquestrar trabalhadores
- Capacidade de escalar "até o infinito"
- Pipelines definidos em Python, permitindo geração dinâmica de fluxos de trabalho

**Principais componentes:**

- **DAG (Directed Acyclic Graph):** Grafos de tarefas sem ciclos direcionados
  - Na teoria dos grafos, um grafo é um conjunto de vértices conectados por arestas
  - Em um grafo direcionado, cada aresta tem direção de um vértice inicial a um final
  - Um DAG não possui ciclos direcionados (não é possível formar laços fechados)

- **Operadores:** Divididos em:
  - **Sensor:** Realiza função de polling com frequência/timeout definidos
  - **Executor:** Realiza operações de trigger (como HiveOperator, PigOperator)

- **Task:** Instância de tarefa considerada para execução em um ponto específico do tempo

- **Hook:** Interface para sistemas externos (como JDBC e HTTP)

**Benefícios do Apache Airflow:**

1. **Dinâmico:** Pipelines construídos como código, proporcionando flexibilidade
2. **Extensível:** Fácil criação de operadores e executores para suportar diferentes ambientes
3. **Elegante:** Pipelines inequívocos graças ao mecanismo de template Jinja
4. **Escalável:** Arquitetura composta por unidades padronizadas com enfileiramento de mensagens
5. **Código aberto:** Comunidade ativa e em constante evolução

O Airflow permite agendar, monitorar e criar fluxos de trabalho complexos, apresentando o status e as dependências das tarefas de forma visual através dos DAGs.

## Barramentos de Mensageria de Dados

### Mensageria de Alta Performance

Com o crescente volume de dados gerados, surgiu a necessidade de transportar informações eficientemente entre diversas aplicações. Um exemplo comum é quando fazemos uma compra com cartão de crédito: a operadora precisa notificar múltiplos sistemas sobre a transação (contabilidade, benefícios, análise antifraude, etc.).

Nesse cenário, cada aplicação deve se concentrar apenas na implementação das regras de negócio, sem se preocupar com a entrega ou captura dos dados. Para resolver este problema complexo, surgem as soluções de data streaming e mensageria.

#### Data Streaming

Um fluxo de dados constante e sem controle é chamado de data streaming. Suas características são:
- Os dados não têm limites definidos (início ou fim)
- O processamento ocorre à medida que os dados chegam ao destino
- Também conhecido como processamento em tempo real ou on-line

Este modelo contrasta com o processamento em bloco (batch ou off-line), onde conjuntos definidos de dados são processados em janelas de tempo.

#### Sistemas de Mensagens

Os sistemas de mensagens permitem desacoplar a geração dos dados do seu processamento de forma assíncrona, permitindo que aplicações continuem funcionando sem esperar que outras terminem seu processamento.

### Apache Kafka

O Apache Kafka é uma plataforma open-source de mensageria projetada para criar aplicações de streaming (fluxo contínuo de dados). É baseado em logs, também chamados de write-ahead logs, commit logs ou transaction logs. Um log é uma forma básica de armazenamento onde novas informações são adicionadas no final do arquivo - este é o princípio fundamental do Kafka.

O Kafka é adequado para soluções com grande volume de dados (big data) devido à sua alta taxa de transferência.

#### Funcionalidades principais do Apache Kafka:

1. **Sistema de mensagens:** Desacopla sistemas com escopos diferentes através de um modelo publish/subscribe
2. **Sistema de armazenamento:** Guarda eventos (logs) de forma consistente, permitindo reconstruir o estado do sistema a qualquer momento
3. **Processamento de stream:** Transforma dados em tempo real (mapeamentos, agregações, junções, etc.)

#### Arquitetura do Apache Kafka:

O Kafka funciona como um intermediário que coleta dados da fonte e os entrega para aplicações consumidoras. Sua arquitetura segue o modelo Publisher/Consumer:

- **Publisher (Produtor):** Componente que publica mensagens em um tópico
- **Broker:** Servidor Kafka que recebe mensagens dos produtores e as armazena em disco
- **Tópico:** Fila onde as mensagens são publicadas
- **Consumer (Consumidor):** Componente que se inscreve em tópicos para receber mensagens

Um cluster Kafka é composto por vários brokers, cada um gerenciando uma lista de tópicos divididos em partições. Esta arquitetura distribuída permite alta disponibilidade e escalabilidade.


### Caso de Uso Real com Apache Kafka

Um caso comum é a integração entre plataformas de marketplace e e-commerce, resolvendo problemas como:

- Lentidão na integração das ofertas dos lojistas com o e-commerce
- Demora de horas para refletir alterações de preço ou disponibilidade no site
- Processos síncronos que geram indisponibilidade devido ao alto volume de integrações
- Necessidade de desligar as integrações durante o dia para evitar problemas de disponibilidade
- Atualizações feitas principalmente por processos batch noturnos

Estes problemas podem causar inconsistências graves, como produtos sem estoque sendo exibidos como disponíveis ou preços desatualizados.

#### Solução com Apache Kafka:

O Kafka permite tornar essas integrações:
- Assíncronas e em tempo real (elimina a necessidade de processos batch)
- Baseadas em eventos (cada alteração em uma oferta gera eventos de criação, atualização ou exclusão)
- Distribuídas, com maior throughput

#### Benefícios adicionais:

1. **Buffer para sistemas:** Evita travamentos ao intermediar o processamento de dados
2. **Redução de múltiplas integrações:** Em vez de criar N×M integrações diretas entre sistemas, cada sistema se conecta apenas ao Kafka
3. **Baixa latência e alto throughput:** Possibilita arquiteturas em tempo real (near real-time)
4. **Centralização de dados:** Qualquer sistema pode acessar os dados sem impactar os sistemas de origem

## Armazenamento em Cache

### O que é o armazenamento em cache?

Na computação, um cache é uma camada de armazenamento físico de dados de alta velocidade que guarda um subconjunto de dados, geralmente temporários, para que futuras solicitações sejam atendidas mais rapidamente do que seria possível ao acessar o local de armazenamento principal.

O cache permite reutilizar eficientemente dados recuperados ou computados anteriormente.

### Como funciona o armazenamento em cache?

Os dados em um cache geralmente são armazenados em hardware de acesso rápido, como RAM (Memória de acesso aleatório), podendo ser usados em conjunto com componentes de software.

O principal objetivo do cache é aumentar a performance da recuperação de dados ao reduzir a necessidade de acessar camadas de armazenamento mais lentas. Isso geralmente implica em armazenar temporariamente um subconjunto dos dados, em contraste com bancos de dados que mantêm dados completos e duráveis.

### Visão geral do armazenamento em cache

**RAM e mecanismos de memória:**
- Suportam altas taxas de solicitação (IOPS - operações de entrada/saída por segundo)
- Proporcionam desempenho de recuperação otimizado
- Reduzem custos em grande escala em comparação com bancos de dados tradicionais e hardware de disco

**Aplicações de cache:**
- Sistemas operacionais
- Camadas de redes (CDNs, DNS)
- Aplicativos web
- Bancos de dados
- Cargas de trabalho computacionais intensivas (recomendações, simulações)

**Padrões de projeto:**
- Uma camada de cache dedicada permite que sistemas e aplicações funcionem independentemente
- Atua como camada central acessível por diferentes sistemas
- Especialmente útil em sistemas que escalam horizontalmente ou verticalmente

**Melhores práticas:**
- Entender a validade dos dados armazenados em cache
- Implementar controles como TTL (Time to Live) para expirar dados
- Considerar requisitos de alta disponibilidade
- Definir RTO (Recovery Time Objective) e RPO (Recovery Point Objective) para dados em memória

### Amazon ElastiCache

O Amazon ElastiCache é um serviço web que facilita a implantação, operação e dimensionamento de armazenamento em cache na nuvem. O serviço melhora a performance de aplicativos web ao permitir a recuperação de informações de datastores rápidos em memória, em vez de depender exclusivamente de bancos de dados em disco.

### Redis

O Redis (REmote DIctionary Server) é um armazenamento de estrutura de dados de chave-valor open-source na memória. Oferece:

- Estruturas de dados versáteis em memória
- Compatibilidade com várias linguagens de desenvolvimento
- Casos de uso incluem cache, gerenciamento de sessões, PUB/SUB e classificações
- Suporte a vários tipos de dados: strings, listas, conjuntos, hashes, HyperLogLogs
- Capacidade de armazenar dados de até 512 MB por chave

O Redis permite armazenar praticamente qualquer tipo de dado na memória, proporcionando acesso ultrarrápido e flexibilidade para diferentes aplicações.

## Processamento Analítico OLAP

### OLAP (Online Analytical Processing)

O processamento analítico online (OLAP) é uma abordagem para responder rapidamente a consultas multidimensionais analíticas. É parte da categoria mais ampla de Business Intelligence (BI), que também inclui relatórios relacionais e mineração de dados.

Aplicações típicas de OLAP incluem:
- Relatórios de negócios para vendas e marketing
- Comunicação e gestão de processos
- Orçamento e previsão financeira
- Relatórios financeiros

#### Características do OLAP:

- Permite análise interativa de dados multidimensionais
- Utiliza modelo de dados multidimensional
- Possibilita consultas analíticas complexas com tempo de execução rápido
- Suporta consultas ad-hoc (não planejadas antecipadamente)

#### Cargas massivas de dados

Um desafio recorrente em ambientes OLAP é executar cargas massivas de dados com alto desempenho e baixo consumo de recursos. Esta situação é comum em:

- Cargas diárias em ambientes OLAP
- Importação de arquivos de texto (flat files) em bancos OLTP

### Dremio

O Dremio é uma plataforma self-service de dados como serviço (DaaS) que:

- Capacita usuários a descobrir, selecionar, acelerar e compartilhar dados independentemente da localização, volume ou estrutura
- Gerencia dados distribuídos em diversas tecnologias (bancos relacionais, NoSQL, sistemas de arquivos, Hadoop)
- Funciona como uma plataforma Data Lakehouse (combinando funcionalidades de data warehouse com a flexibilidade de data lakes)

#### Segurança no Dremio

O Dremio atende a requisitos de segurança para diferentes frameworks e certificações:

- **SOC 2 Tipo 2:** Conformidade com os controles do Instituto Americano (AICPA)
- **ISO 27001:** Operação de sistema de gerenciamento de segurança da informação em conformidade com padrões internacionais

#### ISO 27001

A ISO 27001 é a norma que define requisitos para um Sistema de Gestão da Segurança da Informação (SGSI), incluindo:

- Abordagem baseada em risco para estabelecer, implementar e monitorar a segurança
- Base para certificação empresarial em gestão da segurança da informação
- Única norma internacional auditável para SGSI
- Complementada pela ISO 27002 (código de práticas com controles)

## Camadas de Consumo por Serviços

### Data Services Layers (DSL)

Uma camada de consumo ou Data Services Layer é uma ferramenta que se posiciona entre usuários de dados e fontes de dados. Ela:

- Recebe consultas SQL como entrada (de ferramentas BI, CLI, ODBC/JDBC)
- Gerencia a execução da consulta, acessando as fontes necessárias
- Pode unir dados entre diferentes fontes
- Expõe fontes de dados subjacentes como serviços de dados (geralmente web services)

As DSL proporcionam serviços de dados discretos, projetados para responder a consultas específicas de maneira eficiente, com velocidade, agilidade e facilidade de gerenciamento.

### GraphQL

GraphQL é uma linguagem de consulta flexível que usa um sistema de tipo para retornar dados de forma eficiente com consultas dinâmicas. Diferente do SQL (específico para bancos relacionais), o GraphQL é adequado para APIs construídas sobre bancos NoSQL.

O nome "Graph" refere-se à modelagem de dados em formato de grafo, permitindo definir dados usando schemas. O resultado é um paradigma similar ao formato JSON:

```graphql
type User {
  id: ID
  name: String
  email: String
  bio: String
}
```

#### Consultas e Mutations no GraphQL

**Consultas (Queries)** - Para buscar dados:
```graphql
query getUsers {
  users {
    name
    bio
  }
}

query getUserById {
  user(id: "123") {
    name
    bio
  }
}
```

**Mutations** - Para criar, alterar ou deletar dados:
```graphql
mutation createUser(name: "João", email: "...", bio: "...") {
  id
  name
  email
  bio
}

mutation updateUser(id: "123", ...) {
  id
  name
  email
  bio
}

mutation deleteUser(id: "123") {
  id
  name
  email
  bio
}
```

#### GraphQL vs REST

O GraphQL está se tornando uma alternativa forte ao REST por várias razões:

**REST:**
- Requer diferentes rotas para diferentes operações (GET /users, GET /users/:id, etc.)
- Necessita de métodos HTTP específicos para cada operação (GET, POST, PUT, DELETE)
- Exige códigos de status, versionamento e outras complexidades

**GraphQL:**
- Utiliza uma única rota para todas as requisições
- As operações são definidas por queries e mutations
- Elimina a necessidade de códigos de status (erros são retornados no corpo da resposta)
- Dispensa versionamento, pois novos campos podem ser adicionados sem alterar queries existentes

#### Vantagens do GraphQL:

- Especificação para consumo de dados com modelagem visual através de schemas
- Uso de queries para chamadas ao servidor
- Esquemas e tipos para modelagem de dados
- Queries e Mutations para leitura e alteração
- Implementação disponível em diversas linguagens de programação

## Plataformas Self-Service

### Importância do Self-Service em Dados

O self-service em dados é um tipo de sistema de análise que ganhou popularidade pela autonomia que proporciona aos usuários não técnicos. O nome vem dessa característica autossuficiente que permite a extração de relatórios baseados em indicadores definidos pelo próprio usuário.

As plataformas se tornaram cada vez mais interativas, dispensando a necessidade de profissionais especializados em TI para a análise de dados. Isso desafogou as equipes de TI e simplificou o processo de obtenção de insights.

### Vantagens das plataformas Self-Service:

- Permitem que usuários criem e editem seus próprios relatórios e painéis
- Aceleram o desenvolvimento por não dependerem do suporte de TI
- Oferecem recursos interativos que facilitam a descoberta de dados
- Distribuem informações de maneira simples
- Disponibilizam análises em tempo quase real
- Democratizam o acesso aos dados na organização

### Exemplos de Ferramentas Self-Service:

#### Power BI
- Desenvolvido pela Microsoft (inicialmente como "Project Crescent")
- Opção popular para empresas que usam o ecossistema Windows/Office/Azure
- Economicamente acessível para organizações que desejam fornecer BI para todos
- Integra funções de visualização, ETL e criação de DW

#### Qlik Sense
- Evolução do QlikView para o modelo de BI self-service
- Baseado em um mecanismo de indexação associativa de dados em memória
- Ferramenta capaz para análise e descoberta de dados
- Conecta-se a praticamente qualquer banco de dados SQL

#### Tableau
- Destacado pela facilidade de identificar padrões visuais
- Forte enfoque na visualização intuitiva e interativa
- Desenvolvido com base em princípios cognitivos de reconhecimento visual

#### Amazon QuickSight
- Executado inteiramente na nuvem AWS
- Bom acesso às fontes de dados da Amazon
- Oferece análise básica a um preço acessível
- Similar ao Power BI, mas sem dependência de desktop
- Conecta-se a diversas fontes de dados e permite preparar conjuntos de dados

#### Dremio
- Plataforma self-service que combina funcionalidades de data warehouse com a flexibilidade de data lake
- Permite análise de autoatendimento em todos os dados da organização

## Design Convergente para Dados

### Arquitetura de Dados Convergente

Nos sistemas e aplicações modernos, os maiores desafios relacionados a dados são:
- A quantidade de informações geradas
- Os múltiplos formatos existentes
- A velocidade em que os dados se modificam

Tradicionalmente, utilizamos diferentes ferramentas para diferentes necessidades:
- Bancos de dados ou sistemas de arquivos para armazenamento
- Mecanismos de cache para acelerar buscas complexas
- Índices para permitir buscas por palavras-chave e consultas ad-hoc
- Brokers de eventos para troca de mensagens entre processos ou sistemas
- Processamento batch para manipular grandes quantidades de dados acumulados

Uma arquitetura de dados convergente propõe unificar essas diferentes ferramentas em uma plataforma integrada, onde:
- Quase todos os tipos de ferramentas e dados são suportados
- Há suporte para schema on write e schema on read
- Inclui funcionalidades de cache e filas
- Quando um recurso não é suportado nativamente, o acesso é virtualizado
- Uma interface unificada permite consumir informações de forma transparente


---
