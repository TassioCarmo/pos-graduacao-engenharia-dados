-- 1 – Quantidade de empregados alocados por setor em cada um dos anos, separando em dois
comandos diferentes, que podem ser views, funcionários ativos e inativos conforme o modelo.
*/

select b.ano, dept_no, count(a.emp_no) qtde_func_alocado
from dept_emp a
left join ( -- para o funcionario ser alocado ele precisa ser cadastrado no setor naquele ano
    SELECT DISTINCT YEAR(FROM_DATE) ano FROM dept_emp
) b
on YEAR(a.FROM_DATE) = b.ano
group by b.ano, a.dept_no
order by b.ano;

/**
2 – Quantidade de cargos ocupada por cada funcionário no histórico de prestação de serviços
de cada um deles na empresa.
*/

select emp_no, count(distinct title) qte_cargos
from titles
group by emp_no;
/**

3 – Média de cargos ocupada por cada funcionário e geral da empresa demonstrado, em
comandos separados, que podem ser views, quais deles ficaram abaixo da média geral de cargos
e quais ficaram acima da média geral de cargos.*/

WITH media_geral AS (
    SELECT AVG(qte_cargos) as media_geral
    FROM (
        select emp_no, count(title) qte_cargos
        from titles
        group by emp_no
    ) as counts
)

SELECT
    emp_no,
    count(title) qte_cargos,
    CASE
        WHEN COUNT(title) > (SELECT media_geral FROM media_geral)
            THEN 'Acima da média'
        ELSE 'Abaixo da média'
    END as comparacao
from titles
group by emp_no;



/**
4 – Qual a média de salários de cada departamento e a média geral da empresa demonstrando
em comandos separados, que podem ser views, quais focaram acima e abaixo da média por
ano**/


-- Criando uma view com os funcionários ativos
create view func_ativos as
select * from dept_emp
where to_date = '9999-01-01';

-- Selecionando a média de salário por departamento
select a.dept_no, avg(b.salary) media_salario
from func_ativos a
inner join salaries b
on a.emp_no = b.emp_no
    and b.to_date = '9999-01-01'  -- salário atual
group by a.dept_no

union all

-- Selecionando a média de salário geral de todos os departamentos
select 'todos departamentos', avg(b.salary) media_salario
from func_ativos a
inner join salaries b
on a.emp_no = b.emp_no
    and b.to_date = '9999-01-01';  -- salário atual


