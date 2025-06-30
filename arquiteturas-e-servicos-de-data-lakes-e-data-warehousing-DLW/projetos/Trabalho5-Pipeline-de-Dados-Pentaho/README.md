# Trabalho Prático - Pipeline de Dados com Pentaho

Este repositório contém os arquivos e instruções para o trabalho prático em grupo sobre a criação de um pipeline de dados utilizando o Pentaho Data Integration (PDI).

## Objetivos

O objetivo principal deste trabalho é desenvolver um processo simplificado de ETL (Extração, Transformação e Carga) utilizando o Pentaho PDI, a partir de arquivos CSV como fonte de dados.

## Requisitos

### Ferramentas Necessárias
- Pentaho Data Integration (PDI/Kettle)
- MySQL ou outro SGBD relacional de sua preferência
- Arquivos CSV de origem (fornecidos separadamente)

## Descrição do Projeto

O projeto consiste em modelar um Data Warehouse (DW) a partir de dados contidos em arquivos CSV. Será necessário criar e executar um pipeline de dados completo que abrange todas as etapas do processo ETL:

1. **Extração**: Leitura dos arquivos CSV de origem
2. **Transformação**: Limpeza, formatação e adequação dos dados
3. **Carga**: Carregamento dos dados transformados no Data Warehouse

## Etapas do Desenvolvimento

### 1. Configuração do Ambiente

#### Instalação do Pentaho PDI
1. Baixe a versão mais recente do Pentaho Data Integration
2. Descompacte o arquivo em uma pasta de sua preferência
3. Execute o arquivo `spoon.bat` (Windows) ou `spoon.sh` (Linux/Mac)

#### Configuração do Banco de Dados
1. Instale o MySQL (ou SGBD de sua preferência)
2. Crie um banco de dados para o Data Warehouse
3. Configure as credenciais de acesso

### 2. Análise dos Dados de Origem
1. Estude a estrutura dos arquivos CSV fornecidos
2. Identifique campos, tipos de dados e relacionamentos
3. Planeje a modelagem dimensional do DW

### 3. Modelagem do Data Warehouse
1. Defina as tabelas de dimensão e fato
2. Estabeleça os relacionamentos entre as tabelas
3. Crie o esquema do banco de dados

### 4. Desenvolvimento do Pipeline ETL

#### Extração
1. Configure os steps de entrada para ler os arquivos CSV
2. Valide os dados extraídos

#### Transformação
1. Aplique transformações para limpeza de dados
2. Realize conversões de tipos quando necessário
3. Implemente regras de negócio
4. Crie chaves surrogate para as dimensões

#### Carga
1. Configure os steps de saída para carregar os dados nas tabelas do DW
2. Implemente estratégias de carga (full load, incremental)
3. Valide a integridade dos dados carregados

### 5. Teste e Validação
1. Execute o pipeline completo
2. Verifique os resultados no banco de dados
3. Identifique e corrija possíveis problemas



## Boas Práticas

- Utilize nomes descritivos para os steps
- Documente as transformações realizadas
- Implemente tratamento de erros
- Crie logs para monitoramento
- Organize as transformações em módulos lógicos
- Utilize parâmetros para valores dinâmicos

## Entrega

A entrega deve ser feita enviando um arquivo compactado contendo:
- Todos os arquivos de transformação (.ktr)
- Arquivos de job (.kjb), se utilizados
- Scripts SQL para criação do esquema do banco de dados (opcional)
- Documentação adicional, se necessário

## Avaliação

O trabalho será avaliado considerando:
- Funcionamento correto do pipeline ETL
- Modelagem adequada do Data Warehouse
- Qualidade e organização do código
- Implementação das melhores práticas de ETL
- Trabalho em equipe e divisão de tarefas

## Recursos Adicionais

- [Documentação oficial do Pentaho Data Integration](https://help.pentaho.com/Documentation/9.0/Products/Data_Integration)
- [Tutoriais sobre modelagem dimensional](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/)
- [Fórum da comunidade Pentaho](https://forums.pentaho.com/)

---

**Observação**: Este trabalho deve ser realizado em grupo, conforme especificado pelo professor. Organize-se com sua equipe para distribuir as tarefas e garantir a entrega de um pipeline completo e funcional.

