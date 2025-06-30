# Arquitetura de Dados: Conceitos Fundamentais e Tecnologias Modernas
# Data Architecture: Fundamental Concepts and Modern Technologies

## Sumário / Summary
- [Introdução / Introduction](#introdução--introduction)
- [Camadas em Dados / Data Layers](#camadas-em-dados--data-layers)
  - [Camadas de Armazenamento / Storage Layers](#camadas-de-armazenamento--storage-layers)
- [ORMs (Object-Relational Mappers)](#orms-object-relational-mappers)
  - [ORMs vs ODMs](#orms-x-odmx)
  - [Integração com Outras Camadas / Integration with Other Layers](#integração-camada-de-armazenamento-com-outras-camadas)
- [Tipos de Bancos de Dados / Database Types](#tipos-de-bancos-de-dados--database-types)
  - [Bancos de Dados Relacionais / Relational Databases](#banco-de-dados-relacional--relational-database)
  - [Normalização / Normalization](#normalização--normalization)
  - [Modelos de Dados / Data Models](#modelos-de-dados--data-models)
- [Bancos de Dados NoSQL / NoSQL Databases](#bancos-de-dados-nosql--nosql-databases)
  - [Características / Characteristics](#nosql---características--characteristics)
  - [Modelos de Bancos NoSQL / NoSQL Database Models](#modelos-de-bancos-nosql--nosql-database-models)
  - [Ausência de Esquema / Schema-less Design](#bancos-de-dados-nosql---schema--nosql-databases---schema)
- [Bancos de Dados NewSQL / NewSQL Databases](#bancos-de-dados-newsql--newsql-databases)
  - [Comparativo: SQL x NoSQL x NewSQL](#sql-x-nosql-x-newsql)
- [Teorema CAP / CAP Theorem](#teorema-cap--cap-theorem)
  - [Consistência Eventual / Eventual Consistency](#consistência-eventual--eventual-consistency)
- [Escalabilidade / Scalability](#escalabilidade--scalability)
- [Sistemas de Arquivos Distribuídos / Distributed File Systems](#sistemas-de-arquivos-distribuídos--distributed-file-systems)
  - [Requisitos / Requirements](#requisitos-de-um-sistemas-de-arquivos--file-system-requirements)
  - [Arquitetura / Architecture](#arquitetura-do-sad--dfs-architecture)
- [Apache Hadoop](#apache-hadoop)
  - [HDFS (Hadoop Distributed File System)](#hdfs)
  - [Módulos do Framework / Framework Modules](#módulos-do-framework-do-apache-hadoop--apache-hadoop-framework-modules)
- [Computação em Nuvem / Cloud Computing](#computação-em-nuvem--cloud-computing)
  - [Arquiteturas Monolíticas / Monolithic Architectures](#arquiteturas-monolíticas--monolithic-architectures)
  - [Arquitetura de Microsserviços / Microservices Architecture](#arquitetura-de-microserviços--microservices-architecture)
- [Containers](#containers)
  - [Orquestração de Containers / Container Orchestration](#ferramentas-de-orquestração-de-containers--container-orchestration-tools)
- [Boas Práticas e Considerações / Best Practices and Considerations](#boas-práticas-e-considerações--best-practices-and-considerations)

## Introdução / Introduction

Este documento apresenta um glossário abrangente sobre conceitos fundamentais de arquitetura de dados, abordando desde os princípios básicos até as tecnologias mais recentes utilizadas no mercado. O conteúdo foi estruturado para servir tanto como material de estudo quanto como referência técnica para profissionais da área de dados.

This document presents a comprehensive glossary of fundamental data architecture concepts, covering everything from basic principles to the latest technologies used in the market. The content has been structured to serve both as study material and as a technical reference for data professionals.

## Camadas em Dados / Data Layers

As camadas em dados referem-se às diferentes etapas ou níveis de processamento e armazenamento em um sistema. Cada camada desempenha uma função específica no fluxo de dados, formando uma arquitetura coesa e eficiente.

### Principais camadas em uma arquitetura de dados:

1. **Camada de Ingestão (Ingestion Layer)**: Responsável pela coleta e importação de dados de diversas fontes (APIs, bancos de dados, arquivos, streams, etc.).

2. **Camada de Armazenamento (Storage Layer)**: Onde os dados são persistidos, utilizando diferentes tecnologias conforme as necessidades (bancos relacionais, NoSQL, sistemas de arquivos distribuídos).

3. **Camada de Processamento (Processing Layer)**: Realiza transformações, limpeza, agregações e demais operações sobre os dados brutos.

4. **Camada de Análise e Modelagem (Analysis and Modeling Layer)**: Responsável pela aplicação de técnicas estatísticas, algoritmos de machine learning e criação de modelos analíticos.

5. **Camada de Apresentação e Visualização (Presentation and Visualization Layer)**: Expõe os insights e resultados em formatos compreensíveis através de dashboards, relatórios e interfaces.

### Camadas de Armazenamento / Storage Layers

A Camada de Armazenamento é fundamental na arquitetura de sistemas de dados, responsável por gerenciar e persistir os dados consumidos e produzidos pela aplicação.

#### Principais funções:

- **Armazenamento de Dados**: Persistência dos dados em meios físicos ou virtuais
- **Recuperação de Dados**: Mecanismos eficientes para busca e recuperação
- **Transações**: Garantia de atomicidade e consistência nas operações
- **Segurança dos Dados**: Controle de acesso, criptografia e proteção
- **Escalabilidade**: Capacidade de crescer conforme o volume de dados aumenta
- **Backup e Recuperação**: Procedimentos para resiliência e continuidade

#### Tecnologias comuns:

- **Bancos de Dados Relacionais (RDBMS)**: PostgreSQL, MySQL, Oracle, SQL Server
- **Bancos de Dados NoSQL**: MongoDB, Cassandra, Redis, Neo4j
- **Data Lakes e Data Warehouses**: Snowflake, Amazon Redshift, Google BigQuery
- **Sistemas de Arquivos Distribuídos**: HDFS, Amazon S3, Azure Blob Storage

## ORMs (Object-Relational Mappers)

ORMs são ferramentas de software que permitem aos desenvolvedores interagirem com bancos de dados relacionais usando conceitos de programação orientada a objetos, abstraindo a necessidade de escrever queries SQL manualmente.

```python
# Exemplo de ORM em Python usando SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    
# Criar um usuário usando orientação a objetos em vez de SQL
novo_usuario = Usuario(nome="João Silva", email="joao@exemplo.com")
session.add(novo_usuario)
session.commit()
```

### ORMs x ODMx

- **ORMs (Object-Relational Mappers)**: Utilizados com bancos de dados relacionais, mapeiam tabelas para classes e registros para objetos. Exemplos: Hibernate (Java), Entity Framework (.NET), SQLAlchemy (Python).

- **ODMs (Object-Document Mappers)**: Utilizados com bancos de dados orientados a documentos, mapeiam documentos para objetos. Exemplos: Mongoose (JavaScript/MongoDB), MongoEngine (Python/MongoDB).

#### Quando usar cada um:

- **ORM**: Ideal para sistemas com relações complexas entre entidades, onde a normalização e integridade referencial são importantes.

```javascript
// Exemplo de ORM em JavaScript com Sequelize
const Usuario = sequelize.define('Usuario', {
  nome: Sequelize.STRING,
  email: Sequelize.STRING
});

const Pedido = sequelize.define('Pedido', {
  data: Sequelize.DATE,
  valor: Sequelize.DECIMAL
});

// Definindo relacionamento
Usuario.hasMany(Pedido);
Pedido.belongsTo(Usuario);
```

- **ODM**: Preferível para casos com estrutura de dados menos complexa, onde todas as informações relacionadas podem ser armazenadas em um único documento, facilitando a escalabilidade.

```javascript
// Exemplo de ODM em JavaScript com Mongoose
const usuarioSchema = new mongoose.Schema({
  nome: String,
  email: String,
  pedidos: [{
    data: Date,
    valor: Number,
    itens: [{
      produto: String,
      quantidade: Number
    }]
  }]
});

const Usuario = mongoose.model('Usuario', usuarioSchema);
```

### Integração Camada de Armazenamento com Outras Camadas

A camada de armazenamento se integra com diversas outras camadas da arquitetura:

- **Camada de Aplicação**: Fornece dados para lógica de negócios
- **Camada de Integração**: Permite interoperabilidade entre sistemas
- **Camada de Apresentação**: Alimenta interfaces e relatórios

#### Desafios na Camada de Armazenamento de Dados

- **Desempenho**: Otimização de consultas e indexação
- **Gerenciamento de Grandes Volumes**: Estratégias para big data
- **Consistência vs. Disponibilidade**: Equilibrar conforme o teorema CAP
- **Segurança e Compliance**: Atender regulamentações como LGPD/GDPR

#### Tendências e Futuro da Camada de Armazenamento

- **Armazenamento em Nuvem**: Adoção crescente de soluções cloud-native
- **Bancos de Dados Multimodelo**: Combinação de paradigmas relacionais e não-relacionais
- **Armazenamento Descentralizado**: Blockchain e soluções distribuídas
- **Automação e IA**: Sistemas auto-otimizáveis e autoadministrados

## Tipos de Bancos de Dados / Database Types

### Banco de Dados Relacional / Relational Database

Bancos de dados relacionais estruturam dados de acordo com o modelo relacional, organizando informações em tabelas (relações) compostas por linhas (registros/tuplas) e colunas (atributos).

#### Principais características:

- **Estrutura rígida**: Schema predefinido
- **Linguagem SQL**: Para consultas e manipulação
- **Integridade referencial**: Garantida por chaves e restrições
- **Transações ACID**: Atomicity, Consistency, Isolation, Durability
- **Normalização**: Redução de redundância

#### Elementos fundamentais:

- **Tabelas (Relações)**: Estruturas que armazenam dados
- **Registros (Tuplas)**: Linhas de uma tabela
- **Atributos (Colunas)**: Propriedades dos dados
- **Chaves**: Primary Key (PK), Foreign Key (FK), Unique Key (UK)
- **Restrições**: Check Key (CK), Not Null (NN)

#### Exemplos de SGBDs relacionais:

- PostgreSQL
- MySQL
- Oracle Database
- Microsoft SQL Server
- IBM DB2

```sql
-- Exemplo de criação de tabela em SQL
CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    data_cadastro DATE DEFAULT CURRENT_DATE,
    status CHAR(1) CHECK (status IN ('A', 'I'))
);
```

### Normalização / Normalization

Normalização é uma técnica de projeto lógico que reestrutura tabelas e atributos para reduzir redundâncias e permitir o crescimento consistente do banco de dados.

#### Problemas evitados com a normalização:

- **Anomalias de inserção**: Impossibilidade de adicionar dados sem informações completas
- **Anomalias de atualização**: Necessidade de alterar múltiplos registros para uma única mudança lógica
- **Anomalias de exclusão**: Perda não intencional de dados relacionados

#### Formas Normais:

1. **1ª Forma Normal (1FN)**: Elimina grupos repetitivos e garante que cada atributo seja atômico (indivisível).

   **Exemplo antes da 1FN:**
   ```
   Cliente(id, nome, telefone1, telefone2, telefone3)
   ```
   
   **Exemplo após 1FN:**
   ```
   Cliente(id, nome)
   Telefone(cliente_id, numero)
   ```

2. **2ª Forma Normal (2FN)**: Aplica-se a 1FN e elimina dependências funcionais parciais, garantindo que atributos não-chave dependam completamente da chave primária.

   **Exemplo antes da 2FN:**
   ```
   Pedido(cliente_id, produto_id, data_pedido, valor_produto, nome_produto)
   ```
   
   **Exemplo após 2FN:**
   ```
   Pedido(cliente_id, produto_id, data_pedido)
   Produto(produto_id, nome_produto, valor_produto)
   ```

3. **3ª Forma Normal (3FN)**: Aplica-se a 2FN e elimina dependências transitivas, onde atributos não-chave dependem de outros atributos não-chave.

   **Exemplo antes da 3FN:**
   ```
   Cliente(id, nome, cidade_id, cidade_nome, estado_sigla)
   ```
   
   **Exemplo após 3FN:**
   ```
   Cliente(id, nome, cidade_id)
   Cidade(cidade_id, cidade_nome, estado_sigla)
   ```

4. **Forma Normal de Boyce-Codd (FNBC)**: Refinamento da 3FN para casos especiais.

5. **4ª Forma Normal (4FN)**: Trata dependências multivaloradas.

6. **5ª Forma Normal (5FN)**: Lida com dependências de junção.

> **Nota**: Considera-se que um banco de dados está "normalizado" quando atinge a 3FN. As formas posteriores (FNBC, 4FN e 5FN) são refinamentos adicionais para casos específicos.

### Modelos de Dados / Data Models

No design de bancos de dados, trabalhamos com três níveis principais de modelos:

#### 1. Modelo Conceitual
Representação de alto nível dos requisitos de negócio, independente de implementação técnica. Normalmente utiliza notação de Diagrama Entidade-Relacionamento (ER).

**Características:**
- Foco em entidades e seus relacionamentos
- Independente de tecnologia
- Usado para comunicação com stakeholders não-técnicos

#### 2. Modelo Lógico
Tradução do modelo conceitual para uma estrutura mais detalhada, mas ainda independente de SGBD específico.

**Características:**
- Define tabelas, colunas e relações
- Especifica tipos de dados
- Identifica chaves primárias e estrangeiras

#### 3. Modelo Físico
Implementação específica do modelo lógico para um SGBD particular, incluindo decisões técnicas de otimização.

**Características:**
- Específico para um SGBD (MySQL, PostgreSQL, etc.)
- Inclui índices, partições, configurações de armazenamento
- Otimizado para desempenho

## Bancos de Dados NoSQL / NoSQL Databases

NoSQL (Not Only SQL) refere-se a bancos de dados não-relacionais desenvolvidos para superar limitações dos bancos relacionais em aplicações web modernas e big data.

### Origem e Evolução:

- Iniciados por empresas como Google, Facebook, Amazon e LinkedIn
- Projetados para lidar com volumes massivos de dados
- Foco em escalabilidade horizontal e disponibilidade
- Flexibilidade para dados não estruturados ou semiestruturados

### NoSQL - Características / Characteristics

- **Escalabilidade horizontal**: Capacidade de adicionar novos nós facilmente
- **Esquema flexível ou ausente**: Adaptação rápida a mudanças nos dados
- **Suporte nativo à replicação**: Alta disponibilidade
- **APIs simples**: Facilidade de uso e integração
- **Consistência eventual**: Priorização de disponibilidade sobre consistência imediata

### Modelos de Bancos NoSQL / NoSQL Database Models

#### 1. Chave-Valor (Key-Value)

O modelo mais simples de NoSQL, onde cada item é armazenado como uma chave associada a um valor.

**Características:**
- Estrutura extremamente simples
- Alto desempenho para operações de leitura/escrita
- Escalabilidade horizontal eficiente
- Ideal para cache, sessões de usuário, preferências

**Exemplos:**
- Redis
- DynamoDB
- Riak

```
// Exemplo conceitual de armazenamento chave-valor
SET "usuario:1001" {
  "nome": "Carlos Oliveira",
  "email": "carlos@email.com",
  "ultimoLogin": "2025-04-09T18:30:00Z"
}

GET "usuario:1001"
```

#### 2. Orientado a Documentos (Document-Oriented)

Armazena dados em documentos semiestruturados (geralmente JSON ou BSON), permitindo hierarquia e consultas ao conteúdo.

**Características:**
- Documentos autocontidos com estrutura flexível
- Consultas ricas ao conteúdo dos documentos
- Indexação para pesquisas eficientes
- Ideal para conteúdo, catálogos, CMS

**Exemplos:**
- MongoDB
- Couchbase
- Firebase Firestore

```json
// Exemplo de documento JSON no MongoDB
{
  "_id": ObjectId("60a2b3c4d5e6f7g8h9i0j1k2"),
  "nome": "Alice Silva",
  "email": "alice@email.com",
  "endereco": {
    "rua": "Av. Principal, 123",
    "cidade": "São Paulo",
    "cep": "01001-000"
  },
  "pedidos": [
    { "id": "P001", "valor": 250.00, "data": "2025-03-15" },
    { "id": "P002", "valor": 175.50, "data": "2025-04-02" }
  ],
  "ativo": true
}
```

#### 3. Orientado a Colunas (Column-Oriented)

Projetado para armazenar e processar grandes volumes de dados distribuídos, organizando-os em famílias de colunas.

**Características:**
- Otimizado para consultas em grandes conjuntos de dados
- Armazenamento eficiente por coluna (não por linha)
- Alta escalabilidade para operações de escrita
- Ideal para data warehousing, big data

**Exemplos:**
- Apache Cassandra
- HBase
- Google Bigtable

```
// Representação conceitual de banco orientado a colunas (Cassandra)
CREATE TABLE usuarios (
  userid uuid PRIMARY KEY,
  nome text,
  email text,
  cidade text
);

// Armazenamento interno organizado por colunas
Coluna "nome": 
  uuid1: "Pedro Souza"
  uuid2: "Maria Santos"
  
Coluna "email":
  uuid1: "pedro@email.com"
  uuid2: "maria@email.com"
```

#### 4. Orientado a Grafos (Graph-Oriented)

Especializado em representar e analisar relações complexas entre entidades.

**Componentes:**
- Nós (vértices): Entidades com propriedades
- Relacionamentos (arestas): Conexões entre nós, com direção e tipo
- Propriedades: Atributos de nós e relacionamentos

**Características:**
- Otimizado para consultas de relacionamentos
- Travessia eficiente de grafos
- Ideal para redes sociais, detecção de fraude, recomendações, conhecimento conectado

**Exemplos:**
- Neo4j
- JanusGraph
- ArangoDB

```cypher
// Exemplo de consulta em Neo4j (Cypher Query Language)
MATCH (user:Pessoa {nome: "João"})-[:AMIGO_DE]->(amigo:Pessoa)
WHERE amigo.cidade = "Rio de Janeiro"
RETURN amigo.nome, amigo.idade
```

### Bancos de Dados NoSQL - Schema / NoSQL Databases - Schema

A ausência de esquema rígido (schema-free) ou esquema flexível é uma característica distintiva dos bancos NoSQL, permitindo:

- **Evolução natural dos dados**: Sem migrações complexas de schema
- **Adaptação rápida**: Para novos requisitos de negócio
- **Heterogeneidade**: Documentos ou registros com estruturas diferentes
- **Alta escalabilidade**: Facilitada pela distribuição sem esquema central

**Desvantagem**: A flexibilidade de esquema pode comprometer a integridade dos dados, exigindo validação na camada de aplicação.

#### JSON (JavaScript Object Notation)

JSON é um formato leve de intercâmbio de dados, amplamente usado em bancos NoSQL orientados a documentos:

- Formato compacto e legível por humanos
- Par atributo-valor
- Suporte a tipos primitivos, arrays e objetos aninhados
- Independente de linguagem de programação

```json
{
  "id": 1001,
  "nome": "Notebook Premium",
  "preco": 4999.90,
  "especificacoes": {
    "processador": "Intel i7",
    "memoria": "16GB",
    "armazenamento": "512GB SSD"
  },
  "categorias": ["eletrônicos", "computadores", "notebooks"],
  "disponivel": true
}
```

## Bancos de Dados NewSQL / NewSQL Databases

NewSQL representa uma classe de SGBDs relacionais modernos que buscam combinar o melhor dos dois mundos:

- A escalabilidade horizontal do NoSQL
- As garantias ACID e linguagem SQL dos bancos relacionais tradicionais

### Características principais:

- Preserva o modelo relacional e SQL
- Mantém transações ACID
- Oferece escalabilidade horizontal
- Alta performance para grandes volumes de dados
- Mantém esquema estruturado

### Exemplos de bancos NewSQL:

- Google Spanner
- CockroachDB
- VoltDB
- NuoDB
- MemSQL (agora SingleStore)

### SQL x NoSQL x NewSQL

| Característica              | SQL Tradicional | NoSQL | NewSQL |
|-----------------------------|:--------------:|:-----:|:------:|
| Relacional                  | ✅             | ❌    | ✅     |
| SQL                         | ✅             | ❌    | ✅     |
| Transações ACID             | ✅             | ❌    | ✅     |
| Escalabilidade horizontal   | ❌             | ✅    | ✅     |
| Performance/grandes volumes | ❌             | ✅    | ✅     |
| Schema-less                 | ❌             | ✅    | ❌     |

## Teorema CAP / CAP Theorem

O teorema CAP, proposto por Eric Brewer, afirma que um sistema distribuído de dados pode garantir apenas duas das três propriedades simultaneamente:

- **Consistência (Consistency)**: Todos os nós veem os mesmos dados ao mesmo tempo
- **Disponibilidade (Availability)**: Todo pedido recebe uma resposta (sem erro)
- **Tolerância a Partição (Partition Tolerance)**: O sistema continua operando mesmo com falhas de comunicação entre nós

![Teorema CAP](https://miro.medium.com/max/1400/1*rxTP-_STj-QRDt1X9fdVlA.png)

### Escolhas comuns nos bancos de dados:

- **CA (Consistência + Disponibilidade)**: Bancos relacionais tradicionais
- **CP (Consistência + Tolerância a Partição)**: MongoDB, HBase
- **AP (Disponibilidade + Tolerância a Partição)**: Cassandra, DynamoDB

### Consistência Eventual / Eventual Consistency

A consistência eventual é um modelo derivado do teorema CAP onde:

- Prioriza-se disponibilidade e tolerância a partição (AP)
- As escritas são aceitas imediatamente
- A sincronização entre nós ocorre posteriormente
- Temporariamente, diferentes nós podem mostrar valores diferentes
- Eventualmente, todos os nós convergem para o mesmo valor

```
Exemplo de consistência eventual:

1. Nó A recebe atualização: perfil.nome = "Carlos"
2. Nó B ainda mostra o valor antigo: perfil.nome = "Carlos Oliveira"
3. Após sincronização (milissegundos/segundos depois), Nó B: perfil.nome = "Carlos"
```

Bancos que implementam consistência eventual:
- Amazon DynamoDB
- Apache Cassandra
- MongoDB (em configurações específicas)
- CouchDB

## Escalabilidade / Scalability

Escalabilidade refere-se à capacidade de um sistema em lidar com crescimento no volume de dados, transações ou usuários.

### Tipos de escalabilidade:

#### 1. Escalabilidade Vertical (Scale-up)
- Aumentar recursos na mesma máquina (CPU, memória, armazenamento)
- Limites físicos de hardware
- Geralmente mais simples de implementar
- Custos exponenciais

```
Exemplo: Atualizar servidor de 16GB RAM para 64GB RAM
```

#### 2. Escalabilidade Horizontal (Scale-out)
- Adicionar mais nós/servidores ao sistema
- Distribuição de carga entre múltiplas máquinas
- Teoricamente sem limite de crescimento
- Desafios de coordenação e sincronização

```
Exemplo: Aumentar cluster de 3 servidores para 10 servidores
```

### Fatores importantes:

- **Throughput**: Capacidade de processar operações por unidade de tempo
- **Latência**: Tempo para completar uma operação
- **Elasticidade**: Capacidade de escalar dinamicamente conforme demanda
- **Linearidade**: Manter desempenho proporcional ao aumento de recursos

## Sistemas de Arquivos Distribuídos / Distributed File Systems

Sistemas de Arquivos Distribuídos (DFS ou SAD) permitem armazenar e acessar arquivos remotos como se fossem locais, distribuindo os dados entre múltiplos servidores.

### Características principais:

- Acesso transparente a arquivos remotos
- Compartilhamento entre múltiplos usuários/aplicações
- Alta disponibilidade através de replicação
- Escalabilidade horizontal
- Tolerância a falhas

### Requisitos de um Sistemas de Arquivos / File System Requirements

- **Transparência**: Usuários não precisam saber onde os arquivos estão fisicamente
- **Concorrência**: Múltiplos usuários podem acessar arquivos simultaneamente
- **Replicação**: Cópias de arquivos em diferentes locais para disponibilidade
- **Heterogeneidade**: Suporte a diferentes plataformas e sistemas
- **Tolerância a falha**: Funcionamento mesmo com falhas parciais
- **Consistência**: Todas as réplicas mostram o mesmo conteúdo
- **Segurança**: Controle de acesso e proteção
- **Eficiência**: Desempenho próximo ao de um sistema local

### Arquitetura do SAD / DFS Architecture

A arquitetura típica divide responsabilidades entre três módulos principais:

1. **Cliente**: Interface com o usuário ou aplicação
2. **Serviço de arquivos planos**: Gerencia o armazenamento e acesso aos dados
3. **Serviço de diretórios**: Mantém a estrutura de diretórios e localização de arquivos

#### Design aberto:
- Compatibilidade com diferentes interfaces de cliente
- Simulação de operações de diversos sistemas operacionais
- Otimização de desempenho para diferentes configurações

#### Exemplos de DFS:
- Network File System (NFS)
- Andrew File System (AFS)
- Google File System (GFS)
- Ceph File System
- GlusterFS

## Apache Hadoop

Hadoop é uma plataforma de código aberto para armazenamento e processamento distribuído de grandes conjuntos de dados em clusters de computadores comuns.

### Características principais:

- Framework Java para computação distribuída
- Processamento paralelo e distribuído
- Alta tolerância a falhas
- Design para hardware comum (commodity hardware)
- Escalabilidade horizontal simples

### Benefícios do Apache Hadoop

- **Capacidade**: Armazenamento e processamento de petabytes de dados
- **Flexibilidade**: Trabalha com dados estruturados e não estruturados
- **Tolerância a falhas**: Replicação automática de dados
- **Custo-efetividade**: Utiliza hardware commodity
- **Escalabilidade**: Adicionar nós conforme necessário

### HDFS

HDFS (Hadoop Distributed File System) é o sistema de arquivos distribuído do Hadoop, projetado para:

- Armazenar arquivos muito grandes (gigabytes a terabytes)
- Executar em hardware comum
- Alta tolerância a falhas
- Otimizado para throughput (não para latência)

#### Arquitetura HDFS:

1. **NameNode (Master)**:
   - Armazena metadados
   - Gerencia o namespace do sistema de arquivos
   - Mantém a árvore de diretórios
   - Rastreia onde os dados estão armazenados

2. **DataNode (Worker)**:
   - Armazena os blocos de dados reais
   - Gerencia o armazenamento local
   - Executa operações de leitura/escrita
   - Reporta status ao NameNode

```
Exemplo de comando HDFS via linha de comando:

# Listar arquivos em um diretório
hdfs dfs -ls /user/data

# Copiar arquivo do sistema local para HDFS
hdfs dfs -put arquivo_local.txt /user/data/

# Ler conteúdo de um arquivo
hdfs dfs -cat /user/data/arquivo.txt
```

### Módulos do Framework do Apache Hadoop / Apache Hadoop Framework Modules

1. **Hadoop Common**: Bibliotecas e utilitários usados por outros módulos
2. **HDFS (Hadoop Distributed File System)**: Sistema de arquivos distribuído
3. **Hadoop YARN (Yet Another Resource Negotiator)**: Gerenciador de recursos e agendador de jobs
4. **Hadoop MapReduce**: Modelo de programação para processamento paralelo


### Módulos do Framework do Apache Hadoop / Apache Hadoop Framework Modules (continuação)

```java
// Exemplo conceitual de MapReduce em Java
public class WordCount {
  
  public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
      
    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }
  }
  
  public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();
      
    public void reduce(Text key, Iterable<IntWritable> values, Context context) 
        throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }
}
```

O ecosistema Hadoop inclui ainda várias ferramentas complementares:

- **Hive**: SQL sobre Hadoop
- **Pig**: Linguagem de alto nível para análise de dados
- **Spark**: Engine para processamento em memória
- **HBase**: Banco de dados NoSQL orientado a colunas
- **ZooKeeper**: Serviço de coordenação para sistemas distribuídos

## Computação em Nuvem / Cloud Computing

A computação em nuvem oferece recursos computacionais sob demanda através da internet, sem necessidade de gerenciamento direto de infraestrutura. Os três principais provedores são AWS (Amazon Web Services), Microsoft Azure e Google Cloud Platform.

### Modelos de serviço:

1. **IaaS (Infrastructure as a Service)**: Provê infraestrutura virtualizada
   - Exemplos: Amazon EC2, Azure VMs, Google Compute Engine

2. **PaaS (Platform as a Service)**: Fornece plataforma de desenvolvimento
   - Exemplos: AWS Elastic Beanstalk, Azure App Service, Google App Engine

3. **SaaS (Software as a Service)**: Entrega aplicações completas
   - Exemplos: Microsoft 365, Google Workspace, Salesforce

### Arquiteturas Monolíticas / Monolithic Architectures

Em arquiteturas monolíticas, todos os componentes da aplicação são desenvolvidos, implantados e escalados como uma única unidade.

#### Características:
- Todos os processos são altamente acoplados
- Componentes compartilham recursos como memória e banco de dados
- Implantação única para toda a aplicação
- Escalabilidade vertical (todo o sistema precisa escalar junto)

#### Limitações:
- Aumento da complexidade com crescimento do sistema
- Dificuldade de manutenção e adição de recursos
- Maior impacto em caso de falhas (um problema afeta todo o sistema)
- Desafios para trabalho em equipes grandes
- Restrições tecnológicas (todo o sistema usa as mesmas tecnologias)

```
Exemplo simplificado de arquitetura monolítica:

[Interface do Usuário]
        ↓
[Lógica de Negócios]
        ↓
[Acesso a Dados]
        ↓
[Banco de Dados Único]
```

### Arquitetura de Microsserviços / Microservices Architecture

Na arquitetura de microsserviços, a aplicação é decomposta em serviços pequenos e independentes, cada um responsável por uma função específica de negócio.

#### Características:
- Serviços independentes com responsabilidades bem definidas
- Comunicação via APIs (geralmente REST ou gRPC)
- Implantação e escalabilidade independentes
- Cada serviço pode ter seu próprio banco de dados
- Flexibilidade tecnológica (diferentes linguagens/frameworks)

#### Vantagens:
- **Escalabilidade flexível**: Escalar apenas os serviços necessários
- **Implantação independente**: Redução de riscos e ciclos mais rápidos
- **Isolamento de falhas**: Problemas em um serviço não afetam todo o sistema
- **Times especializados**: Equipes menores focadas em serviços específicos
- **Adoção tecnológica incremental**: Liberdade para usar a tecnologia mais adequada para cada componente

```
Exemplo simplificado de arquitetura de microsserviços:

[UI]     [UI Mobile]     [UI Admin]
   ↓          ↓             ↓
[API Gateway / Load Balancer]
   ↓          ↓             ↓
[Serviço    [Serviço      [Serviço
Usuários]   Produtos]     Pedidos]
   ↓          ↓             ↓
[BD       [BD           [BD
Usuários]  Produtos]     Pedidos]
```

## Containers

Containers são unidades de software padronizadas que empacotam código e todas as suas dependências para que a aplicação seja executada de forma rápida e confiável em diferentes ambientes computacionais.

### Principais características:

- **Isolamento**: Container inclui todo o necessário para executar a aplicação
- **Leveza**: Não incluem sistema operacional completo (diferente de VMs)
- **Portabilidade**: Executam consistentemente em qualquer ambiente
- **Eficiência**: Compartilham kernel do host, consumindo menos recursos
- **Inicialização rápida**: Iniciam em segundos (vs. minutos das VMs)

### Docker

Docker é a plataforma mais popular para criação e execução de containers:

```dockerfile
# Exemplo de Dockerfile simples
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Ferramentas de Orquestração de Containers / Container Orchestration Tools

Orquestradores de containers gerenciam múltiplos containers em ambientes de produção, automatizando:

- **Implantação (deployment)**: Distribuição de containers em clusters
- **Escalonamento (scaling)**: Aumento/diminuição do número de instâncias
- **Balanceamento de carga**: Distribuição de tráfego
- **Descoberta de serviços**: Localização de serviços na rede
- **Self-healing**: Detecção e recuperação automática de falhas
- **Atualizações graduais**: Roll-outs e roll-backs controlados

### Principais orquestradores:

1. **Kubernetes (K8s)**:
   - Desenvolvido pelo Google, agora mantido pela CNCF
   - Padrão de facto para orquestração
   - Altamente escalável e extensível
   - Recursos poderosos de rede, armazenamento e segurança

2. **Amazon ECS (Elastic Container Service)**:
   - Serviço gerenciado da AWS
   - Integração nativa com outros serviços AWS
   - Mais simples que Kubernetes, mas menos flexível

3. **Docker Swarm**:
   - Solução nativa do Docker
   - Mais simples de configurar e usar
   - Adequado para implantações menores

```yaml
# Exemplo de configuração Kubernetes para um deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: microservice
  template:
    metadata:
      labels:
        app: microservice
    spec:
      containers:
      - name: api-container
        image: myregistry/myapp:v1.2
        ports:
        - containerPort: 8080
        resources:
          limits:
            cpu: "1"
            memory: "512Mi"
          requests:
            cpu: "0.5"
            memory: "256Mi"
```

## Boas Práticas e Considerações / Best Practices and Considerations

### Indicadores de Desempenho (KPIs)

Ao trabalhar com arquitetura de dados, é fundamental estabelecer métricas para monitorar o desempenho e a eficácia dos sistemas:

- **Latência**: Tempo para completar operações
- **Throughput**: Volume de operações por tempo
- **Taxa de erro**: Percentual de falhas
- **Tempo de resposta**: Experiência do usuário final
- **Utilização de recursos**: CPU, memória, I/O, rede
- **Disponibilidade**: Uptime do sistema (muitas vezes medido em "noves" - 99,9%, 99,99%, etc.)

### Atemporalidade em Análise de Dados

Ao analisar dados temporais, é crucial considerar a atemporalidade para evitar comparações incorretas:

- **Sazonalidade**: Padrões que se repetem em períodos específicos
- **Eventos especiais**: Feriados, promoções, mudanças climáticas
- **Comparações período-a-período**: Comparar períodos equivalentes (mesmo mês de anos diferentes, dias úteis vs. fins de semana)

**Exemplo:** Ao analisar uso de transporte público, comparar março (com Carnaval) e fevereiro pode levar a conclusões errôneas devido aos dias atípicos durante o feriado.

### Ferramentas para Processamento

Familiarize-se com ferramentas modernas para processamento de dados:

- **Apache Airflow**: Orquestração e agendamento de workflows
- **Apache Beam**: Modelo unificado para processamento batch e streaming
- **Apache Spark**: Processamento analítico de alta velocidade
- **Apache Kafka**: Plataforma de streaming distribuído
- **Apache Flink**: Processamento de streams em tempo real

### Considerações para Escolha de Tecnologias

Ao selecionar tecnologias para sua arquitetura de dados, considere:

1. **Volume de dados**: Atual e projeção futura
2. **Velocidade de ingestão**: Batch vs. streaming vs. tempo real
3. **Variedade dos dados**: Estruturados, semiestruturados, não estruturados
4. **Requisitos de consistência**: ACID vs. eventual
5. **Padrões de acesso**: Leitura intensiva vs. escrita intensiva
6. **Escalabilidade necessária**: Vertical vs. horizontal
7. **Expertise da equipe**: Conhecimento tecnológico disponível
8. **Custos**: Licenciamento, hardware, desenvolvimento, manutenção
9. **Requisitos de disponibilidade**: SLAs esperados
10. **Conformidade e regulamentações**: LGPD, GDPR, segurança
