-- sakila-practice.sql
-- Author: Tassio Luiz Dantas do Carmo
-- Description: Prática de comandos SQL com base no banco de dados Sakila.
-- Problemas baseados em exercícios de modelagem e manipulação de dados.

-- Problema 1 - Utilizando o banco de dados Sakila
-- Corrigir e executar os comandos com erro

-- a) Erro: uso incorreto de nomes de colunas e tabela
-- Comando com erro:
-- SELECT category id FROM film category;
-- Correto:
SELECT category_id FROM film_category;

-- b) Erro: nome incorreto de tabela e coluna
-- Comando com erro:
-- SELECT payment_id, rentalid, amount, payment_date FROM amount;
-- Correto:
SELECT payment_id, rental_id, amount, payment_date FROM payment;

-- c) Erro: uso incorreto de BETWEEN para múltiplos valores
-- Comando com erro:
-- SELECT * FROM address WHERE district BETWEEN ('Georgia', 'Tete', 'Gois') AND ('Georgia', 'Tete', 'Gois');
-- Correto:
SELECT * FROM address WHERE district IN ('Georgia', 'Tete', 'Gois');

-- d) Erro: coluna que não existe na tabela actor (address_id) e erro no nome da coluna 'first name'
-- Comando com erro:
-- SELECT address_id, last_name FROM actor WHERE first name like 'J%';
-- Correto (exibindo os atores com nomes começando com J):
SELECT last_name FROM actor WHERE first_name LIKE 'J%';
