# Data Wrangling com Linguagem R

Este repositório contém um exercício prático focado em técnicas de Data Wrangling utilizando a linguagem R para transformar e manipular dados do IBGE.

## Objetivos

Executar uma prática em R para avaliar as técnicas de Data Wrangler. Data wrangling é o processo de transformar e manipular dados brutos (raw data) para outro formato com o intuito de melhorar a visibilidade da informação. Com esse processo é possível construir gráficos, aplicar funções estatísticas, entre outros.

## Enunciado

Através do pacote `sidrar`, vamos utilizar a linguagem R para coletar dados da base de dados do IBGE. Esse pacote é essencial para quem precisa trabalhar com dados e pesquisas da instituição, tais como:
- PNAD Contínua
- PME
- PMC
- Contas Nacionais

Vamos coletar dados à partir de "2020-01-01" referentes a ocupados/desocupados na força de trabalho e aplicar técnicas de Data Wrangling.

## Pacote dplyr e suas Funções Principais

Em R, o pacote `dplyr` contém funções (também chamadas de verbs) que facilitam o processo de data wrangling, permitindo transformações em dataframes:

* **arrange()** - ordena as linhas em ordem ascendente ou descendente
* **filter()** - filtra as linhas de um data frame de acordo com alguma condição informada
* **group_by()** - agrupa as linhas. É utilizado em conjunto com summarize() para calcular estatísticas por grupo
* **mutate()** - utiliza colunas existentes do data frame para criar novas colunas
* **recode()** - permite alterar o nome das observações de uma coluna
* **select()** - seleciona as colunas especificadas e permite alterar seus nomes
* **summarize()** - sumariza uma ou mais colunas, calculando estatísticas por meio do agrupamento (group_by)

## Ambiente de Desenvolvimento

### Requisitos
- R versão 4.1 ou superior
- RStudio Cloud (ou RStudio Desktop)

### Configuração do RStudio Cloud
1. Acesse https://rstudio.cloud/
2. Crie uma conta gratuita
3. Clique em "New Project" e escolha "New RStudio Project"
4. A interface será criada conforme a imagem abaixo
   ![Interface RStudio Cloud](https://exemplo.com/rstudio_interface.png)

## Atividades Realizadas

### Código
O código para este exercício está disponível em: [Google Drive](https://drive.google.com/drive/folders/15aDvao85AKxiS2wsjC6AJFzC9uq27Ex2?usp=sharing)

### Descrição das Funções Aplicadas

#### 1. select()
Foram selecionadas as colunas necessárias e renomeadas:
- 'Trimestre Móvel (Código)' → `date`
- 'Condição em relação à força de trabalho e condição de ocupação' → `variable`
- 'Valor' → `value`

#### 2. mutate()
Realizou as seguintes transformações:
- `date`: Converteu o formato de data de YYYYMM para YYYY-MM-DD
- `variable`: Renomeou os valores presentes na coluna
- `value`: Converteu os valores para milhões de pessoas

#### 3. filter()
Filtrou os dados para datas posteriores a "2020-01-01"

#### 4. group_by()
Agrupou os dados por `date` e `variable`, preparando para operações de agregação

#### 5. summarize()
Somou os valores considerando o agrupamento realizado, permitindo:
- Soma dos valores por mês
- Cálculo da média anual dos valores somados

## Resultados

### Gráficos Gerados

Os gráficos gerados a partir dos dados processados mostram a evolução da força de trabalho (ocupados/desocupados) ao longo do tempo.

![Gráfico de Força de Trabalho](https://exemplo.com/grafico_forca_trabalho.png)
![Gráfico de Média Anual](https://exemplo.com/grafico_media_anual.png)

## Conclusão

Este exercício demonstra a eficácia das técnicas de Data Wrangling na transformação de dados brutos do IBGE em informações visuais e estruturadas, facilitando análises estatísticas e compreensão de tendências no mercado de trabalho brasileiro.

## Referências

- Documentação do pacote sidrar: [CRAN - sidrar](https://cran.r-project.org/web/packages/sidrar/index.html)
- Documentação do pacote dplyr: [dplyr - A Grammar of Data Manipulation](https://dplyr.tidyverse.org/)
- IBGE: [Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/)
