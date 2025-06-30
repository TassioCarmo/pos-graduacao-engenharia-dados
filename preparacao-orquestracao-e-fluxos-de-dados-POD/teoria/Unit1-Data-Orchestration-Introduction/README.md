
# Orquestração de Dados: Preparação, Fluxo e Automação
# Data Orchestration: Preparation, Flow and Automation

## Sumário
- [Introdução](#introdução)
  - [Importância da Preparação, Orquestração e Fluxo de Dados](#importância-da-preparação-orquestração-e-fluxo-de-dados)
  - [Jornada dos Dados](#jornada-dos-dados)
- [Preparação de Dados](#preparação-de-dados)
  - [Conceito, Objetivos e Benefícios](#conceito-objetivos-e-benefícios)
  - [Etapas da Preparação de Dados](#etapas-da-preparação-de-dados)
    - [Definição dos Objetivos](#definição-dos-objetivos)
    - [Coleta dos Dados](#coleta-dos-dados)
    - [Limpeza dos Dados](#limpeza-dos-dados)
    - [Transformação de Dados](#transformação-de-dados)
    - [Integração de Dados](#integração-de-dados)
  - [Exemplos Práticos](#exemplos-práticos)
- [Fluxo de Dados](#fluxo-de-dados)
  - [Conceitos e Tipos de Fluxos](#conceitos-e-tipos-de-fluxos)
  - [Arquiteturas de Fluxo de Dados](#arquiteturas-de-fluxo-de-dados)
  - [Ferramentas e Soluções](#ferramentas-e-soluções-para-fluxo-de-dados)
- [Orquestração de Fluxos de Dados](#orquestração-de-fluxos-de-dados)
  - [Conceito, Objetivos e Benefícios](#conceito-objetivos-e-benefícios-da-orquestração)
  - [Modelos de Orquestração](#modelos-de-orquestração)
  - [Ferramentas e Soluções](#ferramentas-e-soluções-para-orquestração)

## Introdução
### Importância da Preparação, Orquestração e Fluxo de Dados

No mundo digital contemporâneo, enfrentamos uma explosão de dados sem precedentes. A quantidade de informações geradas cresce exponencialmente em todas as áreas, desde negócios até pesquisas científicas. Essa abundância de dados traz consigo oportunidades extraordinárias, mas também desafios significativos.

A preparação, orquestração e o fluxo de dados são processos cruciais que transformam dados brutos em informações valiosas e acionáveis. Através desses processos, as organizações podem:

#### Melhorar a Qualidade dos Dados
- Limpar, corrigir e padronizar dados para garantir confiabilidade e precisão
- Eliminar inconsistências e duplicações que podem comprometer análises
- Estabelecer padrões de qualidade que garantem decisões baseadas em informações confiáveis

#### Integrar Dados de Diferentes Fontes
- Combinar dados de diferentes sistemas, departamentos e organizações
- Obter uma visão holística que revela padrões e correlações antes invisíveis
- Unificar silos de informação, criando uma "fonte única da verdade"

#### Transformar Dados em Informações
- Aplicar técnicas analíticas para identificar padrões, tendências e insights valiosos
- Extrair conhecimento acionável de conjuntos de dados complexos
- Converter dados brutos em narrativas compreensíveis para stakeholders

#### Automatizar o Processamento de Dados
- Criar fluxos de trabalho eficientes para agilizar a entrega de insights
- Reduzir intervenção manual, minimizando erros humanos
- Estabelecer processos replicáveis e escaláveis

#### Garantir Segurança e Governança
- Implementar medidas para proteger dados contra acesso não autorizado
- Assegurar conformidade com regulamentações (LGPD, GDPR, etc.)
- Manter controle sobre o ciclo de vida dos dados

Dominar esses processos permite que profissionais e organizações:

- **Tomem decisões mais inteligentes** baseadas em dados confiáveis e insights precisos
- **Resolvam problemas complexos** através da análise e exploração de dados
- **Otimizem processos e operações** identificando ineficiências e oportunidades de melhoria
- **Criem novos produtos e serviços** alinhados às necessidades dos clientes

A preparação, orquestração e o fluxo de dados são habilidades essenciais para diversos profissionais, incluindo cientistas de dados, analistas, engenheiros de software e gestores de dados. Esses processos guiam a jornada completa dos dados, desde a coleta inicial até a entrega de informações que embasam decisões estratégicas.

### Jornada dos Dados

A jornada dos dados pode ser compreendida como um ciclo contínuo de cinco etapas interconectadas:

#### 1. COLETA

**Objetivo:**
Obter dados relevantes de diversas fontes para responder ao problema em questão.

**Fontes para coleta de dados:**
- **Fontes internas:** Transações financeiras, registros de clientes, dados de produção, logs de sistemas
- **Fontes externas:** Mídias sociais, websites, APIs públicas, sensores, pesquisas de mercado

**Ferramentas para coleta de dados:**
- **Web scraping:** Scrapy, BeautifulSoup, Selenium
- **Integração de APIs:** Python requests, Google Cloud Platform API Client Library
- **Sensores:** Arduino, Raspberry Pi
- **Pesquisas:** SurveyMonkey, Google Forms

**Exemplo prático:**
Uma empresa de e-commerce coleta dados de vendas de seu sistema ERP, dados de comportamento do usuário de seu site via Google Analytics, e informações de concorrentes através de web scraping de sites de comparação de preços.

#### 2. ARMAZENAMENTO

**Objetivo:**
Armazenar os dados coletados de forma segura, escalável e acessível.

**Soluções de armazenamento:**
- **Bancos de dados relacionais:** MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database
- **Armazenamento de objetos (Data lake):** Hadoop, Amazon S3, Azure Datalake Storage Gen 2, Google Cloud Storage
- **Data warehouses:** Snowflake, Amazon Redshift, Google BigQuery, Azure Synapse Analytics, Databricks

**Considerações importantes:**
- Escolher a solução de armazenamento adequada conforme volume, variedade e velocidade dos dados
- Implementar políticas de backup e recuperação
- Definir estratégias de particionamento e indexação para otimizar o acesso

#### 3. PREPARAÇÃO

**Objetivo:**
Limpar, transformar e integrar os dados para análise.

**Tarefas:**
- **Limpeza:** Corrigir erros, remover valores inconsistentes e duplicados
- **Transformação:** Padronizar formatos, aplicar funções matemáticas e criar novas features
- **Integração:** Combinar dados de diferentes fontes em um único conjunto

**Ferramentas:**
- **Open-source:** Apache Hop, Apache NiFi, Pandas, Apache Spark, Pentaho PDI
- **Comerciais:** Alteryx, SQL Server Integration Services, Informatica

#### 4. ANÁLISE

**Objetivo:**
Explorar os dados, identificar padrões e gerar insights acionáveis.

**Técnicas:**
- **Análise estatística:** Média, mediana, desvio padrão, correlação, regressão linear
- **Visualização de dados:** Gráficos de linha, histogramas, gráficos de pizza, mapas de calor
- **Machine Learning:** Modelos de classificação, regressão, clusterização, detecção de anomalias

**Ferramentas:**
- **Open-source:** Jupyter Notebook, RStudio, Apache Metabase, Kibana
- **Comerciais:** Microsoft Excel, Power BI, Qlik Sense, Tableau, Google Looker

#### 5. AÇÃO

**Objetivo:**
Comunicar os resultados da análise e tomar decisões baseadas em dados.

**Tarefas:**
- **Comunicação:** Criar relatórios, dashboards, apresentações para stakeholders, notificações (e-mail, celular, etc.)
- **Tomada de decisão:** Utilizar insights para decisões estratégicas e operacionais

**Ferramentas:**
- **BI:** Microsoft Power BI, Qlik Sense, Tableau, Google Looker
- **Comunicação:** Microsoft PowerPoint, Google Slides, Chatbots

**Exemplo prático:**
Uma empresa de varejo utiliza dashboards em Power BI para monitorar vendas diárias e envia alertas automáticos via email quando determinados produtos atingem níveis críticos de estoque, permitindo reposições rápidas.

É importante ressaltar que a jornada dos dados é um ciclo iterativo, onde cada etapa pode ser revisitada e aprimorada continuamente. A escolha das ferramentas e tecnologias mais adequadas depende das necessidades específicas do projeto e da organização, sendo fundamental contar com uma equipe multidisciplinar com habilidades em cada uma das etapas.

## Preparação de Dados
### Conceito, Objetivos e Benefícios

A preparação de dados é o processo fundamental de transformação de dados brutos em um formato adequado para análise. Esta etapa crítica engloba tarefas como limpeza, transformação e integração de dados, estabelecendo as bases para análises confiáveis e insights valiosos.

#### Principais Objetivos

1. **Melhorar a Qualidade dos Dados**
   - Eliminar erros, inconsistências e duplicações
   - Padronizar formatos e unidades de medida
   - Tratar valores ausentes ou extremos

2. **Facilitar a Análise e Exploração**
   - Estruturar dados de forma lógica e intuitiva
   - Criar features relevantes para modelos analíticos
   - Otimizar o desempenho de consultas e algoritmos

3. **Aumentar a Confiabilidade dos Resultados**
   - Garantir que as análises se baseiem em dados precisos
   - Reduzir vieses e distorções nos dados
   - Criar documentação e metadados para rastreabilidade

4. **Reduzir Tempo e Custo da Análise**
   - Automatizar processos repetitivos de preparação
   - Minimizar retrabalho e correções posteriores
   - Acelerar ciclos de desenvolvimento analítico

#### Benefícios Tangíveis

1. **Melhores Insights e Decisões**
   - Análises baseadas em dados de alta qualidade produzem conclusões mais confiáveis
   - Redução de falsos positivos e falsos negativos em modelos preditivos
   - Maior confiança dos stakeholders nos resultados apresentados

2. **Maior Eficiência e Produtividade**
   - Cientistas de dados passam menos tempo limpando dados e mais tempo gerando insights
   - Ciclos de desenvolvimento analítico mais rápidos
   - Reutilização de pipelines de preparação para múltiplos projetos

3. **Redução de Custos e Riscos**
   - Menos recursos computacionais desperdiçados com dados irrelevantes
   - Diminuição de decisões erradas baseadas em dados imprecisos
   - Menor exposição a violações regulatórias

4. **Maior Confiabilidade e Governança**
   - Rastreabilidade completa da origem à transformação dos dados
   - Conformidade com regulamentações de proteção de dados
   - Consistência nas definições e métricas em toda a organização

**Estatísticas relevantes:**
Segundo pesquisas do setor, cientistas de dados tipicamente gastam entre 60% e 80% de seu tempo preparando dados, destacando a importância crítica desta etapa no processo analítico.

### Etapas da Preparação de Dados

#### Definição dos Objetivos

A definição clara dos objetivos é o primeiro e crucial passo no processo de preparação de dados. Esta etapa estabelece o direcionamento para todo o trabalho subsequente.

**Atividades principais:**
- **Compreender a pergunta do negócio:** Identificar precisamente o que se deseja descobrir ou resolver com a análise
- **Definir as variáveis relevantes:** Determinar quais dados são necessários para responder à pergunta de negócio
- **Determinar o formato desejado:** Especificar como os dados devem ser estruturados para facilitar a análise

**Exemplo prático:**
Uma empresa de telecomunicações quer reduzir a taxa de churn (cancelamento) de clientes. O objetivo da análise é identificar fatores que predizem quando um cliente está propenso a cancelar o serviço. As variáveis relevantes incluirão histórico de pagamentos, padrões de uso, registros de reclamações e dados demográficos. O formato desejado será uma tabela onde cada linha representa um cliente e cada coluna um atributo relevante.

#### Coleta dos Dados

A coleta eficiente de dados envolve a identificação, extração e armazenamento de informações de diversas fontes.

**Atividades principais:**
- **Identificar fontes de dados:** Mapear todos os sistemas, bancos de dados e APIs onde os dados relevantes estão disponíveis
- **Coletar os dados:** Extrair dados utilizando métodos apropriados como consultas SQL, APIs, web scraping ou outras técnicas
- **Armazenar os dados:** Salvar os dados coletados em um local seguro, acessível e escalável

**Ferramentas comuns:**
- **Consultas de banco de dados:** SQL para extrair dados de bancos relacionais
- **API clients:** Bibliotecas como Python requests para acessar APIs REST
- **Web scraping:** Ferramentas como Beautiful Soup ou Scrapy para extrair dados de websites
- **ETL tools:** Plataformas como Apache NiFi ou Talend para extrações complexas

**Exemplo de código para coleta via API:**
```python
import requests
import pandas as pd
import json

# Configurar autenticação
api_key = "sua_chave_api"
headers = {"Authorization": f"Bearer {api_key}"}

# Fazer requisição à API
response = requests.get("https://api.exemplo.com/dados", headers=headers)

# Verificar sucesso e converter para DataFrame
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data["results"])
    # Salvar dados em CSV
    df.to_csv("dados_coletados.csv", index=False)
else:
    print(f"Erro na coleta: {response.status_code}")
```

#### Limpeza dos Dados

A limpeza de dados é o processo de identificar e corrigir problemas nos dados brutos, garantindo sua qualidade e confiabilidade.

**Atividades principais:**
- **Identificar e remover outliers:** Detectar valores extremos que podem distorcer análises
- **Tratar valores ausentes (missing):** Decidir entre remover, imputar ou flagar dados faltantes
- **Padronizar strings:** Corrigir erros de ortografia, remover caracteres especiais, normalizar caixa

**Técnicas comuns para tratamento de valores ausentes:**
1. **Remoção:** Eliminar registros ou colunas com muitos valores ausentes
2. **Imputação estatística:** Substituir por média, mediana ou moda
3. **Imputação por modelo:** Usar algoritmos como KNN ou regressão para estimar valores
4. **Flags de ausência:** Criar colunas indicadoras para sinalizar onde havia valores ausentes

**Exemplo de código para limpeza em Python:**
```python
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Carregar dados
df = pd.read_csv("dados_brutos.csv")

# Remover duplicatas
df = df.drop_duplicates()

# Tratamento de outliers usando IQR (Intervalo Interquartil)
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Aplicar em uma coluna numérica
df = remove_outliers(df, 'valor_compra')

# Padronizar strings em coluna categórica
df['categoria'] = df['categoria'].str.lower().str.strip()

# Imputação de valores ausentes usando KNN
numeric_columns = ['idade', 'renda', 'gasto_mensal']
imputer = KNNImputer(n_neighbors=5)
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])

# Salvar dados limpos
df.to_csv("dados_limpos.csv", index=False)
```

#### Transformação de Dados

A transformação de dados envolve modificar a estrutura, formato ou valores dos dados para torná-los mais adequados para análise.

**Atividades principais:**
- **Normalizar/escalonar:** Ajustar dados para uma escala comum
- **Codificar variáveis categóricas:** Converter categorias em representações numéricas
- **Criar novas features:** Derivar atributos a partir de dados existentes

**Técnicas comuns:**
1. **Normalização Min-Max:** Escalona valores para o intervalo [0,1]
2. **Padronização Z-score:** Transforma dados para média 0 e desvio padrão 1
3. **One-Hot Encoding:** Cria colunas binárias para cada categoria
4. **Feature engineering:** Cria atributos derivados como razões, diferenças ou agregações

**Exemplo de código para transformação em Python:**
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Carregar dados limpos
df = pd.read_csv("dados_limpos.csv")

# Separar colunas numéricas e categóricas
numeric_features = ['idade', 'renda', 'gasto_mensal']
categorical_features = ['categoria', 'estado', 'segmento']

# Criar pipeline de transformação
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse=False), categorical_features)
    ])

# Aplicar transformações
transformed_data = preprocessor.fit_transform(df)

# Criar feature de recência (dias desde última compra)
from datetime import datetime
df['ultima_compra'] = pd.to_datetime(df['ultima_compra'])
hoje = datetime.now()
df['dias_desde_ultima_compra'] = (hoje - df['ultima_compra']).dt.days

# Criar razão entre variáveis
df['proporcao_gasto_renda'] = df['gasto_mensal'] / df['renda']
```

#### Integração de Dados

A integração de dados envolve combinar dados de diferentes fontes em um conjunto único e coerente.

**Atividades principais:**
- **Identificar chaves de junção:** Determinar atributos comuns que podem conectar diferentes conjuntos de dados
- **Realizar junções (joins):** Combinar tabelas usando operações como inner join, left join, etc.
- **Resolver conflitos:** Tratar diferenças de valores, formatos ou definições entre fontes

**Técnicas comuns:**
1. **SQL joins:** Para dados em bancos relacionais
2. **Pandas merge/join:** Para dados em DataFrames
3. **Fuzzy matching:** Para junções aproximadas quando as chaves não são exatamente iguais

**Exemplo de código para integração em Python:**
```python
import pandas as pd

# Carregar diferentes conjuntos de dados
clientes = pd.read_csv("clientes.csv")
transacoes = pd.read_csv("transacoes.csv")
produtos = pd.read_csv("produtos.csv")

# Inner join entre transações e produtos
trans_prod = pd.merge(
    transacoes,
    produtos,
    on='id_produto',
    how='inner'
)

# Left join com dados de clientes
dados_completos = pd.merge(
    trans_prod,
    clientes,
    on='id_cliente',
    how='left'
)

# Agregação de dados transacionais por cliente
resumo_cliente = transacoes.groupby('id_cliente').agg({
    'valor': ['sum', 'mean', 'count'],
    'data': ['min', 'max']
}).reset_index()

# Renomear colunas resultantes
resumo_cliente.columns = ['id_cliente', 'valor_total', 'valor_medio', 
                          'num_transacoes', 'primeira_compra', 'ultima_compra']

# Junção final
dados_finais = pd.merge(
    clientes,
    resumo_cliente,
    on='id_cliente',
    how='left'
)

# Salvar conjunto de dados integrado
dados_finais.to_csv("dados_integrados.csv", index=False)
```

### Exemplos Práticos

#### Análise de Vendas

Um departamento de marketing deseja analisar padrões de venda para otimizar campanhas promocionais:

1. **Definição dos objetivos:**
   - Identificar produtos frequentemente comprados juntos
   - Entender sazonalidade de vendas por categoria
   - Determinar perfil de clientes para cada linha de produto

2. **Preparação de dados necessária:**
   - Limpeza de registros duplicados de vendas
   - Padronização de nomes de produtos e categorias
   - Transformação de timestamps em atributos como dia da semana, mês, estação do ano
   - Integração de dados transacionais com informações de clientes e produtos

3. **Resultados:**
   - Identificação de regras de associação para cross-selling
   - Criação de dashboards sazonais para planejamento de estoque
   - Desenvolvimento de segmentos de clientes para marketing direcionado

#### Análise de Risco de Crédito

Uma instituição financeira quer melhorar seus modelos de avaliação de risco de crédito:

1. **Definição dos objetivos:**
   - Prever probabilidade de inadimplência
   - Identificar fatores de risco mais relevantes
   - Segmentar clientes por perfil de risco

2. **Preparação de dados necessária:**
   - Integração de dados internos (histórico de pagamentos, contas) com bureaus de crédito
   - Tratamento de valores ausentes em histórico financeiro
   - Criação de features derivadas como:
     - Razão dívida/renda
     - Tempo médio de atraso em pagamentos
     - Volatilidade de saldo em conta

3. **Resultados:**
   - Modelo preditivo com melhor AUC (área sob a curva ROC)
   - Identificação de indicadores antecipados de inadimplência
   - Sistema de scoring mais preciso e transparente

#### Análise de Sentimentos em Mídias Sociais

Uma empresa de bens de consumo quer monitorar a recepção pública a um novo produto:

1. **Definição dos objetivos:**
   - Medir sentimento geral sobre o produto
   - Identificar aspectos específicos elogiados ou criticados
   - Comparar percepção do produto com concorrentes

2. **Preparação de dados necessária:**
   - Coleta de menções do produto em diferentes plataformas
   - Limpeza de texto (remoção de stop words, correção de typos)
   - Normalização de emojis e gírias
   - Enriquecimento com dados contextuais (horário, localização, demografia)

3. **Resultados:**
   - Dashboard em tempo real de sentimento por região
   - Relatório de principais pontos fortes e fracos percebidos
   - Recomendações para ajustes de marketing e desenvolvimento de produto

## Fluxo de Dados

### Conceitos e Tipos de Fluxos

O fluxo de dados refere-se ao trajeto completo percorrido pelos dados desde sua origem até seu uso final. É um processo contínuo que abrange múltiplas etapas, desde a coleta inicial até o consumo dos dados processados para tomada de decisões.

#### Etapas Principais do Fluxo de Dados

1. **Coleta**
   - Os dados são capturados de diversas fontes como sensores, sistemas de registro, formulários, APIs ou interações de usuários
   - Esta fase determina a qualidade inicial e os formatos dos dados que entrarão no pipeline

2. **Processamento**
   - Os dados brutos são transformados em formatos estruturados e padronizados
   - Inclui operações como parsing, formatação e validação inicial

3. **Tratamento**
   - Os dados são manipulados seguindo regras de negócio específicas
   - Inclui limpeza, enriquecimento, normalização e transformações avançadas

4. **Distribuição**
   - Os dados processados são encaminhados para os destinatários finais
   - Pode incluir carregamento em data warehouses, publicação em APIs, geração de relatórios ou alimentação de aplicações

#### Tipos de Fluxos de Dados

Existem dois tipos principais de fluxos de dados, cada um com características e casos de uso específicos:

##### Fluxo Batch (em Lote)

**Características:**
- Processamento periódico de grandes volumes de dados em janelas de tempo definidas
- Os dados são coletados, armazenados e processados em conjuntos discretos
- Geralmente operado em horários predeterminados (diário, semanal, mensal)

**Vantagens:**
- Eficiência para grandes volumes de dados
- Menor complexidade de implementação e manutenção
- Ideal para relatórios periódicos e análises históricas

**Desvantagens:**
- Latência significativa entre geração e disponibilização dos dados
- Não adequado para casos que exigem reações imediatas

**Exemplos de aplicação:**
- Relatórios financeiros mensais
- Cálculos de folha de pagamento
- Análises de vendas diárias
- Consolidação de dados para data warehouses

**Implementação típica:**
```python
# Exemplo simplificado de processamento batch com PySpark
from pyspark.sql import SparkSession

# Inicializar Spark
spark = SparkSession.builder \
    .appName("ProcessamentoBatchDiario") \
    .getOrCreate()

# Definir janela de processamento
data_processamento = "2023-04-10"

# Carregar dados do dia
vendas_diarias = spark.read.parquet(f"s3://dados/vendas/dt={data_processamento}")

# Processar dados
vendas_processadas = vendas_diarias \
    .groupBy("categoria", "loja") \
    .agg({"valor": "sum", "quantidade": "sum"})

# Salvar resultados
vendas_processadas.write \
    .mode("overwrite") \
    .parquet(f"s3://dados/vendas_sumarizadas/dt={data_processamento}")
```

##### Fluxo Streaming (Tempo Real)

**Características:**
- Processamento contínuo de dados à medida que são gerados
- Orientado a eventos, com reações imediatas a novos dados
- Operação 24/7 com latência mínima

**Vantagens:**
- Baixíssima latência entre geração e processamento dos dados
- Capacidade de reação rápida a eventos
- Detecção de padrões em tempo real

**Desvantagens:**
- Maior complexidade de implementação e manutenção
- Necessidade de infraestrutura robusta para alta disponibilidade
- Desafios no tratamento de picos de carga

**Exemplos de aplicação:**
- Detecção de fraudes em transações financeiras
- Monitoramento de equipamentos industriais
- Recomendações em tempo real em sites de e-commerce
- Análise de sentimentos em mídias sociais

**Implementação típica:**
```python
# Exemplo simplificado de processamento streaming com Kafka e PySpark Streaming
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, window
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType

# Definir schema dos dados
schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("timestamp", TimestampType()),
    StructField("amount", DoubleType()),
    StructField("customer_id", StringType()),
    StructField("merchant", StringType())
])

# Inicializar Spark com suporte a streaming
spark = SparkSession.builder \
    .appName("DeteccaoFraudeRealTime") \
    .getOrCreate()

# Conectar ao stream do Kafka
transacoes_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker1:9092,broker2:9092") \
    .option("subscribe", "transacoes") \
    .load()

# Processar dados do stream
parsed_transactions = transacoes_stream \
    .select(from_json(col("value").cast("string"), schema).alias("data")) \
    .select("data.*")

# Detectar padrões (exemplo: várias transações em curto período)
suspicious_patterns = parsed_transactions \
    .groupBy(
        window(col("timestamp"), "5 minutes"),
        col("customer_id")
    ) \
    .count() \
    .filter(col("count") > 5)

# Publicar alertas
query = suspicious_patterns \
    .writeStream \
    .outputMode("update") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker1:9092,broker2:9092") \
    .option("topic", "fraude_alertas") \
    .option("checkpointLocation", "/checkpoints/fraud_detection") \
    .start()

query.awaitTermination()
```

### Arquiteturas de Fluxo de Dados

As arquiteturas de fluxo de dados definem a estrutura e organização dos componentes em um sistema de processamento de dados. Três principais arquiteturas se destacam no cenário atual:

#### Arquitetura Pipeline

A arquitetura Pipeline é a abordagem tradicional e linear para processamento de dados.

**Características:**
- Fluxo sequencial onde cada etapa depende da conclusão da anterior
- Estrutura simples e intuitiva, seguindo um caminho direto da origem ao destino
- Geralmente orientada a lotes (batch)

**Vantagens:**
- Fácil de entender e implementar
- Rastreabilidade direta do fluxo de dados
- Baixa complexidade operacional

**Limitações:**
- Pouca flexibilidade para processar dados em tempo real
- Risco de gargalos em etapas individuais
- Desafios de escalonamento para volumes muito grandes

**Exemplo de implementação:**
Um pipeline ETL clássico usando Apache Airflow, onde cada tarefa é executada em sequência:

```python
# Exemplo de DAG de Pipeline no Apache Airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Funções para cada etapa do pipeline
def extrair_dados():
    print("Extraindo dados do banco de origem")
    # Lógica de extração...
    return {'dados_extraidos': 'caminho/para/dados_extraidos.csv'}

def transformar_dados(**context):
    dados_extraidos = context['ti'].xcom_pull(task_ids='extrair')
    print(f"Transformando dados de {dados_extraidos['dados_extraidos']}")
    # Lógica de transformação...
    return {'dados_transformados': 'caminho/para/dados_transformados.csv'}

def carregar_dados(**context):
    dados_transformados = context['ti'].xcom_pull(task_ids='transformar')
    print(f"Carregando dados de {dados_transformados['dados_transformados']} para o destino")
    # Lógica de carregamento...

# Definir DAG
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'pipeline_etl_simples',
    default_args=default_args,
    description='Pipeline ETL linear',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:

    # Definir tarefas
    extrair = PythonOperator(
        task_id='extrair',
        python_callable=extrair_dados
    )

    transformar = PythonOperator(
        task_id='transformar',
        python_callable=transformar_dados,
        provide_context=True
    )

    carregar = PythonOperator(
        task_id='carregar',
        python_callable=carregar_dados,
        provide_context=True
    )

    # Definir dependências (fluxo linear)
    extrair >> transformar >> carregar
```

#### Arquitetura Lambda

A arquitetura Lambda é projetada para lidar com dados em lote e em tempo real simultaneamente, oferecendo o melhor dos dois mundos.

**Características:**
- Combina processamento batch e streaming em uma única arquitetura
- Mantém uma camada de processamento em lote para análises completas e precisas
- Adiciona uma camada de processamento em tempo real para resultados imediatos
- Utiliza uma camada de serviço para combinar resultados de ambas as camadas

**Vantagens:**
- Alta disponibilidade e baixa latência para casos de uso críticos
- Resultados consistentes através da camada batch
- Capacidade de corrigir erros retroativamente na camada de lote

**Limitações:**
- Duplicação de código e lógica de negócios entre as camadas
- Complexidade operacional para manter ambas as camadas sincronizadas
- Custo mais elevado devido à infraestrutura duplicada

**Diagrama conceitual:**
```
         ┌───────────────┐
         │   Fonte de    │
         │    Dados      │
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │               │
┌────────┤  Ingestão de  ├─────────┐
│        │    Dados      │         │
│        └───────────────┘         │
│                                  │
▼                                  ▼
┌───────────────┐         ┌────────────────┐
│    Camada     │         │     Camada     │
│     Batch     │         │    Streaming   │
│               │         │                │
└───────┬───────┘         └────────┬───────┘
        │                          │
        │                          │
▼       │                          │       ▼
┌───────▼───────┐         ┌────────▼───────┐
│    Serving    │         │     Serving    │
│     Layer     │         │      Layer     │
│    (Batch)    │         │   (Real-time)  │
└───────┬───────┘         └────────┬───────┘
        │                          │
        └──────────┬───────────────┘
                   │
         ┌─────────▼───────────┐
         │                     │
         │   Aplicações e      │
         │   Visualizações     │
         │                     │
         └─────────────────────┘
```

**Exemplo de implementação:**
```python
# Componentes da arquitetura Lambda

# 1. Ingestão - usando Kafka como buffer de mensagens
from kafka import KafkaProducer
import json

def publicar_evento(evento):
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    # Publica na fila para processamento em tempo real
    producer.send('eventos_real_time', evento)
    # Publica na fila para armazenamento em batch
    producer.send('eventos_batch', evento)
    producer.flush()

# 2. Camada Batch - usando Spark para processamento diário
def processar_batch():
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder \
        .appName("ProcessamentoBatch") \
        .getOrCreate()
    
    # Carrega dados de um dia inteiro
    dados_dia = spark.read.parquet("s3://bucket/dados/batch/dt=2023-04-10")
    
    # Processamento analítico completo
    resultados = dados_dia.groupBy("categoria").agg({"valor": "sum"})
    
    # Salva no serving layer
    resultados.write.mode("overwrite").parquet("s3://bucket/serving/batch/dt=2023-04-10")

# 3. Camada Streaming - usando Spark Streaming para processamento em tempo real
def processar_streaming():
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import window
    
    spark = SparkSession.builder \
        .appName("ProcessamentoStreaming") \
        .getOrCreate()
    
    stream = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "eventos_real_time") \
        .load()
    
    # Processamento em tempo real (versão simplificada da lógica batch)
    processado = stream.selectExpr("CAST(value AS STRING)") \
        .groupBy(window("timestamp", "5 minutes")) \
        .count()
    
    # Salva no serving layer em tempo real
    query = processado.writeStream \
        .outputMode("update") \
        .format("memory") \
        .queryName("real_time_results") \
        .start()

# 4. Serving Layer - API para consulta aos resultados
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/metricas/<tipo>')
def obter_metricas(tipo):
    if tipo == 'real_time':
        # Busca dados da camada de tempo real
        return jsonify({"fonte": "real_time", "dados": [...]})
    else:
        # Busca dados da camada batch
        return jsonify({"fonte": "batch", "dados": [...]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### Arquitetura Kappa

A arquitetura Kappa é uma simplificação da arquitetura Lambda, focada em tratar todos os dados como streams.

**Características:**
- Utiliza apenas um único caminho de processamento (streaming)
- Armazena dados brutos em um log de eventos imutável e replicável
- Permite reprocessamento completo quando necessário, sem camada batch separada

**Vantagens:**
- Simplicidade operacional com apenas um pipeline para manter
- Economia de recursos computacionais
- Código unificado para processamento de dados
- Facilidade de manutenção e evolução

**Limitações:**
- Reprocessamento pode ser mais custoso para grandes volumes históricos
- Pode não ser adequada para análises muito complexas que exigem visão completa dos dados
- Maior dependência da infraestrutura de streaming

**Diagrama conceitual:**
```
         ┌───────────────┐
         │   Fonte de    │
         │    Dados      │
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │               │
         │  Sistema de   │
         │   Streaming   │
         │ (Kafka/Kinesis)│
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │               │
         │ Processamento │
         │ de Streaming  │
         │               │
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │               │
         │  Serving Layer│
         │               │
         └───────┬───────┘
                 │
         ┌───────▼───────┐
         │               │
         │  Aplicações/  │
         │ Visualizações │
         │               │
         └───────────────┘
```

**Exemplo de implementação:**
```python
# Arquitetura Kappa com Apache Kafka e Spark Structured Streaming

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StringType, TimestampType, DoubleType

# Definir schema dos eventos
schema = StructType().add("id", StringType()) \
                    .add("timestamp", TimestampType()) \
                    .add("valor", DoubleType()) \
                    .add("categoria", StringType())

# Inicializar Spark
spark = SparkSession.builder \
    .appName("KappaArchitecture") \
    .getOrCreate()

# Conectar ao stream do Kafka (log de eventos imutável)
stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "eventos_raw") \
    .option("startingOffsets", "earliest") \  # Permite reprocessamento
    .load()

# Processar dados
parsed = stream.select(from_json(col("value").cast("string"), schema).alias("data")) \
    .select("data.*")

# Análise por janelas de tempo
windowed = parsed.withWatermark("timestamp", "10 minutes") \
    .groupBy(window("timestamp", "1 hour"), "categoria") \
    .agg({"valor": "sum"}) \
    .withColumnRenamed("sum(valor)", "total_valor")

# Processamento em tempo real para serving layer
query1 = windowed.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "s3://bucket/serving/dados_processados") \
    .option("checkpointLocation", "s3://bucket/checkpoints/streaming") \
    .partitionBy("window") \
    .start()

# Saída para visualização em tempo real
query2 = windowed.writeStream \
    .outputMode("complete") \
    .format("memory") \
    .queryName("resultados_tempo_real") \
    .start()

# API para consulta de resultados
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/metricas/recentes')
def obter_metricas_recentes():
    # Consulta o último estado em memória
    resultados = spark.sql("SELECT * FROM resultados_tempo_real ORDER BY window DESC LIMIT 10")
    pdf = resultados.toPandas()
    return jsonify(pdf.to_dict(orient='records'))

@app.route('/metricas/historicas/<categoria>')
def obter_metricas_historicas(categoria):
    # Consulta dados históricos do serving layer
    historico = spark.read.parquet("s3://bucket/serving/dados_processados") \
        .filter(f"categoria = '{categoria}'") \
        .orderBy("window")
    pdf = historico.toPandas()
    return jsonify(pdf.to_dict(orient='records'))

# Iniciar servidor API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Manter aplicação rodando
query1.awaitTermination()
```

### Ferramentas e Soluções para Fluxo de Dados

#### Soluções Open-Source

**Apache Hop**
- Plataforma visual para design, desenvolvimento e execução de pipelines de dados
- Foco em metadados e reutilização de componentes
- Suporte a múltiplos ambientes de execução (local, nuvem, containerizado)

**Apache NiFi**
- Sistema de gerenciamento de fluxo de dados baseado em interface gráfica
- Projetado para automatizar o movimento de dados entre sistemas
- Recursos integrados para transformação, roteamento e monitoramento
- Escalabilidade horizontal e alta disponibilidade

**Exemplo de uso:**
NiFi é particularmente útil para integração de sistemas heterogêneos, como ingestão de dados de IoT ou integrações entre diferentes plataformas corporativas.

#### Soluções em Nuvem

**Azure Data Factory**
- Serviço de integração de dados na nuvem da Microsoft
- Criação, agendamento e orquestração de pipelines de dados
- Integração com diversos sistemas de armazenamento e processamento
- Recursos de monitoramento e auditoria integrados

**AWS Glue**
- Serviço ETL gerenciado da Amazon
- Descoberta e catalogação automática de dados
- Integração com o ecossistema de serviços AWS
- Suporte a transformações em Python e Scala

**Microsoft SQL Server Integration Services (SSIS)**
- Plataforma para construção de soluções de integração e transformação de dados
- Parte do ecossistema Microsoft SQL Server
- Rico em componentes pré-construídos para várias tarefas de ETL
- Integração com outras ferramentas Microsoft

**Comparação entre soluções:**

| Ferramenta | Tipo de Processamento | Facilidade de Uso | Escalabilidade | Integração com Ecossistemas | Modelo de Custo |
|------------|------------------------|-------------------|----------------|----------------------------|----------------|
| Apache Hop | Batch e Streaming | Média | Alta | Agnóstico | Open-source |
| Apache NiFi | Batch e Streaming | Alta (visual) | Alta | Agnóstico | Open-source |
| Azure Data Factory | Batch (principalmente) | Alta | Alta | Microsoft | Pagamento por uso |
| AWS Glue | Batch | Média | Alta | AWS | Pagamento por uso |
| SSIS | Batch | Média | Média | Microsoft | Licenciamento |

## Orquestração de Fluxos de Dados

### Conceito, Objetivos e Benefícios da Orquestração

A orquestração de dados refere-se ao processo de coordenação automatizada, gerenciamento e execução de fluxos de dados complexos, garantindo que as diversas tarefas e sistemas envolvidos trabalhem de forma harmoniosa e eficiente.

#### Conceito Expandido

A orquestração de dados pode ser comparada ao trabalho de um maestro em uma orquestra: coordenar diversos instrumentos (sistemas e processos) para criar uma sinfonia harmoniosa (fluxo de dados integrado e eficiente). Este processo envolve:

- **Coordenação de tarefas** entre diferentes sistemas e plataformas
- **Gerenciamento de dependências** entre etapas do pipeline de dados
- **Monitoramento em tempo real** do progresso e da saúde dos fluxos
- **Tratamento de erros e recuperação** de falhas automaticamente
- **Otimização de recursos** computacionais através de escalonamento dinâmico

#### Objetivos Principais

1. **Automatização de Processos**
   - Eliminar intervenções manuais em fluxos de dados recorrentes
   - Reduzir erros humanos e inconsistências
   - Liberar tempo dos profissionais para tarefas analíticas de maior valor

2. **Garantia de Qualidade e Confiabilidade**
   - Implementar verificações e validações em cada etapa do pipeline
   - Assegurar consistência e integridade dos dados processados
   - Estabelecer mecanismos de auditoria e rastreabilidade

3. **Escalabilidade e Flexibilidade**
   - Adaptar-se a volumes crescentes de dados sem redesenho completo
   - Suportar picos de processamento com alocação dinâmica de recursos
   - Permitir inclusão ou modificação de fontes e destinos de dados

4. **Governança e Segurança**
   - Controlar e documentar o acesso aos dados em cada estágio
   - Implementar políticas de segurança consistentes
   - Garantir conformidade com regulamentações (LGPD, GDPR, etc.)

#### Benefícios Tangíveis

1. **Agilidade na Tomada de Decisões**
   - Acesso mais rápido a dados atualizados e confiáveis
   - Redução do tempo entre a geração do dado e sua transformação em insight
   - Capacidade de reagir prontamente a eventos e anomalias

2. **Aceleração da Inovação**
   - Simplificação da experimentação com novos tipos de análises
   - Facilitação da implantação de modelos de machine learning
   - Criação mais rápida de novos produtos baseados em dados

3. **Controle e Visibilidade**
   - Monitoramento centralizado de todos os fluxos de dados
   - Observabilidade detalhada do desempenho e da saúde dos pipelines
   - Alertas proativos sobre problemas potenciais ou reais

4. **Otimização de Custos**
   - Uso mais eficiente de recursos computacionais
   - Redução de tempo ocioso em sistemas de processamento
   - Melhor planejamento de capacidade e infraestrutura

**Caso de Uso Ilustrativo:**

Uma empresa de e-commerce implementou orquestração de dados para integrar informações de vendas, estoque, logística e atendimento ao cliente. Antes da orquestração, relatórios gerenciais demoravam 48 horas para serem gerados manualmente. Com a orquestração automatizada:

- Relatórios são atualizados a cada 30 minutos
- Alertas automáticos são disparados quando produtos atingem níveis críticos de estoque
- Equipes de marketing recebem insights personalizados sobre comportamento de compra
- Processos de reposição são automaticamente iniciados com base em previsões de demanda

O resultado foi uma redução de 30% nos custos operacionais e um aumento de 15% nas vendas devido à melhor gestão de estoque e campanhas mais direcionadas.

### Modelos de Orquestração

Existem duas abordagens principais para a orquestração de fluxos de dados, cada uma com características, vantagens e desafios específicos:

#### Orquestração Centralizada

Na orquestração centralizada, uma plataforma ou sistema central controla e monitora todos os aspectos do fluxo de dados.

**Características:**
- Um único ponto de controle gerencia todo o pipeline
- Visão global de todo o fluxo de dados em um único lugar
- Configuração e gerenciamento centralizado de regras e políticas

**Vantagens:**
- **Maestro Unificado:** Simplificação do gerenciamento e administração através de um único ponto de controle
- **Visão Abrangente:** Facilidade de identificar gargalos e oportunidades de otimização com uma visão holística
- **Controle Granular:** Capacidade de definir políticas uniformes para todo o fluxo de dados
- **Implantação Simplificada:** Menor complexidade inicial de configuração e integração

**Exemplos de ferramentas:**
- Apache Airflow
- Azure Data Factory
- AWS Step Functions

**Arquitetura típica:**
```
┌─────────────────────────────────┐
│         Sistema Central         │
│        de Orquestração          │
└─┬───────────┬───────────┬───────┘
  │           │           │
  ▼           ▼           ▼
┌─────┐    ┌─────┐    ┌─────┐
│Fonte│    │Proc.│    │Dest.│
│Dados│    │Dados│    │Dados│
└─────┘    └─────┘    └─────┘
```

**Código de exemplo (usando Apache Airflow):**
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.emr import EmrAddStepsOperator
from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
from datetime import datetime, timedelta

# Definir DAG
default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email': ['alerts@empresa.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'pipeline_dados_centralizado',
    default_args=default_args,
    description='Pipeline de dados com orquestração centralizada',
    schedule_interval='0 0 * * *',  # Diariamente à meia-noite
    start_date=datetime(2023, 1, 1),
    catchup=False
)

# Definir tarefas
def validar_fonte():
    """Verifica se os dados de origem estão disponíveis e corretos"""
    print("Validando dados de origem...")
    # Lógica de validação...
    return {'status': 'success', 'validation_time': datetime.now().isoformat()}

validacao = PythonOperator(
    task_id='validar_fonte',
    python_callable=validar_fonte,
    dag=dag
)

# Definir job Spark a ser executado no EMR
spark_steps = [
    {
        'Name': 'Processamento de dados',
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': [
                'spark-submit',
                '--deploy-mode', 'cluster',
                's3://bucket/scripts/process_data.py',
                '--data-path', 's3://bucket/input/{{ ds }}/',
                '--output-path', 's3://bucket/output/{{ ds }}/'
            ]
        }
    }
]

# Submeter job para o EMR
submit_job = EmrAddStepsOperator(
    task_id='submit_spark_job',
    job_flow_id='j-XXXXXXXXXXXXX',  # ID do cluster EMR
    steps=spark_steps,
    dag=dag
)

# Monitorar execução do job
monitor_job = EmrStepSensor(
    task_id='monitor_spark_job',
    job_flow_id='j-XXXXXXXXXXXXX',
    step_id="{{ task_instance.xcom_pull(task_ids='submit_spark_job')[0] }}",
    aws_conn_id='aws_default',
    dag=dag
)

# Copiar dados processados para área de apresentação
copy_to_presentation = S3CopyObjectOperator(
    task_id='copy_to_presentation',
    source_bucket_key='s3://bucket/output/{{ ds }}/resultado.parquet',
    dest_bucket_key='s3://bucket/presentation/latest/resultado.parquet',
    source_bucket_name='bucket',
    dest_bucket_name='bucket',
    dag=dag
)

# Notificar conclusão do pipeline
def notificar_conclusao(**context):
    """Envia notificação de conclusão do pipeline"""
    execution_date = context['ds']
    print(f"Pipeline concluído com sucesso para data {execution_date}")
    # Lógica de notificação...

notificacao = PythonOperator(
    task_id='notificar_conclusao',
    python_callable=notificar_conclusao,
    provide_context=True,
    dag=dag
)

# Definir fluxo de execução
validacao >> submit_job >> monitor_job >> copy_to_presentation >> notificacao
```

**Desafios a se considerar:**
- **Escalabilidade Limitada:** Pode se tornar um gargalo com volumes crescentes de dados
- **Ponto Único de Falha:** Problemas no sistema central podem afetar todo o pipeline
- **Adaptação a Mudanças:** Modificações complexas podem requerer alterações em todo o sistema central
- **Sobrecarga Administrativa:** Manutenção do sistema central pode se tornar complexa com o crescimento

#### Orquestração Descentralizada

Na orquestração descentralizada, diferentes componentes do sistema gerenciam partes específicas do fluxo de dados, com comunicação e coordenação entre eles.

**Características:**
- Responsabilidades distribuídas entre múltiplos componentes
- Cada sistema ou processo gerencia sua própria parte do fluxo
- Comunicação entre componentes através de eventos ou mensagens

**Vantagens:**
- **Orquestra Distribuída:** Maior capacidade de escala e resiliência com tarefas distribuídas
- **Autonomia e Flexibilidade:** Cada componente pode evoluir independentemente
- **Resistência a Falhas:** Falhas em um componente não comprometem todo o sistema
- **Adaptação Contínua:** Facilidade para adicionar ou modificar componentes sem afetar outros

**Exemplos de ferramentas:**
- Apache Kafka + Kafka Connect + Kafka Streams
- Sistemas baseados em Event Sourcing
- Plataformas de microsserviços com coreografia

**Arquitetura típica:**
```
┌─────┐    ┌─────────────┐    ┌─────┐
│Fonte│    │Sistema de   │    │Dest.│
│Dados├───►│Mensagens    ├───►│Dados│
└─────┘    │(Kafka/MQTT) │    └─────┘
           └─────┬───────┘
                 │
         ┌───────▼───────┐
         │Componente de  │
         │Processamento 1│
         └───────┬───────┘
                 │
                 ▼
         ┌───────────────┐
         │Componente de  │
         │Processamento 2│
         └───────────────┘
```

**Código de exemplo (usando Apache Kafka):**
```python
# Componente 1: Produtor de Dados
from confluent_kafka import Producer
import json
import time
from datetime import datetime

def publish_data():
    """Publica dados no tópico Kafka"""
    config = {
        'bootstrap.servers': 'kafka:9092',
        'client.id': 'data_producer'
    }
    
    producer = Producer(config)
    
    # Simulação de geração de dados
    for i in range(100):
        data = {
            'id': i,
            'timestamp': datetime.now().isoformat(),
            'value': i * 10,
            'category': 'product_' + str(i % 5)
        }
        
        # Publicar mensagem
        producer.produce(
            'raw_data', 
            key=str(i), 
            value=json.dumps(data).encode('utf-8'),
            callback=delivery_report
        )
        producer.flush()
        time.sleep(0.1)

def delivery_report(err, msg):
    """Callback para confirmação de entrega"""
    if err is not None:
        print(f'Erro na entrega: {err}')
    else:
        print(f'Mensagem entregue para {msg.topic()}[{msg.partition()}] @ {msg.offset()}')

# Componente 2: Processador de Dados
from confluent_kafka import Consumer, Producer
import json

def process_data():
    """Consome, processa e republica dados"""
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'data_processor',
        'auto.offset.reset': 'earliest'
    }
    
    producer_config = {
        'bootstrap.servers': 'kafka:9092',
        'client.id': 'data_processor'
    }
    
    consumer = Consumer(consumer_config)
    producer = Producer(producer_config)
    
    consumer.subscribe(['raw_data'])
    
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                continue
                
            if msg.error():
                print(f"Erro no consumo: {msg.error()}")
                continue
                
            # Processar dados
            try:
                data = json.loads(msg.value().decode('utf-8'))
                
                # Aplicar transformação
                processed_data = {
                    'id': data['id'],
                    'timestamp': data['timestamp'],
                    'value': data['value'],
                    'category': data['category'],
                    'processed_value': data['value'] * 2,  # Exemplo de transformação
                    'processing_timestamp': datetime.now().isoformat()
                }
                
                # Publicar resultado processado
                producer.produce(
                    'processed_data',
                    key=str(data['id']),
                    value=json.dumps(processed_data).encode('utf-8')
                )
                producer.flush()
                
            except Exception as e:
                print(f"Erro no processamento: {e}")
                
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

# Componente 3: Consumidor para Armazenamento
from confluent_kafka import Consumer
import json
import psycopg2

def store_data():
    """Armazena dados processados no banco de dados"""
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',
        'group.id': 'data_storer',
        'auto.offset.reset': 'earliest'
    }
    
    consumer = Consumer(consumer_config)
    consumer.subscribe(['processed_data'])
    
    # Conexão com banco de dados
    conn = psycopg2.connect(
        host="postgres",
        database="datastore",
        user="postgres",
        password="password"
    )
    cursor = conn.cursor()
    
    try:
        while True:
            msg = consumer.poll(1.0)
            
            if msg is None:
                continue
                
            if msg.error():
                print(f"Erro no consumo: {msg.error()}")
                continue
                
            # Armazenar dados
            try


