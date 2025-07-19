
Aqui está o texto de estudo em português, fácil de ler e ideal para consulta rápida, criado com base no conteúdo fornecido e enriquecido com informações adicionais para torná-lo mais completo e didático. Ele foi formatado em Markdown para ser usado em um README.md no GitHub.

---

# Bancos de Dados NoSQL: Conceitos e Características

Este documento explica de forma clara e objetiva o que são bancos de dados NoSQL, suas características, modelos e aplicações. Ele foi projetado como uma referência rápida para facilitar o estudo ou a revisão dos conceitos de NoSQL.

---

## O que é NoSQL?

O termo **NoSQL** significa "Not Only SQL" (Não apenas SQL), indicando que esses sistemas vão além do modelo relacional tradicional, podendo complementá-lo ou substituí-lo. Bancos NoSQL são projetados para processar grandes volumes de dados de forma rápida, escalável e flexível, atendendo às demandas de aplicações modernas que priorizam desempenho e disponibilidade.

### Características Principais

- **Não-relacional**: Não utilizam tabelas fixas como os bancos relacionais, mas sim estruturas variadas (documentos, chave-valor, grafos, etc.).
- **Distribuído**: Funcionam em múltiplos servidores, distribuindo os dados para maior eficiência.
- **Código aberto**: Muitos são open-source, incentivando adoção e colaboração.
- **Escalável horizontalmente**: Aumentam a capacidade adicionando mais máquinas (nós), não apenas melhorando um único servidor.
- **Ausência de esquema ou esquema flexível**: Não exigem uma estrutura fixa, permitindo maior agilidade.
- **Suporte à replicação nativo**: Replicam dados entre nós para alta disponibilidade.
- **Acesso via APIs simples**: Oferecem interfaces fáceis para interação com os dados.
- **Diminuição do tempo de recuperação**: Otimizados para consultas rápidas em grandes volumes.

---

## Conceitos Importantes

### Persistência Poliglota

Aplicações modernas muitas vezes usam mais de um tipo de banco de dados para lidar com dados variados (estruturados, não estruturados, grafos, etc.). Isso é chamado de **persistência poliglota**. Por exemplo, um sistema pode combinar um banco relacional para dados financeiros e um NoSQL para logs ou documentos.

### Consistência Eventual

Nos bancos NoSQL, a **consistência eventual** significa que os dados podem estar temporariamente inconsistentes entre nós, mas eventualmente se tornam consistentes. Isso é baseado no **Teorema CAP**, que diz que um sistema distribuído só pode garantir duas das três propriedades: **Consistência**, **Disponibilidade** e **Tolerância a Partição**. NoSQL geralmente prioriza disponibilidade e tolerância, aceitando consistência eventual.

### Propriedades BASE vs. ACID

Os bancos NoSQL seguem o modelo **BASE**, enquanto os relacionais seguem o **ACID**:

- **BASE** (Basically Available, Soft-state, Eventual consistency):
  - **Basicamente Disponível**: O sistema funciona mesmo com inconsistências temporárias.
  - **Estado Flexível**: Os dados podem mudar para alcançar consistência.
  - **Consistência Eventual**: O sistema fica consistente com o tempo.

- **ACID** (Atomicity, Consistency, Isolation, Durability):
  - **Atomicidade**: Transações são completas ou não ocorrem.
  - **Consistência**: Os dados sempre estão em um estado válido.
  - **Isolamento**: Transações não interferem entre si.
  - **Durabilidade**: Dados confirmados são permanentes.

NoSQL relaxa a consistência para ganhar desempenho e escalabilidade.


##  ACID x BASE

| Propriedade | ACID (Relacional) | BASE (NoSQL)           |
| ----------- | ----------------- | ---------------------- |
| A/B         | Atomicidade       | Disponibilidade básica |
| C/S         | Consistência      | Estado flexível        |
| I/E         | Isolamento        | Consistência eventual  |
| D           | Durabilidade      | —                      |

* ACID garante consistência imediata ao custo de performance e escala.
* BASE prioriza disponibilidade e escalabilidade, aceitando consistência tardia.


---

## Escalabilidade Horizontal

A **escalabilidade horizontal** permite adicionar mais máquinas para suportar mais dados e tráfego, usando técnicas como **sharding** (divisão dos dados entre nós). Isso reduz a concorrência e melhora o desempenho, algo difícil nos bancos relacionais devido a bloqueios.

---

## Schemaless (Sem Esquema)

Bancos NoSQL são **schemaless**, ou seja, não exigem um esquema fixo. Isso facilita a adaptação a dados variados ou em evolução, mas pode comprometer a integridade, já que não há verificação automática de estrutura.

---

## Suporte Nativo à Replicação

A replicação aumenta a disponibilidade e tolerância a falhas. Nos bancos NoSQL, ela pode ser:

- **Master-Slave**: Um nó mestre grava os dados, e os escravos replicam.
- **Multi-Master**: Vários nós gravam, sincronizando dados (ex.: topologia de anel).

---

## APIs Simples

Bancos NoSQL oferecem **APIs simples** para acesso rápido aos dados, sendo ideais em arquiteturas como microsserviços.

---

## Tipos de Bancos NoSQL

Cada tipo é otimizado para um propósito:

1. **Chave-Valor**  
   - Armazena pares chave-valor.  
   - Ideal para: caches, sessões.  
   - Exemplos: Redis, DynamoDB.

2. **Armazém de Documentos**  
   - Armazena documentos (ex.: JSON).  
   - Ideal para: dados semi-estruturados.  
   - Exemplos: MongoDB, Couchbase.

3. **Orientado a Coluna**  
   - Organiza dados por colunas.  
   - Ideal para: big data, análises.  
   - Exemplos: Cassandra, HBase.

4. **Grafo**  
   - Usa nós e arestas para relações.  
   - Ideal para: redes sociais, recomendações.  
   - Exemplos: Neo4j, Neptune.

5. **Motor de Busca**  
   - Otimizado para buscas em texto.  
   - Ideal para: logs, pesquisas.  
   - Exemplos: Elasticsearch, Solr.

---

## Comparação: SQL vs. NoSQL

| **Característica**    | **SQL (Relacional)**         | **NoSQL**                   |
|-----------------------|------------------------------|-----------------------------|
| Modelo de Dados       | Tabelas com esquema fixo     | Variado (documentos, grafos)|
| Escalabilidade        | Vertical (mais poder)        | Horizontal (mais máquinas)  |
| Consistência          | Forte (ACID)                 | Eventual (BASE)             |
| Flexibilidade         | Baixa (esquema rígido)       | Alta (schemaless)           |
| Casos de Uso          | Transações, integridade      | Big data, escalabilidade    |

---

## Quando Usar NoSQL?

- Necessidade de **escalabilidade** e **desempenho** com grandes volumes.  
- Dados **não estruturados** ou **semi-estruturados**.  
- Projetos que exigem **flexibilidade** no esquema.  
- Aplicações que priorizam **disponibilidade** sobre consistência imediata.


## Replicação nativa

* **Master–Slave**: um nó master recebe gravações e replica para nós slaves.
* **Multi‑Master**: vários masters aceitam gravações, usados em cenários geograficamente distribuídos.
* Topologia em anel ou estrela para garantir sincronização e resiliência.

## APIs e Microsserviços

* Acesso a dados via **APIs REST**, drivers ou bibliotecas específicas.
* Integração natural com arquitetura de **microsserviços**, onde cada serviço usa seu próprio banco.



## Teorema de cap















# Características dos bancos de dados NoSQL



- O termo NoSQL (Not Only SQL) tem sido usado com o significado de “Não apenas SQL” como tentativa da comunidade de reconhecer a utilidade dos modelos tradicionais e não divergir as discussões.
-  NoSQL não define precisamente esses bancos de dados, mas no geral cada um deles apresenta a maioria das seguintes características:

✓ Não-relacional
✓ Distribuído
✓ Código aberto
✓ Escalável horizontalmente
✓ Ausência de esquema ou esquema flexível
✓ Suporte à replicação nativo
✓ Acesso via APIs simples
✓ Diminuição do tempo de recuperação de informações

## O que é um banco de dados NoSQL?

Sistemas NoSQL não existe uma padronização para as linguagens de manipulação e consulta de dados como no Modelo Relacional, o qual utiliza o padrão SQL.
Sistemas NoSQL não requerem qualquer padronização mesmo em ferramentas que tratam o mesmo modelo de dados 

NoSQL é um conjunto de conceitos que permite o processamento rápido e eficiente de conjuntos de dados com foco em desempenho, confiabilidade e agilidade.
O surgimento desses SGBDs tem como motivação aplicações cujos requisitos não se ajustam a apenas um modelo de dados


## Persistência poliglota

• Aplicações com essas características, ou seja, que necessitam acessar dois ou mais SGBDs com modelos de dados diferentes são chamadas de poliglotas, uma vez que realizam persistência de dados em diversos formatos devido à natureza heterogênea dos dados que manipulam.
• Este conceito de persistência poliglota, pode ser denominado por alguns autores como SGBD NoSQL multimodelo.

## Consistência eventual

- Consistência eventual: Essa característica está relacionada ao fato da consistência nem sempre ser mantida entre os vários pontos de distribuição de dados.
-  Ela tem como princípio o teorema de CAP (Consistency, Availability, Partition and Tolerance) que diz que só é possível garantir duas das três propriedades entre consistência, disponibilidade e tolerância à partição.
-  No contexto da Web geralmente são privilegiadas a disponibilidade e a tolerância à partição.
-   NoSQL implementa as propriedades BASE (Basically Avaliable, Softstate, Eventual consistency), que foram propostas para contrapor as propriedades ACID (Atomicity, Consistency, Isolation, Durability) do Modelo Relacional.
-   A ideia principal é dispensar a consistência (por um intervalo de tempo) em favor da disponibilidade e escalabilidade.

## Propriedades dosbancos de dados NoSQL 

### ACID
- Atomicidade: significa que em uma transação envolvendo duas ou mais partes de informações discretas, ou a transação será executada totalmente ou não será executada, garantindo assim que as transações sejam atômica.
- Consistência: é quando uma transação cria um novo estado válido dos dados ou, em caso de falha, retorna todos os dados ao seu estado anterior ao início da transação.
- Isolamento: significa que uma transação em andamento, mas ainda não validada, deve permanecer isolada de qualquer outra operação externa, ou seja, garante-se que a transação não será interferida por nenhuma outra transação concorrente.
- Durabilidade: indica que dados validados são registados pelo sistema de tal forma que, mesmo no caso de uma falha ou reinício do sistema, os dados estão disponíveis em seu estado correto

- As propriedades ACID forçam a consistência ao final de cada operação, as propriedades BASE permitem que o banco de dados esteja - de forma eventual em um estado consistente.
- Em outras palavras, para obtenção do alto desempenho e disponibilidade, não há priorização da consistência dos dados.
- NoSQL são capazes de processar um grande número de operações simples de leitura e gravação por segundo porém sem garantia de consistência imediata

### Escalabilidade Horizontal

- Escalabilidade horizontal: devido ao volume de dados há a necessidade de escalar e melhorar o desempenho do sistema a escalabilidade horizontal, é o aumento do número de nós (máquinas) disponíveis para o armazenamento e processamento dos dados.
-  Para que a escalabilidade horizontal seja eficiente, ela requer que diversos processos de uma única tarefa sejam criados e distribuídos
-   Esta característica torna inviável a utilização de um banco de dados relacional, uma vez que todos estes processos conectados geram grande concorrência, aumentando consequentemente o tempo de acesso às tabelas desejadas.
- A escalabilidade horizontal somente é permitida nos BDs NoSQL por causa da ausência de bloqueios.
-  Utiliza-se para alcançar esta escalabilidade é o Sharding, que consiste em dividir os dados em várias tabelas, armazenando-as ao longo de múltiplos nós de uma rede quebrando a lógica de relacionamentos.

### schemaless

 - Ausência de esquema ou esquema flexível: a ausência completa ou parcial de esquema que define a estrutura dos dados é uma característica dos bancos NoSQL.
 -  Essa falta de esquema simplifica escalabilidade do sistema bem como aumenta a sua disponibilidade no entanto, não há garantia da integridade dos dados.

### Supor te nativo à replicação

- Suporte nativo à replicação: prover escalabilidade realizando a replicação nativa dos dados, pois isso ajuda a diminuir o tempo gasto na recuperação das informações.
-  Existem basicamente duas abordagens para realizar a replicação:
✓ Master Slave: permite que um servidor slave copie todas as alterações realizadas em um outro servidor, denominado de master.
 Multi-Master: para aplicações distribuídas geograficamente, pode-se criar servidores masters próximos às regiões que manipulam os dados, permitindo uma redução no tempo de acesso ao dado através da rede.
✓ Para isto, é necessário manter todas as regiões sincronizadas, e para isto, utilizamos a topologia de anel, onde define-se vários masters.

### API - Application Programming Interface

 API : No NoSQL o foco não está na forma em que os dados são acessados, mas sim em como são recuperados.
• O uso de APIs se torna essencial para tornar simples o acesso a essas informações, permitindo que qualquer aplicação possa fazer uso do banco de forma rápida e eficiente.
• Tudo vinculado ao conceito de arquitetura de microsserviços MAS (MicroServices Architecture)

# Definição de negócios e motivação

## BASE

Basic Availability: permite que os
sistemas fiquem temporariamente
inconsistentes para que as transações
sejam gerenciáveis.
✓Soft-state: reconhece que alguma
imprecisão é temporariamente permitida
e os dados mudam enquanto são usados
reduzindo os recursos consumidos.

✓Eventual consistency: significa que,
eventualmente, quando toda a lógica de
serviço é executada, o sistema é deixado
em um estado consistente.
✓Soft-state: reconhece que alguma
imprecisão é temporariamente permitida
e os dados mudam enquanto são usados
reduzindo os recursos consumidos.

## Teorema CAP

NoSQL. Este teorema afirma que é impossível para
qualquer sistema distribuído fornecer
simultaneamente todos os três recursos:
✓Consistência: todos os nós veem os
mesmos dados ao mesmo tempo.
✓Disponibilidade: garantia de resposta em
cada solicitação sobre conclusão bem-
sucedida ou falha.
✓Tolerância de partição: o sistema
continua a operar apesar da perda
arbitrária de mensagens ou da falha de
uma parte do sistema.

### ACID X BASE tabela
### SQL X NoSQL tabela

# Tipos de Bancos NOSQL e principais bancos do mercado

## LINGUAGENS DE MARCAÇÃO

 LINGUAGENS DE MARCAÇÃO são sistemas usados para definir padrões e formatos
de exibição dentro de um documento.
• Funcionam para definir como um determinado conteúdo vai ser visualizado na tela
ou como os dados serão distribuídos.
• Essa codificação interna é feita pelo uso de marcadores ou tags.
• TAGS: são palavras-chave para relacionar informações semelhantes.
• METADADOS: são dados usados para classificar e organizar arquivos, páginas e
outros conteúdos.

• Arquivos estruturados de dados são arquivos que seguem padrões para
entendimento dos dados que estão ali armazenados.
• Qualquer que seja o arquivo estruturado, existem diversas maneiras de representá-la
por formatos como CSV (Comma/Character Separeted Values) – Esse quase todo
mundo já utilizou pelo menos uma vez, não é? – ou por formatos ODS, XLSX entre
outros.
• Todos os citados acima, respeitam diferentes graus a estrutura linha coluna que
vem dos bancos de dados relacionais.

### CSV

### JSON

### XML


### JSON x XML


## HASHING

### Hash


## 5 modelos de armazenamento para os bancos de dados NoSQL:

###  Orientado a Coluna (tabular) vantagens e desvantagens
### Armazém de Documentos vantagens e desvantagens

###  Chave/Valor vantagens e desvantagens

###  Grafo vantagens e desvantagens
 
### Motor de Busca vantagens e desvantagens

• A escolha do banco de dados NoSQL depende do tipo de dados que você precisa armazenar, seu tamanho e complexidade.

## Armazém de Documentos

# Principais bancos NOSQL do mercado e sua aplicação

## Chave/Valor

 Amazon's Dynamo
• Redis
• Riak
• Oracle NoSQL

## Armazém deDocumentos

• MongoDB
• Couchbase

## Orientado a Coluna

• Cassanda
• Hypertable
• Amazon SimpleDB
• Apache Hbase
• Google BigTabl

## Grafo

• Neo4J
• AllegroGraph
• Amazon Neptune
• OpenLink Virtuoso

## Motor de Busca

• Elastic Search AWS
• Algolia
• Apache Solr
• Google cloud Search
