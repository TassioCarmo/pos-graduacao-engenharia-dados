# BANCO DE DADOS CASSANDRA

• O Apache Cassandra é um sistema de armazenamento de dados distribuído gratuito e de código aberto que difere bastante dos sistemas de gerenciamento de banco de dados relacional.

## CASSANDRA CARACTERÍSTICAS PRINCIAPAIS
1. ESCALÁVEL
2. DESCENTRALIZADO
3. SIMÉTRICO: NÃO HÁ UM ÚNICO PONTO DE FALHA
4. LINGUAGEM DE PROGRAMAÇÃO PARA INTERAÇÃO CQL
5. SUPOTA ALTOS VOLUMES DE DADOS
6. SUPORTA ARMAZENAMENTO ELÁSTICO
7. ESCRITO EM LINGUAGEM JAVA
8. TEM CONECTORES PARA UMA DIVERSIDADE DELINGUAGENS C#, Phyton, PHP, Ruby e Go

• Dentre as classificações que vimos dos tipos de bancos NoSQL o Cassandra é se enquadra nos bancos de dados orientado a linhas.
• O Design de distribuição foi baseado no Dynamo da Amazon e seu modelo de dados no Bigtable do Google, com uma linguagem de consulta semelhante ao SQL.
• É uma tecnologia que nasceu para ser distribuída então faz pouco sentido utilizá-lo em um só nó.
• Ao contrário de outros bancos com Oracle e BigTable, os nós não são réplicas (modelo master/slave por exemplo) todos são idênticos (simetria do servidor).
• Dentre as classificações que vimos dos tipos de bancos NoSQL o Cassandra é se enquadra nos bancos de dados orientado a linhas.
• O Design de distribuição foi baseado no Dynamo da Amazon e seu modelo de dados no Bigtable do Google, com uma linguagem de consulta semelhante ao SQL.
• É uma tecnologia que nasceu para ser distribuída então faz pouco sentido utilizá-lo em um só nó.
• Ao contrário de outros bancos com Oracle e BigTable, os nós não são réplicas (modelo master/slave por exemplo) todos são idênticos (simetria do servidor).
Em comparação com o MongoDB, que implementa o modelo master/slave para distribuição dos dados o Cassandra tem duas vantagens principais:
1.É mais simples do que as configurações de replicação;
2.Tem uma disponibilidade maior com a garantia de menos interrupções.

### ESCALABILIDADE ELASTICA

### CASSANDRA MODELOS DE CONSISTÊNCIA

# MODELO DE DADOS

• O modelo de dados de Cassandra pode ser descrito como um armazenamento de linha particionado, no qual os dados são armazenados em tabelas de hash multidimensionais esparsas.
• Nesta forma de funcionamento para qualquer linha, você pode ter uma ou mais colunas, mas cada linha não precisa ter todas as mesmas colunas que outras linhas semelhantes.
• Particionado significa que cada linha tem uma chave de partição exclusiva usada para distribuir as linhas em vários armazenamentos de dados.
• Frequentemente você irá ouvir que o Cassandra é um banco de dados colunar ou orientado a colunas, mas isso não é tecnicamente correto.
• A orientação a colunas se deve ao fato de os dados estarem armazenados por colunas, ao contrário dos bancos de dados relacionais, que armazenam dados em linhas (daí o termo orientado a linhas).
• O Cassandra armazena dados em uma tabela de hash multidimensional e classificada e como os dados são armazenados em cada coluna, eles são armazenados como uma entrada separada na tabela de hash

### CASSANDRA Aplicações práticas

• Muitas das primeiras implantações de produção do Cassandra envolviam o armazenamento de atualizações de atividade do usuário, uso de redes sociais, recomendações/revisões e estatísticas de aplicativos.
• Um dos principais recursos do Cassandra é a capacidade de lidar com cargas de trabalho de aplicativos que exigem alto desempenho em volumes de gravação significativos com muitos encadeamentos de clientes simultâneos.
• Cassandra foi construído para ser implantado em vários datacenters e esses datacenters podem ser de vários fornecedores diferentes.
• Dentre as classificações que vimos dos tipos de bancos NoSQL o Cassandra é se enquadra nos bancos de dados orientado a linhas.
• O Design de distribuição foi baseado no Dynamo da Amazon e seu modelo de dados no Bigtable do Google, com uma linguagem de consulta semelhante ao SQL.
• É uma tecnologia que nasceu para ser distribuída então faz pouco sentido utilizá-lo em um só nó.
• Ao contrário de outros bancos com Oracle e BigTable, os nós não são réplicas (modelo master/slave por exemplo) todos são idênticos (simetria do servidor).

### CQL - Cassandra

• CQL fornece uma maneira de definir o esquema por meio de uma sintaxe semelhante à Structured Query Language (SQL), que é familiar para aqueles que vêm de um histórico relacional.
• Cassandra não limita totalmente a capacidade de estender dinamicamente o esquema em tempo real, mas a maneira como ele funciona é significativamente diferente.
• As coleções CQL, como listas, conjuntos e mapas, fornecem a capacidade de adicionar um número variável de valores de um determinado tipo.

### CASSANDRA Acesso chave-valor

### CASSANDRA Estrutura básica

## OPERAÇÕES CASSANDRA

### Criando keyspace
• Na linha de comando a ferramenta oferecida para manipulação dos dados é o cqlsh.
• Para o acesso é necessário informar o endereço do no onde você acessará o Cassandra.
• KEYSPACE: armazena uma lista de uma ou mais famílias de coluna. Análogo a uma base de dados que armazena tabelas no banco relacional.
 SimpleStrategy: Uma estratégia de replicação simples para todo o cluster.
• replication_fator : define o fator de replicação que é obrigatório.
• NetworkTopologyStrategy : define o fator de replicação independente para cada centro de dados.

### Criando estruturas
