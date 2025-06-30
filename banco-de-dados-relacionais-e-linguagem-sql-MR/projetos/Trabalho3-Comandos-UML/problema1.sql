-- 1- Quantos proprietários condominiais são adimplentes
SELECT DISTINCT pe.nome
FROM mydb.proprietarios_unidadesCondominais a
LEFT JOIN mydb.proprietarios p ON p.idProprietarios = a.proprietarios_idProprietarios
LEFT JOIN mydb.pessoa pe ON pe.idPessoa = p.pessoas_idPessoa
LEFT JOIN mydb.unidades_condominiais b ON b.idUnidadesCondominais = a.unidades_condominiais_idUnidadesCondominais
LEFT JOIN mydb.registros_pagamentos_taxa_condominio c 
  ON c.unidades_condominiais_idUnidadesCondominais = b.idUnidadesCondominais
WHERE c.data_pagamento IS NOT NULL;

-- 2- Quantos imóveis temos por bairro e por cidade
SELECT cidade, bairro, COUNT(1) AS quantidade
FROM mydb.unidades_condominiais
GROUP BY cidade, bairro;

-- 3- Qual a quantidade de locatários de imóveis
SELECT DISTINCT nome
FROM mydb.locatario l
LEFT JOIN mydb.pessoa pe ON pe.idPessoa = l.pessoas_idPessoa;

-- 4- Qual o valor médio dos imóveis por região
SELECT cidade, bairro, AVG(valor_imovel) AS media_valor_imovel
FROM mydb.unidades_condominiais
GROUP BY cidade, bairro;

-- 5- Qual o maior valor de aluguel pago em um ano
SELECT MAX(valor_deposito) AS maior_valor_deposito
FROM mydb.registros_pagamentos_aluguel
WHERE YEAR(data_pagamento) >= 2024;

