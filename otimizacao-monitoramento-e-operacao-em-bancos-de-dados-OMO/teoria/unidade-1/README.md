# O Gerenciamento de Banco de Dados

## Introdução ao Gerenciamento

- **Soluções de armazenamento**: armazenam arquivos, que nada mais são do que coleções de informações organizadas de forma lógica.

---

## Métodos de Acesso ao Disco

### Conceitos Básicos

- **Gravação (IN)**: ação de incluir ou alterar dados no dispositivo.  
- **Leitura (OUT)**: ação de recuperar arquivos gravados no dispositivo.  
- **Particionar**: dividir um disco rígido em múltiplas unidades lógicas (partições).  
- **Blocos**: pequenas áreas contíguas do disco, cujo tamanho é definido na criação do sistema de arquivos.

### Estruturas de Discos e Cache

- O Sistema de Arquivos é a parte mais visível de um SO, pois a manipulação de arquivos é a atividade mais frequente.  
- A organização dos arquivos varia conforme o tipo de informação armazenada.  
- A manipulação de arquivos independe do tipo de dispositivo e é controlada pelo SO.  
- A forma de acesso aos arquivos não pode ser modificada pelo usuário; existem vários métodos de acesso.

#### Métodos de Acesso

- **Sequencial**  
  - A gravação de novos registros só é possível no final do arquivo.

- **Acesso Direto**  
  - Leitura/gravação de um registro diretamente pela sua posição (número do registro).  
  - Requer arquivos com registros de tamanho fixo.

- **Acesso Direto + Sequencial**  
  - Acesso direto a um registro qualquer e, a partir dele, leitura sequencial dos demais.

- **Acesso Indexado por Chave**  
  - Baseado em acesso direto, porém usa uma área de índice com ponteiros para os registros.

- **Cache de Disco**  
  - Canais de I/O podem implementar sistemas de cache para melhorar o tempo de acesso.  
  - **Buffer Cache**: área da memória que armazena dados de disco para acesso instantâneo.

---

## Funções do Gerenciamento em um SGBD

- O SGBD é o software que facilita o gerenciamento do banco de dados, atuando como interface entre os dados no disco e seus usuários.  
- Interpreta requisições, executa instruções e responde ao usuário.  
- Supera o gerenciamento de arquivos ao oferecer organização sofisticada e recuperação de dados em tempo real.

### Desafios e Responsabilidades

- Com muitos usuários acessando dados, o SGBD resolve problemas de cópias e duplicação incontrolável, que geram inconsistência.  
- Permite alterações estruturais (como adicionar campos) de forma controlada.  
- O controle de concorrência é fundamental para compartilhar informações com desempenho.

---

## Transações

- Transações garantem que um conjunto de operações seja executado **totalmente** ou **não executado**, assegurando consistência dos dados.  
- O SGBD intermedia todas as operações de armazenamento, atualização e recuperação, impedindo o acesso direto aos arquivos.

---

## Papel do DBA

- O Administrador de Banco de Dados (DBA) é responsável pelo controle técnico do sistema.  
- Define esquema físico e lógico, relacionamento com usuários, políticas de segurança e integridade.  
- Planeja backup, recuperação e monitoramento de indicadores de desempenho.

---

## Monitoramento e Métricas Básicas

### Escolha da Melhor Arquitetura

- **Shard (fragmentação)**: particiona um banco lógico em vários servidores físicos.  
- Usado em grandes sites (Facebook, Twitter) junto a cache e replicação para escalar bancos relacionais.  
- Desvantagens:
  - Complexidade do aplicativo (roteamento de SQL).  
  - **“Crippled SQL”**: não é possível operações entre shards.  
  - Perda de integridade transacional (ACID).  
  - Complexidade operacional (balanceamento de carga).

### Métricas de Sistema e Resposta

- Monitorar métricas de SO (CPU, memória) e métricas de aplicação (tempo de resposta).  
- Alta utilização de CPU não é crítica se os tempos de resposta forem aceitáveis.  
- Métricas de SO auxiliam no diagnóstico e análise de desempenho.

---

## Sistemas de Alertas e Integração com Esteiras

### ITIL e Gerenciamento de Incidentes

- ITIL fornece melhores práticas para gerenciamento de serviços de TI.  
- Oferece listas de tarefas e técnicas para operação de serviços.  
- Incidentes e monitoramento são disciplinas do ITIL.  
- O Sistema de Valor de Serviço ITIL mostra como componentes e atividades criam valor.

### Tipos de Alertas

- **Críticos**: ação imediata necessária para evitar inatividade.  
- **Pró-ativos**: indicar problemas iminentes antes da interrupção.  
- **De conhecimento**: sem impacto imediato, mas registram eventos relevantes.

### Objetivo do Registro de Incidentes

- Conhecer o que acontece no ambiente.  
- Verificar repetição de eventos (ligação com Gerenciamento de Problemas).  
- Analisar custos de interrupção e satisfação dos usuários.  
- Documentar ocorrências e soluções para reaproveitamento futuro.
```
