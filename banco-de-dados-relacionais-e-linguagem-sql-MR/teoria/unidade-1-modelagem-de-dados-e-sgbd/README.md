# Unidade 1 – Modelagem de dados e Sistemas Gerenciadores de Banco de Dados Relacionais / Data Modeling and Relational Database Management Systems

Este repositório contém o material da disciplina de Bancos de Dados Relacionais e Linguagem SQL, parte do programa de pós-graduação.

# Bancos de Dados Relacionais e Linguagem SQL - Unidade 1

## Sumário

- [1.1 Processo de Modelagem de Dados](#11-processo-de-modelagem-de-dados)
  - [Conceitos Fundamentais](#conceitos-fundamentais)
  - [Processo de Modelagem de Dados](#processo-de-modelagem-de-dados)
  - [Características dos Modelos](#características-dos-modelos)

- [1.2 Entidades e Atributos, Regras de Negócio, Super e Subtipos](#12-entidades-e-atributos-regras-de-negócio-super-e-subtipos)
  - [Entidades](#entidades)
  - [Atributos](#atributos)
  - [Relacionamentos](#relacionamentos)
  - [Super e Subtipos](#super-e-subtipos)
  - [Regras de Negócio](#regras-de-negócio)

- [1.3 Fundamentos de Relacionamentos: UIDs e Normalização](#13-fundamentos-de-relacionamentos-uids-e-normalização)
  - [UIDs (Unique Identifiers)](#uids-unique-identifiers)
  - [Tipos de Entidades](#tipos-de-entidades)
  - [Implementação de Relacionamentos](#implementação-de-relacionamentos)
  - [Tipos de Relacionamentos](#tipos-de-relacionamentos)
  - [Normalização](#normalização)

- [1.4 Modelagem Histórica e Recursiva: Mapeamento, Arcos, Hierarquias](#14-modelagem-histórica-e-recursiva-mapeamento-arcos-hierarquias)
  - [Modelagem de Dados Históricos](#modelagem-de-dados-históricos)
  - [Arcos](#arcos)
  - [Hierarquias](#hierarquias)

- [1.5 Aplicações Práticas do Modelo Relacional](#15-aplicações-práticas-do-modelo-relacional)
  - [Implementação do Modelo ER](#implementação-do-modelo-er)
  - [Conceitos Práticos](#conceitos-práticos)
  - [Elementos Fundamentais](#elementos-fundamentais)
  - [Regras de Integridade](#regras-de-integridade)
  - [Regras de Transformação](#regras-de-transformação)

---

## 1.1 Processo de Modelagem de Dados

### Conceitos Fundamentais

#### Dados vs. Informações
- **Dados**: Material bruto ou não processado
- **Informação**: Conhecimento, inteligência, dado com significado ou função especial, resultado de combinar, comparar, analisar ou executar cálculos

#### O que é um Banco de Dados?
- Conjunto centralizado e estruturado de dados armazenados em sistema de computador
- Fornece recursos para recuperar, adicionar, modificar e excluir dados
- Permite transformação de dados em informações úteis
- Na era da informação, todos os dados têm valor financeiro

### Processo de Modelagem de Dados

#### Etapas do Processo
1. **Projeto Conceitual**
   - Produto: Diagrama Entidade Relacionamento (DER)
   - Mapeamento dos requisitos e variáveis necessárias
   - Captura precisa das necessidades de dados do negócio

2. **Projeto Lógico**
   - Produto: Script de criação das estruturas
   - Transforma o projeto conceitual em diagrama equivalente
   - Utiliza ferramentas CASE de modelagem para automação

3. **Projeto Físico**
   - Produto: Schemas otimizados nos SGBDs
   - Implementa política de armazenamento e otimização
   - Criação de políticas de backup, rotinas de importação e manutenção

#### Características dos Modelos

**Modelo Conceitual:**
- Descreve necessidades de informação da empresa
- Documenta processos e regras de negócio
- Identifica entidades e relacionamentos
- Independente da tecnologia

**Modelo Lógico:**
- Descreve dados com maior detalhe
- Deriva do modelo conceitual
- Inclui todas as entidades e relacionamentos
- Ilustra o DER completo

**Modelo Físico:**
- Extensão do modelo lógico
- Define precisão, tipos de dados e definições de tabelas
- Descreve implementação em banco específico
- Mostra estruturas, colunas, chaves primárias e estrangeiras

---

## 1.2 Entidades e Atributos, Regras de Negócio, Super e Subtipos

### Entidades
- Nome para um conjunto de coisas similares que podem ser listadas
- Itens sobre os quais armazenamos coleção de dados descritivos
- Permitem tirar conclusões úteis sobre fatos aparentemente aleatórios

### Atributos
- Item da coleção de dados que descreve, qualifica, quantifica, classifica e especifica uma entidade
- Possui valor único: número, string, data, imagem, som, etc.
- Cada atributo possui tipo/formato específico

#### Tipos de Atributos
**Por Volatilidade:**
- **Voláteis**: Valores que mudam constantemente (ex: idade)
- **Não voláteis**: Mudam raramente (ex: data de nascimento) - *preferíveis*

**Por Obrigatoriedade:**
- **Obrigatórios**: Devem conter valor
- **Opcionais**: Podem ser deixados nulos

**Por Unicidade:**
- **UID (Unique Identifier)**: Valor exclusivo para o atributo

### Relacionamentos
- Mostram como partes do sistema se afetam mutuamente
- Tão importantes quanto as próprias entidades
- Representam conexões entre entidades

#### Características dos Relacionamentos
- Existem apenas entre entidades (não obrigatórios)
- São bidirecionais com nomes nas duas pontas
- Possuem **opcionalidade** e **cardinalidade**

**Opcionalidade:** Relacionamento pode não existir sempre
**Cardinalidade:** Quantidade em que o relacionamento pode acontecer
- Um-um (1:1)
- Um-muitos (1:N)
- Muitos-muitos (M:N)

### Representação no DER
#### Símbolos para Atributos:
- `#` - Identificadores únicos (UID)
- `*` - Obrigatórios
- `o` - Opcionais

#### Símbolos para Relacionamentos:
- Linha contínua: obrigatório
- Linha pontilhada: opcional
- Linha única: relação de um elemento
- Ramificação: cardinalidade múltipla

### Super e Subtipos
#### Definições
- **Supertipo**: Entidade principal que possui propriedades gerais
- **Subtipo**: Subdivisão de entidade com propriedades especiais

#### Características dos Subtipos
- Herdam todos os atributos e relacionamentos do supertipo
- Possuem atributos ou relacionamentos próprios
- Extraídos do supertipo (nunca existem sozinhos)
- Podem ter seus próprios subtipos

### Regras de Negócio
#### Tipos:
- **Procedurais**: Definem fluxos de trabalho e processos
- **Estruturais**: Indicam tipos de informações e relacionamentos

---

## 1.3 Fundamentos de Relacionamentos: UIDs e Normalização

### UIDs (Unique Identifiers)
- Valores únicos identificáveis para cada linha de uma entidade
- Sinônimo prático: chave primária
- Cada entidade pode ter mais de um identificador único
- Se não houver UID natural, criar UID artificial sequencial

### Tipos de Entidades

#### Entidade Regular
- Estrutura com atributos simples
- Deve ter atributo com valor único escolhido como UID

#### Entidade Fraca
- Estrutura com atributos compostos por atributos de outras entidades
- Requer relacionamento com entidade forte
- Registro secundário tem vínculo existencial com primário

### Implementação de Relacionamentos

#### Três Formas Básicas:

1. **Tabela Própria**
   - Relacionamento implementado através de entidade própria
   - Contém identificadores das entidades relacionadas

2. **Colunas Adicionais**
   - Inserção de colunas em tabela de uma das entidades
   - Mais comum para relacionamentos 1:N

3. **Fusão de Tabelas**
   - Fusão das tabelas das entidades envolvidas
   - Apenas para relacionamentos 1:1

### Tipos de Relacionamentos

| Tipo | Características | Obrigatoriedades |
|------|----------------|------------------|
| 1:1 | Direto entre duas entidades, campo único dos dois lados | Mesmo atributo de valor único |
| 1:N | Mais comum, campo único no primário, repetível no secundário | Único no primário, repetível no secundário |
| M:N | Existe no conceitual, transforma-se em dois 1:N na implementação | Segue regras do 1:N |

### Normalização

#### Primeira Forma Normal (1FN)
- **Objetivo**: Eliminar atributos multivalorados
- **Regra**: Apenas um valor para cada instância de entidade
- **Prática**: Criar nova entidade para dados repetidos com relacionamento

#### Segunda Forma Normal (2FN)
- **Pré-requisito**: Estar na 1FN
- **Regra**: Registros não-chave devem depender da chave primária integralmente
- **Objetivo**: Prevenir redundância de dados
- **Prática**: Criar entidades separadas para conjuntos de dados específicos

#### Terceira Forma Normal (3FN)
- **Pré-requisito**: Estar na 2FN
- **Regra**: Atributos não-chave devem ser mutuamente independentes
- **Proíbe**: Dependências transitivas
- **Prática**: Nenhuma coluna não-chave pode depender de outra coluna não-chave

---

## 1.4 Modelagem Histórica e Recursiva: Mapeamento, Arcos, Hierarquias

### Modelagem de Dados Históricos

#### Quando Usar:
- Registro de auditoria necessário
- Mudança de valores na linha do tempo
- Mudança de relacionamentos temporais
- Relatórios baseados em dados antigos
- Manutenção de versões por tempo determinado

#### Implementação:
- Utiliza relacionamento N:N (transforma-se em dois 1:N)
- Adiciona terceira entidade com chaves das outras tabelas
- Recomenda-se UID virtual registrado
- Permite atributos adicionais temporais

### Arcos

#### Definição:
- Representam relacionamentos OR exclusivos
- Relacionamento entre entidade e outras (duas ou mais) não coexistentes
- Apenas um relacionamento ocorre por vez

#### Características:
- Sempre pertencem a uma entidade
- Podem incluir mais que dois relacionamentos
- Nem todos os relacionamentos precisam estar no arco
- Entidade pode ter vários arcos
- Devem ter mesma opcionalidade
- Podem ter cardinalidade diferente

#### Quando Não Usar:
- Situações melhor modeladas com super/subtipos
- Exemplo: diferentes tipos de conta bancária

### Hierarquias

#### Representação Hierárquica Estrutural:
- Entidades separadas para cada nível
- Relacionamentos explícitos entre níveis
- Semelhante a organogramas

#### Relacionamento Recursivo (Auto-relacionamento):
- Uma única entidade relacionando-se consigo mesma
- Conhecido como "orelha de porco"
- Representação mais simples visualmente
- Mais flexível para mudanças estruturais

#### Comparação:
- **Hierárquica**: Relações explícitas, fácil entendimento
- **Recursiva**: Mais simples, uma única entidade, maior flexibilidade

---

## 1.5 Aplicações Práticas do Modelo Relacional

### Implementação do Modelo ER

#### Transformação:
- Modelo conceitual → Design de banco relacional
- Entidades, atributos, relacionamentos, UIDs → Objetos de banco

### Conceitos Práticos

#### Banco de Dados Relacional:
- Coleção de objetos/relações com operadores
- Mantém integridade, precisão e consistência
- Visto como coleção de tabelas bidimensionais (linhas e colunas)

#### SQL (Structured Query Language):
- Permite acesso eficiente a dados relacionais
- Elimina necessidade de pesquisa manual
- Comandos estruturados simples

### Elementos Fundamentais

#### Chaves:

**Chave Primária (PK - Primary Key):**
- Restrição que garante não-nulidade e unicidade
- Identifica exclusivamente cada linha
- Cada tabela deve ter uma chave primária

**Chave Candidata:**
- Colunas ou combinações que podem ser chave primária
- Não escolhidas tornam-se chaves exclusivas (UK)

**Chave Estrangeira (FK - Foreign Key):**
- Coluna com valores correspondentes à PK de outra tabela
- Se PK composta incluir FK, FK não pode ser NULL
- Pode referenciar a mesma tabela (auto-referência)

#### Estruturas Básicas:
- **Linha**: Entrada na tabela com valores para cada coluna
- **Coluna**: Implementação de atributo ou relacionamento
- Deve conter valores consistentes com formato definido

### Regras de Integridade

| Tipo | Explicação |
|------|------------|
| Integridade das Entidades | PK exclusiva e não-nula |
| Integridade Referencial | FK deve corresponder a PK existente ou ser nula |
| Integridade das Colunas | Valores consistentes com formato da coluna |
| Integridade Definida pelo Usuário | Dados devem cumprir regras da empresa |

### Regras de Transformação

#### Mapeamento:
- **Entidades** → Tabelas
- **Instâncias** → Linhas
- **Atributos** → Colunas
- **UIDs primários** → Chaves primárias
- **UIDs secundários** → Chaves exclusivas
- **Relacionamentos** → Colunas e restrições FK

#### Padronização de Nomes:
- **Tabelas**: Plural do nome da entidade
- **Colunas**: Nome do atributo com underline (_) substituindo espaços
- **Evitar**: Palavras-chave SQL (SELECT, CREATE, FROM, etc.)
- **FKs**: Abreviatura da tabela + nome da coluna (ex: Est_ID_Estado)

#### Considerações Finais:
- Restrições de verificação armazenadas no banco
- Reforçam regras simples de uma única linha
- Garantem integridade e consistência dos dados








## Sumário | Summary
- [Processo de Modelagem de Dados | Data Modeling Process](#processo-de-modelagem-de-dados--data-modeling-process)
- [Entidades, Atributos e Regras de Negócio | Entities, Attributes and Business Rules](#entidades-atributos-e-regras-de-negócio--entities-attributes-and-business-rules)
- [Fundamentos de Relacionamentos | Relationship Fundamentals](#fundamentos-de-relacionamentos--relationship-fundamentals)
- [Modelagem Histórica e Recursiva | Historical and Recursive Modeling](#modelagem-histórica-e-recursiva--historical-and-recursive-modeling)
- [Aplicações Práticas | Practical Applications](#aplicações-práticas--practical-applications)
- [Glossário | Glossary](#glossário--glossary)

## Processo de Modelagem de Dados | Data Modeling Process

### Dados vs Informações | Data vs Information
- **Dados**: Material bruto
- **Informação**: Conhecimento, inteligência, dado com significado ou função especial. Geralmente, é um resultado de combinação, comparação, análise ou cálculos.

### O que é um Banco de Dados? | What is a Database?
Um conjunto centralizado e estruturado de dados armazenados em um sistema de computador para fornecer recursos para recuperar, adicionar, modificar e excluir dados quando necessário.

### Ciclo de Vida da Ciência dos Dados | Data Science Lifecycle
1. Entendimento do Problema
2. Coleta de Dados
3. Processamento de Dados
4. Exploração de Dados
5. Comunicação de Resultados
6. Feedback

### Etapas da Modelagem de Dados | Data Modeling Steps
1. **Projeto Conceitual | Conceptual Design**
   - Mapeamento dos requisitos e variáveis necessárias
   - Criação de diagrama conceitual
   - Documentação das necessidades de informação
   - Identificação de entidades e relacionamentos

2. **Projeto Lógico | Logical Design**
   - Transformação do projeto conceitual em diagrama equivalente
   - Geração de scripts para criação de estruturas
   - Descrição detalhada dos dados sem preocupação com implementação física
   - Desenvolvimento do Diagrama Entidade Relacionamento (DER)

3. **Projeto Físico | Physical Design**
   - Execução dos scripts de criação
   - Implementação de políticas de armazenamento
   - Otimização de acesso aos dados
   - Estruturas de cache, backup e manutenção
   - Definição de tipos de dados e tabelas

## Entidades, Atributos e Regras de Negócio | Entities, Attributes and Business Rules

### Entidades | Entities
- Conjunto de coisas similares que podem ser listadas
- Permitem tirar conclusões úteis sobre fatos aparentemente aleatórios
- Itens sobre os quais armazenamos dados descritivos

### Atributos | Attributes
- Itens da coleção de dados que descrevem uma entidade
- Possuem valor único (número, string, data, imagem, som, etc.)
- Podem ser voláteis (mudam constantemente) ou não voláteis (raramente mudam)

### Regras de Negócio | Business Rules
- O Diagrama Entidade Relacionamento (DER) representa os requisitos de dados
- Modelos conceituais são independentes da tecnologia a ser utilizada

#### Objetivos do DER | ERD Objectives
- Capturar todas as informações necessárias
- Garantir que os dados apareçam apenas uma vez
- Não modelar dados derivados
- Projetar dados em local lógico e previsível

### Relacionamentos | Relationships
- Representam conexões importantes entre entidades
- São bidirecionais com nomes nas duas pontas
- Possuem opcionalidade e cardinalidade

#### Opcionalidade | Optionality
- Indica se um relacionamento deve sempre existir

#### Cardinalidade | Cardinality
- Indica a quantidade em que o relacionamento pode ocorrer
- Pode ser um-um, um-muitos ou muitos-muitos

### Super e Subtipos | Super and Subtypes
- Subdivisão de uma entidade quando um grupo de instâncias possui propriedades especiais
- Subtipo herda todos os atributos e relacionamentos do supertipo
- Subtipo pode ter atributos e relacionamentos próprios

### Tipos de Regras de Negócio | Types of Business Rules
- **Procedurais**: Definem fluxos de trabalho ou processos
- **Estruturais**: Indicam tipos de informações e inter-relacionamentos

## Fundamentos de Relacionamentos | Relationship Fundamentals

### UIDs (Identificadores Únicos) | Unique Identifiers
- Valores únicos identificáveis para cada linha de uma entidade
- Sinônimo de chave primária na prática
- Uma entidade pode ter mais de um identificador único

### Tipos de Entidades | Entity Types
- **Entidade Regular**: Estrutura com atributos simples
- **Entidade Fraca**: Estrutura com atributos compostos por atributos de outras entidades

### Implementação de Relacionamentos | Relationship Implementation
- Determinada pela cardinalidade mínima e máxima das entidades
- Três formas básicas:
  1. Tabela própria
  2. Colunas adicionais dentro da tabela entidade
  3. Fusão de tabelas de entidades

| **Tipo de Relacionamento** | **Características** | **Obrigatoriedades** |
|---------------------------|-------------------|-------------------|
| **1:1 (um para um)** | Campo de ligação em comum que pode ser utilizado uma única vez em ambas entidades | Mesmo atributo de valor único dos dois lados |
| **1:N (um para muitos)** | Campo de ligação que pode ser utilizado uma vez no lado primário e repetido no secundário | Atributo de valor único do lado primário e correspondente que pode se repetir no secundário |
| **M:N (muitos para muitos)** | Existe no modelo conceitual, mas na implementação transforma-se em dois relacionamentos 1:N | Segue as regras do relacionamento 1:N |

### Normalização | Normalization

#### Primeira Forma Normal (1FN) | First Normal Form
- Elimina atributos multivalorados
- Cada instância de entidade deve ter apenas um valor
- Remove dados repetidos criando novas entidades relacionadas

#### Segunda Forma Normal (2FN) | Second Normal Form
- Atende à 1FN
- Registros não-chave devem depender da chave primária em sua totalidade
- Previne redundância de dados criando entidades separadas

#### Terceira Forma Normal (3FN) | Third Normal Form
- Nenhum atributo não-UID pode depender de outro atributo não-UID
- Proíbe dependências transitivas
- Elimina dados desnecessários que poderiam causar desatualização

| **Forma Normal** | **Requisitos** | **Objetivo** | **Exemplo de Violação** |
|-----------------|--------------|------------|---------------------|
| **1FN** | Eliminar grupos repetitivos e garantir valores atômicos | Cada campo com apenas um valor por registro | `"1234, 5678"` em uma célula |
| **2FN** | 1FN + atributos não-chave dependem da chave primária inteira | Eliminar dependências parciais | `Curso` depender só de `Aluno_ID` |
| **3FN** | 2FN + atributos não-chave dependem somente da chave primária | Remover dependências transitivas | `Cidade` → `Estado` → `País` |

## Modelagem Histórica e Recursiva | Historical and Recursive Modeling

### Modelagem Histórica | Historical Modeling
- Necessária quando precisamos:
  - Registrar auditoria
  - Acompanhar mudanças de valores na linha do tempo
  - Produzir relatórios com base em dados antigos
  - Manter versões antigas por tempo determinado
- Implementada com relação N:N transformada em duas relações 1:N

### Arcos | Arcs
- Esclarecem relacionamentos OR exclusivos
- Representam relacionamentos não coexistentes (apenas um ocorre por vez)
- Pertencem a uma entidade e podem incluir múltiplos relacionamentos
- Devem consistir em relacionamentos da mesma opcionalidade
- Podem ter cardinalidade diferente

### Hierarquias | Hierarchies
- Comuns em organogramas corporativos e escolares
- Diferença entre hierarquia nos relacionamentos e representação no mundo real
- Relacionamento hierárquico: relações explícitas como gráfico organizacional
- Relacionamento recursivo (auto-relacionamento): representação mais simples usando apenas uma entidade

## Aplicações Práticas | Practical Applications

### Modelo Relacional | Relational Model
- Transforma o modelo conceitual em design de banco de dados
- Converte entidades, atributos, relacionamentos e identificadores em objetos de banco de dados
- Coleção de objetos ou relações com operadores que mantêm integridade, precisão e consistência

### SQL | Structured Query Language
- Permite acesso eficiente a dados em bancos relacionais
- Elimina pesquisa manual com comandos simples

### Conceitos Fundamentais | Fundamental Concepts
- **Chave Primária**: Garante valores não nulos e identifica cada linha de forma exclusiva
- **Chave Candidata**: Coluna que pode ser selecionada como chave primária
- **Chave Exclusiva**: Restrição que exige valor exclusivo em coluna ou conjunto de colunas
- **Chave Estrangeira**: Coluna com valores correspondentes à chave primária de outra tabela
- **Linha**: Entrada em uma tabela com valores para cada coluna
- **Coluna**: Implementação de atributo ou relacionamento

### Regras de Integridade | Integrity Rules
- Definem o estado correto das relações de um banco de dados
- Garantem consistência dos dados

| **Tipo de Restrição** | **Explicação** |
|----------------------|---------------|
| **Integridade das Entidades** | Chave primária exclusiva e não nula |
| **Integridade Referencial** | Chave estrangeira corresponde a valor de chave primária existente |
| **Integridade das Colunas** | Valores consistentes com formato definido |
| **Integridade Definida pelo Usuário** | Dados cumprem regras da empresa |

### Padronização de Nomes | Naming Standards
- Nome da tabela: plural do nome da entidade
- Nomes das colunas: idênticos aos nomes dos atributos (caracteres especiais substituídos por _)
- Evitar palavras-chave do SQL
- Usar abreviatura do nome da tabela para nomear chave estrangeira


