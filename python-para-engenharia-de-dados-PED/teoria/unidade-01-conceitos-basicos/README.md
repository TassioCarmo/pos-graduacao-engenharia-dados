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
| `%` | Módulo (resto) | `5 % 3` → `2` |
| `**` | Exponenciação | `5 ** 3` → `125` |

**Exemplos de uso:**
```python
a = 10
b = 3

soma = a + b          # 13
diferenca = a - b     # 7
produto = a * b       # 30
quociente = a / b     # 3.3333333333333335
quociente_int = a // b  # 3
resto = a % b         # 1
potencia = a ** b     # 1000
```

**Operadores de atribuição combinados:**
```python
x = 10
x += 5   # Equivalente a: x = x + 5   (x agora é 15)
x -= 3   # Equivalente a: x = x - 3   (x agora é 12)
x *= 2   # Equivalente a: x = x * 2   (x agora é 24)
x /= 4   # Equivalente a: x = x / 4   (x agora é 6.0)
x //= 2  # Equivalente a: x = x // 2  (x agora é 3.0)
x %= 2   # Equivalente a: x = x % 2   (x agora é 1.0)
x **= 3  # Equivalente a: x = x ** 3  (x agora é 1.0)
```

### Operadores Lógicos / Logical Operators

Os operadores lógicos são usados para combinar expressões condicionais.

| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `and` | Verdadeiro se ambas as expressões forem verdadeiras | `x > 0 and x < 10` |
| `or` | Verdadeiro se pelo menos uma das expressões for verdadeira | `x < 0 or x > 10` |
| `not` | Inverte o valor da expressão | `not (x > 0)` |

**Exemplos de uso:**
```python
idade = 25
salario = 3000

# Usando operador and (E)
if idade > 18 and salario > 2000:
    print("Elegível para empréstimo")

# Usando operador or (OU)
if idade < 18 or idade > 65:
    print("Faixa etária especial")

# Usando operador not (NÃO)
if not (idade < 18):
    print("Maior de idade")
```

**Operadores de comparação:**
```python
a = 10
b = 5

igual = a == b        # False
diferente = a != b    # True
maior = a > b         # True
menor = a < b         # False
maior_igual = a >= b  # True
menor_igual = a <= b  # False
```

**Operadores de identidade:**
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

mesmo_objeto = a is c    # True (a e c referenciam o mesmo objeto)
objetos_diferentes = a is b  # False (a e b são objetos diferentes com o mesmo valor)
```

**Operadores de pertencimento:**
```python
lista = [1, 2, 3, 4, 5]

existe = 3 in lista     # True
nao_existe = 6 in lista  # False
```

## Estruturas de Controle / Control Structures

### Controle de Fluxo if/elif/else / Flow Control if/elif/else

As estruturas condicionais permitem executar diferentes blocos de código dependendo de condições específicas.

**Estrutura básica:**
```python
if condição:
    # Código executado se a condição for verdadeira
elif outra_condição:
    # Código executado se a primeira condição for falsa e esta for verdadeira
else:
    # Código executado se todas as condições anteriores forem falsas
```

**Exemplo prático:**
```python
nota = 85

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
elif nota >= 60:
    conceito = "D"
else:
    conceito = "F"

print(f"Nota: {nota}, Conceito: {conceito}")  # Nota: 85, Conceito: B
```

**Operador ternário:**
```python
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
```

### Repetição (loop) for / For Loop

O loop `for` é usado para iterar sobre uma sequência (lista, tupla, dicionário, string, etc.) ou outros objetos iteráveis.

**Estrutura básica:**
```python
for elemento in sequência:
    # Código a ser executado para cada elemento
```

**Exemplos:**
```python
# Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

# Iterando sobre uma string
for letra in "Python":
    print(letra)

# Iterando sobre um dicionário
aluno = {"nome": "Maria", "idade": 25, "curso": "Python"}
for chave in aluno:
    print(f"{chave}: {aluno[chave]}")

# Iterando sobre pares chave-valor de um dicionário
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Iterando com índices usando enumerate
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")
```

**Controle de loops:**
```python
# break - interrompe o loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Imprime 0, 1, 2, 3, 4

# continue - pula para a próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Imprime apenas números ímpares: 1, 3, 5, 7, 9

# else com for - executado quando o loop termina normalmente (sem break)
for i in range(5):
    print(i)
else:
    print("Loop concluído com sucesso!")
```

### Repetição (loop) while / While Loop

O loop `while` executa um bloco de código enquanto uma condição for verdadeira.

**Estrutura básica:**
```python
while condição:
    # Código a ser executado enquanto a condição for verdadeira
```

**Exemplos:**
```python
# Contagem regressiva
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("Fim!")

# Loop infinito com break
while True:
    resposta = input("Digite 'sair' para encerrar: ")
    if resposta.lower() == 'sair':
        break
    print(f"Você digitou: {resposta}")

# while com else - executado quando a condição se torna falsa
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
else:
    print("Contagem concluída!")
```

## Funções / Functions

Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas ajudam a organizar o código, evitar repetição e aumentar a legibilidade.

**Definição de funções:**
```python
def nome_da_funcao(parametro1, parametro2):
    """
    Docstring: descrição da função.
    
    Args:
        parametro1: Descrição do parâmetro 1.
        parametro2: Descrição do parâmetro 2.
        
    Returns:
        Descrição do que a função retorna.
    """
    # Corpo da função
    resultado = parametro1 + parametro2
    return resultado
```

**Exemplos de funções:**
```python
# Função simples sem parâmetros
def saudacao():
    print("Olá, mundo!")

# Função com parâmetros
def soma(a, b):
    return a + b

# Função com parâmetros padrão
def potencia(base, expoente=2):
    return base ** expoente

# Função com número variável de argumentos
def soma_tudo(*args):
    return sum(args)

# Função com argumentos nomeados variáveis
def info_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
```

**Chamando funções:**
```python
saudacao()                        # Olá, mundo!
resultado = soma(5, 3)            # 8
quadrado = potencia(4)            # 16 (expoente padrão é 2)
cubo = potencia(4, 3)             # 64
total = soma_tudo(1, 2, 3, 4, 5)  # 15
info_pessoa(nome="Ana", idade=25, profissao="Desenvolvedora")
```

**Funções lambda (anônimas):**
```python
# Função lambda simples
quadrado = lambda x: x ** 2

# Usando lambda com funções de ordem superior
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))  # [1, 4, 9, 16, 25]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

### Função range / range Function

A função `range()` gera uma sequência de números, comumente usada em loops for.

**Sintaxe:**
```python
range(start, stop, step)
```
- `start`: Valor inicial (inclusivo), padrão é 0
- `stop`: Valor final (exclusivo)
- `step`: Incremento, padrão é 1

**Exemplos:**
```python
# range com um argumento
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# range com dois argumentos
for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(i)

# range com três argumentos
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)

# range com passo negativo
for i in range(10, 0, -1):  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    print(i)

# Convertendo range para lista
lista = list(range(5))  # [0, 1, 2, 3, 4]
```

### Números Aleatórios / Random Numbers

Python fornece o módulo `random` para gerar números aleatórios.

**Principais funções:**
```python
import random

# Número aleatório entre 0.0 e 1.0
aleatorio = random.random()  # Ex: 0.7134543848485449

# Número inteiro aleatório em um intervalo
inteiro = random.randint(1, 10)  # Ex: 7 (inclui 1 e 10)

# Escolha aleatória de elementos de uma sequência
frutas = ["maçã", "banana", "laranja", "uva"]
escolhida = random.choice(frutas)  # Ex: "laranja"

# Embaralhando uma lista
random.shuffle(frutas)  # A lista original é modificada

# Amostra aleatória de elementos (sem repetição)
amostra = random.sample(frutas, 2)  # Ex: ["uva", "maçã"]

# Semente aleatória para reproduzibilidade
random.seed(42)  # Garante que a sequência de números seja a mesma
```

## Manipulação de Arquivos / File Handling

A manipulação de arquivos em Python é uma operação fundamental para entrada e saída de dados. Python oferece funções simples e intuitivas para trabalhar com arquivos.

**Abrindo e fechando arquivos:**
```python
# Método básico (requer close explícito)
arquivo = open("exemplo.txt", "r")  # Modo de leitura
conteudo = arquivo.read()
arquivo.close()

# Usando o gerenciador de contexto 'with' (recomendado)
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
# O arquivo é fechado automaticamente ao sair do bloco with
```

**Modos de abertura de arquivo:**
- `"r"`: Leitura (padrão)
- `"w"`: Escrita (cria novo arquivo ou sobrescreve existente)
- `"a"`: Anexar (append) ao final do arquivo

