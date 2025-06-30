-- sakila-practice.sql
-- Author: Tassio Luiz Dantas do Carmo
-- Description: Prática de comandos SQL com base no banco de dados Sakila.
-- Problemas baseados em exercícios de modelagem e manipulação de dados.

-- Problema 2 - Utilizando o banco de dados sakila

-- a) Calcule os valores das multas das locações na tabela payment considerando que todos estão atrasados e aplicando um percentual de 20% para todos pelo atraso.
SELECT payment_id, amount, amount * 1.2 AS TotalComMulta
FROM payment;

-- b) Listar as cidades que contêm parte do nome com a sequência de caracteres "ana".
SELECT city
FROM city
WHERE city LIKE '%ana%';

-- c) Listar os países que iniciam com "R" e terminam com "A", sem considerar maiúsculas e minúsculas.
SELECT country
FROM country
WHERE LOWER(country) LIKE 'r%a';

-- d) Listar os nomes dos filmes que fazem alguma menção ao assunto feminismo.
SELECT title
FROM film
WHERE description LIKE '%feminis%';

-- e) Listar as locações que foram feitas pelos clientes com IDs entre 100 e 300.
SELECT *
FROM rental
WHERE customer_id BETWEEN 100 AND 300;

-- f) Listar os funcionários cujas senhas registradas para utilização dos sistemas são nulas.
SELECT staff_id, first_name, last_name, password
FROM staff
WHERE password IS NULL;
