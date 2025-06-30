# Documentação Python para Pós-Graduação
# Python Documentation for Post-Graduation

## Sumário / Summary
- [Introdução / Introduction](#introdução--introduction)
  - [O que é Python? / What is Python?](#o-que-é-python--what-is-python)
  - [Por que usar Python? / Why use Python?](#por-que-usar-python--why-use-python)
- [Variáveis / Variables](#variáveis--variables)
  - [Variáveis String / String Variables](#variáveis-string--string-variables)
  - [Variáveis Numéricas / Numeric Variables](#variáveis-numéricas--numeric-variables)
    - [Inteiros (int) / Integers (int)](#inteiros-int--integers-int)
    - [Ponto Flutuante (float) / Floating Point (float)](#ponto-flutuante-float--floating-point-float)
    - [Booleanos (bool) / Booleans (bool)](#booleanos-bool--booleans-bool)
    - [Números Complexos (complex) / Complex Numbers (complex)](#números-complexos-complex--complex-numbers-complex)
- [Estruturas de Dados / Data Structures](#estruturas-de-dados--data-structures)
  - [Dicionários / Dictionaries](#dicionários--dictionaries)
    - [Método get / get Method](#método-get--get-method)
    - [Método del / del Method](#método-del--del-method)
    - [Método clear / clear Method](#método-clear--clear-method)
    - [Método copy / copy Method](#método-copy--copy-method)
  - [Tuplas / Tuples](#tuplas--tuples)
  - [Listas / Lists](#listas--lists)
- [Operadores / Operators](#operadores--operators)
  - [Operadores Aritméticos / Arithmetic Operators](#operadores-aritméticos--arithmetic-operators)
  - [Operadores Lógicos / Logical Operators](#operadores-lógicos--logical-operators)
- [Estruturas de Controle / Control Structures](#estruturas-de-controle--control-structures)
  - [Controle de Fluxo if/elif/else / Flow Control if/elif/else](#controle-de-fluxo-ifelifelse--flow-control-ifelifelse)
  - [Repetição (loop) for / For Loop](#repetição-loop-for--for-loop)
  - [Repetição (loop) while / While Loop](#repetição-loop-while--while-loop)
- [Funções / Functions](#funções--functions)
  - [Função range / range Function](#função-range--range-function)
  - [Números Aleatórios / Random Numbers](#números-aleatórios--random-numbers)
- [Manipulação de Arquivos / File Handling](#manipulação-de-arquivos--file-handling)
- [Conexões com Bancos de Dados e Arquivos / Database and File Connections](#conexões-com-bancos-de-dados-e-arquivos--database-and-file-connections)
- [Programação Orientada a Objetos / Object-Oriented Programming](#programação-orientada-a-objetos--object-oriented-programming)
  - [Motivações / Motivations](#motivações--motivations)
  - [Características / Characteristics](#características--characteristics)
  - [Conceito de Objetos / Object Concept](#conceito-de-objetos--object-concept)
  - [Definição / Definition](#definição--definition)
  - [Pilares da POO / OOP Pillars](#pilares-da-poo--oop-pillars)
    - [Abstração / Abstraction](#abstração--abstraction)
    - [Encapsulamento / Encapsulation](#encapsulamento--encapsulation)
    - [Herança / Inheritance](#herança--inheritance)
    - [Polimorfismo / Polymorphism](#polimorfismo--polymorphism)
  - [Classes / Classes](#classes--classes)
  - [Instâncias / Instances](#instâncias--instances)
  - [Construtores / Constructors](#construtores--constructors)
  - [Métodos / Methods](#métodos--methods)
    - [Parâmetros / Parameters](#parâmetros--parameters)
    - [Self / Self](#self--self)
    - [Modificadores de Acesso / Access Modifiers](#modificadores-de-acesso--access-modifiers)

## Introdução / Introduction

### O que é Python? / What is Python?

Python é uma linguagem de programação relativamente simples que foi criada por Guido van Rossum em 1991. É uma linguagem de alto nível, interpretada e conhecida por sua alta produtividade.

Python foi desenvolvida com foco na legibilidade de código e na produtividade do programador. O nome da linguagem foi inspirado no grupo de comédia britânico Monty Python, refletindo a intenção do criador de fazer uma linguagem divertida de usar.

Características principais do Python:

#### Simples
- **Elegante**: Requer menos linhas de código comparado a linguagens como Java, C e C++
- **Sintaxe clara**: Utiliza indentação para definir blocos de código, o que força uma formatação padronizada
- **Documentação gratuita e de fácil acesso**: Ampla documentação disponível em [python.org](https://docs.python.org/)

#### Alto nível
- **Abstração elevada**: Oculta complexidades da máquina do programador
- **Distante do código de máquina**: Não é necessário gerenciar memória manualmente
- **Próximo à linguagem humana**: A leitura do código se assemelha à linguagem natural

#### Interpretada
- **Não precisa ser compilada**: O código é executado linha por linha
- **Desenvolvimento ágil**: Facilita testes e alterações rápidas

#### Multiplataforma
- **Executa em diversos sistemas**: Windows, Linux, macOS, entre outros
- **Portabilidade**: O mesmo código funciona em diferentes plataformas

### Por que usar Python? / Why use Python?

Python se tornou uma das linguagens mais populares do mundo por diversas razões:

1. **Versatilidade**: Pode ser usada para desenvolvimento web, análise de dados, inteligência artificial, automação, desenvolvimento de aplicações desktop e muito mais.

2. **Comunidade ativa**: Possui uma enorme comunidade que contribui com bibliotecas, frameworks e suporte.

3. **Riqueza de bibliotecas**: O Python Package Index (PyPI) contém mais de 300.000 pacotes para diversas finalidades.

4. **Produtividade**: A sintaxe simples e legível permite desenvolver soluções rapidamente.

5. **Curva de aprendizado suave**: Ideal para iniciantes, mas também poderosa para profissionais experientes.

6. **Integração**: Facilidade para integrar com outras linguagens e tecnologias.

**Exemplo de código Python simples:**
```python
# Este é um exemplo simples de código Python
print("Olá, mundo!")

# Calculando a soma de dois números
a = 5
b = 3
soma = a + b
print(f"A soma de {a} e {b} é {soma}")

# Usando uma função
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Estudante")
print(mensagem)
```

## Variáveis / Variables

Em Python, as variáveis são utilizadas para armazenar dados na memória do computador. Uma das características mais notáveis do Python é que as variáveis são dinamicamente tipadas, o que significa que você não precisa declarar o tipo de uma variável antes de usá-la. O tipo é determinado automaticamente quando você atribui um valor à variável.

Regras para nomear variáveis em Python:
- Devem começar com uma letra ou underscore (_)
- Podem conter letras, números e underscores
- São case-sensitive (nome ≠ Nome)
- Não podem usar palavras reservadas como if, for, class, etc.

**Exemplos de declaração de variáveis:**
```python
nome = "Maria"           # String
idade = 25               # Integer
altura = 1.65            # Float
is_estudante = True      # Boolean
```

### Variáveis String / String Variables

Strings são sequências de caracteres e são usadas para representar texto em Python. Podem ser definidas usando aspas simples (`'`) ou duplas (`"`).

**Criação de strings:**
```python
nome = "João Silva"
curso = 'Python para Pós-Graduação'
```

**Operações com strings:**
```python
# Concatenação
primeiro_nome = "João"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome  # João Silva

# Repetição
linha = "-" * 20  # --------------------

# Indexação (acesso a caracteres individuais)
primeira_letra = nome[0]  # J

# Fatiamento (slicing)
primeiros_caracteres = nome[0:4]  # João

# Comprimento
tamanho = len(nome)  # 10

# Métodos de string
maiusculo = nome.upper()  # JOÃO SILVA
minusculo = nome.lower()  # joão silva
capitalizado = nome.title()  # João Silva
```

**Formatação de strings:**
```python
# Usando format()
mensagem1 = "Olá, {}. Bem-vindo ao curso de {}.".format(nome, curso)

# Usando f-strings (Python 3.6+)
mensagem2 = f"Olá, {nome}. Você tem {idade} anos."

# Formatação com especificadores
preco = 49.99
mensagem3 = f"O preço do curso é R$ {preco:.2f}"  # R$ 49.99
```

### Variáveis Numéricas / Numeric Variables

Python oferece diversos tipos numéricos para diferentes necessidades.

#### Inteiros (int) / Integers (int)

Representam números inteiros sem parte decimal.

```python
idade = 25
quantidade = -10
numero_grande = 1_000_000  # O underscore ajuda na legibilidade
```

Operações com inteiros:
```python
soma = 5 + 3          # 8
subtracao = 10 - 4    # 6
multiplicacao = 3 * 4 # 12
divisao = 10 / 3      # 3.3333333333333335 (retorna float)
divisao_inteira = 10 // 3  # 3
resto = 10 % 3        # 1
potencia = 2 ** 3     # 8
```

#### Ponto Flutuante (float) / Floating Point (float)

Representam números reais com parte decimal.

```python
altura = 1.75
pi = 3.14159
notacao_cientifica = 1.5e3  # 1500.0
```

Operações com floats são similares às operações com inteiros, mas sempre resultam em um float quando pelo menos um dos operandos é float.

Cuidados com precisão:
```python
# Problemas de precisão são comuns em operações com ponto flutuante
resultado = 0.1 + 0.2  # 0.30000000000000004
```

#### Booleanos (bool) / Booleans (bool)

Representam valores lógicos: True (verdadeiro) ou False (falso).

```python
is_estudante = True
esta_aprovado = False
```

Os booleanos são frequentemente usados em expressões condicionais:
```python
if idade >= 18:
    pode_dirigir = True
else:
    pode_dirigir = False
```

Valores que são considerados False em contexto booleano:
- `False`
- `None`
- Zero em qualquer tipo numérico: `0`, `0.0`
- Sequências vazias: `""`, `[]`, `()`
- Dicionários vazios: `{}`

Todos os outros valores são considerados True.

#### Números Complexos (complex) / Complex Numbers (complex)

Representam números complexos com parte real e imaginária.

```python
z = 2 + 3j
```

Propriedades e operações:
```python
parte_real = z.real      # 2.0
parte_imaginaria = z.imag  # 3.0
conjugado = z.conjugate()  # (2-3j)
```

## Estruturas de Dados / Data Structures

### Dicionários / Dictionaries

Dicionários são estruturas de dados que armazenam pares de chave-valor. São mutáveis e não ordenados (em versões do Python anteriores à 3.7).

**Criação de dicionários:**
```python
# Dicionário vazio
dic_vazio = {}

# Dicionário com valores iniciais
aluno = {
    "nome": "Ana Silva",
    "idade": 28,
    "curso": "Python Avançado",
    "notas": [8.5, 9.0, 7.8]
}
```

**Acesso a valores:**
```python
nome_aluno = aluno["nome"]  # Ana Silva

# Acesso a chaves inexistentes gera erro KeyError
# nota_final = aluno["nota_final"]  # KeyError
```

#### Método get / get Method

O método `get()` é uma forma segura de acessar valores em um dicionário, pois ele retorna None (ou um valor padrão especificado) se a chave não existir, em vez de gerar um erro.

```python
# Sem erro para chaves inexistentes
nota_final = aluno.get("nota_final")  # Retorna None

# Com valor padrão
nota_final = aluno.get("nota_final", 0)  # Retorna 0
```

#### Método del / del Method

A instrução `del` permite remover um par chave-valor de um dicionário.

```python
del aluno["notas"]  # Remove a chave "notas" e seu valor
```

#### Método clear / clear Method

O método `clear()` remove todos os pares chave-valor de um dicionário.

```python
aluno.clear()  # Dicionário fica vazio: {}
```

#### Método copy / copy Method

O método `copy()` cria uma cópia superficial do dicionário.

```python
aluno_copia = aluno.copy()
```

**Outros métodos úteis:**
```python
chaves = aluno.keys()       # Retorna um objeto dict_keys com todas as chaves
valores = aluno.values()    # Retorna um objeto dict_values com todos os valores
itens = aluno.items()       # Retorna um objeto dict_items com tuplas (chave, valor)

# Adicionando ou atualizando valores
aluno["nota_final"] = 8.5

# Atualizando com outro dicionário
info_adicional = {"matricula": 12345, "turma": "T01"}
aluno.update(info_adicional)
```

### Tuplas / Tuples

Tuplas são sequências imutáveis e ordenadas. Uma vez criadas, seus elementos não podem ser alterados.

**Criação de tuplas:**
```python
# Tupla vazia
tupla_vazia = ()

# Tupla com um único elemento (observe a vírgula)
tupla_unica = (1,)

# Tupla com múltiplos elementos
coordenadas = (10, 20)
pessoa = ("João", 30, "Engenheiro")
```

**Operações com tuplas:**
```python
# Acesso por índice
nome = pessoa[0]       # João
idade = pessoa[1]      # 30

# Fatiamento
primeiros = pessoa[0:2]  # ("João", 30)

# Comprimento
tamanho = len(pessoa)    # 3

# Concatenação
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
concatenada = tupla1 + tupla2  # (1, 2, 3, 4, 5, 6)

# Repetição
repetida = tupla1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

**Desempacotamento de tuplas:**
```python
# Atribuição múltipla
nome, idade, profissao = pessoa

# Uso com o operador *
primeiro, *resto = (1, 2, 3, 4, 5)  # primeiro = 1, resto = [2, 3, 4, 5]
```

### Listas / Lists

Listas são sequências mutáveis e ordenadas. Podem conter elementos de tipos diferentes e serem modificadas após a criação.

**Criação de listas:**
```python
# Lista vazia
lista_vazia = []

# Lista com elementos
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "Bruno", "Carla"]
mista = [1, "texto", True, [1, 2]]
```

**Operações com listas:**
```python
# Acesso por índice
primeiro = numeros[0]      # 1
ultimo = numeros[-1]       # 5

# Fatiamento
primeiros_tres = numeros[0:3]  # [1, 2, 3]

# Comprimento
tamanho = len(numeros)     # 5

# Modificação
numeros[0] = 10            # [10, 2, 3, 4, 5]

# Adição de elementos
numeros.append(6)          # [10, 2, 3, 4, 5, 6]
numeros.insert(1, 15)      # [10, 15, 2, 3, 4, 5, 6]
numeros.extend([7, 8, 9])  # [10, 15, 2, 3, 4, 5, 6, 7, 8, 9]

# Remoção de elementos
numeros.remove(3)           # Remove o primeiro 3 encontrado
valor_removido = numeros.pop()  # Remove e retorna o último elemento
valor_removido = numeros.pop(0) # Remove e retorna o elemento no índice 0
del numeros[1]              # Remove o elemento no índice 1

# Ordenação
numeros.sort()              # Ordena a lista in-place
numeros.sort(reverse=True)  # Ordena em ordem decrescente
sorted_list = sorted(numeros)  # Retorna uma nova lista ordenada

# Reversão
numeros.reverse()           # Inverte a ordem dos elementos
```

**Compreensão de listas:**

Uma forma concisa de criar listas com base em outras sequências.

```python
# Criando lista de quadrados
quadrados = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condicional
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

## Operadores / Operators

### Operadores Aritméticos / Arithmetic Operators

Os operadores aritméticos são usados para realizar operações matemáticas básicas.

| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `+` | Adição | `5 + 3` → `8` |
| `-` | Subtração | `5 - 3` → `2` |
| `*` | Multiplicação | `5 * 3` → `15` |
| `/` | Divisão | `5 / 3` → `1.6666...` |
| `//` | Divisão inteira | `5 // 3` → `1` |
| `
