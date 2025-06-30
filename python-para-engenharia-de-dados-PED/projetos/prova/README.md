---

# Prova de Python – Análise de Dados e Visualização Gráfica

Este repositório contém a resolução de questões de uma prova da disciplina de Python, com foco em análise de dados utilizando `pandas` e visualização de dados com `matplotlib`.

Cada questão aborda um problema prático envolvendo manipulação de dados, geração de estatísticas e construção de gráficos com base nos dados apresentados.

---

## Tecnologias utilizadas

- Python 3.x  
- pandas  
- matplotlib  
- openpyxl (para exportação de arquivos `.xlsx`)  
- json (biblioteca padrão)

---

## Conteúdo das questões

### Questão 1 – Análise de vendas de produtos

Calcular o faturamento total por produto a partir de um DataFrame contendo informações de quantidade, preço e data de venda. O resultado deve ser exibido em um gráfico de barras.

### Questão 2 – Análise de presença de alunos

A partir de um dicionário de presenças (valores 0 ou 1), calcular o percentual de presença de cada aluno e exibir os resultados em um gráfico de pizza.

### Questão 3 – Análise de média por categoria

Calcular a média de avaliações de desempenho de funcionários por departamento e exibir os dados em um gráfico de barras horizontais.

### Questão 4 – Análise temporal de produção

Plotar um gráfico de linha representando a evolução da produção mensal de uma fábrica. O gráfico deve conter título e rótulos nos eixos.

### Questão 5 – Correlação entre variáveis

A partir de um DataFrame contendo horas de estudo e notas de estudantes, calcular a correlação entre essas variáveis e visualizar os dados com um gráfico de dispersão.

### Questão 6 – Gráfico de popularidade de filmes

Utilizar um dicionário com as pontuações médias por gênero e ano para construir um gráfico de linha para cada gênero, comparando a evolução das notas ao longo dos anos. Cada linha deve ter uma cor e estilo distintos, acompanhados de legenda.

### Questão 7 – Análise de vendas em regiões

A partir de um dicionário com valores de vendas por região e categoria, criar um gráfico de barras agrupadas exibindo as comparações entre categorias em cada região. O gráfico deve conter rótulos no eixo X e legenda.

### Questão 8 – Visualização de dados de sensores

Gerar gráficos de linha para leituras de sensores ao longo do dia. Deve-se também utilizar a função `fill_between` para representar graficamente o intervalo entre os valores máximos e mínimos registrados em cada horário.

### Questão 9 – Dados do Censo IBGE 2022

A partir dos dados públicos do Censo Demográfico 2022 (IBGE), desenvolver um programa em Python que:

- (a) Identifique os 10 municípios com maior índice de envelhecimento.
- (b) Identifique os 10 municípios com menor índice de envelhecimento.

Os resultados devem ser exportados nos formatos `.xlsx` e `.json`.

Fonte dos dados:  
https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-2022.html?edicao=38166&t=resultados


---

## Instalação de dependências

Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install pandas matplotlib openpyxl
```

---

## Execução

Execute cada script individualmente com o Python:

```bash
python questoes/questao_1_vendas.py
```

