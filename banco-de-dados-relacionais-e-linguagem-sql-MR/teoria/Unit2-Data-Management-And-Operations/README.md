# Banco de Dados Relacionais e Linguagem SQL - Parte II | Relational Databases and SQL Language - Part II

Este repositório contém o material complementar da disciplina de Bancos de Dados Relacionais e Linguagem SQL (Parte II), integrante do programa de pós-graduação.

## Sumário | Summary
- [Ciclo de Vida do Desenvolvimento de Banco de Dados | Database Development Lifecycle](#ciclo-de-vida-do-desenvolvimento-de-banco-de-dados--database-development-lifecycle)
- [Modelos de Dados, Esquemas e Instâncias | Data Models, Schemas and Instances](#modelos-de-dados-esquemas-e-instâncias--data-models-schemas-and-instances)
- [Linguagem SQL: DDL, DML, DCL e TCL | SQL Language: DDL, DML, DCL and TCL](#linguagem-sql-ddl-dml-dcl-e-tcl--sql-language-ddl-dml-dcl-and-tcl)
- [Álgebra e Cálculo Relacional | Relational Algebra and Calculus](#álgebra-e-cálculo-relacional--relational-algebra-and-calculus)
- [Glossário | Glossary](#glossário--glossary)

## Ciclo de Vida do Desenvolvimento de Banco de Dados | Database Development Lifecycle

O desenvolvimento de banco de dados segue uma abordagem sistemática top-down que transforma requisitos de informações de negócio em um banco de dados operacional. Conhecer cada estágio deste ciclo ajuda a planejar melhor um projeto e a ser mais produtivo na construção dos modelos.

### Estratégia e Análise | Strategy and Analysis
- Estudar e analisar os requisitos de negócio utilizando entrevistas com usuários
- Identificar os requisitos de dados
- Prever possíveis necessidades futuras do sistema
- Criar e revisar os modelos conceituais do sistema
- Criar a representação gráfica do modelo

### Design | Design
- Transformar o modelo desenvolvido na fase de estratégia e análise
- Mapear entidades para tabelas, atributos para colunas, relacionamentos para chaves estrangeiras e regras de negócios para restrições

### Criação | Creation
- Gravar e executar os comandos para criar as tabelas e os objetos de apoio do banco de dados
- Preencher as tabelas com dados
- Desenvolver a documentação do usuário, o texto da ajuda e os manuais de operação

### Transição | Transition
- Conduzir o teste de aceitação do usuário
- Verificar se o desenvolvimento atende aos requisitos de negócio
- Operar de forma paralela e converter dados existentes quando necessário
- Proceder com as correções apontadas
- Implantar o sistema para usuários
- Operar o sistema de produção
- Monitorar o desempenho e refinar a operação do sistema

## Modelos de Dados, Esquemas e Instâncias | Data Models, Schemas and Instances

### Revisão de Conceitos Básicos | Basic Concepts Review
- **Tabela**: estrutura de armazenamento básica
- **Coluna**: um tipo de dados em uma tabela
- **Linha**: dado para uma instância de tabela
- **Campo**: o valor encontrado na intersecção entre uma linha e uma coluna
- **Chave Primária**: identificador exclusivo de cada linha
- **Chave Estrangeira**: coluna que se refere a uma coluna de chave primária em outra tabela

### Propriedades Fundamentais | Fundamental Properties
- P1: As entradas nas colunas têm um valor único
- P2: As entradas nas colunas são do mesmo tipo
- P3: Cada linha é única
- P4: A sequência das colunas não é significativa
- P5: A sequência das linhas não é significativa
- P6: Cada coluna tem um nome exclusivo

### Schema | Schema
Quando nosso diagrama entidade-relacionamento é implantado no SGBD (estrutura), ele ainda não possui dados armazenados. Neste momento, ele é apenas o projeto e, portanto, é chamado de esquema de banco de dados, que é modificado com pouca frequência.

**Exemplo de criação de schema:**
```sql
-- Criando um novo schema
CREATE SCHEMA vendas;

-- Definindo o schema como padrão
SET search_path TO vendas;

-- Criando tabela no schema específico
CREATE TABLE vendas.produtos (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2)
);
```

### Instância | Instance
Informações começam a ser inseridas, atualizadas ou apagadas, sendo gerenciadas pelos mecanismos disponíveis no SGBD. A partir deste momento, com o banco de dados implantado, todo este conjunto passa a se chamar instância de banco de dados.

Na prática, quando formos nos conectar a uma instância de banco de dados, teremos que fornecer:
- Endereço (IP ou nome DNS)
- Porta de conexão
- Nome do schema

**Exemplo de conexão com uma instância:**
```sql
-- Exemplo de string de conexão em um aplicativo Java
String url = "jdbc:postgresql://servidor.exemplo.com:5432/banco_dados";
String usuario = "usuario";
String senha = "senha";
Connection conn = DriverManager.getConnection(url, usuario, senha);
```

### Instância em Nuvem | Cloud Instance
No contexto da computação em nuvem, quando tivermos que contratar uma instância para nossos BDs, o conceito envolverá também recursos computacionais como:
- CPU
- Memória
- Largura de banda
- Performance de rede disponível

## Linguagem SQL: DDL, DML, DCL e TCL | SQL Language: DDL, DML, DCL and TCL

### DML (Data Manipulation Language) | Linguagem de Manipulação de Dados

Instruções utilizadas para modificar os dados da tabela por meio da inclusão de novas linhas e alteração ou remoção de linhas existentes:
- INSERT
- UPDATE
- DELETE
- MERGE
- SELECT (limitada à consulta)

#### SELECT | Selecionar
A instrução SELECT acessa os dados no banco de dados. Apesar de não manipular os dados (não faz alterações permanentes), pode operar nos dados acessados retornando valores calculados ou organizados de forma diferente dos originais.

**Exemplo básico:**
```sql
-- Estrutura básica do SELECT
SELECT nome_coluna1, nome_coluna2
FROM nome_tabela
WHERE condição;

-- Exemplo prático
SELECT primeiro_nome, sobrenome
FROM clientes
WHERE cidade = 'São Paulo';
```

#### Conceitos Importantes | Important Concepts
- **Palavra-chave**: comando individual (SELECT, FROM)
- **Cláusula**: parte da instrução (SELECT last_name)
- **Instrução**: combinação de duas ou mais cláusulas (SELECT name FROM actor)

#### Operadores Aritméticos | Arithmetic Operators
- Ordem MDAS (Multiplicação, Divisão, Adição, Subtração)
- Se operadores aparecerem juntos, multiplicação e divisão são avaliadas primeiro
- Se operadores tiverem mesma prioridade, avaliação é feita da esquerda para direita
- Para melhor organização, use parênteses para indicar prioridades

**Exemplo:**
```sql
-- Uso de operadores aritméticos
SELECT 
    produto_id,
    nome,
    preco,
    quantidade,
    preco * quantidade AS valor_total,
    (preco * quantidade) * 0.9 AS valor_com_desconto
FROM produtos
WHERE (preco * quantidade) > 1000;
```

#### NULL | Valor Nulo
- NULL representa valor indisponível, inaplicável, desconhecido ou não atribuído
- Não é zero, espaço, traço ou qualquer outra representação de ausência de valor
- Qualquer operação aritmética com NULL resulta em NULL (exceto divisão por 0, que gera erro)

**Exemplo:**
```sql
-- Tratamento de valores NULL
SELECT 
    produto_id,
    nome,
    preco,
    COALESCE(desconto, 0) AS desconto,
    preco * (1 - COALESCE(desconto, 0)) AS preco_final
FROM produtos;

-- Verificação de valores NULL
SELECT *
FROM funcionarios
WHERE salario IS NULL;
```

#### Aliases | Apelidos
- Renomeia a coluna de saída para leitura mais amigável
- Útil para cálculos
- Deve vir imediatamente após o nome da coluna, usando a palavra AS

**Exemplo:**
```sql
-- Uso de aliases para colunas
SELECT 
    primeiro_nome AS nome,
    sobrenome AS "Nome de Família",
    data_nascimento AS nascimento,
    (salario * 12) AS "Salário Anual"
FROM funcionarios;
```

#### DESCRIBE/DESC | Descrever
Retorna informações sobre a estrutura da tabela:
- Nome da tabela
- Tipos de dados
- Chaves primárias e estrangeiras
- Colunas anuláveis
- Comentários

**Exemplo:**
```sql
-- No Oracle/MySQL
DESCRIBE clientes;
-- ou
DESC clientes;

-- No PostgreSQL
\d clientes;

-- No SQL Server
EXEC sp_columns 'clientes';
```

#### Função de Concatenação | Concatenation Function
- Vincula colunas a outras
- Deixa a saída mais amigável
- Economiza código

**Exemplo:**
```sql
-- No PostgreSQL/MySQL
SELECT 
    produto_id,
    CONCAT(nome, ' - ', categoria) AS produto_categoria
FROM produtos;

-- No Oracle
SELECT 
    produto_id,
    nome || ' - ' || categoria AS produto_categoria
FROM produtos;

-- No SQL Server
SELECT 
    produto_id,
    nome + ' - ' + categoria AS produto_categoria
FROM produtos;
```

#### DISTINCT | Distinto
Elimina linhas duplicadas, útil para saber quantas instâncias únicas existem em uma tabela.

**Exemplo:**
```sql
-- Obtendo valores únicos
SELECT DISTINCT cidade
FROM clientes
ORDER BY cidade;

-- Combinação de colunas para valores únicos
SELECT DISTINCT cidade, estado
FROM clientes
ORDER BY cidade, estado;
```

#### Operadores de Comparação | Comparison Operators
- = (igual)
- > (maior que)
- < (menor que)
- >= (maior ou igual)
- <= (menor ou igual)
- <> ou != (diferente)

#### BETWEEN AND | Entre
Seleciona e exibe linhas com base em uma faixa de valores (inclusive).

**Exemplo:**
```sql
-- Selecionando registros dentro de uma faixa
SELECT produto_id, nome, preco
FROM produtos
WHERE preco BETWEEN 100 AND 500;

-- Equivalente a
SELECT produto_id, nome, preco
FROM produtos
WHERE preco >= 100 AND preco <= 500;
```

#### IN | Conjunto
Testa se um valor está dentro de um conjunto específico de valores.

**Exemplo:**
```sql
-- Verificando se valor está em um conjunto
SELECT produto_id, nome, categoria
FROM produtos
WHERE categoria IN ('Eletrônicos', 'Informática', 'Acessórios');

-- Equivalente a
SELECT produto_id, nome, categoria
FROM produtos
WHERE categoria = 'Eletrônicos' OR categoria = 'Informática' OR categoria = 'Acessórios';
```

#### LIKE | Padrão
Seleciona linhas correspondentes a caracteres, datas ou padrões de números usando caracteres curinga:
- % representa qualquer sequência de zero ou mais caracteres
- _ representa um único caractere

**Exemplo:**
```sql
-- Encontrando nomes que começam com "Jo"
SELECT primeiro_nome, sobrenome
FROM clientes
WHERE primeiro_nome LIKE 'Jo%';

-- Encontrando nomes que têm "an" em qualquer posição
SELECT primeiro_nome, sobrenome
FROM clientes
WHERE primeiro_nome LIKE '%an%';

-- Encontrando nomes com exatamente 4 caracteres
SELECT primeiro_nome, sobrenome
FROM clientes
WHERE primeiro_nome LIKE '____';
```

#### IS NULL / IS NOT NULL | É Nulo / Não é Nulo
Verifica se um valor é NULL ou não.

**Exemplo:**
```sql
-- Encontrando registros com valores nulos
SELECT produto_id, nome, descricao
FROM produtos
WHERE descricao IS NULL;

-- Encontrando registros com valores não nulos
SELECT funcionario_id, nome, data_demissao
FROM funcionarios
WHERE data_demissao IS NOT NULL;
```

#### INSERT | Inserir
Insere novos registros em uma tabela.

**Exemplo:**
```sql
-- Inserção básica com todos os campos
INSERT INTO clientes (cliente_id, nome, email, telefone)
VALUES (1, 'João Silva', 'joao@email.com', '(11) 99999-8888');

-- Inserção com campos opcionais (NULL)
INSERT INTO clientes (cliente_id, nome, email)
VALUES (2, 'Maria Santos', 'maria@email.com');

-- Inserção de múltiplos registros
INSERT INTO clientes (cliente_id, nome, email)
VALUES 
    (3, 'Pedro Oliveira', 'pedro@email.com'),
    (4, 'Ana Souza', 'ana@email.com');

-- Inserção com subconsulta
INSERT INTO clientes_vip (cliente_id, nome, email)
SELECT cliente_id, nome, email
FROM clientes
WHERE total_compras > 10000;
```

#### UPDATE | Atualizar
Modifica linhas existentes em uma tabela.

**Exemplo:**
```sql
-- Atualização básica
UPDATE produtos
SET preco = 199.99
WHERE produto_id = 10;

-- Atualização com múltiplas colunas
UPDATE funcionarios
SET salario = salario * 1.1,
    ultima_atualizacao = CURRENT_DATE
WHERE departamento_id = 5;

-- Atualização com subconsulta
UPDATE pedidos
SET status = 'Enviado'
WHERE cliente_id IN (
    SELECT cliente_id
    FROM clientes
    WHERE tipo = 'Premium'
);
```

> **IMPORTANTE**: Nunca faça UPDATE sem WHERE, pois isso modificará todas as linhas da tabela!

#### FOR UPDATE / COMMIT | Para Atualização / Confirmar
Bloqueia registros para atualização e confirma as alterações.

**Exemplo:**
```sql
-- Bloqueando registros para atualização (transação)
BEGIN;
SELECT * FROM contas
WHERE cliente_id = 1234
FOR UPDATE;

-- Fazendo alterações
UPDATE contas
SET saldo = saldo - 1000
WHERE cliente_id = 1234;

-- Confirmando as alterações
COMMIT;
```

#### DELETE | Excluir
Remove linhas de uma tabela.

**Exemplo:**
```sql
-- Exclusão básica
DELETE FROM produtos_obsoletos
WHERE data_fabricacao < '2020-01-01';

-- Exclusão com subconsulta
DELETE FROM pedidos
WHERE cliente_id IN (
    SELECT cliente_id
    FROM clientes
    WHERE status = 'Inativo'
);
```

> **IMPORTANTE**: Todas as linhas na tabela serão excluídas se você não usar a cláusula WHERE!

#### MERGE | Mesclar
Faz inserção e atualização simultaneamente.

**Exemplo:**
```sql
-- No Oracle/SQL Server
MERGE INTO produtos_destino d
USING produtos_origem o
ON (d.produto_id = o.produto_id)
WHEN MATCHED THEN
    UPDATE SET 
        d.nome = o.nome,
        d.preco = o.preco,
        d.estoque = o.estoque,
        d.ultima_atualizacao = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
    INSERT (produto_id, nome, preco, estoque, ultima_atualizacao)
    VALUES (o.produto_id, o.nome, o.preco, o.estoque, CURRENT_TIMESTAMP);

-- No PostgreSQL (alternativa com CTE)
WITH atualizacoes AS (
    SELECT o.produto_id, o.nome, o.preco, o.estoque
    FROM produtos_origem o
    LEFT JOIN produtos_destino d ON o.produto_id = d.produto_id
)
INSERT INTO produtos_destino (produto_id, nome, preco, estoque)
SELECT produto_id, nome, preco, estoque FROM atualizacoes
ON CONFLICT (produto_id) DO UPDATE
SET nome = EXCLUDED.nome,
    preco = EXCLUDED.preco,
    estoque = EXCLUDED.estoque,
    ultima_atualizacao = CURRENT_TIMESTAMP;
```

### Data Warehouse | Armazém de Dados
Uma coleção de dados feita para auxiliar no processo de tomada de decisão do gerenciamento de negócios. Contém uma grande variedade de dados (pessoais, vendas, clientes, folhas de pagamento, contabilidade) que apresentam uma imagem coerente das condições dos negócios em um ponto único no tempo.

**Exemplo de carga de dados para DW:**
```sql
-- Carga incremental para fatos de vendas
INSERT INTO dw_fatos_vendas (
    data_id, 
    produto_id, 
    cliente_id, 
    loja_id, 
    quantidade, 
    valor_total
)
SELECT 
    d.data_id,
    p.produto_id,
    c.cliente_id,
    l.loja_id,
    v.quantidade,
    v.valor_total
FROM vendas v
JOIN dim_data d ON v.data_venda = d.data
JOIN dim_produto p ON v.produto_codigo = p.codigo_origem
JOIN dim_cliente c ON v.cliente_codigo = c.codigo_origem
JOIN dim_loja l ON v.loja_codigo = l.codigo_origem
WHERE v.data_venda > (SELECT MAX(ultima_carga) FROM controle_carga WHERE tabela = 'fatos_vendas');

-- Atualização do controle de carga
UPDATE controle_carga
SET ultima_carga = CURRENT_TIMESTAMP
WHERE tabela = 'fatos_vendas';
```

## Álgebra e Cálculo Relacional | Relational Algebra and Calculus

### Terminologia | Terminology
- **Linha = Tupla | Row = Tuple**
- **Coluna = Atributo | Column = Attribute**
- **Tabela = Relação | Table = Relation**
- **Tipos de Dados = Domínio | Data Types = Domain**

### Operações | Operations

#### Operações Unárias | Unary Operations
- Seleção (σ)
- Projeção (π)

#### Operações com Base na Teoria dos Conjuntos | Set Theory Operations
- União (∪)
- Interseção (∩)
- Diferença (-)
- Produto Cartesiano (×)

#### Operações Binárias | Binary Operations
- Junção (⋈)
- Divisão (÷)

#### Seleção (σ) | Selection
Escolhe um subconjunto de tuplas de uma relação que satisfaça uma condição de seleção. Funciona como um filtro que mantém apenas as tuplas que satisfazem uma condição qualificadora.

**Notação:**
```
σ condição (Relação)
```

**Equivalente SQL:**
```sql
SELECT *
FROM Tabela
WHERE condição;
```

**Exemplo:**
```sql
-- Álgebra Relacional: σ idade > 30 (Funcionarios)
-- SQL equivalente:
SELECT *
FROM Funcionarios
WHERE idade > 30;
```

#### Projeção (π) | Projection
Seleciona certos atributos enquanto descarta outros. É uma partição vertical da relação.

**Notação:**
```
π expressões (Relação)
```

**Equivalente SQL:**
```sql
SELECT atributo1, atributo2, ...
FROM Tabela;
```

**Exemplo:**
```sql
-- Álgebra Relacional: π nome, salario (Funcionarios)
-- SQL equivalente:
SELECT nome, salario
FROM Funcionarios;
```

#### Operações de Conjunto | Set Operations

##### União (∪) | Union
Inclui todas as tuplas que estão na relação R ou S ou em ambas, desconsiderando duplicatas.

**Notação:**
```
Relação₁ ∪ Relação₂
```

**Equivalente SQL:**
```sql
SELECT *
FROM Tabela1
UNION
SELECT *
FROM Tabela2;
```

**Exemplo:**
```sql
-- Álgebra Relacional: Clientes_SP ∪ Clientes_RJ
-- SQL equivalente:
SELECT *
FROM Clientes
WHERE estado = 'SP'
UNION
SELECT *
FROM Clientes
WHERE estado = 'RJ';
```

##### Interseção (∩) | Intersection
Inclui todas as tuplas que estão tanto na relação R quanto em S.

**Notação:**
```
Relação₁ ∩ Relação₂
```

**Equivalente SQL:**
```sql
SELECT *
FROM Tabela1
INTERSECT
SELECT *
FROM Tabela2;
```

**Exemplo:**
```sql
-- Álgebra Relacional: Produtos_Eletronicos ∩ Produtos_Promocao
-- SQL equivalente:
SELECT produto_id
FROM Produtos
WHERE categoria = 'Eletrônicos'
INTERSECT
SELECT produto_id
FROM Produtos
WHERE em_promocao = true;
```

##### Diferença (-) | Difference
Contém as tuplas que estão na relação R, mas não em S.

**Notação:**
```
Relação₁ - Relação₂
```

**Equivalente SQL:**
```sql
SELECT *
FROM Tabela1
EXCEPT (ou MINUS, dependendo do SGBD)
SELECT *
FROM Tabela2;
```

**Exemplo:**
```sql
-- Álgebra Relacional: Funcionarios - Gerentes
-- SQL equivalente:
SELECT funcionario_id
FROM Funcionarios
EXCEPT
SELECT funcionario_id
FROM Funcionarios
WHERE cargo = 'Gerente';
```

#### Produto Cartesiano (×) | Cartesian Product
Combina informações de duas relações quaisquer, resultando em todas as combinações possíveis entre os elementos das relações originais.

**Notação:**
```
Relação₁ × Relação₂
```

**Equivalente SQL:**
```sql
SELECT *
FROM Tabela1
CROSS JOIN Tabela2;
```

**Exemplo:**
```sql
-- Álgebra Relacional: Produtos × Fornecedores
-- SQL equivalente:
SELECT *
FROM Produtos
CROSS JOIN Fornecedores;
```

## Glossário | Glossary

| Termo | Definição |
|------|-----------|
| **Álgebra Relacional** | Coleção de operações formais em relações, que servem como base para linguagens de consulta em bancos de dados relacionais. |
| **Atributo** | Coluna de uma tabela ou relação que armazena um tipo específico de informação. |
| **Banco de Dados** | Conjunto centralizado e estruturado de dados armazenados em um sistema de computador. |
| **Cardinalidade** | Indica a quantidade em que um relacionamento pode ocorrer (um-um, um-muitos, muitos-muitos). |
| **Chave Estrangeira (FK)** | Coluna que referencia a chave primária de outra tabela. |
| **Chave Primária (PK)** | Identificador único que garante a individualidade de cada registro. |
| **DML** | Data Manipulation Language - linguagem utilizada para manipular dados (INSERT, UPDATE, DELETE, SELECT). |
| **DDL** | Data Definition Language - linguagem utilizada para definir estruturas de dados (CREATE, ALTER, DROP). |
| **DCL** | Data Control Language - linguagem utilizada para controlar acesso aos dados (GRANT, REVOKE). |
| **TCL** | Transaction Control Language - linguagem utilizada para controlar transações (COMMIT, ROLLBACK). |
| **Data Warehouse** | Coleção de dados integrados, orientada por assunto, variável com o tempo e não volátil, que suporta o processo de tomada de decisão. |
| **Domínio** | Conjunto de valores permitidos para um atributo. |
| **Esquema** | Descrição da estrutura lógica do banco de dados, incluindo tabelas, colunas e relacionamentos. |
| **Instância** | Estado atual do banco de dados com todos os dados armazenados em um determinado momento. |
| **MERGE** | Comando SQL que combina operações de INSERT e UPDATE em uma única instrução. |
| **NULL** | Valor especial que representa dados ausentes, desconhecidos ou não aplicáveis. |
| **Produto Cartesiano** | Operação que combina cada linha de uma tabela com todas as linhas de outra tabela. |
| **Projeção** | Operação da álgebra relacional que seleciona atributos específicos de uma relação. |
| **Relação** | Tabela em um banco de dados relacional formada por linhas e colunas. |
| **Seleção** | Operação da álgebra relacional que filtra tuplas de acordo com uma condição. |
| **SGBD** | Sistema Gerenciador de Banco de Dados - software que gerencia o armazenamento, manipulação e recuperação de dados. |
| **SQL** | Structured Query Language - linguagem padrão para trabalhar com bancos de dados relacionais. |
| **Tupla** | Linha de uma tabela ou relação que representa uma entidade específica. |
