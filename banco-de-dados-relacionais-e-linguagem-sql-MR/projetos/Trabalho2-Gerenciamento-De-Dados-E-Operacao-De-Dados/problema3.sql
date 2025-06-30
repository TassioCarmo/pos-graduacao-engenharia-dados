-- sakila-practice.sql
-- Author: Tassio Luiz Dantas do Carmo
-- Description: Prática de comandos SQL com base no banco de dados Sakila.
-- Problemas baseados em exercícios de modelagem e manipulação de dados.


-- Problema 3 - Utilizando o banco de dados sakila

-- Criar cópias das tabelas payment e film_actor
CREATE TABLE payment_copia LIKE payment;
CREATE TABLE film_actor_copia LIKE film_actor;

-- Inserir os dados das tabelas originais nas cópias
INSERT INTO payment_copia SELECT * FROM payment;
INSERT INTO film_actor_copia SELECT * FROM film_actor;

-- a) Alterar o valor dos aluguéis menores do que 1.99 para 19.99
SET SQL_SAFE_UPDATES = 0;

UPDATE payment_copia
SET amount = 19.99
WHERE amount < 1.99;

SET SQL_SAFE_UPDATES = 1;

-- b) Listar os valores dos aluguéis que estão entre 6.00 e 10.00
SELECT a.rental_id, a.payment_id, a.amount
FROM payment_copia a
INNER JOIN rental b ON a.rental_id = b.rental_id
WHERE a.amount BETWEEN 6 AND 10;

-- c) Listar os nomes dos filmes que contêm o ator com id 36
SELECT b.title
FROM film_actor_copia a
INNER JOIN film b ON a.film_id = b.film_id
WHERE a.actor_id = 36;

-- d) Substituir o ator com id 36 pelos registros do ator com id 44,
-- evitando duplicatas em filmes onde ambos já atuam.

-- Criar tabela temporária com filmes onde os dois atores atuam
CREATE TEMPORARY TABLE temp AS
SELECT film_id
FROM film_actor_copia
WHERE actor_id = 36
AND film_id IN (
    SELECT film_id
    FROM film_actor_copia
    WHERE actor_id = 44
);

-- Deletar os registros do ator 36 nesses filmes para evitar duplicação
DELETE FROM film_actor_copia
WHERE actor_id = 36
AND film_id IN (SELECT film_id FROM temp);

-- Atualizar os demais registros do ator 36 para o ator 44
UPDATE film_actor_copia
SET actor_id = 44
WHERE actor_id = 36;
