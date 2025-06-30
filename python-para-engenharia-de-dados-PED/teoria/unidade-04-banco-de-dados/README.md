# Operações de Banco de Dados em Python 

## Sumário 
- [Introdução](#introdução--introduction)
- [Operações SQL Básicas ](#operações-sql-básicas--basic-sql-operations)
  - [INSERT / Inserção](#insert--inserção)
  - [DELETE / Remoção](#delete--remoção)
  - [UPDATE / Atualização](#update--atualização)
- [Conexões com Bancos de Dados / Database Connections](#conexões-com-bancos-de-dados--database-connections)
  - [MySQL](#mysql)
  - [PostgreSQL](#postgresql)
  - [MongoDB (NoSQL)](#mongodb-nosql)
- [Bibliotecas de Análise de Dados / Data Analysis Libraries](#bibliotecas-de-análise-de-dados--data-analysis-libraries)
  - [Pandas](#pandas)
  - [NumPy](#numpy)
  - [Matplotlib e Seaborn](#matplotlib-e-seaborn)
- [Outras Bibliotecas Úteis / Other Useful Libraries](#outras-bibliotecas-úteis--other-useful-libraries)
  - [Requests e JSON](#requests-e-json)
  - [SQLAlchemy e SQLite3](#sqlalchemy-e-sqlite3)
  - [OpenPyXL](#openpyxl)

## Introdução / Introduction

Este documento serve como uma referência completa para operações de banco de dados em Python, abrangendo desde comandos SQL básicos até integrações com diversas bibliotecas de análise de dados. O material é destinado tanto para estudo acadêmico quanto para demonstração de competências técnicas em ambientes profissionais.

## Operações SQL Básicas / Basic SQL Operations

### INSERT / Inserção

O comando INSERT é utilizado para adicionar novos registros em uma tabela.

**Sintaxe Básica:**
```python
cursor.execute("INSERT INTO nome_tabela (coluna1, coluna2) VALUES (%s, %s)", (valor1, valor2))
```

**Exemplo Detalhado:**
```python
import mysql.connector

# Estabelecer conexão
conn = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="senha",
    database="nome_banco"
)
cursor = conn.cursor()

# Inserção simples
cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", 
               ("Maria Silva", "maria@exemplo.com"))

# Inserção múltipla
clientes = [
    ("João Santos", "joao@exemplo.com"),
    ("Pedro Oliveira", "pedro@exemplo.com")
]
cursor.executemany("INSERT INTO clientes (nome, email) VALUES (%s, %s)", clientes)

# Confirmar alterações
conn.commit()
print(f"Total de registros inseridos: {cursor.rowcount}")

# Fechar conexão
cursor.close()
conn.close()
```

### DELETE / Remoção

O comando DELETE é utilizado para remover registros de uma tabela.

**Sintaxe Básica:**
```python
cursor.execute("DELETE FROM nome_tabela WHERE condição")
```

**Exemplo Detalhado:**
```python
import psycopg2

# Estabelecer conexão
conn = psycopg2.connect(
    host="localhost",
    user="usuario",
    password="senha",
    database="nome_banco"
)
cursor = conn.cursor()

# Excluir um registro específico
cursor.execute("DELETE FROM produtos WHERE id = %s", (123,))

# Excluir registros com base em condição
cursor.execute("DELETE FROM produtos WHERE preco < %s AND estoque = %s", (10.00, 0))

# Confirmar alterações
conn.commit()
print(f"Total de registros excluídos: {cursor.rowcount}")

# Fechar conexão
cursor.close()
conn.close()
```

### UPDATE / Atualização

O comando UPDATE é utilizado para modificar registros existentes em uma tabela.

**Sintaxe Básica:**
```python
cursor.execute("UPDATE nome_tabela SET coluna1 = %s WHERE condição", (novo_valor,))
```

**Exemplo Detalhado:**
```python
import sqlite3

# Estabelecer conexão
conn = sqlite3.connect("banco_dados.db")
cursor = conn.cursor()

# Atualizar um campo específico
cursor.execute("UPDATE funcionarios SET salario = ? WHERE id = ?", (3500.00, 42))

# Atualizar múltiplos campos
cursor.execute("""
    UPDATE funcionarios 
    SET 
        departamento = ?, 
        cargo = ?
    WHERE 
        data_contratacao < ? AND setor = ?
""", ("Vendas", "Analista Sr", "2020-01-01", "Comercial"))

# Confirmar alterações
conn.commit()
print(f"Total de registros atualizados: {cursor.rowcount}")

# Fechar conexão
cursor.close()
conn.close()
```

## Conexões com Bancos de Dados / Database Connections

### MySQL

MySQL é um dos sistemas de gerenciamento de banco de dados relacionais mais populares.

**Instalação:**
```bash
pip install mysql-connector-python
```

**Exemplo Completo:**
```python
import mysql.connector
from mysql.connector import Error

def conectar_mysql():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="senha",
            database="empresa"
        )
        
        if conexao.is_connected():
            info_servidor = conexao.get_server_info()
            print(f"Conectado ao servidor MySQL versão {info_servidor}")
            
            cursor = conexao.cursor()
            cursor.execute("SELECT DATABASE();")
            banco = cursor.fetchone()
            print(f"Conectado ao banco de dados: {banco[0]}")
            
            return conexao
            
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def executar_consulta(conexao, consulta):
    cursor = conexao.cursor()
    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Erro ao executar consulta: {e}")
        return None
    finally:
        cursor.close()

# Exemplo de uso
conexao = conectar_mysql()
if conexao:
    resultados = executar_consulta(conexao, "SELECT * FROM funcionarios LIMIT 5")
    
    if resultados:
        for linha in resultados:
            print(linha)
    
    # Lembre-se de fechar a conexão quando terminar
    conexao.close()
    print("Conexão fechada com sucesso")
```

### PostgreSQL

PostgreSQL é um poderoso sistema de banco de dados relacional de código aberto.

**Instalação:**
```bash
pip install psycopg2-binary
```

**Exemplo Completo:**
```python
import psycopg2
from psycopg2 import Error

def conectar_postgresql():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="empresa",
            user="usuario",
            password="senha",
            port="5432"
        )
        
        # Criar cursor para executar operações com o banco de dados
        cursor = conexao.cursor()
        
        # Verificar a versão do PostgreSQL
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()
        print(f"Conectado ao PostgreSQL: {versao[0]}")
        
        return conexao, cursor
        
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None, None

def criar_tabela(conexao, cursor):
    try:
        # Criar tabela de exemplo
        criar_tabela_query = '''
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                data_registro DATE DEFAULT CURRENT_DATE
            )
        '''
        cursor.execute(criar_tabela_query)
        conexao.commit()
        print("Tabela criada com sucesso")
        
    except Error as e:
        print(f"Erro ao criar tabela: {e}")

# Exemplo de uso
conexao, cursor = conectar_postgresql()

if conexao and cursor:
    criar_tabela(conexao, cursor)
    
    # Inserir dados de exemplo
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (%s, %s) RETURNING id",
            ("Ana Carolina", "ana@exemplo.com")
        )
        id_inserido = cursor.fetchone()[0]
        conexao.commit()
        print(f"Cliente inserido com ID: {id_inserido}")
        
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
    
    # Fechar cursor e conexão
    cursor.close()
    conexao.close()
    print("Conexão PostgreSQL fechada")
```

### MongoDB (NoSQL)

MongoDB é um banco de dados NoSQL orientado a documentos que armazena dados em formato semelhante a JSON.

**Instalação:**
```bash
pip install pymongo
```

**Exemplo Completo:**
```python
from pymongo import MongoClient
from pprint import pprint
import datetime

def conectar_mongodb():
    try:
        # Conectar ao servidor MongoDB
        cliente = MongoClient('mongodb://localhost:27017/')
        
        # Acessar banco de dados (será criado se não existir)
        db = cliente['empresa']
        print("Conexão com MongoDB estabelecida com sucesso")
        
        return cliente, db
        
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None, None

def operacoes_crud_basicas(db):
    # Referência à coleção (equivalente a uma tabela em RDBMS)
    colecao = db['funcionarios']
    
    # Criação (INSERT)
    funcionario = {
        'nome': 'Ricardo Souza',
        'email': 'ricardo@exemplo.com',
        'departamento': 'TI',
        'habilidades': ['Python', 'MongoDB', 'Docker'],
        'endereco': {
            'rua': 'Av. Principal',
            'cidade': 'São Paulo',
            'estado': 'SP'
        },
        'data_contratacao': datetime.datetime.now()
    }
    
    id_inserido = colecao.insert_one(funcionario).inserted_id
    print(f"Documento inserido com ID: {id_inserido}")
    
    # Leitura (FIND/SELECT)
    print("\nBuscar um funcionário:")
    pprint(colecao.find_one({'nome': 'Ricardo Souza'}))
    
    # Inserir vários documentos
    varios_funcionarios = [
        {
            'nome': 'Carla Gomes',
            'email': 'carla@exemplo.com',
            'departamento': 'Marketing',
            'habilidades': ['SEO', 'Redes Sociais']
        },
        {
            'nome': 'Paulo Menezes',
            'email': 'paulo@exemplo.com',
            'departamento': 'Finanças',
            'habilidades': ['Excel', 'SQL']
        }
    ]
    
    resultado = colecao.insert_many(varios_funcionarios)
    print(f"IDs inseridos: {resultado.inserted_ids}")
    
    # Atualização (UPDATE)
    resultado = colecao.update_one(
        {'nome': 'Ricardo Souza'},
        {'$set': {'habilidades': ['Python', 'MongoDB', 'Docker', 'AWS']}}
    )
    print(f"\nDocumentos atualizados: {resultado.modified_count}")
    
    # Exclusão (DELETE)
    resultado = colecao.delete_one({'nome': 'Paulo Menezes'})
    print(f"\nDocumentos excluídos: {resultado.deleted_count}")
    
    # Consulta com filtros
    print("\nFuncionários do departamento de TI:")
    for funcionario in colecao.find({'departamento': 'TI'}):
        pprint(funcionario)

# Exemplo de uso
cliente, db = conectar_mongodb()

if cliente and db:
    operacoes_crud_basicas(db)
    
    # Fechar conexão
    cliente.close()
    print("\nConexão MongoDB fechada")
```

## Bibliotecas de Análise de Dados / Data Analysis Libraries

### Pandas

Pandas é uma biblioteca poderosa para análise e manipulação de dados.

**Instalação:**
```bash
pip install pandas
```

**Exemplo de Uso:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Criar um DataFrame de exemplo
df = pd.DataFrame({
    'ID': range(1, 6),
    'Nome': ['Ana', 'Bruno', 'Carolina', 'Diego', 'Elena'],
    'Departamento': ['TI', 'Marketing', 'TI', 'Finanças', 'RH'],
    'Salario': [5000, 4500, 6000, 5200, 4800]
})

print("DataFrame original:")
print(df)

# Operações básicas com DataFrame
print("\nInformações do DataFrame:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

# Filtragem de dados
print("\nFuncionários do departamento de TI:")
ti_df = df[df['Departamento'] == 'TI']
print(ti_df)

# Agrupamento e agregação
print("\nMédia salarial por departamento:")
salario_medio = df.groupby('Departamento')['Salario'].mean().reset_index()
print(salario_medio)

# Salvando para CSV
df.to_csv('funcionarios.csv', index=False)
print("\nDados salvos em CSV")

# Lendo de CSV
df_lido = pd.read_csv('funcionarios.csv')
print("\nDados lidos do CSV:")
print(df_lido)

# Trabalhando com banco de dados
# Criar conexão usando SQLAlchemy
engine = create_engine('sqlite:///empresa.db')

# Salvar DataFrame no banco
df.to_sql('funcionarios', engine, if_exists='replace', index=False)
print("\nDados salvos no banco SQLite")

# Ler dados do banco usando consulta SQL
query = "SELECT * FROM funcionarios WHERE Salario > 5000"
df_sql = pd.read_sql(query, engine)
print("\nDados recuperados do banco usando SQL:")
print(df_sql)
```

### NumPy

NumPy é uma biblioteca fundamental para computação científica em Python.

**Instalação:**
```bash
pip install numpy
```

**Exemplo de Uso:**
```python
import numpy as np
import time

# Criação de arrays
print("Arrays NumPy básicos:")
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array 1D: {array_1d}")
print(f"Array 2D:\n{array_2d}")

# Funções de criação de arrays
print("\nCriação de arrays específicos:")
print(f"Zeros: {np.zeros(5)}")
print(f"Matriz identidade 3x3:\n{np.eye(3)}")
print(f"Range linear: {np.linspace(0, 10, 5)}")
print(f"Range com passo: {np.arange(0, 10, 2)}")
print(f"Valores aleatórios: {np.random.random(5)}")

# Operações matemáticas
print("\nOperações matemáticas:")
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"Soma dos elementos: {np.sum(a)}")
print(f"Média dos elementos: {np.mean(a)}")
print(f"Desvio padrão: {np.std(a)}")

# Exemplo: comparando velocidade entre listas Python e arrays NumPy
tamanho = 1000000
print("\nComparação de desempenho - Python vs NumPy:")

# Lista Python
inicio = time.time()
lista_python = list(range(tamanho))
resultado_python = [x ** 2 for x in lista_python]
tempo_python = time.time() - inicio
print(f"Tempo com lista Python: {tempo_python:.6f} segundos")

# Array NumPy
inicio = time.time()
array_numpy = np.arange(tamanho)
resultado_numpy = array_numpy ** 2
tempo_numpy = time.time() - inicio
print(f"Tempo com array NumPy: {tempo_numpy:.6f} segundos")
print(f"NumPy é {tempo_python/tempo_numpy:.1f}x mais rápido")

# Reshape e manipulação dimensional
print("\nReshape e manipulação de arrays:")
arr = np.arange(12)
print(f"Array original: {arr}")
reshaped = arr.reshape(3, 4)
print(f"Após reshape para 3x4:\n{reshaped}")
print(f"Transposta:\n{reshaped.T}")
```

### Matplotlib e Seaborn

Matplotlib e Seaborn são bibliotecas para visualização de dados em Python.

**Instalação:**
```bash
pip install matplotlib seaborn
```

**Exemplo de Uso:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para melhor visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 12
sns.set_palette("deep")

# Criar dados para visualização
np.random.seed(42)
df = pd.DataFrame({
    'departamento': np.random.choice(['TI', 'Marketing', 'Finanças', 'RH', 'Operações'], 100),
    'salario': np.random.normal(5000, 1000, 100),
    'tempo_empresa': np.random.randint(1, 10, 100),
    'desempenho': np.random.normal(7.5, 1.5, 100),
    'horas_extras': np.random.randint(0, 30, 100)
})

# 1. Gráfico de barras com Matplotlib
plt.figure()
contagem_dept = df['departamento'].value_counts()
contagem_dept.plot(kind='bar', color='skyblue')
plt.title('Número de Funcionários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Número de Funcionários')
plt.tight_layout()
plt.savefig('funcionarios_por_departamento.png')

# 2. Histograma com Matplotlib
plt.figure()
plt.hist(df['salario'], bins=10, color='green', alpha=0.7)
plt.title('Distribuição de Salários')
plt.xlabel('Salário (R$)')
plt.ylabel('Frequência')
plt.tight_layout()
plt.savefig('distribuicao_salarios.png')

# 3. Gráfico de dispersão com Seaborn
plt.figure()
sns.scatterplot(data=df, x='tempo_empresa', y='salario', hue='departamento', size='desempenho', sizes=(50, 200))
plt.title('Relação entre Tempo de Empresa e Salário')
plt.xlabel('Anos na Empresa')
plt.ylabel('Salário (R$)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('tempo_vs_salario.png')

# 4. Boxplot com Seaborn
plt.figure()
sns.boxplot(data=df, x='departamento', y='salario')
plt.title('Distribuição de Salários por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Salário (R$)')
plt.tight_layout()
plt.savefig('boxplot_salarios.png')

# 5. Heatmap de correlação com Seaborn
plt.figure()
correlacao = df.corr(numeric_only=True)
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação entre Variáveis')
plt.tight_layout()
plt.savefig('matriz_correlacao.png')

# 6. Gráfico de linha com Matplotlib
# Simulando dados de desempenho ao longo do tempo
anos = range(2018, 2025)
desempenho_ti = [75, 78, 83, 81, 85, 89, 92]
desempenho_mkt = [62, 70, 75, 79, 78, 82, 84]

plt.figure()
plt.plot(anos, desempenho_ti, marker='o', linestyle='-', label='TI')
plt.plot(anos, desempenho_mkt, marker='s', linestyle='--', label='Marketing')
plt.title('Desempenho Departamental ao Longo do Tempo')
plt.xlabel('Ano')
plt.ylabel('Índice de Desempenho')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('desempenho_temporal.png')

print("Todos os gráficos foram gerados e salvos como arquivos PNG")
```

## Outras Bibliotecas Úteis / Other Useful Libraries

### Requests e JSON

Requests é utilizada para fazer requisições HTTP em Python e JSON para manipular dados nesse formato.

**Instalação:**
```bash
pip install requests
```

**Exemplo de Uso:**
```python
import requests
import json
from pprint import pprint

def consumir_api_rest():
    # API pública para testes
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Fazer requisição GET
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("Requisição bem-sucedida!")
        
        # Converter resposta para JSON
        dados = response.json()
        
        # Imprimir primeiro usuário formatado
        print("\nPrimeiro usuário:")
        pprint(dados[0])
        
        # Salvar dados em arquivo JSON
        with open('usuarios.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("\nDados salvos em 'usuarios.json'")
        
        # Mostrar exemplo de processamento de dados
        print("\nEmails dos usuários:")
        for usuario in dados:
            print(f"- {usuario['name']}: {usuario['email']}")
            
        return dados
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def postar_dados(dados_usuario):
    url = "https://jsonplaceholder.typicode.com/users"
    
    # Dados para enviar no POST
    novo_usuario = {
        "name": "Ana Carolina Silva",
        "username": "anacarol",
        "email": "ana@exemplo.com",
        "address": {
            "street": "Av. Principal",
            "suite": "Apt. 101",
            "city": "São Paulo",
            "zipcode": "01000-000"
        },
        "phone": "11 98765-4321"
    }
    
    # Fazer requisição POST
    response = requests.post(url, json=novo_usuario)
    
    if response.status_code in [200, 201]:
        print("\nPost bem-sucedido!")
        print("Dados do novo usuário:")
        pprint(response.json())
        return response.json()
    else:
        print(f"Erro ao postar dados: {response.status_code}")
        return None

def manipular_json_local():
    # Criar dicionário Python
    empresa = {
        "nome": "Tech Solutions",
        "fundacao": 2010,
        "areas": ["Desenvolvimento", "Consultoria", "Infraestrutura"],
        "funcionarios": [
            {"id": 1, "nome": "Carlos", "cargo": "CTO"},
            {"id": 2, "nome": "Fernanda", "cargo": "Desenvolvedora Senior"},
            {"id": 3, "nome": "Rafael", "cargo": "Analista de Dados"}
        ],
        "localizacoes": {
            "matriz": "São Paulo",
            "filiais": ["Rio de Janeiro", "Porto Alegre"]
        }
    }
    
    # Salvar como JSON
    with open('empresa.json', 'w', encoding='utf-8') as arquivo:
        json.dump(empresa, arquivo, indent=4, ensure_ascii=False)
    print("\nDados da empresa salvos em 'empresa.json'")
    
    # Ler de JSON
    with open('empresa.json', 'r', encoding='utf-8') as arquivo:
        empresa_lida = json.load(arquivo)
    
    # Modificar dados
    empresa_lida["funcionarios"].append({"id": 4, "nome": "Juliana", "cargo": "UX Designer"})
    empresa_lida["localizacoes"]["filiais"].append("Recife")
    
    # Salvar modificações
    with open('empresa_atualizada.json', 'w', encoding='utf-8') as arquivo:
        json.dump(empresa_lida, arquivo, indent=4, ensure_ascii=False)
    print("Dados atualizados salvos em 'empresa_atualizada.json'")

# Executar exemplos
print("=== Exemplo de Requests e JSON ===")
dados = consumir_api_rest()
if dados:
    postar_dados(dados)
    manipular_json_local()
```

### SQLAlchemy e SQLite3

SQLAlchemy é um ORM (Object Relational Mapper) para Python, e SQLite3 é uma biblioteca para banco de dados em arquivo.

**Instalação:**
```bash
pip install sqlalchemy
```

**Exemplo de Uso:**
```python
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

# Exemplo 1: SQLite3 puro
def exemplo_sqlite3():
    print("=== Exemplo SQLite3 Puro ===")
    
    # Conectar ao banco de dados (cria se não existir)
    conn = sqlite3.connect('empresa_sqlite3.db')
    cursor = conn.cursor()
    
    # Criar tabela
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cargo TEXT,
        salario REAL,
        data_contratacao TEXT
    )
    ''')
    
    # Inserir dados
    funcionarios = [
        (1, 'Ana Silva', 'Desenvolvedora', 6000.00, '2019-05-10'),
        (2, 'Pedro Santos', 'Analista', 5500.00, '2020-02-15'),
        (3, 'Carla Gomes', 'Gerente', 8000.00, '2018-11-20')
    ]
    
    cursor.executemany('''
    INSERT OR REPLACE INTO funcionarios 
    VALUES (?, ?, ?, ?, ?)
    ''', funcionarios)
    
    conn.commit()
    print("Dados inseridos com sucesso")
    
    # Consultar dados
    cursor.execute('SELECT * FROM funcionarios')
    resultados = cursor.fetchall()
    
    print("\nFuncionários cadastrados:")
    for funcionario in resultados:
        print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: R${funcionario[3]:.2f}")
    
    # Consulta com filtro
    cursor.execute('SELECT nome, salario FROM funcionarios WHERE salario > ?', (6000,))
    print("\nFuncionários com salário acima de R$6000:")
    for nome, salario in cursor.fetchall():
        print(f"Nome: {nome}, Salário: R${salario:.2f}")
    
    # Fechar conexão
    conn.close()
    print("\nConexão SQLite3 fechada")

# Exemplo 2: SQLAlchemy (ORM)
def exemplo_sqlalchemy():
    print("\n=== Exemplo SQLAlchemy ORM ===")
    
    # Configurar base declarativa
    Base = declarative_base()
    
    # Definir modelo de dados (classe)
    class Departamento(Base):
        __tablename__ = 'departamentos'
        
        id = Column(Integer, primary_key=True)
        nome = Column(String(50), nullable=False)
        
        # Relacionamento com a tabela funcionários
        funcionarios = relationship("Funcionario", back_populates="departamento")
        
        def __repr__(self):
            return f"Departamento(id={self.id}, nome='{self.nome}')"
    
    class Funcionario(Base):
        __tablename__ = 'funcionarios'
        
        id = Column(Integer, primary_key=True)
        nome = Column(String(100), nullable=False)
        cargo = Column(String(50))
        salario = Column(Float)
        data_contratacao = Column(DateTime, default=datetime.datetime.now)
        departamento_id = Column(Integer, ForeignKey('departamentos.id'))
        
        # Relacionamento com a tabela departamentos
        departamento = relationship("Departamento", back_populates="funcionarios")
        
        def __repr__(self):
            return f"Funcionario(id={self.id}, nome='{self.nome}', cargo='{self.cargo}')"
    
    # Criar engine e tabelas
    engine = create_engine('sqlite:///empresa_sqlalchemy.db')
    Base.metadata.create_all(engine)
    
    # Criar sessão
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Inserir dados (transacional)
    try:
        # Verificar se já existem departamentos
        dept_ti = session.query(Departamento).filter_by(nome="TI").first()
        if not dept_ti:
            dept_ti = Departamento(nome="TI")
            session.add(dept_ti)
        
        dept_rh = session.query(Departamento).filter_by(nome="RH").first()
        if not dept_rh:
            dept_rh = Departamento(nome="RH")
            session.add(dept_rh)
        
        # Adicionar funcionários
        novos_funcionarios = [
            Funcionario(nome
