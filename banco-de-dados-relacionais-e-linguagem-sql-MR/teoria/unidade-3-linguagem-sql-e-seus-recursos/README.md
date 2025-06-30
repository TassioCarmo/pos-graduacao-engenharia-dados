# Banco de Dados SQL: Glossário e Conceitos Fundamentais

Este documento serve como um guia abrangente para a disciplina de Banco de Dados SQL da pós-graduação, organizando conceitos fundamentais de SQL e administração de bancos de dados relacionais.

## Sumário

1. [Comandos DML e Funções](#comandos-dml-e-funções)
2. [Junções](#junções)
3. [Subconsultas](#subconsultas)
4. [Constraints e Views](#constraints-e-views)
5. [Sequences, Índices e Sinônimos](#sequences-índices-e-sinônimos)
6. [Privilégios e Expressões Regulares](#privilégios-e-expressões-regulares)

## Comandos DML e Funções

### Classificação de Linhas (Row Sorting)

- A classificação de resultados é um recurso essencial do SQL
- Embora o design do BD organize funções de negócio por entidade e atributos, o SQL utiliza a cláusula `ORDER BY` para ordenação de dados
- Por padrão, a ordenação é crescente (do menor para o maior)
- Valores NULL são exibidos por último, mas podem ser configurados com `NULL FIRST` ou `NULL LAST`

Exemplo:
```sql
-- Ordenação básica crescente (padrão)
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary;

-- Ordenação decrescente
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary DESC;

-- Configurando posição dos valores NULL
SELECT employee_id, first_name, commission_pct
FROM employees
ORDER BY commission_pct NULLS FIRST;
```

### Tipos de Funções

#### Função de Linha Única (Single-Row Functions)

- Operam em linhas individuais e retornam um resultado por linha
- Incluem funções de caractere, número, data e conversão de tipos
- Úteis para padronização de registros, principalmente quanto a maiúsculas e minúsculas

Exemplo:
```sql
-- Função de caractere: converte para maiúsculo
SELECT UPPER(first_name) AS nome_maiusculo
FROM employees;

-- Função numérica: arredonda para uma casa decimal
SELECT employee_id, salary, ROUND(salary/12, 1) AS salario_mensal
FROM employees;
```

#### Função Multilinha (Multi-Row Functions)

- Manipulam grupos de linhas para fornecer um resultado por grupo
- Também conhecidas como funções de grupo
- Aceitam múltiplas linhas como entrada e retornam um único valor como saída

Exemplo:
```sql
-- Média salarial
SELECT AVG(salary) AS media_salarial
FROM employees;

-- Contagem de funcionários por departamento
SELECT department_id, COUNT(*) AS total_funcionarios
FROM employees
GROUP BY department_id;
```

### Tabela DUAL

- Recurso que permite testar funções sem necessidade de uma tabela física
- Usada para criar instruções SELECT e executar funções não relacionadas a uma tabela específica
- Útil para cálculos e avaliação de expressões

Exemplo:
```sql
-- Calculando expressão matemática
SELECT 24*60 AS minutos_dia FROM DUAL;

-- Testando função de data
SELECT SYSDATE, SYSDATE + 7 AS proxima_semana FROM DUAL;

-- Manipulação de string
SELECT UPPER('teste de função') FROM DUAL;
```

### Manipulação de Strings

Exemplos:
```sql
-- Convertendo strings para maiúsculo/minúsculo
SELECT 
    UPPER('texto exemplo') AS maiusculo,
    LOWER('TEXTO EXEMPLO') AS minusculo,
    INITCAP('texto exemplo') AS primeiras_maiusculas
FROM DUAL;

-- Concatenando strings
SELECT 
    first_name || ' ' || last_name AS nome_completo,
    CONCAT(first_name, last_name) AS nome_concatenado
FROM employees;

-- Extraindo substrings
SELECT 
    SUBSTR('Banco de Dados', 1, 5) AS primeiros_cinco,
    SUBSTR('Banco de Dados', 7) AS a_partir_setimo
FROM DUAL;
```

### Funções Numéricas

#### ROUND
Arredonda um número para o número especificado de casas decimais.

```sql
SELECT 
    ROUND(125.678) AS sem_decimais,       -- 126
    ROUND(125.678, 1) AS uma_decimal,     -- 125.7
    ROUND(125.678, -1) AS dezena          -- 130
FROM DUAL;
```

#### TRUNCATE
Termina o número em um ponto determinado sem arredondamento.

```sql
SELECT 
    TRUNC(125.678) AS sem_decimais,      -- 125
    TRUNC(125.678, 1) AS uma_decimal,    -- 125.6
    TRUNC(125.678, -1) AS dezena         -- 120
FROM DUAL;
```

#### MOD
Retorna o resto da divisão.

```sql
SELECT 
    MOD(15, 4) AS resto,    -- 3
    MOD(15, 5) AS resto2    -- 0
FROM DUAL;
```

## Junções

### Natural Join

- Une tabelas sem necessidade de especificar as colunas correspondentes
- Nomes e tipos de dados das colunas devem ser idênticos em ambas as tabelas

```sql
-- Natural Join usando sintaxe ANSI
SELECT e.employee_id, e.last_name, d.department_name
FROM employees e NATURAL JOIN departments d;
```

### Cross Join

- Apresenta todas as linhas possíveis entre as tabelas, sem aplicação de filtros
- Operação potencialmente pesada que pode comprometer o desempenho do banco

```sql
-- Cross Join (produto cartesiano)
SELECT e.employee_id, e.last_name, d.department_id, d.department_name
FROM employees e CROSS JOIN departments d;
```

### Junções Externas (Outer Joins)

#### Full Outer Join
Retorna todas as linhas de ambas as tabelas, independentemente de haver correspondência.

```sql
-- Full Outer Join
SELECT e.employee_id, e.last_name, d.department_id, d.department_name
FROM employees e FULL OUTER JOIN departments d
ON e.department_id = d.department_id;
```

### Equijunção e Não Equijunção

- **Equijunção**: Combina linhas que têm os mesmos valores nas colunas especificadas, usando o operador de igualdade (=)
- **Não Equijunção**: Une tabelas sem correspondências exatas entre colunas, usando operadores como <, >, <=, >=, BETWEEN

```sql
-- Equijunção
SELECT e.employee_id, e.last_name, d.department_name
FROM employees e JOIN departments d
ON e.department_id = d.department_id;

-- Não Equijunção
SELECT e.last_name, e.salary, g.grade_level
FROM employees e JOIN salary_grades g
ON e.salary BETWEEN g.lowest_sal AND g.highest_sal;
```

### Tratamento de Valores NULL

#### NULLIF
Compara duas expressões e retorna NULL se iguais, ou a primeira expressão se diferentes.

```sql
SELECT 
    NULLIF(10, 10) AS resultado1,  -- NULL
    NULLIF(10, 20) AS resultado2   -- 10
FROM DUAL;
```

#### COALESCE
Retorna o primeiro valor não NULL da lista.

```sql
-- Substitui commission_pct NULL por 0
SELECT 
    employee_id, 
    salary, 
    COALESCE(commission_pct, 0) AS comissao
FROM employees;
```

### Expressões Condicionais - CASE

```sql
SELECT 
    employee_id, 
    salary,
    CASE 
        WHEN salary < 5000 THEN 'Baixo'
        WHEN salary BETWEEN 5000 AND 10000 THEN 'Médio'
        ELSE 'Alto'
    END AS nivel_salarial
FROM employees;
```

### Autojunção e Consulta Hierárquica

Autojunção permite relacionar uma tabela com ela mesma.

```sql
-- Encontrar os gerentes dos funcionários
SELECT 
    e.employee_id, 
    e.last_name AS funcionario, 
    m.last_name AS gerente
FROM employees e JOIN employees m
ON e.manager_id = m.employee_id;
```

## Funções de Grupo

Principais funções:

```sql
-- Média
SELECT AVG(salary) AS media_salarial FROM employees;

-- Contagem
SELECT COUNT(*) AS total_funcionarios FROM employees;

-- Contagem de valores distintos
SELECT COUNT(DISTINCT department_id) AS total_departamentos FROM employees;

-- Valor máximo e mínimo
SELECT 
    MAX(salary) AS maior_salario,
    MIN(salary) AS menor_salario
FROM employees;

-- Soma
SELECT SUM(salary) AS folha_pagamento FROM employees;

-- Variância e desvio padrão
SELECT 
    VARIANCE(salary) AS variancia,
    STDDEV(salary) AS desvio_padrao
FROM employees;
```

### DISTINCT

- Tem custo computacional alto
- Deve ser evitado em full table scan em tabelas grandes

```sql
-- Usar DISTINCT para valores únicos
SELECT DISTINCT department_id FROM employees;
```

### GROUP BY

Agrupa linhas com valores iguais em colunas resumidas.

```sql
-- Contagem de funcionários por departamento
SELECT 
    department_id, 
    COUNT(*) AS total_funcionarios,
    AVG(salary) AS media_salarial
FROM employees
GROUP BY department_id;
```

### HAVING

Filtra grupos, diferente de WHERE que filtra linhas.

```sql
-- Filtrando departamentos com mais de 5 funcionários
SELECT 
    department_id, 
    COUNT(*) AS total_funcionarios
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

### ROLLUP, CUBE e GROUPING SETS

Extensões do GROUP BY para análises multidimensionais.

```sql
-- ROLLUP: totais hierárquicos
SELECT 
    department_id, 
    job_id, 
    SUM(salary) AS soma_salarios
FROM employees
GROUP BY ROLLUP(department_id, job_id);

-- CUBE: todas as combinações de agrupamento
SELECT 
    department_id, 
    job_id, 
    SUM(salary) AS soma_salarios
FROM employees
GROUP BY CUBE(department_id, job_id);
```

### Operadores de Conjunto

- **UNION**: Retorna todas as linhas de ambas as tabelas, eliminando duplicatas
- **UNION ALL**: Retorna todas as linhas sem eliminar duplicatas
- **INTERSECT**: Retorna linhas comuns a ambas as tabelas
- **MINUS**: Retorna linhas da primeira tabela que não existem na segunda

```sql
-- União de resultados
SELECT employee_id, last_name FROM employees
UNION
SELECT employee_id, last_name FROM former_employees;

-- Interseção de resultados
SELECT department_id FROM employees
INTERSECT
SELECT department_id FROM departments;

-- Diferença de conjuntos
SELECT department_id FROM departments
MINUS
SELECT department_id FROM employees;
```

## Subconsultas

Consultas aninhadas dentro de outras consultas.

```sql
-- Funcionários com salário acima da média
SELECT employee_id, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subconsulta correlacionada
SELECT e.employee_id, e.last_name
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);
```

## Constraints e Views

### Constraints (Restrições)

Regras aplicadas às colunas de uma tabela para garantir a integridade dos dados.

#### Nível da Coluna
```sql
-- Constraint de nível de coluna
CREATE TABLE employees (
    employee_id NUMBER(6) PRIMARY KEY,
    first_name VARCHAR2(20),
    last_name VARCHAR2(25) NOT NULL,
    email VARCHAR2(25) UNIQUE,
    hire_date DATE DEFAULT SYSDATE,
    salary NUMBER(8,2) CHECK (salary > 0)
);
```

#### Nível da Tabela
```sql
-- Constraint de nível de tabela
CREATE TABLE employees (
    employee_id NUMBER(6),
    first_name VARCHAR2(20),
    last_name VARCHAR2(25),
    email VARCHAR2(25),
    hire_date DATE,
    salary NUMBER(8,2),
    CONSTRAINT pk_emp PRIMARY KEY (employee_id),
    CONSTRAINT unq_email UNIQUE (email),
    CONSTRAINT chk_salary CHECK (salary > 0)
);
```

#### Principais Tipos de Constraints

- **PRIMARY KEY**: Identifica exclusivamente cada registro
- **FOREIGN KEY**: Garante a integridade referencial
- **UNIQUE**: Garante que todos os valores numa coluna sejam diferentes
- **CHECK**: Garante que valores atendam a uma condição específica
- **NOT NULL**: Garante que uma coluna não possa ter valores NULL

### Views

Tabelas virtuais baseadas em consultas SQL.

```sql
-- Criação básica de view
CREATE VIEW emp_dept_view AS
SELECT e.employee_id, e.last_name, d.department_name
FROM employees e JOIN departments d
ON e.department_id = d.department_id;

-- View com CHECK OPTION
CREATE OR REPLACE VIEW high_salary_emp AS
SELECT employee_id, last_name, salary, department_id
FROM employees
WHERE salary > 10000
WITH CHECK OPTION CONSTRAINT high_sal_chk;

-- View somente leitura
CREATE OR REPLACE VIEW dept_summary AS
SELECT department_id, COUNT(*) AS emp_count
FROM employees
GROUP BY department_id
WITH READ ONLY;
```

#### Opções para Views

| **COMANDO** | **COMMAND** | **OPERAÇÃO** | **OPERATION** |
|-------------|-------------|--------------|---------------|
| OR REPLACE | OR REPLACE | Recria a view, caso já exista | Recreates the view if it already exists |
| FORCE | FORCE | Cria a view mesmo que as tabelas básicas não existam | Creates the view even if base tables do not exist |
| NOFORCE | NOFORCE | Cria a view apenas se a tabela básica existir (padrão) | Creates the view only if the base table exists (default) |
| WITH CHECK OPTION | WITH CHECK OPTION | Garante que linhas permaneçam acessíveis à view após operações DML | Ensures rows remain visible through the view after INSERT/UPDATE operations |
| CONSTRAINT * | CONSTRAINT * | Nome atribuído ao constraint CHECK OPTION | Name assigned to the CHECK OPTION constraint |
| WITH READ ONLY | WITH READ ONLY | Garante que nenhuma operação DML possa ser executada na view | Guarantees no DML operations can be performed on the view |

#### Análise TOP-N

Técnica para recuperar um número específico de registros ordenados.

```sql
-- Top 5 salários mais altos
SELECT employee_id, last_name, salary
FROM employees
ORDER BY salary DESC
FETCH FIRST 5 ROWS ONLY;

-- Alternativa com ROWNUM (Oracle)
SELECT employee_id, last_name, salary
FROM (
    SELECT employee_id, last_name, salary
    FROM employees
    ORDER BY salary DESC
)
WHERE ROWNUM <= 5;
```

## Sequences, Índices e Sinônimos

### Sequences

Objetos do banco de dados usados para gerar automaticamente números sequenciais.

```sql
-- Criação de sequence
CREATE SEQUENCE emp_seq
  START WITH 1000
  INCREMENT BY 1
  NOCACHE
  NOCYCLE;

-- Utilizando sequence
INSERT INTO employees (employee_id, last_name, email)
VALUES (emp_seq.NEXTVAL, 'Smith', 'smith@example.com');

-- Verificando valor atual
SELECT emp_seq.CURRVAL FROM DUAL;
```

### Índices

Objetos que aceleram a recuperação de linhas por meio de ponteiros.

```sql
-- Índice simples
CREATE INDEX idx_emp_last_name
ON employees(last_name);

-- Índice composto/concatenado
CREATE INDEX idx_emp_dept_job
ON employees(department_id, job_id);

-- Índice único
CREATE UNIQUE INDEX idx_emp_email
ON employees(email);
```

#### Quando Criar Índices

- Colunas com alta cardinalidade (muitos valores distintos)
- Colunas frequentemente usadas em cláusulas WHERE ou condições de junção
- Tabelas grandes onde consultas recuperam menos de 2-4% das linhas

#### Quando Não Criar Índices

- Tabelas pequenas
- Tabelas frequentemente atualizadas
- Colunas raramente usadas em condições de consulta
- Colunas com baixa cardinalidade
- Colunas referenciadas como parte de expressões

### Sinônimos (Synonyms)

Nomes alternativos para objetos do banco de dados.

```sql
-- Criando sinônimo privado
CREATE SYNONYM emp FOR employees;

-- Criando sinônimo público (requer privilégios)
CREATE PUBLIC SYNONYM dept FOR hr.departments;

-- Utilizando sinônimo
SELECT * FROM emp WHERE emp_id = 100;
```

## Privilégios e Expressões Regulares

### Privilégios

Direitos para executar certas instruções SQL, gerenciados pelo DBA.

#### Categorias de Segurança

- **Segurança de Sistema**: Controla acesso ao banco de dados em nível de sistema (criar usuários, alocar espaço, conceder privilégios)
- **Segurança de Dados**: Relaciona-se aos privilégios sobre objetos específicos do banco de dados

```sql
-- Concedendo privilégios de objeto
GRANT SELECT, INSERT ON employees TO user1;

-- Concedendo privilégios com opção de repasse
GRANT SELECT ON departments TO user1 WITH GRANT OPTION;

-- Revogando privilégios
REVOKE SELECT ON employees FROM user1;
```

### Expressões Regulares

Método para descrever padrões simples e complexos para pesquisa e manipulação de strings.

#### Metacaracteres Principais

| **Símbolo** | **Descrição** | **Description** |
|-------------|---------------|-----------------|
| `.` | Corresponde a qualquer caractere único, exceto NULL | Matches any single character except NULL |
| `?` | Corresponde a zero ou uma ocorrência | Matches zero or one occurrence |
| `*` | Corresponde a zero ou mais ocorrências | Matches zero or more occurrences |
| `+` | Corresponde a uma ou mais ocorrências | Matches one or more occurrences |
| `()` | Agrupamento: trata o conteúdo como subexpressão | Grouping: treats content as a subexpression |
| `\` | Caractere de escape | Escape character |
| `\|` | Alternância: especifica correspondências alternativas | Alternation: specifies alternative matches |
| `^` / `$` | Corresponde ao início/fim da linha | Matches start/end of line |
| `[]` | Conjunto de caracteres: qualquer um dos caracteres listados | Character class: any one of the listed characters |

```sql
-- Encontrando emails com padrão específico
SELECT first_name, email
FROM employees
WHERE REGEXP_LIKE(email, '^[A-Z]{4}_[A-Z]{3}$');

-- Substituindo padrões com expressões regulares
SELECT 
    REGEXP_REPLACE('abc123def456', '[0-9]+', 'NUM') AS resultado
FROM DUAL;
-- Resultado: abcNUMdefNUM

-- Extraindo substrings que correspondem ao padrão
SELECT 
    REGEXP_SUBSTR('Contato: (11) 98765-4321', '[0-9]{2}\) [0-9\-]+') AS telefone
FROM DUAL;
-- Resultado: 11) 98765-4321
```

## Glossário

| **Termo** | **Term** | **Definição** | **Definition** |
|-----------|----------|---------------|---------------|
| Comandos DML | DML Commands | Linguagem de Manipulação de Dados - comandos usados para manipular dados como SELECT, INSERT, UPDATE e DELETE | Data Manipulation Language - commands used to manipulate data like SELECT, INSERT, UPDATE and DELETE |
| Função de Linha Única | Single-Row Function | Função que opera em uma linha por vez e retorna um resultado para cada linha | Function that operates on one row at a time and returns one result per row |
| Função de Grupo | Group Function | Função que opera em conjuntos de linhas para retornar um único resultado por grupo | Function that operates on sets of rows to return one result per group |
| Junção | Join | Operação que combina linhas de duas ou mais tabelas com base em colunas relacionadas | Operation that combines rows from two or more tables based on related columns |
| Natural Join | Natural Join | Junção que combina tabelas baseada em colunas com mesmo nome e tipo de dados | Join that combines tables based on columns with the same name and data type |
| Equijunção | Equijoin | Junção baseada em valores iguais entre colunas relacionadas | Join based on equal values between related columns |
| Junção Externa | Outer Join | Junção que inclui linhas não correspondentes de uma ou ambas as tabelas | Join that includes non-matching rows from one or both tables |
| Subconsulta | Subquery | Consulta aninhada dentro de outra consulta SQL | Query nested inside another SQL query |
| Constraint | Constraint | Regra que limita os valores permitidos em uma tabela | Rule that restricts the values allowed in a table |
| View | View | Tabela virtual baseada em uma consulta SQL | Virtual table based on a SQL query |
| Sequence | Sequence | Objeto que gera valores numéricos sequenciais | Object that generates sequential numeric values |
| Índice | Index | Estrutura para melhorar a velocidade de recuperação de dados | Structure to improve the speed of data retrieval |
| Sinônimo | Synonym | Nome alternativo para um objeto de banco de dados | Alternative name for a database object |
| Privilégio | Privilege | Permissão para executar determinadas operações no banco de dados | Permission to perform certain operations in the database |
| Expressão Regular | Regular Expression | Padrão que descreve um conjunto de strings | Pattern that describes a set of strings |
| GROUP BY | GROUP BY | Cláusula que agrupa linhas com valores iguais | Clause that groups rows with equal values |
| HAVING | HAVING | Cláusula que filtra grupos após o agrupamento | Clause that filters groups after grouping |
| ROLLUP | ROLLUP | Extensão do GROUP BY que produz totais hierárquicos | Extension of GROUP BY that produces hierarchical totals |
| CUBE | CUBE | Extensão do GROUP BY que produz todas as combinações de agrupamento | Extension of GROUP BY that produces all grouping combinations |
| DBA | DBA | Administrador de Banco de Dados - profissional responsável pela administração | Database Administrator - professional responsible for database administration |
