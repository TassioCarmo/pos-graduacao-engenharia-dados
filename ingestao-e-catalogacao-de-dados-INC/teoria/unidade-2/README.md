## Coleta de dados

* A coleta de dados é a parte das etapas dos processos ETL/ELT responsável por mapear e coletar informações utilizando algumas técnicas de extração de dados.
* Os dados coletados são armazenados num repositório com o objetivo de garantir confiabilidade, acessibilidade, disponibilidade e precisão de informações.
* Nesse cenário, devemos conhecer a origem dos dados (estão vindo de bases de dados relacionais, API's, crawlers, arquivos et.al?) para definir qual a melhor estratégia para coletar o seu conteúdo.

**Algumas das técnicas de coleta de dados são:**

* **Entrevistas**: Perguntas feitas diretamente a pessoas para obter informações detalhadas.
* **Questionários**: Formulários com perguntas estruturadas que podem ser preenchidos por respondentes.
* **Observação**: Registrar comportamentos ou fenômenos sem intervenção direta.
* **Sistemas Automatizados**: Uso de sensores ou software para captar dados automaticamente.
* **Rastreamento de Logs**: Coleta de dados sobre uso e comportamento em sistemas digitais.
  
---

## Manipulação de dados

* A manipulação de dados é a parte das etapas dos processos ETL/ELT responsável por acessar, alterar, processar, transformar ou eliminar dados para atingir um objetivo definido.
* Os dados podem ser limpos e organizados para remover informações desnecessárias/redundantes, agregados, convertidos de um formato para outro e outras operações.
* É importante ter cuidado com as transformações realizadas nos dados, uma vez que podem levar usuários e sistemas a interpretações falsas ou enganosas, causando uma série de implicações de áreas de negócio.

**Há alguns tipos de manipulações que podemos executar em dados para que ele esteja pronto para consumo, como:**

* Limpeza de dados
* Normalização/formatação de dados
* Transformação de dados

  * Codificação de caracteres
  * Delimitador
  * Tratamento de campos textuais
* Filtragem de dados
* Combinação de dados

---

### Limpeza de dados

* A limpeza de dados é o processo de identificar e corrigir (ou remover) informações incorretas, incompletas, duplicadas ou desnecessárias de um conjunto de dados.

**Algumas das técnicas aplicadas nesse tipo de manipulação são:**

* Remover registros duplicados: Se houver múltiplas entradas idênticas no conjunto de dados, é possível eliminar as cópias para evitar contagem dupla.
* Corrigir inconsistências de entrada: Se um mesmo campo tem diferentes formas de escrita ou abreviações, padronizá-las para garantir uniformidade.
* Preencher valores ausentes: Valores em branco podem ser substituídos por médias, mediana, ou valores padrão para evitar impactos negativos na análise.
* Eliminar ou corrigir erros de entrada: Pode-se ajustar erros de digitação ou corrigir dados mal formatados, como códigos postais ou números de telefone.

---

### Normalização/formatação dos dados

* A normalização envolve transformar dados brutos para que estejam em um formato consistente e padronizado.
* Isso facilita a análise e integração de diferentes fontes de dados.
* É importante conhecer o formato do dado para determinar os tipos de operações que podem ser aplicadas em seu conteúdo.

**Algumas técnicas são:**

* Unificar formatos de data: Converter todas para um único formato padrão.
* Padronizar unidades de medida: Escolher uma unidade padrão e converter os valores.
* Ajustar capitalização de texto: Uniformizar a capitalização para evitar distinções semânticas.
* Remover símbolos indesejados: Excluir ou ajustar símbolos, como vírgulas em valores numéricos.

---

### Codificação de caracteres

* A codificação de caracteres refere-se ao processo de conversão de caracteres alfabéticos, números e símbolos em uma sequência de bits que podem ser armazenados/transmitidos em sistemas computacionais.
* A codificação é necessária porque as informações armazenadas em um computador são representadas internamente em formato binário.
* Deve-se levar em consideração o alfabeto dos diversos países do mundo.

**Alguns tipos de codificação:**

* ASCII
* Unicode
* UTF-8
* ISO-8859-1

Cada encoding possui um conjunto de caracteres especiais e interpretação para o alfabeto a qual foi codificado.

---

### Encoding

**Formas de descobrir a codificação de dados:**

* Verificar a documentação dos dados
* Detecção Automática com bibliotecas (ex.: `chardet`, `ftfy`)
* Conversão e visualização manual em editores de texto (Notepad++, Sublime Text etc.)
* Ferramentas de linha de comando (`file`, `enca`) no Linux

---

### Delimitador

* Um delimitador de dados é um caractere ou conjunto de caracteres usado para separar campos em um arquivo ou texto.
* É comum em arquivos como CSV (Comma Separated Values) ou TSV (Tab Separated Values).
* A escolha do delimitador pode variar de acordo com os dados trabalhados.

**Outros delimitadores possíveis:**

* `;` (ponto e vírgula)
* `|` (pipe ou barra vertical)
* `#` (cerquilha)
* `:` (dois pontos)

**Dicas adicionais:**

* Se o dado contiver o delimitador, utilize aspas duplas (`"`) ou simples (`'`) para isolar o campo.
* Caracteres de escape (`\`) também podem ser usados.

**Como identificar delimitadores:**

* Visualizar o arquivo em um editor de texto
* Escolher delimitador menos comum no conteúdo
* Escapar delimitadores internos com aspas

---

### Tratamento de campos textuais

* O tratamento de campos textuais é o processo de ajustar e padronizar dados textuais para melhorar a consistência, precisão e usabilidade.

**Técnicas comuns:**

* Remoção de espaços em branco (`strip()`, `lstrip()`, `rstrip()`)
* Padronização de capitalização (`upper()`, `lower()`)
* Correção ortográfica e erros comuns (ex.: biblioteca `spellchecker`)
* Tokenização de texto (ex.: `split()`, `nltk`)

**Caracteres de quebra de linha:**

* `LF (\n)`: Unix/Linux
* `CR (\r)`: Antigo Mac
* `CRLF (\r\n)`: Windows

---
````markdown
## Filtragem de dados

- A filtragem de dados é o processo de selecionar apenas os registros (linhas) que atendem a determinadas condições.

**Utilidade da filtragem:**

- Isolar dados relevantes  
- Eliminar ruídos ou dados desnecessários  
- Preparar subconjuntos para análises, relatórios ou visualizações  

---

## Mecanismos de inferência e correção de tipagem de dados

- A etapa de reconhecimento das informações tem por objetivo mapear o domínio dos atributos (tipo, estrutura, nome de colunas) para determinar os tipos de operações que podem ser realizadas nos dados.  
- Algumas técnicas para reconhecer os dados podem envolver a leitura dos metadados dos arquivos (estruturas que descrevem o conteúdo de um objeto).  
- Também é possível armazenar as informações de um arquivo/tabela num catálogo de dados.  

---

## Normalização de dados

- Em geral, a normalização requer a criação de algumas tabelas (ou arquivos) adicionais e isso pode ser complicado para quem não está acostumado com visão relacional de dados.  
- Na literatura, existem conceitos de Formas Normais (FN) para tratar casos e garantir a conformidade “perfeita” dos dados:

  1. **1ª Forma Normal** – Valores atômicos  
  2. **2ª Forma Normal** – Dependência completa  
  3. **3ª Forma Normal** – Sem dependência transitiva  

### 1ª Forma Normal – Valores atômicos

- Cada célula de uma tabela deve conter um único valor, não podendo agrupar múltiplos valores em um mesmo campo.  
- Cada linha deve ter uma chave primária única e não pode haver linhas duplicadas.

**Exemplo**  
Uma tabela de clientes (nome, CPF, e-mail, endereço) em que um cliente pode ter vários telefones. Para garantir a 1ª FN, criamos:

```text
Clientes       Telefones
---------      -------------------
IdCliente      IdTelefone   Telefone
1              1            (11) 9999-0000
1              2            (11) 9888-0000
2              3            (21) 9777-0000
````

### 2ª Forma Normal – Dependência completa

* Deve atender à 1ª FN.
* Toda coluna que não faz parte da chave primária deve depender **totalmente** da chave primária, e não de parte dela.

**Exemplo**
Tabela de notas por aluno e curso:

```text
(IdAluno, IdCurso) → chave composta
- Nota           depende de (IdAluno, IdCurso)
- DescricaoCurso depende apenas de IdCurso (violação da 2ª FN)
```

### 3ª Forma Normal – Sem dependência transitiva

* Deve atender à 2ª FN.
* Não pode haver dependências transitivas entre colunas não-chave: cada coluna não-chave deve depender apenas da chave primária.

**Exemplo**
Tabela de funcionários:

```text
IdFuncionario → chave primária
- Nome
- IdCargo
- DescricaoCargo depende de IdCargo (violação da 3ª FN)
```

---

## Atualização de dados

Existem diferentes métodos para atualização de dados em sistemas analíticos:

* Atualização completa
* Atualização incremental
* Atualização por mesclagem (merge)
* SCD (Slowly Changing Dimension)
* CDC (Change Data Capture)

### Atualização completa

* Transferência de **todo** o conteúdo de dados entre sistemas, sobrescrevendo o destino.
* Indicada para migração de dados ou backup completo.
* Processo demorado e intensivo, requer planejamento para minimizar impacto.

### Atualização incremental

* Transfere apenas dados **adicionados ou modificados** desde a última carga.
* Ideal para grandes volumes, melhora a performance.

### Atualização por mesclagem (Merge)

* Combina informações de múltiplas fontes em um único conjunto.
* Atualiza registros existentes sem substituir todo o conjunto de dados.

### SCD (Slowly Changing Dimension)

Define como tratar mudanças em dimensões de Data Warehouse. Tipos comuns de SCD:

1. **Tipo 0** – Carga fria (sem mudanças)
2. **Tipo 1** – Sobrescrever valores antigos
3. **Tipo 2** – Adicionar nova linha histórica
4. **Tipo 3** – Adicionar novo campo
5. **Tipo 4** – Híbrido dos tipos 1 e 2
6. **Tipo 6** – Combinação dos anteriores

### Change Data Capture (CDC)

Técnica para identificar e capturar mudanças em tempo real. Três abordagens principais:

#### CDC Log-Based

* Captura mudanças a partir dos **logs de transação** do banco de dados.
* Registra eventos de inserção, atualização e remoção em ordem cronológica.

#### CDC Trigger-Based

* Usa **triggers** definidos no SGBD para registrar alterações em tabelas de captura (inserted/deleted).
* Permite diferenciar valores antigos e novos durante a modificação.

#### CDC Query-Based

* Executa **consultas periódicas** para detectar registros alterados desde a última execução.
* Extrai apenas as linhas modificadas para processamento posterior.

```
