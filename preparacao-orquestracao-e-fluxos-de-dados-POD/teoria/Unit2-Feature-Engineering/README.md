# Feature Engineering / Engenharia de Atributos

##  Sumário
- [Introdução (Introduction)](#introdução-introduction)
- [Importância do Feature Engineering](#importância-do-feature-engineering)
  - [Representatividade dos Dados (Data Representativeness)](#representatividade-dos-dados-data-representativeness)
  - [Redução de Ruído (Noise Reduction)](#redução-de-ruído-noise-reduction)
  - [Captura de Relacionamentos Complexos (Capturing Complex Relationships)](#captura-de-relacionamentos-complexos-capturing-complex-relationships)
  - [Eficiência Computacional (Computational Efficiency)](#eficiência-computacional-computational-efficiency)
  - [Interpretabilidade (Interpretability)](#interpretabilidade-interpretability)
- [Técnicas de Feature Engineering](#técnicas-de-feature-engineering-feature-engineering-techniques)
  - [Transformações Lineares (Linear Transformations)](#transformações-lineares-linear-transformations)
    - [Transformação Logarítmica (Logarithmic Transformation)](#transformação-logarítmica-logarithmic-transformation)
    - [Features de Interação (Interaction Features)](#features-de-interação-interaction-features)
    - [Normalização e Padronização (Normalization and Standardization)](#normalização-e-padronização-normalization-and-standardization)
  - [Transformações Não Lineares (Non-linear Transformations)](#transformações-não-lineares-non-linear-transformations)
    - [Extração de Features (Feature Extraction)](#extração-de-features-feature-extraction)
    - [Feature Engineering em NLP (NLP Feature Engineering)](#feature-engineering-em-nlp-nlp-feature-engineering)
    - [Feature Engineering em Visão Computacional (Computer Vision Feature Engineering)](#feature-engineering-em-visão-computacional-computer-vision-feature-engineering)
    - [Feature Engineering em Séries Temporais (Time Series Feature Engineering)](#feature-engineering-em-séries-temporais-time-series-feature-engineering)
  - [Transformações Categóricas (Categorical Transformations)](#transformações-categóricas-categorical-transformations)
    - [One-Hot Encoding](#one-hot-encoding)
    - [Label Encoding](#label-encoding)
    - [Target Encoding (Mean Encoding)](#target-encoding-mean-encoding)
  - [Transformações de Seleção (Selection Transformations)](#transformações-de-seleção-selection-transformations)
    - [Engenharia de Atributos Temporais (Temporal Feature Engineering)](#engenharia-de-atributos-temporais-temporal-feature-engineering)
    - [Seleção de Features (Feature Selection)](#seleção-de-features-feature-selection)
- [Benefícios do Feature Engineering](#benefícios-do-feature-engineering-benefits-of-feature-engineering)
- [Melhores Práticas (Best Practices)](#melhores-práticas-best-practices)
- [Exemplos Práticos (Practical Examples)](#exemplos-práticos-practical-examples)
- [Referências (References)](#referências-references)

## Introdução (Introduction)

Feature Engineering (Engenharia de Atributos) é o processo sistemático de criação, transformação e seleção de variáveis (features) para que sejam mais adequadas e informativas para algoritmos de aprendizado de máquina. Esta etapa é crucial no ciclo de vida de desenvolvimento de modelos de machine learning e análise de dados, podendo impactar significativamente o desempenho final dos modelos.

### O que são Features?

No contexto de machine learning, features (ou características/atributos) são as variáveis ou propriedades que representam os dados de entrada que um modelo utiliza para fazer previsões ou classificações. Estes atributos são as informações que o algoritmo analisa para identificar padrões e fazer inferências.

Features podem se apresentar em diversos formatos:
- **Numéricas**: idade, altura, renda, preço
- **Categóricas**: gênero, cor, categoria de produto
- **Textuais**: comentários, artigos, tweets
- **Visuais**: pixels em imagens
- **Séries temporais**: dados sequenciais ao longo do tempo
- **Geoespaciais**: coordenadas geográficas

A qualidade e relevância das features são determinantes para o sucesso de um modelo de machine learning. Features inadequadas ou pouco informativas podem resultar em modelos imprecisos, enquanto features bem projetadas podem ajudar o modelo a capturar eficientemente os relacionamentos subjacentes nos dados.

## Importância do Feature Engineering

### Representatividade dos Dados (Data Representativeness)

Dados brutos frequentemente não capturam adequadamente a complexidade do problema que estamos tentando resolver. A criação de features adicionais pode ajudar a expressar melhor as informações relevantes contidas nos dados.

**Exemplo prático:**
```python
# Dados de vendas com data
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Criando features mais representativas
df['mes'] = df['data_venda'].dt.month
df['dia_semana'] = df['data_venda'].dt.dayofweek
df['fim_de_semana'] = df['dia_semana'].apply(lambda x: 1 if x >= 5 else 0)
df['trimestre'] = df['data_venda'].dt.quarter

# Agora temos features que representam melhor o aspecto temporal das vendas
```

Este exemplo cria novas features que representam diferentes aspectos temporais das vendas, permitindo que o modelo identifique padrões sazonais que não seriam evidentes apenas com a data original.

### Redução de Ruído (Noise Reduction)

Dados reais frequentemente contêm ruído, outliers e valores atípicos que podem afetar negativamente o desempenho do modelo. O Feature Engineering pode ajudar a mitigar esses problemas, tornando os dados mais limpos e confiáveis.

**Exemplo prático:**
```python
# Aplicando transformação logarítmica para reduzir o impacto de outliers em valores monetários
import numpy as np

# Valores originais com grande variação
precos = [100, 120, 95, 5000, 110, 130]

# Transformação logarítmica
precos_log = np.log1p(precos)  # log(1+x) para lidar com zeros

print("Valores originais:", precos)
print("Valores após log:", precos_log)

# Resultado:
# Valores originais: [100, 120, 95, 5000, 110, 130]
# Valores após log: [4.61, 4.79, 4.56, 8.52, 4.70, 4.87]
```

Observe como os valores após a transformação logarítmica estão em uma escala mais uniforme, reduzindo o impacto do outlier (5000) e tornando a distribuição mais simétrica.

### Captura de Relacionamentos Complexos (Capturing Complex Relationships)

Muitos algoritmos de machine learning, especialmente modelos lineares, podem não ser capazes de entender relacionamentos complexos ou não-lineares entre features diretamente. A criação de features de interação ou transformações não-lineares pode ajudar a representar esses relacionamentos de maneira mais compreensível para o modelo.

**Exemplo prático:**
```python
# Criando features de interação em um dataset de precificação de imóveis
import pandas as pd

# Dataset de exemplo
imoveis = pd.DataFrame({
    'area_m2': [70, 100, 120, 150, 200],
    'quartos': [2, 3, 3, 4, 4],
    'preco': [250000, 320000, 380000, 480000, 550000]
})

# Criando feature de interação: área por quarto
imoveis['area_por_quarto'] = imoveis['area_m2'] / imoveis['quartos']

# Feature polinomial
imoveis['area_quadrada'] = imoveis['area_m2'] ** 2

print(imoveis)
```

Neste exemplo, criamos duas novas features que capturam relações mais complexas: a área por quarto (que pode ser um indicador melhor de espaço útil) e a área ao quadrado (que pode capturar relações não-lineares entre tamanho e preço).

### Eficiência Computacional (Computational Efficiency)

O número e a dimensionalidade das features podem afetar significativamente o tempo de treinamento e os recursos computacionais necessários. O Feature Engineering pode ajudar a reduzir a dimensionalidade dos dados, tornando o processo de treinamento mais eficiente.

**Exemplo prático:**
```python
# Selecionando as features mais importantes usando Random Forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

# Carregando dados
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target

# Treinando modelo para avaliar importância das features
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Calculando e visualizando importância das features
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print(feature_importance.head(10))  # Top 10 features mais importantes

# Selecionando apenas as 5 features mais importantes para um modelo mais eficiente
top_features = feature_importance['Feature'][:5].tolist()
X_reduced = X[top_features]

print(f"\nDimensionalidade reduzida de {X.shape[1]} para {X_reduced.shape[1]} features")
```

Este exemplo demonstra como podemos identificar as features mais importantes e reduzir a dimensionalidade do dataset, o que pode melhorar significativamente a eficiência computacional do treinamento.

### Interpretabilidade (Interpretability)

Algumas features podem ser projetadas para tornar os resultados do modelo mais interpretáveis. Isso é especialmente importante em aplicações onde a explicação do modelo é essencial, como em setores regulamentados ou em tomadas de decisão críticas.

**Exemplo prático:**
```python
# Criando features interpretáveis para análise de crédito
import pandas as pd

# Dataset de exemplo
clientes = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'renda_mensal': [5000, 3000, 8000, 4000, 6000],
    'despesas_fixas': [2000, 1800, 3000, 2200, 2800],
    'valor_emprestimo': [100000, 50000, 200000, 80000, 150000]
})

# Criando features interpretáveis
clientes['comprometimento_renda'] = clientes['despesas_fixas'] / clientes['renda_mensal']
clientes['emprestimo_vs_renda_anual'] = clientes['valor_emprestimo'] / (clientes['renda_mensal'] * 12)

print(clientes)

# Interpretação: 
# - comprometimento_renda: proporção da renda já comprometida com despesas fixas
# - emprestimo_vs_renda_anual: quantos anos de renda seriam necessários para pagar o empréstimo
```

Neste exemplo, criamos duas novas features que são facilmente interpretáveis e fornecem insights diretos sobre a capacidade de pagamento do cliente, o que é crucial em modelos de análise de crédito.

## Técnicas de Feature Engineering (Feature Engineering Techniques)

### Transformações Lineares (Linear Transformations)

Transformações lineares são operações matemáticas relativamente simples e diretas que produzem resultados proporcionais aos valores originais. Estas transformações são frequentemente utilizadas como primeiro passo no processo de Feature Engineering.

#### Transformação Logarítmica (Logarithmic Transformation)

A transformação logarítmica é particularmente útil para:
- Lidar com distribuições assimétricas à direita (skewed)
- Reduzir o impacto de outliers
- Linearizar relações exponenciais

**Implementação em Python:**
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados com distribuição assimétrica (ex: preços de imóveis)
precos = np.random.exponential(scale=300000, size=1000)

# Aplicando transformação logarítmica
precos_log = np.log1p(precos)  # log(1+x) para lidar com zeros

# Visualizando o efeito
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
sns.histplot(precos, ax=ax1)
ax1.set_title('Distribuição Original')
sns.histplot(precos_log, ax=ax2)
ax2.set_title('Após Transformação Logarítmica')
plt.tight_layout()
plt.show()
```

#### Features de Interação (Interaction Features)

As features de interação capturam a relação entre duas ou mais variáveis existentes, geralmente através de operações como multiplicação, divisão ou adição.

**Exemplos:**
- Em um modelo de precificação de imóveis: `area_total * qualidade_acabamento`
- Em modelos de conversão de e-commerce: `tempo_no_site * páginas_visitadas`
- Para análise de desempenho: `velocidade / consumo_combustível`

**Implementação em Python:**
```python
import pandas as pd

# Dataset de exemplo para previsão de vendas
df = pd.DataFrame({
    'preco': [20, 15, 25, 30, 18],
    'marketing_budget': [5000, 3000, 7000, 8000, 4000],
    'competidores': [2, 5, 1, 0, 3],
    'vendas': [120, 80, 200, 250, 100]
})

# Criando features de interação
df['preco_por_competidor'] = df['preco'] / (df['competidores'] + 1)  # +1 para evitar divisão por zero
df['marketing_eficiencia'] = df['marketing_budget'] / df['vendas']
df['marketing_competicao'] = df['marketing_budget'] / (df['competidores'] + 1)

print(df.head())
```

#### Normalização e Padronização (Normalization and Standardization)

Estas técnicas são fundamentais para garantir que features em diferentes escalas tenham o mesmo impacto no modelo.

**Normalização (Min-Max Scaling):**
Transforma os valores para um intervalo específico, geralmente [0, 1].

Fórmula: $Z_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$

**Padronização (Z-score):**
Centraliza os valores em torno da média e escala pelo desvio padrão.

Fórmula: $Z = \frac{X - \mu}{\sigma}$

**Implementação em Python:**
```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np

# Dados de exemplo
dados = pd.DataFrame({
    'idade': [25, 35, 45, 20, 60],
    'salario': [50000, 70000, 90000, 30000, 120000],
    'anos_experiencia': [2, 8, 15, 1, 25]
})

# Normalização (Min-Max)
min_max_scaler = MinMaxScaler()
dados_norm = pd.DataFrame(
    min_max_scaler.fit_transform(dados),
    columns=dados.columns
)

# Padronização (Z-score)
standard_scaler = StandardScaler()
dados_std = pd.DataFrame(
    standard_scaler.fit_transform(dados),
    columns=dados.columns
)

# Comparando os resultados
print("Dados originais:")
print(dados)
print("\nDados normalizados (0-1):")
print(dados_norm)
print("\nDados padronizados (z-score):")
print(dados_std)
```

### Transformações Não Lineares (Non-linear Transformations)

Transformações não lineares são operações matemáticas mais complexas que não produzem resultados proporcionais aos valores originais. Estas transformações são particularmente úteis para capturar relações não lineares nos dados.

#### Extração de Features (Feature Extraction)

A extração de features consiste em criar novas representações dos dados originais, geralmente com o objetivo de reduzir a dimensionalidade ou extrair informações latentes mais relevantes.

**Técnicas comuns:**
- Análise de Componentes Principais (PCA)
- Decomposição de Valores Singulares (SVD)
- t-SNE (t-Distributed Stochastic Neighbor Embedding)
- Autoencoders

**Implementação em Python (PCA):**
```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Carregando dados (imagens de dígitos 8x8)
digits = load_digits()
X = digits.data
y = digits.target

# Aplicando PCA para reduzir para 2 dimensões
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizando o resultado
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', alpha=0.8)
plt.colorbar(scatter, label='Dígito')
plt.title('Visualização PCA dos dígitos MNIST')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()

# Quanto de variância é explicada por cada componente?
print(f"Variância explicada pelos 2 primeiros componentes: {sum(pca.explained_variance_ratio_):.2f}")
```

#### Feature Engineering em NLP (NLP Feature Engineering)

O processamento de linguagem natural (NLP) requer técnicas específicas para converter texto em formato numérico que algoritmos de ML possam processar.

**Técnicas principais:**
- Bag of Words (BoW)
- TF-IDF (Term Frequency-Inverse Document Frequency)
- Word Embeddings (Word2Vec, GloVe, FastText)
- N-gramas
- Features linguísticas (contagem de substantivos, verbos, adjetivos)

**Implementação em Python (TF-IDF):**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Dados de exemplo
textos = [
    "O machine learning é uma área fascinante da inteligência artificial",
    "Processamento de linguagem natural é um subcampo do machine learning",
    "Feature engineering é essencial para modelos de machine learning eficientes",
    "Inteligência artificial tem revolucionado muitos setores da indústria"
]

# Aplicando TF-IDF
vectorizer = TfidfVectorizer(stop_words=['é', 'um', 'uma', 'para', 'da', 'do'])
X_tfidf = vectorizer.fit_transform(textos)

# Convertendo para DataFrame para visualização
df_tfidf = pd.DataFrame(
    X_tfidf.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print(df_tfidf)
```

#### Feature Engineering em Visão Computacional (Computer Vision Feature Engineering)

Em visão computacional, existem diversas técnicas para extrair características relevantes de imagens.

**Técnicas comuns:**
- Descritores de cores (histogramas de cores)
- Descritores de textura (LBP, GLCM)
- Descritores de forma (HOG, contornos)
- Features extraídas de CNN pré-treinadas

**Exemplo conceitual (extração de features usando VGG16):**
```python
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Carregando modelo pré-treinado sem a camada fully-connected
base_model = VGG16(weights='imagenet', include_top=False)

# Função para extrair features
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    # Extraindo features da penúltima camada
    features = base_model.predict(img_array)
    features = features.reshape((features.shape[0], -1))
    
    return features

# Exemplo de uso
img_path = 'caminho/para/imagem.jpg'
features = extract_features(img_path)
print(f"Features extraídas: {features.shape}")
```

#### Feature Engineering em Séries Temporais (Time Series Feature Engineering)

Para dados sequenciais ao longo do tempo, existem técnicas específicas que ajudam a capturar padrões temporais.

**Técnicas principais:**
- Lags (valores defasados)
- Médias móveis
- Decomposição de série temporal (tendência, sazonalidade, resíduo)
- Features baseadas em calendário
- Features de frequência (FFT)

**Implementação em Python:**
```python
import pandas as pd
import numpy as np
from datetime import datetime

# Criando série temporal de exemplo
np.random.seed(42)
dates = pd.date_range(start='2020-01-01', end='2022-12-31', freq='D')
ts = pd.Series(np.random.normal(0, 1, len(dates)) + np.sin(np.arange(len(dates)) * 2 * np.pi / 365), index=dates)

# Criando DataFrame com features temporais
df = pd.DataFrame({'valor': ts})

# Criando features de lag
for i in [1, 7, 30]:
    df[f'lag_{i}'] = df['valor'].shift(i)

# Criando médias móveis
for window in [7, 30, 90]:
    df[f'ma_{window}'] = df['valor'].rolling(window=window).mean()

# Features baseadas em calendário
df['ano'] = df.index.year
df['mes'] = df.index.month
df['dia_semana'] = df.index.dayofweek
df['trimestre'] = df.index.quarter
df['dia_ano'] = df.index.dayofyear
df['fim_semana'] = df['dia_semana'].apply(lambda x: 1 if x >= 5 else 0)

# Adicionando sazonalidade explícita
df['sen_anual'] = np.sin(df['dia_ano'] * 2 * np.pi / 365)
df['cos_anual'] = np.cos(df['dia_ano'] * 2 * np.pi / 365)
df['sen_semanal'] = np.sin(df['dia_semana'] * 2 * np.pi / 7)
df['cos_semanal'] = np.cos(df['dia_semana'] * 2 * np.pi / 7)

print(df.head(10))
```

### Transformações Categóricas (Categorical Transformations)

Transformações categóricas são essenciais para converter variáveis categóricas (não numéricas) em formatos que os algoritmos de machine learning possam processar eficientemente.

#### One-Hot Encoding

O One-Hot Encoding transforma cada categoria em uma coluna binária (0 ou 1). É ideal para variáveis categóricas sem relação ordinal entre as categorias.

**Implementação em Python:**
```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Dados de exemplo
df = pd.DataFrame({
    'cor': ['vermelho', 'azul', 'verde', 'vermelho', 'azul'],
    'tamanho': ['pequeno', 'médio', 'grande', 'médio', 'pequeno']
})

# Aplicando One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False)
encoded_features = encoder.fit_transform(df)

# Criando DataFrame com os resultados
encoded_df = pd.DataFrame(
    encoded_features,
    columns=encoder.get_feature_names_out(['cor', 'tamanho'])
)

print("Dados originais:")
print(df)
print("\nDados após One-Hot Encoding:")
print(encoded_df)
```

**Vantagens:**
- Não introduz relações ordinais onde não existem
- Cada feature é interpretável (presença ou ausência da categoria)

**Desvantagens:**
- Cria muitas colunas para categorias com alta cardinalidade
- Pode levar à "maldição da dimensionalidade"

#### Label Encoding

O Label Encoding substitui cada categoria por um valor numérico único (tipicamente 0, 1, 2, ...). É mais adequado para categorias com uma relação ordinal natural.

**Implementação em Python:**
```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Dados de exemplo com categorias ordinais
df = pd.DataFrame({
    'educacao': ['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Pós-Graduação', 'Mestrado'],
    'nivel_satisfacao': ['Baixo', 'Médio', 'Alto', 'Médio', 'Muito Alto']
})

# Aplicando Label Encoding
le = LabelEncoder()
df['educacao_encoded'] = le.fit_transform(df['educacao'])
df['satisfacao_encoded'] = le.fit_transform(df['nivel_satisfacao'])

print(df)

# Mapeamento dos valores
print("\nEducação - Mapeamento:")
for i, categoria in enumerate(le.classes_):
    print(f"{categoria} -> {i}")
```

**Vantagens:**
- Mantém a dimensionalidade original do conjunto de dados
- Adequado para variáveis ordinais

**Desvantagens:**
- Introduz uma ordem implícita que pode não existir
- Modelo pode interpretar erroneamente a diferença entre categorias

#### Target Encoding (Mean Encoding)

O Target Encoding substitui cada categoria pela média (ou outra estatística) da variável alvo para aquela categoria. É particularmente útil para categorias de alta cardinalidade.

**Implementação em Python:**
```python
import pandas as pd
import numpy as np

# Dados de exemplo
np.random.seed(42)
df = pd.DataFrame({
    'cidade': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Recife'], 1000),
    'renda': np.random.normal(5000, 2000, 1000)
})

# Calculando o target encoding (média da renda por cidade)
target_means = df.groupby('cidade')['renda'].mean().to_dict()
df['cidade_encoded'] = df['cidade'].map(target_means)

# Visualizando o resultado
print("Codificação por média da renda:")
for cidade, mean_value in target_means.items():
    print(f"{cidade}: {mean_value:.2f}")

print("\nPrimeiras linhas do dataframe com a nova feature:")
print(df.head())
```

**Vantagens:**
- Muito eficaz para categorias de alta cardinalidade
- Incorpora informação da variável alvo

**Desvantagens:**
- Risco de overfitting (requer validação cruzada ou outras técnicas de regularização)
- Não aplicável na ausência de variável alvo (não supervisionado)

### Transformações de Seleção (Selection Transformations)

As transformações de seleção envolvem a escolha ou criação estratégica de features para melhorar o desempenho do modelo.

#### Engenharia de Atributos Temporais (Temporal Feature Engineering)

A engenharia de atributos temporais foca na extração de informações úteis de datas e horários, transformando-os em features que capturam padrões temporais relevantes.

**Implementação em Python:**
```python
import pandas as pd
from datetime import datetime
import holidays

# Criando dataset com datas
df = pd.DataFrame({
    'data': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
    'vendas': [100 + i % 30 * 5 for i in range(365)]  # Dados fictícios de vendas
})

# Extraindo componentes de data básicos
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month
df['dia'] = df['data'].dt.day
df['dia_semana'] = df['data'].dt.dayofweek  # 0 = Segunda, 6 = Domingo
df['dia_ano'] = df['data'].dt.dayofyear
df['semana_ano'] = df['data'].dt.isocalendar().week
df['trimestre'] = df['data'].dt.quarter

# Features mais elaboradas
df['fim_semana'] = df['dia_semana'].apply(lambda x: 1 if x >= 5 else 0)
df['mes_inicio'] = df['dia'].apply(lambda x: 1 if x <= 10 else 0)
df['mes_meio'] = df['dia'].apply(lambda x: 1 if 11 <= x <= 20 else 0)
df['mes_fim'] = df['dia'].apply(lambda x: 1 if x >= 21 else 0)

# Identificando feriados (Brasil)
feriados_br = holidays.Brazil()
df['feriado'] = df['data'].apply(lambda x: 1 if x in feriados_br else 0)

# Proximidade de datas especiais (ex: Natal)
df['dias_ate_natal'] = df['data'].apply(lambda x: abs((pd.Timestamp(x.year, 12, 25) - x).days))
df['prox_natal'] = df['dias_ate_natal'].apply(lambda x: 1 if x <= 15 else 0)

print(df.head())
```

#### Seleção de Features (Feature Selection)

A seleção de features consiste em identificar e escolher o subconjunto mais relevante de features para um modelo, reduzindo ruído e dimensionalidade.

**Principais abordagens:**
1. **Métodos baseados em filtro**: Selecionam features com base em métricas estatísticas
2. **Métodos baseados em wrapper**: Avaliam subconjuntos de features com o próprio modelo
3. **Métodos incorporados (embedded)**: A seleção é parte do processo de treinamento do modelo

**Implementação em Python:**
```python
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Carregando dataset para demonstração
cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data, columns=cancer.feature_names)
y = cancer.target

print(f"Dimensões originais: {X.shape}")

# 1. Seleção baseada em filtro (estatística)
# Usando ANOVA F-value
selector_f = SelectKBest(f_classif, k=10)
X_filtered = selector_f.fit_transform(X, y)

# Features selecionadas
mask = selector_f.get_support()
selected_features = X.columns[mask]
print("\nTop 10 features segundo ANOVA F-test:")
print(selected_features.tolist())

# 2. Seleção baseada em wrapper
# Recursive Feature Elimination (RFE)
model = LogisticRegression(max_iter=1000)
rfe = RFE(estimator=model, n_features_to_select=10)
X_rfe = rfe.fit_transform(X, y)

# Features selecionadas
rfe_selected = X.columns[rfe.support_]
print("\nTop 10 features segundo RFE:")
print(rfe_selected.tolist())

# 3. Importância de features incorporada ao modelo
# Random Forest para importância de features
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

# Extraindo e visualizando importância das features
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)

print("\nTop 10 features segundo Random Forest:")
print(feature_importances.head(10))

# Visualizando a importância das features
plt.figure(figsize=(10, 6))
plt.barh(feature_importances['Feature'][:10], feature_importances['Importance'][:10])
plt.xlabel('Importância')
plt.ylabel('Feature')
plt.title('Top 10 Features mais Importantes')
plt.gca().invert_yaxis()  # Inverter para visualizar a mais importante no topo
plt.tight_layout()
plt.show()
```

## Benefícios do Feature Engineering (Benefits of Feature Engineering)

A aplicação de técnicas eficazes de Feature Engineering pode trazer múltiplos benefícios ao processo de modelagem e análise de dados:

1. **Redução da Dimensionalidade**:
   - Diminui o número de variáveis, simplificando o modelo
   - Mitiga problemas de overfitting (especialmente em datasets com poucas amostras)
   - Reduz custos computacionais durante treinamento e inferência

2. **Qualidade dos Dados**:
   - Melhora a qualidade geral do conjunto de dados
   - Elimina ou reduz o impacto de outliers e valores atípicos
   - Preenche lacunas de informação com features derivadas

3. **Melhoria do Desempenho**:
   - Aumenta a precisão e capacidade preditiva dos modelos
   - Permite que modelos mais simples capturem relacionamentos complexos
   - Reduz a necessidade de arquiteturas complexas de deep learning em muitos casos

4. **Economia de Recursos**:
   - Diminui o tempo de treinamento
   - Reduz requisitos de hardware
   - Otimiza processos de experimentação e iteração

5. **Interpretabilidade**:
   - Facilita a compreensão das decisões do modelo
   - Permite insights mais claros sobre os fatores que influenciam as previsões
   - Auxilia na explicabilidade para stakeholders não técnicos

## Melhores Práticas (Best Practices)

Para maximizar os benefícios do Feature Engineering, recomenda-se seguir estas práticas:

### 1. Compreenda o Domínio do Problema

Antes de começar a criar ou transformar features, é essencial compreender profundamente o domínio do problema:
- Converse com especialistas do domínio
- Estude a literatura e pesquisas relacionadas
- Entenda as relações causais entre as variáveis

### 2. Realize uma Análise Exploratória Detalhada

A análise exploratória de dados (EDA) é fundamental para guiar o processo de Feature Engineering:
- Examine a distribuição de cada variável
- Identifique correlações e padrões
- Detecte outliers e valores faltantes
- Entenda as relações entre as features e a variável alvo

### 3. Considere as Limitações dos Algoritmos

Diferentes algoritmos têm diferentes sensibilidades e requisitos:
- Modelos lineares precisam de features que capturem relações não lineares
- Árvores de decisão podem lidar com features não escaladas, mas redes neurais geralmente não
- Algoritmos baseados em distância (como KNN) são sensíveis a escalas e dimensionalidade

### 4. Experimente Diferentes Abordagens

O Feature Engineering é uma arte que requer experimentação:
- Teste várias transformações e combinações
- Avalie o impacto no desempenho do modelo
- Use validação cruzada para evitar overfitting
- Mantenha um registro das características que funcionam melhor

### 5. Automatize Quando Possível

Para pipelines de produção ou conjuntos de dados muito grandes:
- Considere ferramentas automatizadas de Feature Engineering
- Crie funções reutilizáveis para transformações comuns
- Implemente pipelines que realizem as transformações de forma consistente nos conjuntos de treino e teste

### 6. Documente o Processo

Mantenha uma documentação clara do processo de Feature Engineering:
- Quais transformações foram aplicadas e por quê
- Como as novas features são calculadas
- Qual o impacto de cada feature no modelo
- Quais considerações de domínio influenciaram as decisões

## Exemplos Práticos (Practical Examples)

### Exemplo 1: Previsão de Churn de Clientes

Neste exemplo, criamos features relevantes para prever a probabilidade de um cliente cancelar um serviço de assinatura.

```python
import pandas as pd
import numpy as np
from datetime import datetime

# Dados fictícios de clientes
dados_clientes = pd.DataFrame({
    'cliente_id': range(1, 101),
    'data_cadastro': pd.date_range('2020-01-01', periods=100, freq='3D'),
    'ultima_compra': pd.date_range('2022-01-15', periods=100, freq='5D'),
    'total_gasto': np.random.normal(500, 200, 100),
    'total_pedidos': np.random.poisson(8, 100),
    'reclamacoes': np.random.poisson(1, 100),
    'idade': np.random.randint(18, 70, 100),
    'categoria_preferida': np.random.choice(['Eletrônicos', 'Moda', 'Casa', 'Esportes', 'Alimentos'], 100),
    'churn': np.random.choice([0, 1], 100, p=[0.8, 0.2])  # Target: cliente cancelou (1) ou não (0)
})

# Feature Engineering para previsão de churn

# 1. Features temporais
hoje = datetime.now().date()
dados_clientes['dias_desde_cadastro'] = (hoje - dados_clientes['data_cadastro'].dt.date).dt.days
dados_clientes['dias_desde_ultima_compra'] = (hoje - dados_clientes['ultima_compra'].dt.date).dt.days
dados_clientes['cliente_antigo'] = dados_clientes['dias_desde_cadastro'].apply(lambda x: 1 if x > 365 else 0)
dados_clientes['inativo'] = dados_clientes['dias_desde_ultima_compra'].apply(lambda x: 1 if x > 90 else 0)

# 2. Features de comportamento
dados_clientes['valor_medio_pedido'] = dados_clientes['total_gasto'] / dados_clientes['total_pedidos']
dados_clientes['taxa_reclamacao'] = dados_clientes['reclamacoes'] / dados_clientes['total_pedidos']
dados_clientes['alto_valor'] = dados_clientes['total_gasto'].apply(lambda x: 1 if x > 700 else 0)

# 3. Features categóricas (one-hot encoding)
categoria_dummies = pd.get_dummies(dados_clientes['categoria_preferida'], prefix='cat')
dados_clientes = pd.concat([dados_clientes, categoria_dummies], axis=1)

# 4. Features de interação
dados_clientes['reclamacoes_recentes'] = dados_clientes['reclamacoes'] * dados_clientes['inativo']
dados_clientes['valor_por_tempo'] = dados_clientes['total_gasto'] / (dados_clientes['dias_desde_cadastro'] + 1)

# Verificando as novas features criadas
features_para_modelo = ['dias_desde_cadastro', 'dias_desde_ultima_compra', 'cliente_antigo', 
                         'inativo', 'valor_medio_pedido', 'taxa_reclamacao', 'alto_valor',
                         'reclamacoes_recentes', 'valor_por_tempo'] + list(categoria_dummies.columns)

print("Features criadas para o modelo de churn:")
print(features_para_modelo)
print("\nAmostra dos dados processados:")
print(dados_clientes[features_para_modelo].head())
```

### Exemplo 2: Feature Engineering para Análise de Sentimentos em Texto

```python
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Baixar recursos necessários do NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Dados fictícios de reviews
reviews = pd.DataFrame({
    'texto': [
        "O produto é excelente, superou minhas expectativas! Recomendo muito.",
        "Não gostei nada, péssima qualidade e atendimento horrível.",
        "Produto bom, mas o preço é um pouco alto para o que oferece.",
        "Entrega rápida e produto conforme o anunciado. Satisfeito com a compra.",
        "Decepcionante. Quebrou após uma semana de uso. Não recomendo."
    ],
    'sentimento': [1, 0, 0.5, 0.8, 0.1]  # 0: negativo, 1: positivo
})

# Função para pré-processamento de texto
def preprocess_text(text):
    # Converter para minúsculas
    text = text.lower()
    # Remover pontuação
    text = re.sub(r'[^\w\s]', '', text)
    # Remover números
    text = re.sub(r'\d+', '', text)
    # Remover stopwords
    stop_words = set(stopwords.words('portuguese'))
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

# Aplicar pré-processamento
reviews['texto_processado'] = reviews['texto'].apply(preprocess_text)

# Feature Engineering para texto

# 1. Features básicas
reviews['contagem_palavras'] = reviews['texto'].apply(lambda x: len(x.split()))
reviews['contagem_caracteres'] = reviews['texto'].apply(len)
reviews['tamanho_medio_palavras'] = reviews['texto'].apply(lambda x: np.mean([len(word) for word in x.split()]))

# 2. Detecção de sentimentos específicos
reviews['tem_excelente'] = reviews['texto'].str.contains('excelente|ótimo|maravilhoso', case=False).astype(int)
reviews['tem_ruim'] = reviews['texto'].str.contains('ruim|péssimo|horrível|decepcionante', case=False).astype(int)
reviews['tem_recomendacao'] = reviews['texto'].str.contains('recomendo', case=False).astype(int)
reviews['tem_negacao'] = reviews['texto'].str.contains('não|nunca|nada', case=False).astype(int)

# 3. Bag of Words
count_vectorizer = CountVectorizer(max_features=20)
bow_matrix = count_vectorizer.fit_transform(reviews['texto_processado'])
bow_df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=[f'bow_{word}' for word in count_vectorizer.get_feature_names_out()]
)

# 4. TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=20)
tfidf_matrix = tfidf_vectorizer.fit_transform(reviews['texto_processado'])
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=[f'tfidf_{word}' for word in tfidf_vectorizer.get_feature_names_out()]
)

# Combinando todas as features
resultado = pd.concat([
    reviews.drop(['texto', 'texto_processado'], axis=1), 
    bow_df, 
    tfidf_df
], axis=1)

print("Features extraídas do texto:")
print(resultado.head())
```

### Exemplo 3: Feature Engineering para Dados Geoespaciais

```python
import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, asin

# Função para calcular distância entre coordenadas (Haversine)
def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula a distância em km entre dois pontos utilizando a fórmula de Haversine
    """
    # Converter graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Fórmula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Raio da Terra em quilômetros
    return c * r

# Dados fictícios de propriedades imobiliárias
imoveis = pd.DataFrame({
    'id': range(1, 101),
    'preco': np.random.normal(500000, 150000, 100),
    'area': np.random.normal(120, 50, 100),
    'quartos': np.random.choice([1, 2, 3, 4], 100),
    'lat': np.random.uniform(-23.65, -23.45, 100),  # Coordenadas para região de São Paulo
    'lon': np.random.uniform(-46.75, -46.55, 100),
})

# Pontos de interesse (POIs) fictícios
pois = pd.DataFrame({
    'nome': ['Centro', 'Parque', 'Shopping', 'Hospital', 'Estação'],
    'tipo': ['centro', 'lazer', 'comercio', 'saude', 'transporte'],
    'lat': [-23.55, -23.58, -23.51, -23.61, -23.54],
    'lon': [-46.64, -46.66, -46.68, -46.60, -46.63]
})

# Feature Engineering para dados geoespaciais

# 1. Distância para cada POI
for _, poi in pois.iterrows():
    imoveis[f'dist_{poi["nome"]}'] = imoveis.apply(
        lambda row: haversine(row['lat'], row['lon'], poi['lat'], poi['lon']),
        axis=1
    )

# 2. Distância mínima para cada tipo de POI
for tipo in pois['tipo'].unique():
    pois_tipo = pois[pois['tipo'] == tipo]
    
    # Para cada imóvel, calcular distância mínima para este tipo de POI
    def dist_min_tipo(row):
        dists = [haversine(row['lat'], row['lon'], poi_lat, poi_lon) 
                for _, _, poi_lat, poi_lon in pois_tipo[['nome', 'tipo', 'lat', 'lon']].itertuples()]
        return min(dists)
    
    imoveis[f'dist_min_{tipo}'] = imoveis.apply(dist_min_tipo, axis=1)

# 3. Contagem de POIs em um raio
raios = [1, 3, 5]  # km
for raio in raios:
    imoveis[f'pois_raio_{raio}km'] = imoveis.apply(
        lambda row: sum(1 for _, poi in pois.iterrows() 
                      if haversine(row['lat'], row['lon'], poi['lat'], poi['lon']) <= raio),
        axis=1
    )

# 4. Feature de densidade por área (preço/m²)
imoveis['preco_por_m2'] = imoveis['preco'] / imoveis['area']

# 5. Área por quarto
imoveis['area_por_quarto'] = imoveis['area'] / imoveis['quartos']

# 6. Cluster geográfico usando quartis de latitude e longitude
imoveis['lat_quartil'] = pd.qcut(imoveis['lat'], 4, labels=False)
imoveis['lon_quartil'] = pd.qcut(imoveis['lon'], 4, labels=False)
imoveis['geo_cluster'] = imoveis['lat_quartil'].astype(str) + '_' + imoveis['lon_quartil'].astype(str)

print("Features geoespaciais criadas:")
print(imoveis.head())
```

## Referências (References)

- Kuhn, M., & Johnson, K. (2019). *Feature Engineering and Selection: A Practical Approach for Predictive Models*. CRC Press.
- Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists*. O'Reilly Media.
- Guyon, I., & Elisseeff, A. (2003). *An Introduction to Variable and Feature Selection*. Journal of Machine Learning Research.
- Dong, G., & Liu, H. (2018). *Feature Engineering for Machine Learning and Data Analytics*. CRC Press.
- Domingos, P. (2012). *A Few Useful Things to Know About Machine Learning*. Communications of the ACM.
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly Media.


