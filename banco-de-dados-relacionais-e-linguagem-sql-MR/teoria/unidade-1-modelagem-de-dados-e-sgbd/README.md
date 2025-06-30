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
