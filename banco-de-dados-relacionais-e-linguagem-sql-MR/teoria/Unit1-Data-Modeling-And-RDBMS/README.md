# Unidade 1 – Modelagem de dados e Sistemas Gerenciadores de Banco de Dados Relacionais / Data Modeling and Relational Database Management Systems

Este repositório contém o material da disciplina de Bancos de Dados Relacionais e Linguagem SQL, parte do programa de pós-graduação.

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


