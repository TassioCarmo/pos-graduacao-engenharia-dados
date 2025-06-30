# Manipulação de Arquivos / File Manipulation

## Sumário
- [Introdução](#introdução--introduction)
- [Abertura de Arquivos / Opening Files](#abertura-de-arquivos--opening-files)
- [Leitura de Arquivos / Reading Files](#leitura-de-arquivos--reading-files)
  - [read()](#read)
  - [readline()](#readline)
  - [readlines()](#readlines)
- [Escrita em Arquivos / Writing Files](#escrita-em-arquivos--writing-files)
  - [write()](#write)
  - [writelines()](#writelines)
  - [append](#append)
- [Fechamento de Arquivos / Closing Files](#fechamento-de-arquivos--closing-files)
- [Navegação em Arquivos / File Navigation](#navegação-em-arquivos--file-navigation)
  - [seek()](#seek)
- [Tratamento de Exceções / Exception Handling](#tratamento-de-exceções--exception-handling)
- [Exemplos Práticos / Practical Examples](#exemplos-práticos--practical-examples)

## Introdução

A manipulação de arquivos é uma habilidade fundamental na programação, permitindo o armazenamento persistente de dados, a comunicação entre programas e o processamento de informações externas. Em Python, esta manipulação é feita de forma intuitiva e poderosa através de diversas funções e métodos que permitem ler, escrever e modificar arquivos. Este documento explora em detalhes os conceitos e técnicas essenciais para manipulação eficiente de arquivos.

## Abertura de Arquivos

A função `open()` é a porta de entrada para manipulação de arquivos em Python. Esta função cria um objeto de arquivo que serve como interface para operações subsequentes.

**Sintaxe:**
```python
file_object = open(file_name, mode, encoding=None)
```

**Parâmetros:**
- `file_name`: O caminho para o arquivo (absoluto ou relativo)
- `mode`: O modo de abertura (leitura, escrita, etc.)
- `encoding`: Codificação do arquivo (UTF-8, Latin-1, etc.)

**Modos de abertura comuns:**
- `'r'`: Leitura (padrão)
- `'w'`: Escrita (cria um novo arquivo ou sobrescreve o existente)
- `'a'`: Append (adiciona ao final do arquivo)
- `'x'`: Criação exclusiva (falha se o arquivo já existir)
- `'b'`: Modo binário
- `'t'`: Modo texto (padrão)
- `'+'`: Atualização (leitura e escrita)

**Exemplo:**
```python
# Abrindo um arquivo para leitura
arquivo = open('dados.txt', 'r', encoding='utf-8')

# Abrindo um arquivo para escrita
arquivo_saida = open('resultados.txt', 'w', encoding='utf-8')

# Abrindo um arquivo binário
arquivo_binario = open('imagem.jpg', 'rb')
```

## Leitura de Arquivos

### read()

O método `read()` lê o conteúdo inteiro de um arquivo ou um número específico de bytes.

**Sintaxe:**
```python
conteudo = file_object.read(size=-1)
```

**Parâmetros:**
- `size`: O número de bytes a serem lidos. Se omitido ou negativo, lê o arquivo inteiro.

**Exemplo:**
```python
# Lendo arquivo inteiro
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Lendo 50 bytes
with open('exemplo.txt', 'r') as arquivo:
    inicio = arquivo.read(50)
    print(inicio)
```

### readline()

O método `readline()` lê uma única linha do arquivo, incluindo o caractere de quebra de linha (`\n`).

**Sintaxe:**
```python
linha = file_object.readline(size=-1)
```

**Parâmetros:**
- `size`: Limite máximo de bytes a serem lidos (raramente usado)

**Exemplo:**
```python
with open('exemplo.txt', 'r') as arquivo:
    primeira_linha = arquivo.readline()
    segunda_linha = arquivo.readline()
    print(primeira_linha, end='')  # end='' evita dupla quebra de linha
    print(segunda_linha, end='')
```

### readlines()

O método `readlines()` lê todas as linhas do arquivo e retorna uma lista, com cada linha como um elemento.

**Sintaxe:**
```python
linhas = file_object.readlines()
```

**Exemplo:**
```python
with open('exemplo.txt', 'r') as arquivo:
    todas_linhas = arquivo.readlines()
    
    # Processando cada linha
    for i, linha in enumerate(todas_linhas):
        print(f"Linha {i+1}: {linha.strip()}")
```

## Escrita em Arquivos / Writing Files

### write()

O método `write()` escreve uma string em um arquivo.

**Sintaxe:**
```python
bytes_escritos = file_object.write(string)
```

**Retorno:**
- Número de caracteres/bytes escritos

**Exemplo:**
```python
with open('saida.txt', 'w') as arquivo:
    arquivo.write("Primeira linha do arquivo.\n")
    arquivo.write("Segunda linha do arquivo.\n")
    bytes = arquivo.write("Terceira linha.")
    print(f"Foram escritos {bytes} bytes na última operação.")
```

### writelines()

O método `writelines()` escreve uma sequência de strings em um arquivo.

**Sintaxe:**
```python
file_object.writelines(sequence)
```

**Parâmetros:**
- `sequence`: Uma sequência de strings (lista, tupla, etc.)

**Observação:** Diferente do que o nome sugere, `writelines()` não adiciona quebras de linha automaticamente.

**Exemplo:**
```python
linhas = [
    "Primeira linha\n",
    "Segunda linha\n",
    "Terceira linha\n"
]

with open('multiplas_linhas.txt', 'w') as arquivo:
    arquivo.writelines(linhas)
```

### append

O modo append (`'a'`) permite adicionar conteúdo ao final de um arquivo sem sobrescrever o conteúdo existente.

**Exemplo:**
```python
# Primeiro, criamos um arquivo com conteúdo
with open('log.txt', 'w') as arquivo:
    arquivo.write("Início do log: 12:00\n")

# Depois, adicionamos mais conteúdo sem apagar o anterior
with open('log.txt', 'a') as arquivo:
    arquivo.write("Nova entrada: 12:30\n")
    arquivo.write("Nova entrada: 13:15\n")
```

## Fechamento de Arquivos / Closing Files

É essencial fechar arquivos após o uso para liberar recursos do sistema e garantir que todos os dados sejam gravados.

### close()

O método `close()` fecha o arquivo e libera quaisquer recursos do sistema associados a ele.

**Sintaxe:**
```python
file_object.close()
```

**Exemplo:**
```python
arquivo = open('exemplo.txt', 'r')
conteudo = arquivo.read()
arquivo.close()  # Importante fechar o arquivo após o uso
```

### Gerenciador de contexto `with`

O gerenciador de contexto `with` fecha automaticamente o arquivo quando o bloco de código é concluído, mesmo se ocorrerem exceções.

**Sintaxe:**
```python
with open(file_name, mode) as file_object:
    # operações com o arquivo
```

**Exemplo:**
```python
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    # O arquivo é fechado automaticamente ao sair do bloco
```

## Navegação em Arquivos / File Navigation

### seek()

O método `seek()` permite posicionar o ponteiro de leitura/escrita em uma posição específica do arquivo.

**Sintaxe:**
```python
file_object.seek(offset, whence=0)
```

**Parâmetros:**
- `offset`: O número de bytes a serem movidos
- `whence`: O ponto de referência para o movimento
  - `0`: Início do arquivo (padrão)
  - `1`: Posição atual
  - `2`: Final do arquivo

**Exemplo:**
```python
with open('exemplo.txt', 'r') as arquivo:
    # Ler os primeiros 5 bytes
    inicio = arquivo.read(5)
    print(f"Primeiros 5 bytes: {inicio}")
    
    # Voltar ao início do arquivo
    arquivo.seek(0)
    
    # Ler 10 bytes a partir do início
    dez_bytes = arquivo.read(10)
    print(f"Primeiros 10 bytes: {dez_bytes}")
    
    # Ir para o byte 15 a partir do início
    arquivo.seek(15)
    posicao_atual = arquivo.tell()  # Obtém a posição atual
    print(f"Posição atual: {posicao_atual}")
    
    # Ler o restante do arquivo a partir da posição 15
    resto = arquivo.read()
    print(f"Resto do arquivo: {resto}")
```

## Tratamento de Exceções / Exception Handling

O tratamento de exceções é crucial ao manipular arquivos para lidar com erros como arquivos inexistentes, problemas de permissão ou disco cheio.

**Exemplo usando `try-except`:**
```python
try:
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Sem permissão para ler o arquivo.")
except IOError as e:
    print(f"Erro de I/O: {e}")
finally:
    print("Operação de leitura finalizada.")
```

## Exemplos Práticos / Practical Examples

### Exemplo 1: Contador de palavras em um arquivo de texto
```python
def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            return len(palavras)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return 0
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return 0

# Uso
quantidade = contar_palavras('artigo.txt')
print(f"O arquivo contém {quantidade} palavras.")
```

### Exemplo 2: Criação de um arquivo de log com timestamp
```python
import datetime

def registrar_log(mensagem):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entrada = f"[{timestamp}] {mensagem}\n"
    
    try:
        with open('aplicacao.log', 'a') as arquivo_log:
            arquivo_log.write(entrada)
        return True
    except Exception as e:
        print(f"Erro ao registrar log: {e}")
        return False

# Uso
registrar_log("Aplicação iniciada")
registrar_log("Usuário 'admin' fez login")
registrar_log("Processando dados...")
registrar_log("Operação concluída com sucesso")
```

### Exemplo 3: Processamento de arquivo CSV
```python
def processar_csv(nome_arquivo):
    resultados = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Pular cabeçalho
            cabecalho = arquivo.readline().strip().split(',')
            
            # Processar linhas de dados
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) == len(cabecalho):
                    # Criar dicionário com os dados da linha
                    registro = {cabecalho[i]: dados[i] for i in range(len(cabecalho))}
                    resultados.append(registro)
        
        return resultados
    except Exception as e:
        print(f"Erro ao processar CSV: {e}")
        return []

# Uso
dados_clientes = processar_csv('clientes.csv')
for cliente in dados_clientes:
    print(f"Nome: {cliente.get('nome')}, Email: {cliente.get('email')}")
```
