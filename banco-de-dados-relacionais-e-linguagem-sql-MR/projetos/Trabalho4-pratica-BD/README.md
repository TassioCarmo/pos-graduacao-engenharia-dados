# Trabalho Final da Unidade 4

Este documento apresenta as diretrizes, requisitos e orientações para a realização do trabalho final da Unidade 4, que tem como foco a aplicação da metodologia prática de projeto de Banco de Dados e o uso das ferramentas disponíveis.

---

## 1. Informações Gerais

- **Curso:** Engenharia de Dados  
- **Disciplina:** Bancos de Dados Relacionais  

---

## 2. Objetivos do Trabalho

O trabalho tem como objetivo a análise dos modelos e tabelas existentes nos bancos de dados restaurados nos ambientes MySQL, aplicados durante as aulas. O foco está em responder a perguntas específicas através da construção de comandos SQL, demonstrando os tempos de resposta e, quando possível, a otimização dos comandos (antes e depois das alterações).

---

## 3. Requisitos e Orientações

- **Ambiente:**  
  - Utilize os bancos de dados já restaurados nos ambientes em MySQL, conforme trabalhado durante as aulas.
  - A ferramenta para execução dos comandos é de livre escolha, podendo ser utilizada em ambiente cloud ou local.

- **Criação de Objetos:**  
  - Se necessário, a criação de novos objetos (views, índices, etc.) é permitida para facilitar a implementação ou melhorar o desempenho dos comandos.
  
- **Medição de Performance:**  
  - Demonstre para cada comando os tempos de resposta.
  - Se realizar otimizações, apresente comparativos de antes e depois da execução, mostrando as versões dos comandos e os ganhos de performance.

- **Individualidade:**  
  - O trabalho é individual. Cada aluno deverá entregar os comandos de forma autônoma, sem necessidade de revisão em conjunto com os colegas.

- **Postagem:**  
  - Realize a postagem dos comandos no item “TRABALHO FINAL DA UNIDADE 4” no Canvas.

---

## 4. Enunciado das Questões para o Schema **Employees**

### 4.1. Pergunta 1
- **Objetivo:**  
  - Apresentar a quantidade de empregados alocados por setor em cada um dos anos.
  - Separar os comandos entre funcionários **ativos** e **inativos** conforme o modelo.
- **Sugestão:**  
  - Pode-se utilizar _views_ para facilitar a visualização e a segmentação dos dados.

### 4.2. Pergunta 2
- **Objetivo:**  
  - Exibir a quantidade de cargos ocupada por cada funcionário no histórico de prestação de serviços.
- **Sugestão:**  
  - Crie um comando SQL que percorra o histórico e agrupe as informações por funcionário.

### 4.3. Pergunta 3
- **Objetivo:**  
  - Calcular a média de cargos ocupada por cada funcionário, bem como a média geral da empresa.
  - Demonstrar, em comandos separados (que podem ser _views_), quais funcionários ficaram abaixo e quais ficaram acima da média geral de cargos.
- **Sugestão:**  
  - Utilize funções agregadas para calcular as médias e condicione a apresentação dos resultados conforme o critério de comparação.

### 4.4. Pergunta 4
- **Objetivo:**  
  - Determinar a média de salários de cada departamento e a média geral da empresa.
  - Apresentar, em comandos separados (que podem ser _views_), quais departamentos ou registros ficaram acima e abaixo da média, segmentados por ano.
- **Sugestão:**  
  - Estruture os comandos para calcular as médias e, em seguida, filtre os resultados de acordo com os critérios de comparação.

---

## 5. Estrutura Recomendada para os Comandos SQL

Para cada uma das perguntas, recomenda-se a seguinte abordagem:

1. **Análise dos Dados Existentes:**  
   - Revisão dos modelos e das tabelas disponíveis para identificar os campos e relacionamentos necessários.

2. **Construção dos Comandos:**  
   - Desenvolvimento dos comandos SQL para extrair as informações solicitadas.
   - Caso necessário, criação de _views_ para facilitar a organização e reutilização dos comandos.

3. **Medição de Performance:**  
   - Execução dos comandos e registro dos tempos de resposta.
   - Caso sejam realizadas otimizações, documentar os comandos antes e depois da melhoria, demonstrando o impacto nas métricas de performance.

4. **Documentação e Comentários:**  
   - Incluir comentários nos scripts explicando a lógica e os passos realizados.
   - Organizar os comandos em seções que correspondam a cada uma das perguntas.

---

## 6. Entrega e Revisão

- **Entrega:**  
  - Realize a postagem dos comandos e da documentação no Canvas, na área destinada ao “TRABALHO FINAL DA UNIDADE 4”.

- **Revisões:**  
  - É permitida a realização de correções no modelo entregue, visando responder adequadamente às perguntas propostas.

---

## 7. Considerações Finais

Este trabalho tem o intuito de avaliar a capacidade de análise e aplicação prática dos conceitos de bancos de dados relacionais, bem como a habilidade de otimização e documentação dos processos realizados. Atenha-se às orientações e seja claro na demonstração dos resultados e das melhorias obtidas.


