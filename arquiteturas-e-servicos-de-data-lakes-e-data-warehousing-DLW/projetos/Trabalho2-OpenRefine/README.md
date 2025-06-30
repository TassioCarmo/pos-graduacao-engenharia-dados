# Exercício de Data Wrangling com OpenRefine

Este repositório contém instruções para realizar um exercício prático utilizando o OpenRefine para técnicas de Data Wrangling (limpeza e transformação de dados).

## Visão Geral

O Data Wrangling é o processo de transformar e manipular dados brutos para melhorar a visibilidade da informação, possibilitando a construção de gráficos, aplicação de funções estatísticas e outras análises.

## Sobre o OpenRefine

O OpenRefine é uma aplicação desktop de código aberto para limpeza e transformação de dados. Principais características:

- Similar a aplicativos de planilha, mas funciona mais como um banco de dados
- Trabalha com linhas de dados que possuem células em colunas
- Opera em todas as linhas visíveis simultaneamente
- Armazena ações executadas no projeto, permitindo replicá-las em outros conjuntos de dados
- Suporta expressões em GREL (General Refine Expression Language), Python (Jython) e Clojure
- Funciona como um aplicativo web local (inicia um servidor web em 127.0.0.1:3333)

## Requisitos

- [OpenRefine](https://openrefine.org/)
- Arquivo de dados: aeronave.csv

## Instalação do OpenRefine

### Windows
1. Baixe o arquivo zip do [link fornecido](https://drive.google.com/drive/folders/1QYnIKMZ4lPAqMY7C36yGflK8rOJxsxo9)
2. Descompacte o arquivo em uma pasta
3. Execute o arquivo `openrefine.exe` ou `refine.bat` se a primeira opção não funcionar
4. Requer Java instalado no computador


## Instruções do Exercício

### 1. Criar o Projeto
- Abra o OpenRefine
- Crie um novo projeto selecionando o arquivo "aeronave.csv"
- Clique em "Next" para carregar os dados
- Clique em "Create Project" no canto superior direito

### 2. Concatenar Colunas
- Clique em tipo_veiculo > Edit column > Add column based on this column
- Nomeie a nova coluna como "veiculo"
- No campo Expression, insira:
  ```
  value + " " + cells["fabricante"].value + " " + cells["modelo"].value + " " + cells["motor_tipo"].value + " " + cells["motor_quantidade"].value
  ```

### 3. Substituir Valores
- Clique em operador_categoria > Replace
- Substitua "***" por "indefinido"

### 4. Transformar para Maiúsculas
- Clique em operador_categoria > Edit Cells > Common transforms > To uppercase

### 5. Ordenar Dados
- Ordene o campo id_ocorrencia_a de forma ascendente

### 6. Exportar Dados
- Exporte os dados transformados para um arquivo CSV

## Entrega do Trabalho
- Como evidência da execução do trabalho, envie o arquivo CSV gerado

## Referências
- [Site Oficial do OpenRefine](https://openrefine.org/)