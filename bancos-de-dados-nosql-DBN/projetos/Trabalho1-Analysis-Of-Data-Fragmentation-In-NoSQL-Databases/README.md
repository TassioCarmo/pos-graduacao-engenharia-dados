# Modelagem-De-Dados-Administradora-De-Imoveis

## Projeto de Modelagem de Dados

Este repositório contém os artefatos do projeto de modelagem conceitual e lógica para um banco de dados de uma administradora de imóveis. O projeto foi desenvolvido como parte da disciplina **Bancos de Dados Relacionais e Linguagem SQL**, do curso de **Engenharia de Dados**.

## Objetivo

Modelar um sistema de banco de dados que atenda aos seguintes requisitos de negócio:

- Administração de condomínios e unidades condominiais
- Gestão de contratos de aluguel
- Armazenamento de contratos de prestação de serviços
- Controle de pagamentos realizados pelos locatários

## Contexto do Problema

Com base em entrevista com o gerente da administradora, foram definidos os seguintes requisitos:

1. A administradora gerencia condomínios formados por unidades condominiais.
2. Cada unidade condominial pode pertencer a uma ou mais pessoas, e uma pessoa pode possuir várias unidades.
3. Cada unidade pode estar alugada para no máximo uma pessoa, porém uma pessoa pode alugar diversas unidades.
4. Os pagamentos são registrados a partir de arquivos de retorno do banco, contendo os campos: número da conta, valor do depósito, data de vencimento e data do depósito.
5. Os locatários podem realizar pagamentos por meio de depósito ou cheque nominal à unidade.
6. Todos os registros de pagamento são vinculados ao CPF do locatário.
7. Os contratos de prestação de serviço devem estar associados à locação correspondente e armazenados no sistema.

## Entregáveis

- Modelo Conceitual: Desenvolvido utilizando a ferramenta [BRModelo Web](https://app.brmodeloweb.com/#!/)
- Modelo Entidade-Relacionamento (ER): Desenvolvido no MySQL Workbench (.mwb)
- Scripts SQL (opcional): Representando a estrutura lógica das tabelas

## Organização do Grupo

- Cada integrante do grupo é responsável individualmente pela construção de um modelo.
- Após a modelagem individual, o grupo realiza reuniões para:
  - Discutir melhorias
  - Realizar revisões
  - Consolidar decisões

### Responsável pelo Grupo (Manager)

- Agendar reuniões
- Reportar a participação de cada integrante para fins de avaliação individual


## Observações

- Os problemas propostos são de complexidade média e baseados em situações reais.
- Algumas sugestões de entidades e atributos foram fornecidas, mas exigem análise crítica e ajustes.
- A modelagem será avaliada com base na clareza, coerência, completude e criatividade.


