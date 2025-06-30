# Bancos de Dados NoSQL (NoSQL Databases)

## Sumário
- [Introdução](#introdução)
- [Características dos Bancos de Dados NoSQL](#características-dos-bancos-de-dados-nosql)
  - [O que é um banco de dados NoSQL?](#o-que-é-um-banco-de-dados-nosql)
  - [Principais características](#principais-características)
  - [Persistência poliglota](#persistência-poliglota)
  - [Propriedades BASE vs ACID](#propriedades-base-vs-acid)
  - [Escalabilidade Horizontal](#escalabilidade-horizontal)
  - [Schema-less (Ausência de esquema)](#schema-less-ausência-de-esquema)
  - [Suporte nativo à replicação](#suporte-nativo-à-replicação)
  - [API (Application Programming Interface)](#api-application-programming-interface)
  - [O que o NoSQL não é](#o-que-o-nosql-não-é)
- [Definição de Negócios e Motivação](#definição-de-negócios-e-motivação)
  - [Contexto de Negócios](#contexto-de-negócios)
  - [Motivação](#motivação)
  - [Big Data](#big-data)
- [Modelos de Transações](#modelos-de-transações)
  - [Teorema CAP](#teorema-cap)
  - [Comparação ACID x BASE](#comparação-acid-x-base)
  - [Quando usar SQL vs NoSQL](#quando-usar-sql-vs-nosql)
- [Tipos de Bancos NoSQL](#tipos-de-bancos-nosql)
  - [Linguagens de Marcação](#linguagens-de-marcação)
  - [Hashing](#hashing)
  - [Classificação dos Bancos NoSQL](#classificação-dos-bancos-nosql)
    - [Chave/Valor (Key/Value)](#chavevalor-keyvalue)
    - [Armazém de Documentos (Document Store)](#armazém-de-documentos-document-store)
    - [Orientado a Coluna (Column-oriented)](#orientado-a-coluna-column-oriented)
    - [Grafo (Graph)](#grafo-graph)
    - [Motor de Busca (Search Engine)](#motor-de-busca-search-engine)
- [Principais Bancos NoSQL do Mercado](#principais-bancos-nosql-do-mercado)

## Introdução

O surgimento dos bancos de dados NoSQL está diretamente relacionado à evolução da Web 2.0 e à explosão de dados que vivenciamos nas últimas décadas. Estamos em uma era onde o número de dispositivos conectados já supera a população mundial, criando um cenário sem precedentes para o armazenamento e processamento de dados.

A Web 2.0 transformou o ambiente online em um espaço colaborativo, permitindo que usuários não apenas consumam conteúdo, mas também contribuam ativamente para a construção de plataformas e serviços. Essa mudança trouxe consigo desafios significativos para as tecnologias tradicionais de armazenamento de dados.

Entre as principais fontes de dados que impulsionaram essa evolução, podemos destacar:

- **Redes Sociais**: Gerando bilhões de interações diárias
- **Internet das Coisas (IoT)**: Conectando dispositivos que emitem dados constantemente
- **Textos não estruturados**: Como e-mails, documentos, mensagens
- **Dispositivos sensoriais**: Microfones, câmeras, GPS, etc.
- **Aplicações interativas**: Jogos, plataformas colaborativas

Essa avalanche de dados heterogêneos expôs as limitações dos bancos de dados relacionais tradicionais, especialmente em relação ao processamento de alto volume, alta velocidade e grande variedade de dados (os "3Vs" do Big Data). O overhead relacionado à manutenção da consistência dos dados em sistemas distribuídos se tornou um gargalo significativo.

Neste contexto, os bancos de dados NoSQL emergiram como solução para os desafios de escalabilidade, desempenho e flexibilidade no armazenamento e processamento de grandes volumes de dados, especialmente em ambientes distribuídos e na nuvem.

## Características dos Bancos de Dados NoSQL

### O que é um banco de dados NoSQL?

O termo NoSQL (Not Only SQL) refere-se a uma categoria de sistemas de gerenciamento de bancos de dados que divergem do modelo relacional tradicional. Surgidos em 1998 como alternativa ao modelo relacional, os sistemas NoSQL não foram criados para invalidar ou substituir completamente os bancos de dados relacionais, mas sim para oferecer novas opções de arquitetura e manipulação de diferentes modelos de dados.

É importante destacar que o termo "NoSQL" pode ser enganoso, pois não significa "ausência de SQL", mas sim "não apenas SQL". Esta terminologia foi adotada pela comunidade como forma de reconhecer a utilidade dos modelos tradicionais e evitar polarizações desnecessárias nas discussões técnicas.

### Principais características

Os bancos de dados NoSQL geralmente apresentam a maioria das seguintes características:

- **Não-relacional**: Não seguem o modelo relacional de tabelas e esquemas rígidos
- **Distribuído**: Projetados para operar em clusters de servidores
- **Código aberto**: Na maioria dos casos, são projetos de código aberto
- **Escalabilidade horizontal**: Capacidade de adicionar mais servidores para aumentar a capacidade
- **Schema-less/Esquema flexível**: Não requerem esquema fixo predefinido
- **Suporte à replicação nativo**: Replicação de dados integrada à arquitetura
- **APIs simples**: Interfaces de programação simplificadas
- **Processamento rápido**: Otimizados para recuperação rápida de informações

### Persistência poliglota

Uma característica importante do ecossistema NoSQL é o conceito de **persistência poliglota**, que se refere a aplicações que acessam dois ou mais SGBDs com modelos de dados diferentes. Isso ocorre devido à natureza heterogênea dos dados que essas aplicações manipulam.

Alguns autores também se referem a este conceito como "SGBD NoSQL multimodelo", onde uma única solução pode oferecer diferentes modelos de armazenamento de dados.

Exemplo prático:
```
Uma aplicação de e-commerce moderna pode utilizar:
- MongoDB (banco de documentos) para armazenar dados de produtos
- Redis (chave-valor) para gerenciar sessões de usuários
- Neo4J (grafo) para implementar um sistema de recomendações
- Cassandra (colunar) para armazenar logs de eventos
```

### Propriedades BASE vs ACID

Os bancos de dados NoSQL implementam as propriedades BASE (Basically Available, Soft-state, Eventually consistent), que contrastam com as propriedades ACID (Atomicity, Consistency, Isolation, Durability) dos bancos relacionais.

#### ACID (Bancos Relacionais)

- **Atomicidade**: Transações são executadas por completo ou não são executadas
- **Consistência**: Transações mantêm o banco em estado válido
- **Isolamento**: Transações em andamento não interferem umas nas outras
- **Durabilidade**: Dados validados são persistidos mesmo em caso de falha do sistema

#### BASE (Bancos NoSQL)

- **Basically Available**: Prioriza a disponibilidade, mesmo que temporariamente inconsistente
- **Soft-state**: Permite imprecisão temporária, reduzindo recursos consumidos
- **Eventually consistent**: Garante que o sistema eventualmente atinge um estado consistente

A principal diferença é que, enquanto ACID força a consistência ao final de cada operação, BASE permite que o banco de dados eventualmente atinja um estado consistente, priorizando disponibilidade e desempenho.

### Escalabilidade Horizontal

A escalabilidade horizontal é uma característica fundamental dos bancos NoSQL. Diferentemente da escalabilidade vertical (aumentar os recursos de um único servidor), a escalabilidade horizontal consiste em aumentar o número de nós (máquinas) disponíveis para o armazenamento e processamento dos dados.

Esta abordagem é essencial para lidar com grandes volumes de dados, pois permite distribuir a carga entre vários servidores. Uma técnica comum para implementar esta escalabilidade é o **Sharding**, que consiste em dividir os dados em várias tabelas, armazenando-as ao longo de múltiplos nós de uma rede.

![Sharding](https://miro.medium.com/v2/resize:fit:1400/1*M-QgPXa_rEjwVdDOWuRKOA.png)
*Exemplo de Sharding: Divisão dos dados entre múltiplos servidores*

### Schema-less (Ausência de esquema)

A ausência completa ou parcial de esquema que define a estrutura dos dados é uma característica marcante dos bancos NoSQL. Esta flexibilidade simplifica a escalabilidade do sistema e aumenta sua disponibilidade, embora não garanta a integridade dos dados da mesma forma que os sistemas relacionais.

Na prática, isso significa que:
- Não é necessário definir previamente a estrutura dos dados
- É possível adicionar ou remover campos sem alterar toda a estrutura
- Documentos ou registros diferentes podem ter estruturas diferentes
- Adaptação mais rápida a mudanças nos requisitos de negócio

### Suporte nativo à replicação

Para prover escalabilidade, bancos NoSQL geralmente oferecem replicação nativa dos dados, ajudando a diminuir o tempo de recuperação das informações. Existem duas abordagens principais para replicação:

1. **Master-Slave**:
   - Um servidor master é a fonte primária de dados
   - Servidores slave copiam todas as alterações realizadas no master
   - Leituras podem ser distribuídas, mas escritas são centralizadas

2. **Multi-Master**:
   - Múltiplos servidores master podem aceitar escritas
   - Ideal para aplicações distribuídas geograficamente
   - Utiliza topologia de anel para manter todas as regiões sincronizadas

### API (Application Programming Interface)

Nos bancos NoSQL, o foco não está na forma como os dados são acessados, mas sim em como são recuperados. O uso de APIs simplifica o acesso às informações, permitindo que qualquer aplicação possa interagir com o banco de forma rápida e eficiente.

Este conceito está fortemente vinculado à arquitetura de microsserviços (MSA - Microservices Architecture), onde diferentes componentes de um sistema se comunicam através de interfaces bem definidas.

### O que o NoSQL não é

É importante esclarecer alguns equívocos comuns sobre NoSQL:

- **Não é sobre a ausência da linguagem SQL**: Muitos bancos NoSQL suportam variantes de SQL ou outras linguagens de consulta
- **Não é apenas código aberto**: Embora muitos sistemas sejam de código aberto, existem produtos comerciais que implementam conceitos NoSQL
- **Não é apenas para Big Data**: NoSQL não se limita a volumes massivos de dados, mas também foca em variabilidade e agilidade
- **Não é sinônimo de computação em nuvem**: Sistemas NoSQL podem ser executados em nuvem ou em servidores corporativos locais
- **Não se trata apenas de uso eficiente de RAM e SSD**: Embora muitos sistemas otimizem o uso de recursos de hardware, isso não é uma característica definidora

## Definição de Negócios e Motivação

### Contexto de Negócios

As organizações modernas estão cada vez mais focadas na criação de plataformas consolidadas que permitam acesso simplificado aos dados e descoberta de conhecimento. Este movimento está intimamente ligado às transformações que as infraestruturas de TI passaram no passado recente:

- **Otimização**: Melhorar o uso dos recursos disponíveis
- **Racionalização**: Eliminar redundâncias e ineficiências
- **Automação**: Reduzir intervenção manual em processos
- **Simplificação**: Tornar mais acessível e compreensível

A computação em nuvem emergiu como o paradigma dominante para alcançar estes ideais, oferecendo infraestrutura de TI (servidores, armazenamentos e soluções de rede) como serviço. Consequentemente, estas infraestruturas estão sendo modernizadas para serem:

- Baseadas em políticas
- Definidas por software
- Orientadas a serviços
- Programáveis
- Preparadas para a era do Big Data

### Motivação

A motivação principal para a adoção de tecnologias NoSQL é a necessidade de lidar com a enorme quantidade de dados, provenientes de várias fontes diferentes, complexos e dinâmicos, que demandam tecnologias e técnicas específicas para armazenamento, análise e visualização.

Embora os bancos de dados relacionais possam escalar, quanto maior o tamanho, mais custosa é a operação – tanto em termos de consumo de recursos quanto financeiramente. Os bancos NoSQL foram desenvolvidos para superar estas limitações, oferecendo:

- **Escalabilidade mais econômica**
- **Flexibilidade de esquema**
- **Melhor desempenho para certos tipos de consultas**
- **Maior disponibilidade em sistemas distribuídos**

### Big Data

Big Data é o termo usado para representar grandes volumes de dados que não se adequam ao modelo relacional tradicional. Ele é frequentemente caracterizado pelos "3Vs":

- **Volume**: Quantidade massiva de dados
- **Velocidade**: Rápida geração e processamento de dados
- **Variedade**: Diversidade de formatos e fontes

Sistemas de banco de dados de nova geração, incluindo NoSQL, foram desenvolvidos para armazenar, recuperar, agregar, filtrar e analisar big data com eficiência.

```
Exemplo: Uma rede social com milhões de usuários
- Volume: Bilhões de postagens, fotos, vídeos e interações
- Velocidade: Milhares de novas interações por segundo
- Variedade: Texto, imagens, vídeos, metadados geoespaciais, etc.
```

## Modelos de Transações

O controle de transações é crucial em ambientes de computação distribuída, especialmente considerando desempenho e consistência. Dois modelos principais são utilizados: ACID (em bancos relacionais) e BASE (em muitos sistemas NoSQL).

É importante destacar que tanto sistemas relacionais quanto NoSQL podem implementar controles transacionais, mas diferem na quantidade de esforço exigida dos desenvolvedores e na camada onde esses controles são implementados.

### Teorema CAP

O Teorema CAP (também conhecido como Teorema de Brewer) estabelece que é impossível para qualquer sistema distribuído fornecer simultaneamente todos os três recursos abaixo:

- **Consistency (Consistência)**: todos os nós veem os mesmos dados ao mesmo tempo
- **Availability (Disponibilidade)**: garantia de resposta em cada solicitação
- **Partition Tolerance (Tolerância a partição)**: o sistema continua operando apesar de falhas na rede

Segundo o teorema, qualquer sistema distribuído pode garantir no máximo dois destes três atributos. Com base nisso, podemos classificar os sistemas em:

#### Sistemas CA (Consistency/Availability)
- Priorizam consistência forte e alta disponibilidade
- Não lidam bem com falhas de partição
- Exemplo: configurações clássicas de bancos relacionais

#### Sistemas CP (Consistency/Partition Tolerance)
- Priorizam consistência forte e tolerância a particionamento
- Sacrificam um pouco da disponibilidade
- Exemplos: BigTable, HBase, MongoDB

#### Sistemas AP (Availability/Partition Tolerance)
- Priorizam disponibilidade mesmo com particionamento
- Aceitam escritas sempre e sincronizam depois
- Exemplos: Amazon Dynamo, Cassandra, Riak

![Teorema CAP](https://miro.medium.com/v2/resize:fit:1400/1*rxTP-_STj-QRDt1X9fdVlA.png)
*Representação visual do Teorema CAP*

### Comparação ACID x BASE

| **Aspecto** | **ACID (SQL)** | **BASE (NoSQL)** |
|-------------|----------------|-----------------|
| **Foco principal** | Consistência | Disponibilidade |
| **Esquema** | Rígido | Flexível ou ausente |
| **Transações** | Complexas e aninhadas | Simples |
| **Integridade** | Garantida pelo sistema | Responsabilidade da aplicação |
| **Disponibilidade** | Pode ser comprometida por bloqueios | Alta disponibilidade |
| **Adaptação a mudanças** | Requer alterações complexas | Flexível e adaptável |
| **Escalabilidade** | Principalmente vertical | Principalmente horizontal |

### Quando usar SQL vs NoSQL

A escolha entre SQL e NoSQL deve ser baseada nas necessidades específicas de cada aplicação:

| **UTILIZE BANCOS RELACIONAIS** | **UTILIZE NoSQL** |
|-------------------------------|-------------------|
| Aplicações centralizadas | Aplicações descentralizadas (Web, IoT, Big Data) |
| Sem requisitos de altíssima disponibilidade | Quando não pode haver interrupção na gravação de dados |
| Geração de dados em velocidade média | Geração de dados em alta velocidade (sensores) |
| Poucas fontes geradoras de dados | Muitas fontes geradoras de dados |
| Dados estruturados | Dados semi ou não-estruturados |
| Transações complexas | Transações simples |
| Armazenamento de médio volume | Alto volume de armazenamento |

Exemplo prático de decisão:
```
Cenário: Sistema de gestão financeira
- Necessita garantia de consistência em transações
- Dados altamente estruturados
- Relacionamentos complexos entre entidades
- Volume moderado de dados
- Operações CRUD padronizadas

Recomendação: Banco de dados relacional (SQL)
```

```
Cenário: Aplicação IoT para monitoramento de temperaturas
- Milhares de sensores enviando dados constantemente
- Alta disponibilidade para receber leituras
- Dados homogêneos mas em grande volume
- Consultas simples e previsíveis

Recomendação: Banco de dados NoSQL (orientado a coluna)
```

## Tipos de Bancos NoSQL

### Linguagens de Marcação

Antes de explorarmos os tipos de bancos NoSQL, é importante entender as linguagens de marcação comumente utilizadas para estruturar dados.

**Linguagens de marcação** são sistemas usados para definir padrões e formatos de exibição dentro de um documento. Elas funcionam para especificar como um determinado conteúdo será visualizado ou como os dados serão distribuídos, utilizando marcadores ou tags.

Os dois formatos mais relevantes no contexto de NoSQL são:

#### XML (eXtensible Markup Language)
- Formato flexível e extensível
- Permite a criação de tags personalizadas
- Foca na estrutura da informação
- Exemplo:
```xml
<produto>
  <nome>Smartphone XYZ</nome>
  <preco>999.99</preco>
  <caracteristicas>
    <tela>6.5 polegadas</tela>
    <memoria>128GB</memoria>
  </caracteristicas>
</produto>
```

#### JSON (JavaScript Object Notation)
- Formato leve e de fácil leitura
- Baseado em pares chave-valor
- Amplamente utilizado em aplicações web
- Exemplo:
```json
{
  "produto": {
    "nome": "Smartphone XYZ",
    "preco": 999.99,
    "caracteristicas": {
      "tela": "6.5 polegadas",
      "memoria": "128GB"
    }
  }
}
```

Comparação entre XML e JSON:

| **Característica** | **XML** | **JSON** |
|--------------------|:-------:|:--------:|
| Natureza auto-descritiva | ✓ | ✓ |
| Representar informação complexa | ✓ | ✓ |
| Transportar informações em AJAX | ✓ | ✓ |
| Independência de linguagem | ✓ | ✓ |
| Codificação em vários formatos | ✓ | ✗ |
| Comentários no arquivo | ✓ | ✗ |
| Leveza e agilidade de tráfego | ✗ | ✓ |
| Requisições AJAX em domínio cruzado | ✗ | ✓ |

### Hashing

Outro conceito fundamental para entender os bancos NoSQL é o **hashing**, também conhecido como tabela de dispersão ou método de cálculo de endereço. Esta técnica é amplamente utilizada para o armazenamento e recuperação eficiente de dados.

O hashing é uma generalização de um array simples, funcionando como uma estrutura de dados do tipo dicionário. A técnica aplica uma função sobre parte da informação (chave) para calcular o índice onde a informação deve ser armazenada ou recuperada.

Exemplo simplificado de hashing:
```
Função hash simples: h(x) = x % 10 (resto da divisão por 10)

Armazenamento:
- Para armazenar o valor 42 com a chave "idade":
  - h("idade") = 5 (supondo que o hash de "idade" seja 5)
  - Armazena 42 na posição 5 da tabela

Recuperação:
- Para recuperar o valor associado à chave "idade":
  - h("idade") = 5
  - Retorna o valor armazenado na posição 5 (42)
```

Em casos de volumes muito grandes de dados, podem ocorrer colisões (duas chaves diferentes gerando o mesmo índice). Existem várias técnicas para tratar estas colisões, como encadeamento (chaining) e endereçamento aberto (open addressing).

### Classificação dos Bancos NoSQL

Os bancos de dados NoSQL podem ser classificados em cinco categorias principais, cada uma com características e casos de uso específicos:

#### Chave/Valor (Key/Value)

O modelo chave/valor é o mais simples de todos os bancos NoSQL. Ele armazena apenas pares de chaves com valores associados, sem se preocupar com a estrutura interna dos valores.

**Estrutura:**
- Cada item consiste em uma chave única e um valor associado
- A chave é um identificador para recuperar o valor
- O valor pode ser qualquer coisa: string, número, objeto JSON, etc.

**Vantagens:**
- Altamente particionáveis e escaláveis horizontalmente
- Simplicidade de implementação
- Desempenho excepcional para operações de leitura/escrita por chave
- Ideal para caches e dados de sessão

**Desvantagens:**
- Não adequado para aplicações complexas devido à simplicidade
- Busca imprecisa (sem usar o índice) perde performance conforme o volume de dados aumenta
- Não projetado para manter consistência em várias transações simultâneas

**Casos de uso:**
- Armazenamento de dados de sessão de usuário
- Armazenamento de preferências e configurações
- Cache de objetos
- Contadores e estatísticas em tempo real

**Exemplos de bancos:**
- Redis
- Amazon DynamoDB
- Riak
- Oracle NoSQL Database

![Modelo Chave/Valor](https://www.3pillarglobal.com/wp-content/uploads/2015/08/key-value-store.png)
*Representação do modelo chave/valor*

#### Armazém de Documentos (Document Store)

Os bancos de dados orientados a documentos armazenam dados em formato de documentos semi-estruturados, geralmente em formato JSON ou XML. A principal característica é a organização de dados livre de esquemas rígidos.

**Estrutura:**
- Armazena documentos completos, que contêm pares chave-valor
- Cada documento pode ter estrutura diferente
- Suporta documentos aninhados e arrays
- Oferece mecanismos de consulta para pesquisar por atributos específicos

**Vantagens:**
- Modelagem de dados flexível, ideal para aplicações que evoluem constantemente
- Alta performance de escrita com priorização da disponibilidade
- Poderosos mecanismos de indexação e consulta
- Estrutura natural para muitos tipos de dados da vida real

**Desvantagens:**
- Não projetado para transações complexas de fluxo empresarial
- Pode não ser a melhor escolha para dados altamente relacionados
- Menor garantia de integridade dos dados

**Casos de uso:**
- Gerenciamento de conteúdo
- Catálogos de produtos
- Perfis de usuários
- Blogs e plataformas de publicação
- Aplicações de e-commerce

**Exemplos de bancos:**
- MongoDB
- Couchbase
- Amazon DocumentDB
- Firebase Firestore

Exemplo de documento no MongoDB:
```json
{
  "_id": "5f8d0d55b54764424b8ce2a4",
  "nome": "João Silva",
  "idade": 35,
  "endereco": {
    "rua": "Av. Principal",
    "numero": 123,
    "cidade": "São Paulo"
  },
  "telefones": [
    {"tipo": "residencial", "numero": "11-5555-1234"},
    {"tipo": "celular", "numero": "11-98765-4321"}
  ],
  "ativo": true
}
```

#### Orientado a Coluna (Column-oriented)

Bancos de dados orientados a coluna armazenam dados em tabelas, mas organizam e indexam os dados por coluna, em vez de por linha. Isso permite uma melhor compressão e desempenho em consultas analíticas.

**Estrutura:**
- Armazena dados em registros com colunas dinâmicas
- Nomes das colunas e chaves não são fixos
- Um registro pode ter bilhões de colunas
- Similar a um sistema chave/valor de duas dimensões

**Vantagens:**
- Consultas mais rápidas para operações analíticas
- Ignora dados não relevantes rapidamente
- Melhor compressão devido à homogeneidade dos dados em cada coluna
- Eficiente para operações em subconjuntos de colunas

**Desvantagens:**
- Ineficiente para recuperar múltiplos campos de uma mesma linha
- Não otimizado para consultas de valores específicos
- Menos eficiente para altos volumes de inserções e atualizações

**Casos de uso:**
- Business Intelligence e Analytics
- Data Warehousing
- Sistemas de informações geográficas
- Armazenamento de dados de preferências de usuários

**Exemplos de bancos:**
- Apache Cassandra
- HBase
- Google Bigtable
- Amazon SimpleDB

![Orientado a Coluna](https://www.scylladb.com/wp-content/uploads/column-oriented-database.png)
*Modelo orientado a coluna vs. orientado a linha*

#### Grafo (Graph)

Bancos de dados de grafo são projetados para representar e analisar relações entre entidades. Eles armazenam entidades como nós e relacionamentos como arestas, permitindo consultas complexas sobre essas relações.

**Estrutura:**
- Nós (vértices): representam entidades
- Relacionamentos (arestas): conectam os nós
- Propriedades: atributos dos nós e relacionamentos

**Vantagens:**
- Representação rica de dados e suas relações
- Capacidade de descobrir padrões e informações "ocultas"
- Flexibilidade para modificação e evolução
- Consultas de travessia de grafo altamente eficientes

**Desvantagens:**
- Mais difíceis de escalar horizontalmente
- Complexidade ao implementar em múltiplos servidores
- Curva de aprendizado mais acentuada

**Casos de uso:**
- Redes sociais
- Sistemas de recomendação
- Detecção de fraude
- Master Data Management (MDM)
- Gerenciamento de identidade e acesso

**Exemplos de bancos:**
- Neo4j
- Amazon Neptune
- JanusGraph
- OrientDB

Exemplo de grafo simples:
```
[Pessoa:Ana] -[:AMIGO_DE]-> [Pessoa:Carlos]
              <-[:TRABALHA_COM]-
[Pessoa:Ana] -[:MORA_EM]-> [Cidade:São Paulo]
[Pessoa:Carlos] -[:MORA_EM]-> [Cidade:Rio de Janeiro]
```

![Banco de Grafo](https://neo4j.com/wp-content/uploads/graph-example.jpg)
*Exemplo de banco de dados de grafo*

#### Motor de Busca (Search Engine)

Bancos de dados de motor de busca são otimizados para pesquisar grandes volumes de texto e retornar resultados relevantes. Eles combinam conceitos de NoSQL com algoritmos de busca avançados.

**Características:**
- Indexação de texto completo
- Suporte a expressões complexas de busca
- Ranqueamento e agrupamento de resultados
- Busca geoespacial
- Processamento distribuído

**Casos de uso:**
- Sistemas de busca em sites e aplicações
- Análise de logs
- Monitoramento de eventos
- Análise de dados não estruturados

**Exemplos de bancos:**
- Elasticsearch
- Apache Solr
- Algolia
- Amazon CloudSearch

Exemplo de consulta Elasticsearch:
```json
{
  "query": {
    "bool": {
      "must": [
        { "match": { "conteudo": "banco de dados" } }
      ],
      "filter": [
        { "term": { "categoria": "tecnologia" } },
        { "range": { "data_publicacao": { "gte": "2023-01-01" } } }
      ]
    }
  },
  "sort": [
    { "relevancia": "desc" },
    { "data_publicacao": "desc" }
  ]
}
```

## Principais Bancos NoSQL do Mercado

### Chave/Valor (Key/Value)
- **Redis**: In-memory database com estruturas de dados avançadas
- **Amazon DynamoDB**: Serviço gerenciado de banco de dados NoSQL da AWS
- **Riak**: Banco de dados distribuído focado em alta disponibilidade
- **Oracle NoSQL Database**: Solução NoSQL da Oracle

### Armazém de Documentos (Document Store)
- **MongoDB**: O banco de documentos mais popular, com uma grande comunidade
- **Couchbase**: Combina características de documento e chave-valor
- **Firebase Firestore**: Solução do Google para aplicações móveis e web
- **Amazon DocumentDB**: Solução compatível com MongoDB da AWS

### Orientado a Coluna (Column-oriented)
- **Apache Cassandra**: Banco de dados distribuído com alta escalabilidade
- **HBase**: Banco de dados distribuído do ecossistema Hadoop
- **Google Bigtable**: Serviço de banco de dados NoSQL da Google Cloud
- **Amazon SimpleDB**: Serviço de banco de dados não relacional da AWS

### Grafo (Graph)
- **Neo4j**: O banco de grafos mais popular
- **Amazon Neptune**: Serviço gerenciado de banco de dados de grafos


