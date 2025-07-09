# SQL vs NoSQL: Um Guia de Estudo Rápido

Este texto foi criado para facilitar o estudo e a consulta rápida sobre bancos de dados SQL e NoSQL. Ele organiza as principais diferenças, vantagens e desvantagens de cada tipo, além de explicar por que o NoSQL surgiu como alternativa. O conteúdo é baseado no material fornecido e complementado para torná-lo mais completo e didático.

---

## Introdução
Os bancos de dados são ferramentas essenciais para gerenciar informações. Existem dois tipos principais:

- **SQL (Structured Query Language)**: Bancos relacionais, como MySQL, PostgreSQL e SQLite. Usam tabelas com esquemas fixos e são ideais para dados estruturados e relações claras.
- **NoSQL (Not Only SQL)**: Bancos não relacionais, como MongoDB, Redis, CouchDB e Firebase. São flexíveis, focados em grandes volumes de dados e alta performance.

A escolha entre SQL e NoSQL depende das necessidades do seu projeto, como escalabilidade, consistência e disponibilidade.

---

## Diferenças Principais entre SQL e NoSQL

| Característica       | SQL                                      | NoSQL                                    |
|----------------------|------------------------------------------|------------------------------------------|
| **Esquema**          | Fixo, com tabelas e colunas definidas.   | Flexível, sem esquema rígido.            |
| **Relações**         | Baseado em relações entre tabelas.       | Documentos ou registros independentes.   |
| **Escalabilidade**   | Vertical (melhor hardware).              | Horizontal (mais servidores).            |
| **Consistência**     | Forte (transações ACID).                 | Eventual (prioriza disponibilidade).     |
| **Desempenho**       | Bom para consultas complexas.            | Ótimo para grandes volumes e velocidade. |
| **Casos de Uso**     | Sistemas financeiros, ERPs.              | Big Data, IoT, redes sociais.            |

- **Exemplo prático**:
  - SQL: Um banco para gerenciar pedidos e clientes, com relações claras entre tabelas.
  - NoSQL: Um sistema de redes sociais, com dados variados (posts, fotos, comentários) em grande escala.

---

## Por que o NoSQL Surgiu? A Mudança de Paradigma
Os bancos SQL tradicionais, baseados em processadores únicos, enfrentam limitações diante das demandas modernas. O NoSQL surgiu para atender a quatro desafios principais:

1. **Volume**:
   - Bancos SQL escalam verticalmente (hardware mais potente), mas isso tem limites (ex.: "power wall" – calor excessivo em chips).
   - NoSQL escala horizontalmente, usando clusters de servidores para lidar com Big Data.

2. **Velocidade**:
   - SQL pode ser lento para inserções e consultas em tempo real, como em sites com alto tráfego.
   - NoSQL é otimizado para leituras e gravações rápidas.

3. **Variabilidade**:
   - Em SQL, mudar o esquema (ex.: adicionar colunas) exige parar o sistema, o que é caro e demorado.
   - NoSQL permite adicionar novos campos sem interrupções.

4. **Agilidade**:
   - SQL exige mapeamento objeto-relacional complexo, atrasando o desenvolvimento.
   - NoSQL simplifica o processo, acelerando projetos.

---

## Tipos de Bancos NoSQL
O NoSQL não é um só modelo. Existem quatro tipos principais:
- **Chave-Valor**: Ex.: Redis. Simples e rápido, ideal para caches.
- **Documentos**: Ex.: MongoDB. Armazena dados em estruturas como JSON, flexíveis.
- **Colunas**: Ex.: Cassandra. Otimizado para grandes volumes e consultas analíticas.
- **Grafos**: Ex.: Neo4j. Focado em relações complexas, como redes sociais.

# Propriedades dos Bancos de Dados NoSQL

**Data e hora de criação:** 14:37 -03, quarta-feira, 9 de julho de 2025

---

## Introdução ao NoSQL

Os bancos de dados **NoSQL** (sigla para "Not Only SQL", ou "Não Apenas SQL") são uma categoria de sistemas de gerenciamento de dados projetada para atender às demandas de aplicações modernas, como manipulação de grandes volumes de dados e necessidade de alta performance. Diferentemente dos bancos relacionais tradicionais, que organizam dados em tabelas com esquemas rígidos, os NoSQL oferecem modelos mais flexíveis, como documentos, grafos, pares chave-valor ou colunas. Essa flexibilidade os torna ideais para cenários de big data, onde os dados variam em estrutura e precisam ser processados rapidamente.

### Por que usar NoSQL?

- **Grandes volumes de dados:** Capazes de gerenciar terabytes ou petabytes de dados distribuídos em múltiplos servidores.
- **Alta performance:** Oferecem tempos de resposta rápidos, essenciais para aplicações em tempo real.
- **Escalabilidade:** Facilitam o crescimento do sistema sem perda de desempenho.
- **Simplicidade:** Arquiteturas mais simples que distribuem recursos pela rede, reduzindo a complexidade de desenvolvimento.

---

## Escalabilidade em NoSQL

**Escalabilidade** é a capacidade de um sistema lidar com um aumento na carga de trabalho (como mais dados ou usuários) ao adicionar recursos proporcionais, mantendo o desempenho. Em NoSQL, isso é fundamental para suportar o crescimento contínuo de dados.

### Tipos de Escalabilidade

1. **Escalabilidade Vertical**
   - **O que é?** Adicionar mais recursos de hardware (CPU, memória, armazenamento) a um único servidor.
   - **Exemplo:** Aumentar a RAM de um computador para suportar mais dados.
   - **Vantagens:** Simples de implementar.
   - **Limitações:** Há um limite físico para o hardware, e os custos podem ser altos.

2. **Escalabilidade Horizontal**
   - **O que é?** Distribuir os dados entre vários servidores (chamados "nós") em um cluster.
   - **Exemplo:** Dividir os dados de uma rede social em vários servidores, cada um cuidando de uma parte dos usuários.
   - **Vantagens:** Permite crescimento ilimitado adicionando mais nós, sendo mais econômico e flexível.
   - **Analogia:** É como abrir novas filiais de uma loja ao invés de expandir uma única unidade.

---

## Sharding em NoSQL

**Sharding** é uma técnica de particionamento que divide os dados em fragmentos (shards) e os distribui entre diferentes nós de um cluster. Isso melhora a escalabilidade horizontal e a disponibilidade do sistema.

### Como funciona?

- **Chave de particionamento:** Uma chave (ex.: ID do usuário) determina em qual shard os dados serão armazenados.
- **Exemplo:** Usuários com nomes de A a M em um shard, e de N a Z em outro.
- **Autosharding:** Muitos sistemas NoSQL redistribuem os dados automaticamente quando novos nós são adicionados ou removidos.

### Benefícios

- **Performance:** Cada nó processa menos dados, acelerando as operações.
- **Disponibilidade:** Se um nó falhar, apenas uma parte dos dados fica afetada.
- **Custo reduzido:** O sharding automático minimiza o tempo de inatividade e facilita a manutenção.

### Desafios

- Escolher uma chave de particionamento eficiente é essencial para evitar desequilíbrios entre os shards.

---

## Variações Arquitetônicas em NoSQL

Os bancos de dados NoSQL variam em sua arquitetura para atender a necessidades específicas, como uso de memória, caching ou armazenamento distribuído. Essas diferenças os tornam adequados para diferentes tipos de aplicações.

### 1. Memcache (Cache em RAM)

- **O que é?** Um sistema de pares chave-valor que armazena dados na RAM de vários servidores.
- **Uso:** Ideal para caching (armazenamento temporário) de dados acessados frequentemente, como resultados de consultas ou variáveis globais.
- **Vantagens:** Acesso ultrarrápido, pois a RAM é mais rápida que discos.
- **Exemplo:** Um site pode usar Memcache para armazenar os produtos mais vistos, reduzindo a carga no banco principal.
- **Limitação:** Dados na RAM são voláteis e podem ser perdidos se o servidor reiniciar, a menos que sejam salvos em outro lugar.

### 2. Armazenamento Distribuído

- **O que é?** Sistemas que distribuem dados entre múltiplos servidores de forma transparente ao usuário.
- **Funcionamento:** A API esconde a localização dos dados, facilitando o uso.
- **Vantagens:** Escalabilidade horizontal e tolerância a falhas, pois os dados podem ser replicados.
- **Exemplo:** Bancos como Cassandra distribuem dados em clusters para garantir alta disponibilidade.

### 3. Uso de SSDs

- **O que é?** Bancos que utilizam SSDs (Solid State Drives) para armazenamento permanente.
- **Vantagens:** Mais rápidos que discos rígidos tradicionais, com tempos de leitura próximos à RAM e maior durabilidade.
- **Exemplo:** Usado em sistemas que precisam de alta performance para leitura e escrita, como análises em tempo real.

---

### MongoDB: Guia de Estudo Rápido

**O que é MongoDB?**

MongoDB é um banco de dados NoSQL orientado a documentos, de código aberto e multi-plataforma. Ele é escrito em C++ e projetado para oferecer alto desempenho, alta disponibilidade e fácil escalabilidade. Diferente dos bancos de dados relacionais tradicionais, que usam tabelas e esquemas rígidos, o MongoDB armazena dados em documentos flexíveis no formato JSON (JavaScript Object Notation).

**Por que usar MongoDB?**

- **Flexibilidade**: Os documentos JSON permitem armazenar dados com estruturas variadas na mesma coleção.
- **Escalabilidade**: Pode ser expandido horizontalmente adicionando mais servidores.
- **Desempenho**: Otimizado para grandes volumes de dados e consultas complexas.
- **Alta Disponibilidade**: Garante acesso contínuo aos dados, mesmo em falhas.

**Principais Recursos**

1. **Consultas Avançadas**
   - Suporta operações CRUD: inserção (Create), leitura (Read), atualização (Update) e exclusão (Delete).
   - Permite consultas complexas, como as de bancos SQL, adaptadas ao modelo de documentos.
   - Oferece consultas de intervalo (ex.: valores entre 10 e 20), expressões regulares (buscas por texto) e projeção (seleção de campos específicos).

2. **Indexação**
   - Suporta índices primários e secundários para acelerar consultas.
   - Índices podem ser aplicados a qualquer campo, incluindo campos aninhados em documentos.

3. **Replicação**
   - Cria cópias dos dados em vários servidores, aumentando a tolerância a falhas.
   - Se um servidor falhar, outro assume automaticamente, mantendo o serviço ativo.

4. **Balanceamento de Carga**
   - Distribui operações de leitura entre servidores secundários, melhorando o desempenho em cenários com muitas solicitações.

5. **Armazenamento de Arquivos**
   - Documentos de até 16 MB podem ser armazenados diretamente nos campos JSON.
   - Para arquivos maiores, o GridFS divide os dados em blocos menores, permitindo o armazenamento eficiente.

6. **Agregação**
   - Realiza cálculos como soma, média, mínimo e máximo em conjuntos de dados.
   - Usa um pipeline de agregação para processar dados em etapas, ideal para análises complexas.

**Tipos de Dados Suportados**

MongoDB oferece diversos tipos de dados para modelagem flexível:

- **String**: Texto (ex.: "Olá, mundo").
- **Double**: Números de ponto flutuante (ex.: 3.14).
- **Inteiro**: Números inteiros (ex.: 42).
- **Object**: Documentos aninhados (ex.: { "nome": "João" }).
- **Array**: Listas de valores (ex.: [1, 2, 3]).
- **Boolean**: Verdadeiro ou falso (true/false).
- **Timestamp**: Data e hora (ex.: 2023-10-15T10:00:00Z).

**Operadores de Consulta Comuns**

Os operadores ajudam a filtrar dados em consultas:

- **$eq**: Igual a (ex.: { "idade": { "$eq": 25 } }).
- **$gt**: Maior que (ex.: { "idade": { "$gt": 18 } }).
- **$gte**: Maior ou igual a.
- **$lt**: Menor que.
- **$lte**: Menor ou igual a.
- **$ne**: Diferente de.
- **$in**: Está em uma lista (ex.: { "cor": { "$in": ["azul", "verde"] } }).
- **$nin**: Não está em uma lista.

**Quando Usar MongoDB?**

- Aplicações com dados semi-estruturados ou não estruturados (ex.: logs, conteúdo dinâmico).
- Projetos que precisam de escalabilidade horizontal.
- Cenários que exigem alta disponibilidade e tolerância a falhas.
- Desenvolvimento ágil, onde o esquema de dados pode mudar com frequência.

**Dicas para Estudo**

- **Pratique com Exemplos**: Use o MongoDB Shell ou o MongoDB Compass para testar comandos e consultas.
- **Leia a Documentação**: A [documentação oficial](https://docs.mongodb.com/) é rica em exemplos e tutoriais.
- **Entenda o Modelo**: Aprenda como modelar dados em documentos e como isso difere de tabelas relacionais.
- **Cursos Gratuitos**: Confira o [MongoDB University](https://university.mongodb.com/) para aprender mais.

**Exemplo Prático**

Inserir um documento:
```json
db.alunos.insertOne({ "nome": "Maria", "idade": 20, "notas": [8, 9, 7] })
```

Consultar alunos com idade maior que 18:
```json
db.alunos.find({ "idade": { "$gt": 18 } })
```

**MongoDB – Guia de Consulta Rápida**

---

## 1. Conceitos Básicos

* **Documento**

  * Unidade básica de dados no MongoDB (equivalente a uma “linha” em SGBD relacional).
  * Estrutura *chave–valor* representada em JSON/BSON (UTF‑8).
  * **Características**:

    * Chaves são *strings* UTF‑8 (exceto `\0`, `.` e `$` em contextos especiais).
    * Sensível a tipos e a maiúsculas/minúsculas (*case sensitive*).
    * Não permite chaves duplicadas.

* **Coleção**

  * Conjunto de documentos (equivalente a “tabela” em SGBD relacional).
  * Esquema **dinâmico**: documentos de formatos distintos podem conviver.
  * Recomenda‑se agrupar na mesma coleção apenas documentos de mesmo “tipo” para simplificar consultas, índices e manutenção.

* **Banco de Dados**

  * Contêiner de coleções.
  * Criado/selecionado com o comando:

    ```js
    use nome_do_database
    ```
  * Listagem de bancos: `show databases` (só aparecem se houver ao menos uma coleção).
  * **Restrições de nome**:

    * UTF‑8, sem caracteres `/ \ . " * < > : | ? $` ou `\0`, máximo 64 bytes.
    * Não diferencia maiúsculas/minúsculas.

---

## 2. Shell `mongo`

* Interpretador JavaScript completo para:

  1. **Administrar instâncias** (configurar réplicas, usuários, etc.).
  2. **Manipular dados** usando queries próprias.
  3. **Criar scripts** para automação de tarefas.

* **Comandos úteis**:

  ```js
  show dbs                   // lista bancos de dados
  use meu_app                // seleciona (ou cria) banco “meu_app”
  show collections           // lista coleções do banco atual
  db.createCollection('col') // cria coleção “col”
  db.minhaCol.insertOne({...})  // insere documento
  db.minhaCol.find({...})       // busca documentos
  db.minhaCol.updateOne(filt, {$set: {...}}) // atualiza
  db.minhaCol.deleteOne(filt)    // remove
  ```

---

## 3. Operações CRUD

| Operação   | Sintaxe                                | Exemplo                                                  |
| ---------- | -------------------------------------- | -------------------------------------------------------- |
| **Create** | `db.colecao.insertOne(documento)`      | `db.usuarios.insertOne({nome:'Ana', idade:30})`          |
| **Read**   | `db.colecao.find(filtro)`              | `db.usuarios.find({idade:{$gt:18}})`                     |
| **Update** | `db.colecao.updateOne(filtro, update)` | `db.usuarios.updateOne({nome:'Ana'}, {$set:{idade:31}})` |
| **Delete** | `db.colecao.deleteOne(filtro)`         | `db.usuarios.deleteOne({nome:'Ana'})`                    |

---

## 4. Tipos de Dados Suportados

* **Null**
* **Boolean** (`true` / `false`)
* **Number**

  * `NumberInt` (32 bits)
  * `NumberLong` (64 bits)
  * `Double` (ponto flutuante)
* **String** (UTF‑8)
* **Date** (milissegundos desde Epoch; não armazena fuso)
* **Array** (lista ordenada de valores)
* **Document** (documento aninhado)
* **ObjectId** (`_id` padrão de 12 bytes)

---

## 5. Campo `_id` e Chave Primária

* Cada documento **obrigatoriamente** possui um campo `_id`.
* Se não fornecido, o MongoDB gera um **ObjectId** de 12 bytes:

  1. 4 bytes: timestamp
  2. 3 bytes: identificador da máquina
  3. 2 bytes: ID do processo
  4. 3 bytes: contador incremental
* `_id` é **único** por coleção e funciona como chave primária.

---

## 6. Schemas Dinâmicos e Boas Práticas

* **Vantagem**: flexibilidade para evoluir estrutura sem migrações complexas.
* **Cuidados**:

  * **Não misturar** tipos muito distintos na mesma coleção.
  * Garantir que cada consulta / aplicação trate corretamente o *shape* esperado.
  * Utilize *field* discriminador (*e.g.*, `tipo`), se necessário, mas prefira coleções separadas para cada “entidade”.
  * Coleções bem organizadas permitem índices mais eficientes e leituras mais rápidas.

---

## 2.5 MongoDB – Operações CRUD

### Introdução

* **CRUD** corresponde às quatro operações básicas em bancos de dados:

  * **C**reate: criar novos registros.
  * **R**ead: ler ou exibir registros.
  * **U**pdate: atualizar registros existentes.
  * **D**elete: remover registros.

---

### 1. Create (Inserção)

* Insere documentos em uma coleção. Se a coleção não existir, o MongoDB a cria automaticamente.
* **Métodos principais:**

  * `db.colecao.insertOne(documento)` — insere um único documento.

    ```js
    db.usuarios.insertOne({
      nome: "João", idade: 28, email: "joao@exemplo.com"
    });
    ```
  * `db.colecao.insertMany([doc1, doc2, ...])` — insere vários documentos de uma vez.

    ```js
    db.produtos.insertMany([
      {nome: "Mouse", preco: 50},
      {nome: "Teclado", preco: 120}
    ]);
    ```

**Dica:** verifique o retorno (`insertedId` / `insertedCount`) para confirmar inserção bem‑sucedida.

---

### 2. Read (Leitura e Consulta)

* Recupera documentos de uma coleção usando filtros, projeções e opções.

#### 2.1 find()

* `db.colecao.find(filtro, projeção)` — busca documentos que satisfaçam o filtro.

  * Filtro vazio (`{}`) retorna todos os documentos.
  * Projeção (`{campo: 1}`) seleciona quais campos serão retornados.

  ```js
  db.usuarios.find({}, {nome: 1, _id: 0});
  ```
* Para exibir de forma legível: no shell use `printjson()` ou `pretty()`:

  ```js
  db.usuarios.find().pretty();
  ```

#### 2.2 Operadores de Filtro

* **Comparação:**

  * `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`
  * Exemplo: `db.produtos.find({preco: {$gt: 100}})`
* **Lógicos:**

  * `$and`, `$or`, `$not`, `$nor`
  * Exemplo: `db.usuarios.find({$and: [{idade: {$gte: 18}}, {ativo: true}]})`
* **Conjunto:**

  * `$in`, `$nin`
  * Exemplo: `db.usuarios.find({pais: {$in: ["BR", "PT"]}})`
* **Expressão Regular:**

  * `$regex` para busca por padrão em strings.
  * Exemplo: `db.posts.find({titulo: {$regex: /^Mongo/i}})`
* **JavaScript Customizado:**

  * `$where` permite funções JS, mas **evite** por impactos de desempenho e segurança.

#### 2.3 Opções de Consulta

* **limit(n):** restringe número de documentos.

  ```js
  db.usuarios.find().limit(5);
  ```
* **skip(n):** pula os primeiros `n` resultados (usado em paginação).

  ```js
  db.usuarios.find().skip(10).limit(5);
  ```
* **sort({campo: 1 ou -1}):** ordena resultados.

  ```js
  db.produtos.find().sort({preco: -1});
  ```

---

### 3. Update (Atualização)

* Altera documentos existentes. **Sempre** passe filtro para evitar alterações indesejadas.

#### 3.1 Métodos Principais

* `db.colecao.updateOne(filtro, modificador, opções)` — atualiza o primeiro documento que casar com o filtro.
* `db.colecao.updateMany(filtro, modificador, opções)` — atualiza todos os que casarem.
* `db.colecao.replaceOne(filtro, novoDocumento, opções)` — substitui o documento inteiro.

#### 3.2 Modificadores Comuns

* **Campos:**

  * `$set`: define ou atualiza valor de campo.

    ```js
    db.usuarios.updateOne(
      {nome: "Ana"},
      {$set: {idade: 31}}
    );
    ```
  * `$unset`: remove um campo.

    ```js
    db.usuarios.updateOne({nome: "Ana"}, {$unset: {email: ""}});
    ```
  * `$inc`: incrementa valor numérico.

    ```js
    db.contadores.updateOne({_id: "visitas"}, {$inc: {valor: 1}});
    ```
* **Opções:**

  * `upsert: true` — cria novo documento se não existir.
  * `multi: true` (deprecated, use updateMany) — aplica em vários.

#### 3.3 Outras Funções

* `findOneAndUpdate()` / `findOneAndReplace()` — retorna documento antes ou depois da modificação.
* `bulkWrite()` — executa múltiplas operações em lote.

---

### 4. Delete (Remoção)

* Remove documentos de uma coleção.

#### 4.1 Métodos

* `db.colecao.deleteOne(filtro)` — remove o primeiro que casar.
* `db.colecao.deleteMany(filtro)` — remove todos que casarem.

#### 4.2 Outras Funções

* `findOneAndDelete()` — remove e retorna o documento.
* `bulkWrite()` — inclui operações de exclusão em lote.


## 2.6 MongoDB – Operações Avançadas e Frameworks

### Introdução

* Após dominar CRUD, explore operações avançadas e frameworks que facilitam extração e análise em bancos de grande volume.
* Continua-se usando o shell `mongo` para exemplificar as consultas.

---

### 1. Trabalhando com Arrays e Subdocumentos

* **Arrays** funcionam como campos com múltiplos valores ordenados.

* **Consultas básicas**:

  * Filtrar documentos cujo array contenha um valor:

    ```js
    db.produtos.find({tags: "office"});
    ```
  * **\$all**: todos os valores especificados devem estar presentes:

    ```js
    db.docs.find({categorias: {$all: ["finance", "yearly"]}});
    ```
  * **\$size**: tamanho exato do array (não combina com operadores de comparação):

    ```js
    db.usuários.find({itens: {$size: 3}});
    ```

* **Modificadores de Arrays**:

  * **\$push**: adiciona elemento ao final do array.

    ```js
    db.usuario.updateOne(
      {_id: 1},
      {$push: {notificações: {mensagem: "Bem-vindo", data: new Date()}}}
    );
    ```
  * **\$slice**: na projeção, retorna apenas um subconjunto do array:

    ```js
    db.documentos.find(
      {_id: 1},
      {logs: {$slice: [10, 5]}}  // pula 10 e retorna 5 elementos
    );
    ```

* **Subdocumentos**:

  * Consultar subdocumento completo (ordem sensível):

    ```js
    db.alunos.find({endereço: {rua: "A", num: 10}});
    ```
  * Consultar campo de subdocumento:

    ```js
    db.alunos.find({"endereço.rua": "A"});
    ```

---

### 2. Avaliando Performance com `explain()`

* Retorna plano de execução, índices usados, número de documentos examinados, etc.

  ```js
  db.pedidos.find({status: "ativo"}).explain("executionStats");
  ```
* No **Compass**, acesse aba **Explain Plan** para visualizar graficamente.

---

### 3. Projeção e Operadores Avançados

* **Projeção**: incluir (`1`) ou excluir (`0`) campos:

  ```js
  db.usuários.find({}, {nome:1, email:1, _id:0});
  ```

* **\$elemMatch**: filtra arrays de documentos retornando apenas elementos que casam:

  ```js
  db.produtos.find(
    {reviews: {$elemMatch: {nota: {$gt: 4}}}},
    {reviews: {$elemMatch: {nota: {$gt: 4}}}}
  );
  ```

* **Operadores Lógicos**:

  * **\$and**, **\$or**, **\$not**, **\$nor**:

    ```js
    db.usuarios.find({
      $and: [
        {idade: {$gte: 18}},
        {pais: {$in: ["BR","PT"]}}
      ]
    });
    ```

* **\$expr**: permite usar expressões de agregação em consultas (sem JS), comparando campos entre si:

  ```js
  db.produtos.find({
    $expr: {$gt: ["$preçoVenda", "$custo"]}
  });
  ```

* **count()**: conta documentos que obedecem ao filtro:

  ```js
  db.usuários.find({ativo:true}).count();
  ```

---

### 4. Aggregation Framework

* Pipeline composto por estágios (`$match`, `$group`, `$project`, `$sort`, etc.).
* **Exemplo**: total de vendas por categoria:

  ```js
  db.vendas.aggregate([
    {$match: {ano: 2024}},
    {$group: {_id: "$categoria", total: {$sum: "$valor"}}},
    {$sort: {total: -1}}
  ]);
  ```
* Vantagens: código mais legível, uso extensivo de índices e operações complexas (joins com `$lookup`, transformações, etc.).

---

### 5. Transações Multidocumento

* Suporte a ACID em múltiplas coleções e documentos.

* **APIs**:

  * **Core**: controle manual de início, commit/abort e tratamento de erros.
  * **Callback**: função que envolve o fluxo e faz retry automático em erros transitórios.

* **Exemplo (Callback API)**:

  ```js
  const session = client.startSession();
  await session.withTransaction(async () => {
    await db.contas.updateOne(
      {_id: 1}, {$inc: {saldo: -100}}, {session}
    );
    await db.contas.updateOne(
      {_id: 2}, {$inc: {saldo: 100}}, {session}
    );
  });
  session.endSession();
  ```

---

### 6. Ferramentas e Frameworks

* **MongoDB Compass** (GUI oficial): design de esquemas, índices, explain, agregations.
* **Mongoose** (Node.js): ODM que define *schemas*, validações e middlewares.
* **Morphia** (Java): mapeamento objeto–documento, integração com Spring.
* **PyMongo** (Python): driver oficial, com suporte a sessions e transações.
* **MongoEngine** (Python): ORM inspirado no Django.
* **Spring Data MongoDB** (Java/Spring): abstração de repositórios e consulta por métodos.

