## Características dos bancos de dados NoSQL


- O termo NoSQL (Not Only SQL) tem sido usado com o significado de “Não apenas SQL” como tentativa da comunidade de reconhecer a utilidade dos modelos tradicionais e não divergir as discussões.
-  NoSQL não define precisamente esses bancos de dados, mas no geral cada um deles apresenta a maioria das seguintes características:

✓ Não-relacional
✓ Distribuído
✓ Código aberto
✓ Escalável horizontalmente
✓ Ausência de esquema ou esquema flexível
✓ Suporte à replicação nativo
✓ Acesso via APIs simples
✓ Diminuição do tempo de recuperação de informações

### O que é um banco de dados NoSQL?

Sistemas NoSQL não existe uma padronização para as linguagens de manipulação e consulta de dados como no Modelo Relacional, o qual utiliza o padrão SQL.
Sistemas NoSQL não requerem qualquer padronização mesmo em ferramentas que tratam o mesmo modelo de dados 

NoSQL é um conjunto de conceitos que permite o processamento rápido e eficiente de conjuntos de dados com foco em desempenho, confiabilidade e agilidade.
O surgimento desses SGBDs tem como motivação aplicações cujos requisitos não se ajustam a apenas um modelo de dados


### Persistência poliglota

• Aplicações com essas características, ou seja, que necessitam acessar dois ou mais SGBDs com modelos de dados diferentes são chamadas de poliglotas, uma vez que realizam persistência de dados em diversos formatos devido à natureza heterogênea dos dados que manipulam.
• Este conceito de persistência poliglota, pode ser denominado por alguns autores como SGBD NoSQL multimodelo.

### Consistência eventual

- Consistência eventual: Essa característica está relacionada ao fato da consistência nem sempre ser mantida entre os vários pontos de distribuição de dados.
-  Ela tem como princípio o teorema de CAP (Consistency, Availability, Partition and Tolerance) que diz que só é possível garantir duas das três propriedades entre consistência, disponibilidade e tolerância à partição.
-  No contexto da Web geralmente são privilegiadas a disponibilidade e a tolerância à partição.
-   NoSQL implementa as propriedades BASE (Basically Avaliable, Softstate, Eventual consistency), que foram propostas para contrapor as propriedades ACID (Atomicity, Consistency, Isolation, Durability) do Modelo Relacional.
-   A ideia principal é dispensar a consistência (por um intervalo de tempo) em favor da disponibilidade e escalabilidade.

## Propriedades dosbancos de dados NoSQL 

### ACID
- Atomicidade: significa que em uma transação envolvendo duas ou mais partes de informações discretas, ou a transação será executada totalmente ou não será executada, garantindo assim que as transações sejam atômica.
- Consistência: é quando uma transação cria um novo estado válido dos dados ou, em caso de falha, retorna todos os dados ao seu estado anterior ao início da transação.
- Isolamento: significa que uma transação em andamento, mas ainda não validada, deve permanecer isolada de qualquer outra operação externa, ou seja, garante-se que a transação não será interferida por nenhuma outra transação concorrente.
- Durabilidade: indica que dados validados são registados pelo sistema de tal forma que, mesmo no caso de uma falha ou reinício do sistema, os dados estão disponíveis em seu estado correto

- As propriedades ACID forçam a consistência ao final de cada operação, as propriedades BASE permitem que o banco de dados esteja - de forma eventual em um estado consistente.
- Em outras palavras, para obtenção do alto desempenho e disponibilidade, não há priorização da consistência dos dados.
- NoSQL são capazes de processar um grande número de operações simples de leitura e gravação por segundo porém sem garantia de consistência imediata

### Escalabilidade Horizontal

- Escalabilidade horizontal: devido ao volume de dados há a necessidade de escalar e melhorar o desempenho do sistema a escalabilidade horizontal, é o aumento do número de nós (máquinas) disponíveis para o armazenamento e processamento dos dados.
-  Para que a escalabilidade horizontal seja eficiente, ela requer que diversos processos de uma única tarefa sejam criados e distribuídos
-   Esta característica torna inviável a utilização de um banco de dados relacional, uma vez que todos estes processos conectados geram grande concorrência, aumentando consequentemente o tempo de acesso às tabelas desejadas.
- A escalabilidade horizontal somente é permitida nos BDs NoSQL por causa da ausência de bloqueios.
-  Utiliza-se para alcançar esta escalabilidade é o Sharding, que consiste em dividir os dados em várias tabelas, armazenando-as ao longo de múltiplos nós de uma rede quebrando a lógica de relacionamentos.

### schemaless

 - Ausência de esquema ou esquema flexível: a ausência completa ou parcial de esquema que define a estrutura dos dados é uma característica dos bancos NoSQL.
 -  Essa falta de esquema simplifica escalabilidade do sistema bem como aumenta a sua disponibilidade no entanto, não há garantia da integridade dos dados.

### Supor te nativo à replicação

- Suporte nativo à replicação: prover escalabilidade realizando a replicação nativa dos dados, pois isso ajuda a diminuir o tempo gasto na recuperação das informações.
-  Existem basicamente duas abordagens para realizar a replicação:
✓ Master Slave: permite que um servidor slave copie todas as alterações realizadas em um outro servidor, denominado de master.
 Multi-Master: para aplicações distribuídas geograficamente, pode-se criar servidores masters próximos às regiões que manipulam os dados, permitindo uma redução no tempo de acesso ao dado através da rede.
✓ Para isto, é necessário manter todas as regiões sincronizadas, e para isto, utilizamos a topologia de anel, onde define-se vários masters.

### API - Application Programming Interface

 API : No NoSQL o foco não está na forma em que os dados são acessados, mas sim em como são recuperados.
• O uso de APIs se torna essencial para tornar simples o acesso a essas informações, permitindo que qualquer aplicação possa fazer uso do banco de forma rápida e eficiente.
• Tudo vinculado ao conceito de arquitetura de microsserviços MAS (MicroServices Architecture)
