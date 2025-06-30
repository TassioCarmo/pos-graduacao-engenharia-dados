# Exercício de ETL com Pentaho Data Integration

Este repositório contém arquivos e instruções para um exercício de ETL (Extração, Transformação e Carga) utilizando o Pentaho PDI (Pentaho Data Integration), também conhecido como Kettle.

## Objetivos

Este exercício visa desenvolver habilidades nos seguintes conceitos:
- ETL (Extract, Transform, Load)
- Ferramentas ETL – Pentaho PDI e Apache Hop
- Processos de carga
- Orquestração de fluxos de dados

## Descrição do Projeto

O projeto utiliza dados da avaliação da Pós-Graduação Stricto Sensu realizada pela CAPES, que tem como objetivo:
- Certificar a qualidade da pós-graduação brasileira
- Identificar assimetrias regionais e áreas estratégicas do conhecimento
- Fortalecer as bases científica, tecnológica e de inovação

A avaliação é orientada pela Diretoria de Avaliação/CAPES com participação da comunidade acadêmico-científica através de consultores ad hoc.

## Arquivos de Entrada

Serão utilizados dois arquivos de entrada contendo dados da CAPES sobre a avaliação da Pós-Graduação Stricto Sensu. Estes arquivos servirão como fonte de dados para as transformações no Pentaho PDI.

## Objetivo Final

Construir uma transformação que alimentará uma tabela Dimensão chamada "Dim-Produção".

## Configuração do Ambiente

### Requisitos

- Pentaho Data Integration (PDI) instalado
- Arquivos de entrada da CAPES (disponibilizados separadamente)
- Conhecimentos básicos em ETL e modelagem dimensional

### Instalação do Pentaho Data Integration

1. Baixe o Pentaho PDI do site oficial ou do repositório do curso
2. Descompacte o arquivo em uma pasta de sua preferência
3. Execute o arquivo `spoon.bat` (Windows) ou `spoon.sh` (Linux/Mac)

## Passos para a Transformação

1. **Extração dos Dados**
   - Configurar os steps de entrada para ler os dois arquivos da CAPES
   - Validar os dados de entrada

2. **Transformação dos Dados**
   - Limpar e formatar os dados conforme necessário
   - Aplicar transformações específicas para adequação ao modelo dimensional
   - Realizar junções (joins) entre os dois conjuntos de dados quando necessário

3. **Carga dos Dados**
   - Configurar o step de saída para alimentar a tabela "Dim-Produção"
   - Validar a integridade dos dados carregados

## Estrutura da Transformação

A transformação deverá seguir a estrutura básica:
1. Input Steps (Leitura dos arquivos)
2. Transformation Steps (Manipulação dos dados)
3. Output Steps (Escrita na tabela dimensional)

## Boas Práticas

- Utilizar nomes descritivos para os steps
- Documentar as transformações realizadas
- Implementar validações de dados
- Tratar possíveis erros e exceções
- Criar logs para monitoramento

## Entrega

A entrega deve ser feita enviando um arquivo compactado contendo:
- Arquivos de transformação (.ktr)
- Documentação adicional, se necessário

## Avaliação

O exercício será avaliado considerando:
- Funcionamento correto da transformação
- Aplicação adequada dos conceitos de ETL
- Qualidade e organização do código
- Cumprimento dos requisitos especificados

## Ferramentas Alternativas

Embora o foco seja o Pentaho PDI, também é mencionado o Apache Hop como alternativa. O Apache Hop é o sucessor espiritual do Pentaho PDI, desenvolvido por parte da equipe original do Kettle.

## Referências

- Documentação oficial do Pentaho Data Integration
- Material sobre modelagem dimensional
- Documentação da CAPES sobre avaliação da Pós-Graduação

