--

# Bancos de Dados NoSQL: Conceitos e Características

Este repositório contém uma introdução abrangente aos bancos de dados NoSQL, cobrindo suas características, conceitos-chave, tipos, comparações com bancos relacionais e cenários de uso. É ideal para estudantes de pós-graduação ou profissionais que buscam compreender os fundamentos técnicos e práticos do NoSQL.

## Tabela de Conteúdos

- [Introdução ao NoSQL](#introdução-ao-nosql)
- [Características dos Bancos de Dados NoSQL](#características-dos-bancos-de-dados-nosql)
- [Conceitos-Chave](#conceitos-chave)
  - [Persistência Poliglota](#persistência-poliglota)
  - [Consistência Eventual e Teorema CAP](#consistência-eventual-e-teorema-cap)
  - [Propriedades BASE vs. ACID](#propriedades-base-vs-acid)
  - [Escalabilidade Horizontal e Sharding](#escalabilidade-horizontal-e-sharding)
  - [Design Sem Esquema](#design-sem-esquema)
  - [Replicação Nativa](#replicação-nativa)
  - [APIs Simples e Microsserviços](#apis-simples-e-microsserviços)
- [Tipos de Bancos de Dados NoSQL](#tipos-de-bancos-de-dados-nosql)
- [Comparação: SQL vs. NoSQL](#comparação-sql-vs-nosql)
- [Quando Usar NoSQL](#quando-usar-nosql)
- [Formatos de Dados Comuns](#formatos-de-dados-comuns)
- [Conteúdos Complementares](#conteúdos-complementares)

---

## Introdução ao NoSQL

NoSQL, abreviação de "Not Only SQL" (Não apenas SQL), refere-se a uma classe de sistemas de gerenciamento de bancos de dados que divergem do modelo relacional tradicional. Esses sistemas são projetados para processar grandes volumes de dados com alta performance, escalabilidade horizontal e flexibilidade, atendendo às necessidades de aplicações modernas, como big data, IoT e sistemas distribuídos.

Os bancos NoSQL surgiram para superar limitações dos bancos relacionais, como esquemas rígidos e dificuldades em escalar horizontalmente, oferecendo modelos de dados variados e arquiteturas distribuídas.

---

## Características dos Bancos de Dados NoSQL

Os bancos NoSQL possuem características que os distinguem dos sistemas relacionais:

- **Não-relacional**: Utilizam modelos como chave-valor, documentos, colunas ou grafos, em vez de tabelas fixas.
- **Distribuído**: Operam em múltiplos servidores, distribuindo dados para maior eficiência e tolerância a falhas.
- **Código aberto**: Muitos são open-source, promovendo colaboração e adoção.
- **Escalável horizontalmente**: Capacidade aumenta com a adição de novos nós, não apenas por upgrade de hardware.
- **Sem esquema ou esquema flexível**: Não exigem estrutura fixa, adaptando-se a dados heterogêneos.
- **Suporte nativo à replicação**: Replicam dados entre nós para alta disponibilidade.
- **APIs simples**: Interfaces acessíveis, como REST ou drivers, facilitam integração.
- **Recuperação rápida**: Otimizados para consultas ágeis em grandes volumes.

---

## Conceitos-Chave

### Persistência Poliglota

Persistência poliglota é o uso de múltiplos tipos de bancos de dados em uma aplicação para atender a diferentes necessidades de dados. Por exemplo:
- Banco relacional para dados estruturados (ex.: finanças).
- Banco de documentos para dados semi-estruturados (ex.: catálogos).
- Banco de grafos para relações complexas (ex.: redes sociais).

### Consistência Eventual e Teorema CAP

**Consistência eventual** implica que os dados podem estar temporariamente inconsistentes entre nós, mas convergem para um estado consistente com o tempo. Isso está ligado ao **Teorema CAP**, que estabelece que um sistema distribuído só pode garantir duas das três propriedades:
- **Consistência**: Todos os nós veem os mesmos dados simultaneamente.
- **Disponibilidade**: Toda requisição recebe resposta, mesmo sem dados atualizados.
- **Tolerância a partição**: O sistema opera apesar de falhas na rede.

NoSQL geralmente prioriza disponibilidade e tolerância, aceitando consistência eventual.

### Propriedades BASE vs. ACID

- **BASE** (NoSQL):
  - **Basically Available**: Sistema responde mesmo com inconsistências temporárias.
  - **Soft-state**: Dados podem mudar até atingir consistência.
  - **Eventual consistency**: Consistência é alcançada com o tempo.
- **ACID** (Relacional):
  - **Atomicidade**: Transações são completas ou não ocorrem.
  - **Consistência**: Dados permanecem válidos após transações.
  - **Isolamento**: Transações não interferem entre si.
  - **Durabilidade**: Dados confirmados são permanentes.

NoSQL sacrifica consistência imediata por desempenho e escalabilidade.

### Escalabilidade Horizontal e Sharding

**Escalabilidade horizontal** adiciona mais servidores para suportar carga, usando **sharding** (particionamento de dados entre nós). Isso melhora o desempenho ao evitar bloqueios, algo comum em bancos relacionais.

### Design Sem Esquema

Bancos NoSQL são **schemaless**, permitindo armazenar dados sem estrutura fixa. Isso oferece flexibilidade, mas exige que a aplicação gerencie a integridade.

### Replicação Nativa

A replicação aumenta disponibilidade e resiliência:
- **Master-Slave**: Um nó grava, outros replicam.
- **Multi-Master**: Múltiplos nós gravam, sincronizando dados (ex.: topologia em anel).

### APIs Simples e Microsserviços

NoSQL oferece **APIs simples** (ex.: REST, drivers), ideais para arquiteturas de microsserviços, onde cada serviço usa o banco mais adequado.

---

## Tipos de Bancos de Dados NoSQL

| **Tipo**              | **Descrição**                          | **Vantagens**                  | **Desvantagens**              | **Exemplos**            |
|-----------------------|----------------------------------------|--------------------------------|--------------------------------|-------------------------|
| **Chave-Valor**       | Pares chave-valor simples             | Rápido, escalável             | Consultas limitadas           | Redis, DynamoDB, Riak  |
| **Documentos**        | Dados em documentos (ex.: JSON)       | Flexível, semi-estruturado    | Menos eficiente para relações | MongoDB, Couchbase     |
| **Colunas**           | Armazenamento por colunas             | Eficiente para análises       | Complexo para transações      | Cassandra, HBase       |
| **Grafo**             | Nós e arestas para relações           | Ideal para dados conectados   | Curva de aprendizado          | Neo4j, Neptune         |
| **Motor de Busca**    | Indexação e busca em texto            | Buscas rápidas, real-time     | Não para uso geral            | Elasticsearch, Solr    |

---

## Comparação: SQL vs. NoSQL

| **Característica**    | **SQL (Relacional)**         | **NoSQL**                   |
|-----------------------|------------------------------|-----------------------------|
| **Modelo de Dados**   | Tabelas com esquema fixo     | Variado (documentos, grafos)|
| **Escalabilidade**    | Vertical (mais poder)        | Horizontal (mais nós)       |
| **Consistência**      | Forte (ACID)                 | Eventual (BASE)             |
| **Flexibilidade**     | Baixa (esquema rígido)       | Alta (schemaless)           |
| **Casos de Uso**      | Transações, integridade      | Big data, escalabilidade    |

---

## Quando Usar NoSQL

Use NoSQL quando:
- Dados são **não estruturados** ou **semi-estruturados**.
- Necessidade de **escalabilidade horizontal** para grandes volumes.
- **Disponibilidade** é mais crítica que consistência imediata.
- Requer **flexibilidade** para mudanças no esquema.

Prefira SQL para:
- Transações complexas com **consistência forte**.
- Dados estruturados e estáveis.

---

## Formatos de Dados Comuns

NoSQL frequentemente usa linguagens de marcação para estruturar dados:
- **JSON**: Leve, amplamente usado em documentos (ex.: `{"id": 1, "nome": "Ana"}`).
- **XML**: Mais verboso, usado em sistemas legados (ex.: `<pessoa><id>1</id><nome>Ana</nome></pessoa>`).
- **CSV**: Simples, tabular, para exportação (ex.: `id,nome\n1,Ana`).

**Hashing** é comum em chave-valor, mapeando chaves a valores via funções hash para acesso rápido.

---

## Conteúdos Complementares

Para enriquecer o curso, sugiro adicionar:
1. **Exemplos Práticos**:
   - Configurar um banco MongoDB com um documento simples:
     ```json
     {
       "nome": "Produto A",
       "preco": 29.99
     }
     ```
   - Consulta em Redis: `SET chave "valor"` e `GET chave`.
2. **Modelagem de Dados**:
   - Como estruturar dados em cada tipo de NoSQL.
3. **Desempenho**:
   - Técnicas de otimização (ex.: índices, caching).
4. **Segurança**:
   - Autenticação e criptografia em NoSQL.

Se o conteúdo crescer, crie subpastas:
- `/exemplos`: Códigos práticos.
- `/modelagem`: Guias de design.
- `/recursos`: Artigos e referências.

---

