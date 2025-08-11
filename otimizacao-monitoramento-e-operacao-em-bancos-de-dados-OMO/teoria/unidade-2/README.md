
## A IMPORTÂNCIA DO PROJETO OU DESIGN

### A MOVIMENTAÇÃO DOS DADOS

- A movimentação de dados do disco para o SGBD e dele para o aplicativo envolve os componentes mais lentos da infraestrutura do aplicativo – as unidades de disco e a rede.
- Passa a ser fundamental que o código do aplicativo que interage com o banco de dados e o próprio banco de dados seja ajustado para desempenho premium.

---

## TIPOS DE BANCO E OS CURSORES

### A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE

- **O que me indica uma melhor escolha do tipo de banco de dados que irei utilizar?**
  - A funcionalidade básica que irá atender ao negócio.
  - O momento da operação não é um bom momento para tentar fazer *tunning* de banco de dados para resolver um problema que não é do especialista em resolver.
  - Mais que isto, temos os recursos ofertados que podem não atender ao requisito do negócio.
  - É importante conhecer as principais funções de cada tipo para não perder tempo na operação!

#### Tipos de Banco de Dados

- **Banco de dados Relacional**:  
  Armazena dados em colunas com a sua descrição nas linhas e atributos; segue regras de normalização de dados que remetem a relacionamentos.

- **Banco de dados Não-Relacional**:  
  Recomendado para dados não estruturados como vídeos, imagens e/ou gráficos, que não podem ser dispostos em tabelas; não é necessário o uso de um sistema de relacionamento.

- **Banco de dados Orientado a Objetos**:  
  A estrutura do banco de dados é voltada para objetos; as informações são dispostas em blocos e têm identificadores.

- **Banco de dados Distribuído**:  
  Cada um dos nós representa um computador, que está em local físico diferente (ou não); são conectados pela Internet e compartilham dados.

- **Banco de dados Gráfico**:  
  As estruturas complexas são armazenadas e as informações ficam interligadas por grafos de conexão; a informação importa mais que a própria estrutura.

- **Banco de dados em Modelo de Rede**:  
  Trabalham com uma estrutura de lista invertida que contém arquivos, registros e campos; não segue e nem exige regras de normalização.

- **Banco de dados em Cloud**:  
  Precisamos do acesso à Internet para acessar os dados; há uma mudança arquitetural enorme, pois os dados ficam no provedor e são gerenciados por ele.

---

### O QUE SÃO CURSORES

- **Cursor** é um recurso importante oferecido pelo SGBD.
- **Na prática**: cursores são áreas de memória que armazenam o resultado de uma consulta.
- Podem ser:
  - **Implícitos**: quando não precisam ser declarados no código.
  - **Explícitos**: quando precisam ser descritos no código.
- Os cursores somente leitura ajudam os usuários a navegar pelo conjunto de resultados.
- Os cursores de leitura/gravação podem implementar atualizações de linha individuais.
- Os cursores devem ser uma das últimas técnicas escolhidas para recuperar os dados.
- Você deve escolher o cursor com o impacto mais baixo possível.
- A utilização de cursores nem sempre é uma boa alternativa, principalmente em aplicações que precisam de atualização em tempo real ou que possuem muita concorrência.




> O cálculo completo pode ser algo como:  
> `OP = (x - (bi1 / 2) + (r / 2)) = 3 + (4 / 2) + (3.000 / 2) = 3 + 2 + 1.500`

---

## OTIMIZAÇÃO DE CONSULTAS

### Considerações gerais

- Otimização = **melhor maneira de recuperar dados** em um SGBD.
- Foco em **redução de tempo e recursos**.
- Melhora:
  - Concorrência
  - Custos de infraestrutura
  - Confiabilidade e escalabilidade
  - Decisões sobre particionamento, *clustering*, carga, etc.
  - Pode justificar uso de SSDs ou bancos em memória

---

### Como começar?

- **Plano de execução**: conjunto de etapas usadas pelo otimizador.
- Um plano mal projetado causa lentidão.

---

### Fatores considerados no plano de execução

- Tamanho das tabelas, número de índices, bloqueios, uso de CPU/memória
- Métricas usadas no cálculo de custo
- Monitoramento em tempo real alimenta o otimizador

---

### Estatísticas de banco de dados

- **Estatísticas** alimentam o otimizador com *meta-dados*.
- Incluem histogramas que mostram distribuição de valores.

---

### A parte sobre o histograma

- **Histograma**: distribuição de frequências.
- Resume dados e permite comparação visual.
- Usado em tempo real pelo otimizador de queries.

---

## TUNNING DOS AMBIENTES DE SGBD

### Gargalos de sistema

- Localizar gargalos (funções ou componentes que limitam o desempenho).
- Exemplo: função que consome 80% do tempo; melhorá-la em 50% impacta 40% do total.
- **Atenção**: resolver um gargalo pode revelar outro — processo contínuo.

---

### O desempenho do banco de dados

- Envolve múltiplos componentes além do SGBD:
  - Entrada de processos
  - Leitura de disco
  - Ciclos de CPU
  - Controle de concorrência
- Tudo somado define o tempo de resposta das transações.

---

### Parâmetros ajustáveis

O DBA pode atuar em três níveis:

1. **Hardware**:
   - Discos, memória, buffers
2. **Parâmetros do SGBD**:
   - Específicos por fornecedor
3. **Esquemas e transações**:
   - Criação de índices, ajustes no projeto

> O ajuste ideal depende da combinação dos três níveis.

---

### Aplicação da heurística na otimização

- Atua na **álgebra relacional**.
- Gera plano mais eficiente **sem uso de estatísticas**.
- Utiliza **regras de equivalência** para transformar árvores ou grafos de consultas.

---

### Principais regras da heurística

- Executar seleções e projeções primeiro.
- Junções apenas depois dessas operações.
- Projetar apenas os atributos necessários.
- Evitar múltiplas tabelas intermediárias.

---

# Dicas

- Nunca mude mais um parâmetro ao mesmo tempo!
- Verifique se as áreas de paginação e SWAP estão de acordo com a realidade do banco de dados.
- Fique atento também ao espaço em disco pois ele pode ser utilizado por completo não existindo assim espaço para execução de um processo do banco de dados.
- ATUALIZE AS ESTATÍSTICAS
