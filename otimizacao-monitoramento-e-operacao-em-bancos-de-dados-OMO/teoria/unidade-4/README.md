# UNIDADE IV – SEGURANÇA E RECUPERAÇÃO DE FALHAS

## CONTINUIDADE DE OPERAÇÕES

### IMPLEMENTAÇÕES DE ALTA DISPONIBILIDADE

- Operação contínua (Continuous operation), também conhecida como disponibilidade contínua (continuous availability) ou disponibilidade sempre ativa (always-on availability), são termos utilizados para descrever um sistema de banco de dadosprojetado para operar continuamente sem interrupção.
- Significa que haverá disponibilidade do serviço de banco de dados mesmo em caso de falha ou interrupção.
- Para obter operação contínua, um sistema de banco de dados deve ser projetado para fornecer alta disponibilidade e tolerância a falhas.
- Envolve o uso de uma combinação de hardware, software e tecnologias de rede para criar uma infraestrutura de banco de dados altamente disponível e resiliente.
- A técnica que você vai utilizar vai depender do tipo de banco que você está usando.

### TÉCNICAS PARA ALTA DISPONIBILIDADE

- Termo comum que iremos ouvir no mercado é a utilização de ferramentas de HA, quesignifica High Availability.
- Estas ferramentas e técnicas evitaram queda de um ou mais nós dentro do mesmo Datacenter ou em localidades distintas.
- Para sistemas de banco de dados SQL, a operação contínua pode ser obtida por meio de técnicas, como clustering, replicação e clustering failover.
- Replicação: envolve a combinação de vários servidores em uma única unidade lógica, neste processo se cria várias cópias do mesmo banco de dados que são mantidas sincronizadas em tempo real.
- A ideia básica da replicação é criar cópias do bancos de dados que sejam idênticas ao banco de dados primário.
- Há uma padronização nas etapas para implementar os tipos de replicação,

1. Captura: o sistema de replicação captura as alterações feitas no banco de dados principal. Envolve o registro de alterações no log de transações ou o monitoramento de updates (tabelas ou colunas) específicas.
2. Transporte: as alterações capturadas são transportadas para os bancos de dados de réplica. O envio das alterações ocorrer por meio de uma conexão de rede, possibilita armazenamento em um dispositivo ou uso de um sistema de mensagens.
3. Aplicação: As alterações são aplicadas aos bancos de dados de réplica, garantindo que todas as cópias dos dados sejam consistentes e atualizadas.

Isso pode envolver a execução de instruções SQL ou a aplicação de transformações de dados às alterações capturadas

### AS TOPOLOGIAS DE REPLICAÇÃO

- Replicação Master-slave: determina que um dos nós será o banco de dados primário (master) e todas as alterações são feitas nesse banco de dados.
- Podem haver vários bancos de dados secundários (slaves) que recebem a replica das alterações feitas no master.
- Este procedimento garante que todas as cópias dos dados sejam consistentes.
- Replicação Multi-Master: vários nós bancos de dados são designados como master e as alterações podem ser feitas em qualquer um desses bancos de dados.
- É semelhante à topologia Master-Slave, com a diferença que quando os nós são master e há replicação circular entre todos que podem ser graváveis.
- Replication Peer-to-peer : vários nós de bancos de dados são designados como master e alterações podem ser feitas em qualquer um desses bancos de dados.
-  Mesmo mecanismo da topologia multi-master porém com vários nós distribuídos em diversas localidades.

✓ Publisher: É o banco de dados de origem, que contém os dados a serem replicados.
✓ Subscriber: Este é o banco de dados de destino e pode haver muitos deles para um único Publisher.
✓ Distribuidor: utilizado para distribuir as transações para o banco de dados do subscriber.

## BANCOS NoSQL

-  Sharding: envolve o particionamento dos dados em vários servidores para aumentar o desempenho e a escalabilidade.
- Replicação: replicação envolve a criação de várias cópias dos dados e sua manutenção sincronizada em tempo real
- Vários Datacenters: envolve a implantação do banco de dados em vários locais geográficos para garantir a redundância e reduzir a latência

## Perda de dados

### o que fazer
