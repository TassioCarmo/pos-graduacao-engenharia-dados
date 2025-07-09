# Resumo - Bancos de Dados NoSQL

## O que mudou no mundo dos dados?

Com a Web 2.0, tudo mudou. Antes, os sites eram páginas estáticas onde você só consumia conteúdo. Agora, somos todos produtores de dados - postando, curtindo, comentando, compartilhando. E isso gera uma quantidade absurda de informações.

Imagina só: temos mais dispositivos conectados do que pessoas no mundo! Celulares, sensores IoT, câmeras, GPS, jogos online... tudo gerando dados 24/7. Estamos falando de volumes na casa dos zetabytes (isso é muito, muito mesmo).

O problema é que os bancos de dados tradicionais não conseguem mais dar conta. Eles foram feitos para um mundo onde os dados eram estruturados e organizados em tabelas. Mas agora? Temos textos, imagens, vídeos, dados de sensores... uma bagunça organizada que precisa de uma nova abordagem.

## NoSQL: A resposta para o caos

### O que é essa tal de NoSQL?

Primeiro, vamos tirar uma confusão: NoSQL não significa "sem SQL". Na verdade, significa "Not Only SQL" (não apenas SQL). É como se fosse um "SQL++", expandindo as possibilidades além do mundo relacional.

O NoSQL surgiu em 1998, mas só ganhou força com a explosão da Web 2.0. A ideia não é jogar o banco relacional no lixo, mas sim ter mais ferramentas na caixa de ferramentas.

### Principais características

Os bancos NoSQL geralmente têm essas características:

- **Não-relacional**: Sem aquelas tabelas com chaves estrangeiras e relacionamentos complexos
- **Distribuído**: Roda em várias máquinas ao mesmo tempo
- **Código aberto**: A maioria é gratuita e de código aberto
- **Escalável horizontalmente**: Precisa de mais poder? Adiciona mais máquinas
- **Esquema flexível**: Não precisa definir estrutura rígida antes
- **Replicação nativa**: Copia dados automaticamente para backup
- **APIs simples**: Acesso fácil via programação
- **Recuperação rápida**: Busca informações mais rapidamente

## As grandes diferenças conceituais

### ACID vs BASE: A batalha dos acrônimos

**ACID** (mundo relacional):
- **Atomicidade**: Ou faz tudo ou não faz nada
- **Consistência**: Dados sempre válidos
- **Isolamento**: Operações não interferem umas nas outras
- **Durabilidade**: Uma vez salvo, sempre salvo

**BASE** (mundo NoSQL):
- **Basically Available**: Basicamente disponível
- **Soft state**: Estado flexível
- **Eventual consistency**: Consistência... eventualmente

A diferença fundamental é que o ACID garante que tudo esteja sempre certinho, mas isso custa performance. O BASE aceita que, por alguns momentos, os dados podem estar um pouco "bagunçados", mas em troca oferece velocidade e disponibilidade.

### O Teorema CAP: Escolha duas de três

Este é um conceito crucial: você só pode ter duas das três propriedades:
- **Consistência**: Todos veem os mesmos dados
- **Disponibilidade**: Sistema sempre no ar
- **Tolerância à partição**: Funciona mesmo se a rede falhar

Na web, geralmente escolhemos disponibilidade e tolerância à partição. Afinal, é melhor ter um sistema funcionando com dados um pouco desatualizados do que um sistema fora do ar.

## Como funciona na prática?

### Escalabilidade horizontal

Imagine que seu banco de dados é como uma mesa. Quando você precisa de mais espaço:
- **Escalabilidade vertical**: Você compra uma mesa maior (mais RAM, CPU mais potente)
- **Escalabilidade horizontal**: Você adiciona mais mesas (mais servidores)

O NoSQL foi feito para a segunda opção. Usa uma técnica chamada **sharding**, que é basicamente dividir os dados em pedaços e espalhar por várias máquinas.

### Ausência de esquema

Sabe aquela regra chata dos bancos relacionais onde você precisa definir exatamente como seus dados vão ser estruturados? No NoSQL, você pode ser mais flexível. Quer adicionar um campo novo? Sem problema. Alguns registros têm campos diferentes? Tranquilo.

Isso acelera o desenvolvimento, mas tem um preço: você perde algumas garantias de integridade dos dados.

### Replicação de dados

O NoSQL copia seus dados automaticamente para várias máquinas. Existem duas formas principais:

**Master-Slave**: Um servidor principal (master) e vários servidores cópia (slaves). Tudo que acontece no master é copiado para os slaves.

**Multi-Master**: Vários servidores principais, geralmente espalhados geograficamente. Útil para aplicações globais.

## Persistência poliglota

Esse nome complicado significa uma coisa simples: usar diferentes tipos de banco para diferentes necessidades. É como ter várias ferramentas:
- MySQL para dados transacionais
- MongoDB para documentos
- Redis para cache
- Neo4j para grafos

# Resumo - Bancos de Dados NoSQL (Unidades 1.1 e 1.2)

## Definição de negócios e motivação

### Por que as empresas estão migrando para NoSQL?

A transformação digital trouxe uma realidade nova para as empresas. Hoje, o foco está em criar **plataformas consolidadas** que simplifiquem o acesso aos dados e permitam descobrir conhecimento rapidamente.

**A revolução da nuvem**
A computação em nuvem virou o padrão de referência porque oferece uma abordagem mais pragmática para otimizar a infraestrutura. As empresas estão investindo em infraestruturas:
- Centralizadas/federadas
- Virtualizadas e automatizadas
- Compartilhadas e otimizadas (privadas, públicas, híbridas)

**Preparando para o Big Data**
Os ambientes de TI estão sendo reformulados para a era do Big Data. As redes definidas por software (SDN) viraram o padrão para transmissão e processamento de dados, porque oferecem mais flexibilidade e controle.

**Critério de sucesso**
O sucesso de qualquer tecnologia se mede pela quantidade de aplicações críticas que ela consegue criar e manter. Como grandes insights estão se tornando obrigatórios para vários setores, há muito espaço para aplicações de Big Data.

**Motivação direta**
A motivação para NoSQL é bem clara: a quantidade absurda de dados de várias fontes diferentes, complexos e dinâmicos, que precisam de tecnologias específicas para armazenamento, análise e visualização.

Bancos relacionais até conseguem escalar, mas quanto maior o tamanho, mais caro fica - tanto em recursos quanto em dinheiro.

## Tipos e modelos de transações

### Por que isso importa?

Em ambientes distribuídos, o controle de transações é fundamental para garantir desempenho e consistência. Existem basicamente dois modelos: **ACID** (usado nos bancos relacionais) e **BASE** (encontrado em muitos sistemas NoSQL).

**Diferença fundamental**: tanto sistemas relacionais quanto NoSQL podem implementar controles transacionais. A diferença está na **quantidade de esforço** exigida dos desenvolvedores e na **localização** desses controles no sistema.

### ACID - O modelo rigoroso

**Atomicidade**: Ou faz tudo ou não faz nada. Sem meio termo.

**Consistência**: Ou cria um estado válido dos dados ou volta tudo para o estado anterior.

**Isolamento**: Uma transação em andamento não pode ser interferida por outras transações concorrentes.

**Durabilidade**: Dados validados ficam registrados permanentemente, mesmo se o sistema falhar.

**Exemplo clássico**: Transação bancária. Imagina transferir R$ 100 da conta A para a conta B. Ou as duas operações acontecem (débito + crédito) ou nenhuma acontece. Não pode debitar e não creditar.

### BASE - O modelo flexível

**Basic Availability**: Permite que o sistema fique temporariamente inconsistente para que as transações sejam gerenciáveis.

**Soft-state**: Reconhece que alguma imprecisão é temporariamente permitida. Os dados mudam enquanto são usados, reduzindo o consumo de recursos.

**Eventual consistency**: Eventualmente, quando toda a lógica é executada, o sistema fica consistente.

**Exemplo prático**: Carrinho de compras online. É melhor aceitar um pedido mesmo que alguns dados estejam temporariamente inconsistentes do que bloquear a venda. Perder um cliente é pior que ter relatórios inconsistentes por alguns minutos.

O modelo BASE **relaxa as regras** e permite que relatórios sejam executados mesmo que nem todas as partes do banco estejam sincronizadas. A ideia é que, eventualmente, tudo se acerta.

### Teorema CAP - Escolha apenas duas

Este teorema é fundamental para entender NoSQL. Ele diz que é **impossível** ter simultaneamente as três propriedades:

**Consistência**: Todos os nós veem os mesmos dados ao mesmo tempo.

**Disponibilidade**: Garantia de resposta em cada solicitação.

**Tolerância a partições**: O sistema continua operando mesmo com falhas de rede ou partes do sistema.

**Você só pode ter duas das três!**

### Tipos de sistemas baseados no CAP

**Sistemas CA (Consistency + Availability)**
- Consistência forte e alta disponibilidade
- Não sabem lidar com falhas de partição
- Se algo falhar, o sistema inteiro pode ficar indisponível
- **Exemplo**: Configurações clássicas de bancos relacionais

**Sistemas CP (Consistency + Partition Tolerance)**
- Consistência forte e tolerância a partições
- Abrem mão de um pouco da disponibilidade
- **Exemplos**: BigTable, HBase, MongoDB

**Sistemas AP (Availability + Partition Tolerance)**
- Jamais podem ficar offline
- Prejudicam um pouco a consistência
- Aceitam escritas sempre e sincronizam depois
- **Exemplos**: Amazon DynamoDB, Cassandra, Riak

### SQL vs NoSQL na prática

**SQL (ACID)**:
- Esquemas rígidos
- Dados estruturados (campos, linhas, colunas)
- Transações complexas com garantias rigorosas
- Alterar esquema depois que os dados estão inseridos é muito complexo

**NoSQL (BASE)**:
- Sem esquema ou esquema flexível
- Dados multiestruturados
- Permite gravação de documentos e metadados
- Facilita incorporação rápida de novos tipos de dados

### Quando usar cada um?

**Use bancos relacionais quando:**
- Aplicações centralizadas
- Não há requisitos de altíssima disponibilidade
- Geração de dados em velocidade média
- Poucas fontes geradoras de dados
- Dados estruturados
- Transações complexas
- Volume médio de dados

**Use NoSQL quando:**
- Aplicações descentralizadas (Web, IoT, Big Data)
- Não pode haver interrupção na gravação de dados
- Geração de dados em alta velocidade (sensores)
- Muitas fontes geradoras de dados
- Dados semi ou não-estruturados
- Transações simples
- Alto volume de armazenamento

## O que mudou no mundo dos dados?

Com a Web 2.0, tudo mudou. Antes, os sites eram páginas estáticas onde você só consumia conteúdo. Agora, somos todos produtores de dados - postando, curtindo, comentando, compartilhando. E isso gera uma quantidade absurda de informações.

Imagina só: temos mais dispositivos conectados do que pessoas no mundo! Celulares, sensores IoT, câmeras, GPS, jogos online... tudo gerando dados 24/7. Estamos falando de volumes na casa dos zetabytes (isso é muito, muito mesmo).

O problema é que os bancos de dados tradicionais não conseguem mais dar conta. Eles foram feitos para um mundo onde os dados eram estruturados e organizados em tabelas. Mas agora? Temos textos, imagens, vídeos, dados de sensores... uma bagunça organizada que precisa de uma nova abordagem.

## NoSQL: A resposta para o caos

### O que é essa tal de NoSQL?

Primeiro, vamos tirar uma confusão: NoSQL não significa "sem SQL". Na verdade, significa "Not Only SQL" (não apenas SQL). É como se fosse um "SQL++", expandindo as possibilidades além do mundo relacional.

O NoSQL surgiu em 1998, mas só ganhou força com a explosão da Web 2.0. A ideia não é jogar o banco relacional no lixo, mas sim ter mais ferramentas na caixa de ferramentas.

### Principais características

Os bancos NoSQL geralmente têm essas características:

- **Não-relacional**: Sem aquelas tabelas com chaves estrangeiras e relacionamentos complexos
- **Distribuído**: Roda em várias máquinas ao mesmo tempo
- **Código aberto**: A maioria é gratuita e de código aberto
- **Escalável horizontalmente**: Precisa de mais poder? Adiciona mais máquinas
- **Esquema flexível**: Não precisa definir estrutura rígida antes
- **Replicação nativa**: Copia dados automaticamente para backup
- **APIs simples**: Acesso fácil via programação
- **Recuperação rápida**: Busca informações mais rapidamente

## As grandes diferenças conceituais

### ACID vs BASE: A batalha dos acrônimos

**ACID** (mundo relacional):
- **Atomicidade**: Ou faz tudo ou não faz nada
- **Consistência**: Dados sempre válidos
- **Isolamento**: Operações não interferem umas nas outras
- **Durabilidade**: Uma vez salvo, sempre salvo

**BASE** (mundo NoSQL):
- **Basically Available**: Basicamente disponível
- **Soft state**: Estado flexível
- **Eventual consistency**: Consistência... eventualmente

A diferença fundamental é que o ACID garante que tudo esteja sempre certinho, mas isso custa performance. O BASE aceita que, por alguns momentos, os dados podem estar um pouco "bagunçados", mas em troca oferece velocidade e disponibilidade.

### O Teorema CAP: Escolha duas de três

Este é um conceito crucial: você só pode ter duas das três propriedades:
- **Consistência**: Todos veem os mesmos dados
- **Disponibilidade**: Sistema sempre no ar
- **Tolerância à partição**: Funciona mesmo se a rede falhar

Na web, geralmente escolhemos disponibilidade e tolerância à partição. Afinal, é melhor ter um sistema funcionando com dados um pouco desatualizados do que um sistema fora do ar.

## Como funciona na prática?

### Escalabilidade horizontal

Imagine que seu banco de dados é como uma mesa. Quando você precisa de mais espaço:
- **Escalabilidade vertical**: Você compra uma mesa maior (mais RAM, CPU mais potente)
- **Escalabilidade horizontal**: Você adiciona mais mesas (mais servidores)

O NoSQL foi feito para a segunda opção. Usa uma técnica chamada **sharding**, que é basicamente dividir os dados em pedaços e espalhar por várias máquinas.

### Ausência de esquema

Sabe aquela regra chata dos bancos relacionais onde você precisa definir exatamente como seus dados vão ser estruturados? No NoSQL, você pode ser mais flexível. Quer adicionar um campo novo? Sem problema. Alguns registros têm campos diferentes? Tranquilo.

Isso acelera o desenvolvimento, mas tem um preço: você perde algumas garantias de integridade dos dados.

### Replicação de dados

O NoSQL copia seus dados automaticamente para várias máquinas. Existem duas formas principais:

**Master-Slave**: Um servidor principal (master) e vários servidores cópia (slaves). Tudo que acontece no master é copiado para os slaves.

**Multi-Master**: Vários servidores principais, geralmente espalhados geograficamente. Útil para aplicações globais.

## Persistência poliglota

Esse nome complicado significa uma coisa simples: usar diferentes tipos de banco para diferentes necessidades. É como ter várias ferramentas:
- MySQL para dados transacionais
- MongoDB para documentos
- Redis para cache
- Neo4j para grafos



