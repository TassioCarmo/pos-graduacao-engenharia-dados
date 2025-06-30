# Trabalho Final da Unidade 3: COMANDOS DML

**Curso:** Arquitetura de Dados  
**Disciplina:** Modelagem e Organização de Dados  
**Professor:** Augusto Zadra  
**Forma de Entrega:** Postagem individual no ambiente CANVAS

## Objetivo

O presente trabalho tem como finalidade a aplicação prática dos conceitos de manipulação de dados por meio da linguagem SQL, com foco em comandos DML (Data Manipulation Language). O aluno deverá desenvolver consultas que respondam às perguntas propostas com base no modelo de dados previamente elaborado pelo grupo. No entanto, a entrega é individual e podem ser realizadas alterações no modelo original, caso necessário, para atender às exigências do problema.

## Instruções

- Cada aluno deve entregar seu próprio arquivo `.sql`, contendo todos os comandos necessários para responder às perguntas listadas no Problema 7.
- A entrega deve ser feita de forma individual por meio do ambiente CANVAS, dentro do prazo estabelecido.
- Correções no modelo de dados são permitidas, desde que viabilizem as consultas solicitadas.

## Problema 7 – Perguntas Respondidas

1. **Quantos proprietários condominiais são adimplentes**  
   Consulta que retorna os nomes dos proprietários que possuem registros de pagamento de taxa condominial (campo `data_pagamento` não nulo).

2. **Quantos imóveis temos por bairro e por cidade**  
   Consulta que realiza a contagem de imóveis agrupados por `cidade` e `bairro`.

3. **Qual a quantidade de locatários de imóveis**  
   Consulta que retorna os nomes distintos de todos os locatários cadastrados no banco de dados.

4. **Qual o valor médio dos imóveis por região**  
   Consulta que calcula a média dos valores dos imóveis, agrupados por cidade e bairro.

5. **Qual o maior valor de aluguel pago em um ano**  
   Consulta que retorna o maior valor de depósito registrado a partir do ano de 2024, considerando os registros de pagamento de aluguel.

## Estrutura do Arquivo Entregue

O arquivo `.sql` enviado contém:

- Comentários explicativos antes de cada consulta, indicando qual questão está sendo respondida;
- Consultas organizadas em sequência, conforme a numeração das perguntas;
- Utilização de aliases e boas práticas de legibilidade.

## Observações Finais

- Todos os comandos foram testados no ambiente MySQL e produzem os resultados esperados com base no modelo de dados utilizado.
- O foco principal foi garantir que as consultas estejam corretas, legíveis e alinhadas às perguntas do enunciado.
- O modelo de dados utilizado foi ajustado, se necessário, para garantir que os dados pudessem responder adequadamente às questões propostas.

---
