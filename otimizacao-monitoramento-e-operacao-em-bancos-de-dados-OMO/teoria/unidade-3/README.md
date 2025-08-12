UNIDADE III – OPERAÇÃO DE AMBIENTES
DE BANCO DE DADOS
OPERAÇÃO DE AMBIENTE
DE BANCOS DE DADOS
ATIVIDADES
DO ADMINISTRADOR
DE BANCO DE DADOS
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
▪ Planejar a infraestrutura
▪ Instalar o SGBD e suas ferramentas de
suporte
▪ Configurar os componentes físicos e lógicos
▪ Modificar ambiente
▪ Criar, monitorar e controlar usuários
▪ Monitorar performance
▪ Auditar atividades
▪ Definir estratégia de backup e recovery
▪ Muitas coisas a se fazer e cada uma delas tem
uma complexidade enorme.
▪ Começamos esta conversa sobre a definição
do que é mais importante, acompanhamentos
em tempo real ou estabelecimento de planos
e testes para que, caso ocorra algum
problema saibamos o que fazer?
▪ Pois bem, esta é uma grande dúvida, mas
não é tão complicado assim resolver!
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
▪ Se observarmos as palavras chaves
que cercam o assunto operação a
visão fica clara do que precisa ser
feito.
▪ Vejam que o administrador de
banco de dados assim como
qualquer gestor de infraestrutura
precisa primar por duas coisas:
▪ Disponibilidade e estabilidade.
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
▪ É necessário que um especialista em infraestrutura de banco de dados conheça a demanda
de informação da empresa.
▪ Em tempos de utilização de nuvem, o custo impacta diretamente na escolha do recurso
e/ou serviços que serão utilizados, esta participação assegura um ambiente computacional
compatível com a necessidade do negócio.
▪ O investimento no hardware, software ou serviço passam a ser importantíssimos na
definição corporativa é cada vez mais é necessário realizar o famoso alinhamento da TI
com os negócios!
▪ A partir daí as escolha dos ambientes operacionais compatíveis com as soluções de SGBD
escolhidas para a solução do problema.
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
ATIVIDADES DE UM DBA
▪ Definir o produto de software e a plataforma
de hardware estão nas atribuições e é ele
quem detém o conhecimento de ambientes
operacionais e as técnicas utilizadas pelo
banco na recuperação de dados.
▪ Este conhecimento é fundamental para
apontar qual o tipo de banco de dados
(relacional, NoSQL (colunas, grafos, chave-
valor, documento), em Rede, OO, ou outros)
será utilizado.
▪ A atualização de ambientes de bancos de
dados é tão importante quanto a instalação e
precisa ser analisado o impacto que a
mudança pode causar no ambiente das
aplicações.
▪ De acordo com a natureza do sistema, a
necessidade de negócio e o conhecimento
do DBA, ele estará apto a apontar as
ferramentas auxiliares que serão
necessárias para a operação do ambiente.
ATIVIDADES DE UM DBA▪ A atualização de ambientes de bancos de
dados é tão importante quanto a instalação e
precisa ser analisado o impacto que a
mudança pode causar no ambiente das
aplicações.
▪ De acordo com a natureza do sistema, a
necessidade de negócio e o conhecimento
do DBA, ele estará apto a apontar as
ferramentas auxiliares que serão
necessárias para a operação do ambiente.
ATIVIDADES DE UM DBA
▪ A configuração dos componentes físicos – define como o sistema será implementado e a
fatores no SGBD específico - e lógicos: desenvolver um mapa técnico de regras e
estruturas de dados, independente do SGBD escolhido.
▪ Modelagem de dados física é considerada uma atividade de DESIGN, lembram? E fica
por conta do administrador de banco de dados.
▪ O cuidado é que as alterações feitas nesta etapa não podem interferir no funcionamento do
sistema, uma das mais conhecidas é o particionamento de tabelas que pode afetar e muito
a performance das consultas, então as ações precisam ter análise de impacto.
▪ A configuração dos componentes físicos e lógicos assim como a implementação das
alterações no ambiente ficam a cargo do administrador de banco de dados.
ATIVIDADES DE UM DBA▪ A configuração dos componentes físicos – define como o sistema será implementado e a
fatores no SGBD específico - e lógicos: desenvolver um mapa técnico de regras e
estruturas de dados, independente do SGBD escolhido.
▪ Modelagem de dados física é considerada uma atividade de DESIGN, lembram? E fica
por conta do administrador de banco de dados.
▪ O cuidado é que as alterações feitas nesta etapa não podem interferir no funcionamento do
sistema, uma das mais conhecidas é o particionamento de tabelas que pode afetar e muito
a performance das consultas, então as ações precisam ter análise de impacto.
▪ A configuração dos componentes físicos e lógicos assim como a implementação das
alterações no ambiente ficam a cargo do administrador de banco de dados.
ATIVIDADES DE UM DBA
▪ O administrador prima pela disponibilidade e estabilidade do ambiente, desta forma, o
maior perigo que possuímos em um ambiente de banco de dados é, sem dúvida o acesso
indevido de usuários.
▪ É prática comum que a criação e definição de perfis de usuários de banco de dados
fiquem a cargo deste profissional assim como o monitoramento e o controle dos acessos
destes usuários.
▪ O monitoramento de performance está incluso neste conjunto de atividades, mesmo
que, na maior parte das vezes não seja possível que o administrador faça as alterações
em a participação do desenvolvedor.
ATIVIDADES DE UM DBA▪ O administrador prima pela disponibilidade e estabilidade do ambiente, desta forma, o
maior perigo que possuímos em um ambiente de banco de dados é, sem dúvida o acesso
indevido de usuários.
▪ É prática comum que a criação e definição de perfis de usuários de banco de dados
fiquem a cargo deste profissional assim como o monitoramento e o controle dos acessos
destes usuários.
▪ O monitoramento de performance está incluso neste conjunto de atividades, mesmo
que, na maior parte das vezes não seja possível que o administrador faça as alterações
em a participação do desenvolvedor.
ATIVIDADES DE UM DBA
▪ Após todas as definições de negócio, tecnológicas, físicas e lógicas incluindo controles de
segurança é hora de fazer a auditoria das atividades realizadas em um SGBD.
▪ E para a manutenção do ambiente, as atividades de Backup e Recovery estão sob a tutela
deste profissional que inclui o plano de contingência, suas estratégias de backup e de
recuperação de banco de dados.
▪ Parece que é moleza não é?
UNIDADE III – OPERAÇÃO DE AMBIENTES
DE BANCO DE DADOS
OPERAÇÃO DE AMBIENTE
DE BANCOS DE DADOS
COMO DEFINIR O FOCO
DE ATUAÇÃO
A REGRA DE PARETO: FOCO E RESULTADO
▪ A questão principal posta pela regra de
Pareto é definir efetivamente o que deve ser
feito primeiro.
▪ Esta técnica irá ajuda-lo a ter foco na atuação
e, mais que isto, a resolver problemas com o
menor esforço.
▪ Veja só um exemplo:
✓ Todos nós temos uma rotina de
trabalho, a ordem de execução das
coisas no nosso dia a dia.
Fonte: Laoyan,2022.
✓ Porém, qual técnica você usa para
definir o que deve ser feito
primeiro?
▪ A dica é a princípio de Pareto, conhecido
como a regra 80/20 (80% dos resultados
resultam de 20% das causas).
▪ Esta regra te ajuda a determinar e priorizar
as tarefas de maior impacto, aumentando a
produtividade durante a jornada de
trabalho.
Fonte: Laoyan,2022.
A REGRA DE PARETO: FOCO E RESULTADO
E NA PRÁTICA...
▪ Na prática quer dizer que você pode
construir uma base de conhecimento com
20% das soluções que você conhece para
resolver 80% dos problemas que irão
aparecer.
▪ A metodologia foi criada por um italiano,
Vilfredo Pareto, e está embutida na
metodologia Six Sigma de controle de
qualidade.
▪ Gestão de Incidentes e Problemas (ITIL).
Fonte: Laoyan,2022.
VAMOS APLICAR NA NOSSA REALIDADE?
▪ O administrador de banco de dados sabendo
organizar estas informações da melhor forma
consegue organizar a operação e investe
tempo na disciplina, ou melhor, conjunto de
tarefas especializadas que irão dar retorno.
▪ No contexto de ambientes de banco de
dados, esse princípio pode ser aplicado
para identificar as áreas mais críticas que
requerem atenção e recursos.
▪ Identifique e contabilize as áreas de maior impacto: é necessário classificar em qual
área de atuação estão concentradas os maiores registros de problemas, segurança,
disponibilidade, desempenho, monitoramento e pode incluir a realização de backups,
ajuste de desempenho, precisão e disponibilidade de dados.
▪ Analise os dados: em seguida, analise os dados contabilizados para determinar quais
áreas estão contribuindo mais para o impacto geral. Em uma operação, você pode
descobrir que 20% das tabelas do banco de dados são responsáveis por 80% das
consultas ao banco de dados ou que 20% dos usuários do banco de dados são
responsáveis por 80% das transações do banco de dados.
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
▪ Priorize as áreas críticas: depois de identificar as áreas críticas, priorize-as com base em
seu impacto sendo que as áreas com impacto mais significativo devem receber a maior
prioridade, seguidas por aquelas com impacto moderado.
▪ Aloque recursos adequadamente: Aloque recursos, como tempo, orçamento e pessoal,
para abordar as áreas críticas e, desta forma, podemos alocar mais tempo e recursos para
ajuste de desempenho e backups de banco de dados do que para áreas menos críticas,
como precisão de dados.
▪ Monitore o progresso: utilize métricas de desempenho e outros indicadores-chave de
desempenho (como numero de incidentes registrados) para acompanhar o progresso e
identificar as áreas que precisam de atenção adicional.
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
▪ Aplicando a Regra de Pareto, é
possível concentrar os recursos nas
áreas mais críticas do ambiente de
banco de dados.
▪ Isto direciona o esforço para os
lugares ideais e pode levar a
melhorias significativas nas
dimensões de desempenho,
segurança e disponibilidade.
DIMENSÕES ENVOLVIDAS NA OPERAÇÃO
EM RESUMO
▪ ORGANIZAR UMA OPERAÇÃO NÃO É
TÃO FÁCIL, NÃO É VERDADE?
▪ Identificar áreas que precisam de melhorias
e tomar medidas proativas para otimizar a
operação de banco de dados traz mais
satisfação os clientes.
▪ Aqui não estamos falando apenas de
identificação de situações para identificação
de problemas de desempenho em queries, por
exemplo.
▪ Inclui-se nesta discussão questões relativas a
tempo de atividade do banco de dados,
tempo de backup e recuperação e
disponibilidade do banco de dados que
ajudam a garantir que seus aplicativos
estejam sempre disponíveis para seus
clientes.
▪ Ferramentas e metodologias como ITIL e
Six Sigma nos ajudam a coletar estes dados
de forma organizada para que nos gerem
indicadores potentes!
MONITORAMENTO DE
AMBIENTES DE PRODUÇÃO
VISBILIDADE DE AMBIENTES DE
PRODUÇÃO
O MONITORAMENTO DE BANCO DE DADOS
▪ As equipes de gestão de infraestrutura de TI
precisam sempre estar um passo à frente e de
alguma forma impedir que o ambiente sofra
problemas.
▪ Em um ambiente de banco de dados são
variáveis que interferem:
✓ rede, o servidor físico, o sistema
operacional;
✓ implementações de novas
funcionalidades;
✓ solicitação de acessos;
✓ manutenções em componentes e suas
integrações;
✓ backups e;
✓ interferências que não sejam
autorizadas.
▪ Todos estes eventos, podem causar impactos
que degradam a performance ou podem
avisá-lo da conclusão de uma tarefa
incompleta, por exemplo.
O MONITORAMENTO DE BANCO DE DADOS
E NOS PAPEIS DO DBA TEREMOS QUE TRATAR...
▪ Configurar alertas: visibilidade dos
indicadores de desempenho (KPIs), por
exemplo: disponibilidade do banco de
dados, tempo de resposta e taxa de
transferência.
▪ Alertas te ajudam a receber notificações
para ação priorizadas, evitando gastar
energia com apontamentos onde você tem
mais tempo para resolver as questões
indicadas e não há impacto na
disponibilidade ou desempenho.
SUGESTÃO DE MONITORAMENTO DE ITENS
▪ Uso de recursos: visibilidade do uso de
recursos em servidores de banco de dados:
CPU, memória e uso de disco (não se
esqueça de verificar espaço livre).
▪ Conexões de banco de dados: monitore o
número de conexões de banco de dados
ativas com foco na verificação de
vazamentos ou erros de conexão que possam
afetar o desempenho.
SUGESTÃO DE MONITORAMENTO DE ITENS
▪ Desempenho da consulta: para identificar
consultas de execução lenta que podem
estar afetando o desempenho, analise os
planos de execução de consultas e
identifique o gargalos.
▪ Replicação do banco de dados: para
ambientes de banco de dados replicados, o
desempenho da replicação garante que os
dados sejam replicados corretamente e em
tempo hábil.
▪ Backups: monitore os backups do banco de
dados para garantir que eles sejam
concluídos com sucesso e dentro da
janela. É necessário testá-los! O teste é para
garantir que o restore será feito
adequadamente.
▪ Vejam que são muitas métricas e o sistema
de alertas com a metodologia de
classificação critical, major e minor,
funciona muito bem.
SUGESTÃO DE MONITORAMENTO DE ITENS
COMO OLHAR/DETERMINAR
CORREAMENTE O
ESCOPO DE ATUAÇÃO?
UNIDADE III – OPERAÇÃO DE AMBIENTES
DE BANCO DE DADOS
MONITORAMENTO DE
AMBIENTES DE PRODUÇÃO
ESTRATÉGIA PARA
MONITORAMENTO DE
AMBIENTES
A ESTRATÉGIA DE MONITORAMENTO (LEMBRANDO)
▪ Tendo em vista que precisamos, enquanto
DBAs, garantir a disponibilidade do
ambiente, otimização da performance,
redução de riscos de segurança e, na
maioria das vezes comprovar requisitos de
conformidade com alguma norma, é
importantíssimo definirmos uma estratégia
de monitoramento.
▪ O foco base é reduzir tempo de resposta a
eventos adversos.
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ Defina seus objetivos: O que você deseja
alcançar com sua estratégia de
monitoramento? Defina suas metas e
objetivos em termos de disponibilidade,
desempenho e segurança do sistema.
▪ PORQUE?
▪ Porque você precisa saber se tem recursos
internos para atacar os problemas com
ferramentas, pessoas, processos definido
questões como:
✓ Definição de ferramentas;
✓ Treinamento de pessoal;
✓ Momento de atuação no apontamento;
✓ Orçamento para ações;
✓ Aquisição de ferramentas;
✓ Pagamento de plantão e Hora extra;
✓ Terceirização da operação;
✓ Contratação de serviços em nuvem;
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ Identifique os componentes
críticos: é necessário determinar
quais componentes de sua
infraestrutura de banco de dados são
mais críticos para suas operações de
negócios.
▪ Isso pode incluir servidores de
banco de dados, sistemas de
armazenamento, conexões de rede
e aplicativos ou serviços em
nuvem.
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ O processo de gestão de
configuração para ambientes de
produção te apoia no mapeamento e
gestão instâncias e componentes da
infraestrutura de banco de dados de
maneira centralizada.
▪ É uma disciplina do ITIL que tem a
sugestão de melhores práticas para
implantação porém o que vale
destacar aqui é o inventário de
ativos para o serviço.
GERENCIAMENTO DE CONFIGURAÇÃO
▪ Pode-se obter recursos como
controle de versão, conformidade
e recomendações de ajuste de
desempenho de forma automática.
▪ MS-;SQL Server Configuration
Manager, Oracle Enterprise
Manager, Dbmaestro, MongoDB
Ops Manager, Puppet, Ansible,
Chef, SaltStack, DataStax
OpsCenter, Bigtable-Hbase, são
várias!
FERRAMENTAS DE GESTÃO DE CONFIGURAÇÃO
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ Escolher e configurar ferramentas de
monitoramento: escolha ferramentas de
monitoramento capazes de coletar e analisar
os dados necessários para monitorar seus
componentes críticos com eficiência.
▪ Há ferramentas open que são bem populares
no mercado como: Nagios, Zabbix e
Prometheus.
▪ Lembre-se das questões orçamentárias
para definir esta escola!
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ Defina suas métricas de monitoramento:
determine quais métricas você acompanhará
para medir a integridade e o plano de ação
para caso cada uma delas seja violada.
▪ Não é eficiente monitorar métricas que não
objetivos bem claros.
▪ Atente-se à natureza de arquitetura do banco
de dados escolhido pois em bancos de dados
não relacionais a observação deve ser
diferente.
▪ Configure alertas e notificações: configure
suas ferramentas de monitoramento para
gerar alertas e notificações quando limites
específicos forem excedidos ou quando uma
atividade incomum for detectada.
▪ Esta definição irá te ajudar a não ficar
olhando aqueles 80% de acontecimentos que
não tem impacto direto na operação (regra de
Pareto).
▪ Apesar de olhar tudo o que aparece é crítico!
MONTANDO A ESTRATÉGIA DE MONITORAMENTO
▪ Teste e refine sua estratégia: teste sua
estratégia de monitoramento regularmente
para garantir que ela esteja funcionando de
maneira eficaz.
▪ Analise os dados coletados e use-os para
refinar suas métricas e procedimentos de
monitoramento ao longo do tempo.
▪ Dica de ouro: Contabilize o quanto custa o
ambiente parado para contrapor ao
investimento em monitoramento!

AMBIENTES E FERRAMENTAS
DE SUPORTE À GESTÃO E OPERAÇÃO
DE SGBD’S
ARQUITETURA DE DADOS
PARA MONITORAMENTO
DE APLICAÇÕES
O QUE A ARQUITETURA DEFINE
▪ Para construir soluções de monitoramento devem
ser levados em consideração os seguintes itens:
✓ Coleta de dados: precisam ler dados de
várias fontes utilizando métodos diversos
como APIs, arquivos de log, monitoramento
de tráfego de rede.
✓ Processamento dos dados: o processamento
dos dados identifica tendências e anomalias.
Estão envolvidas aqui técnicas como ML,
reconhecimento de padrões e estatística. Fonte: Gartner,2022
▪ Alertas e relatórios: os alertas precisam
ser gerados para notificar os
administradores e operadores sobre as
anomalias. Devem entregar também
relatórios consolidados sobre
desempenho e disponibilidade.
▪ Integração: precisam se integrar com
outras soluções.
▪ Personalização: devem atender a
demanda específica do negócio. Fonte: Gartner,2022
O QUE A ARQUITETURA DEFINE
VAMOS INICIAR COM O CONCEITO DE APM
▪ Application Performance Management
(APM) é a prática de monitorar e gerenciar o
desempenho e a disponibilidade de
aplicativos de software.
▪ Não faz muito sentido monitorarmos as
coisas de forma separada, o que as
ferramentas fazem hoje é uma entrega
centralizada da visualização de todas as
informações.
▪ Esta análise foca na infraestrutura. Fonte: Gartner,2022
▪ Esta categoria de ferramentas (APM)
geralmente monitoram vários aspectos do
desempenho de um aplicativo, incluindo seu
tempo de resposta, utilização de recursos e
outras métricas que podem ajudar a identificar
problemas e otimizar o desempenho.
▪ Podem envolver a análise de logs de
aplicativos e outros dados para identificar
padrões e tendências que podem ajudar a
identificar possíveis gargalos de desempenho.
Fonte: Gartner,2022
VAMOS INICIAR COM O CONCEITO DE APM
UM NOVO TERMO NO MERCADO
▪ O termo mais evoluído que iremos ouvir no
mercado é o de observabilidade.
▪ Refere-se à capacidade de observar e
entender o desempenho, o comportamento
e o estado de um sistema, aplicativo ou
serviço, por meio de suas saídas ou
interações externas, sem necessariamente
ter acesso direto ao seu funcionamento
interno.
ONDE ENTRA A NUVEM NESTA CONVERSA TODA?
▪ O objetivo da observabilidade é permitir que
as equipes detectem e diagnostiquem
problemas rapidamente, identifiquem
possíveis gargalos de desempenho e
entendam como diferentes componentes de um
sistema interagem entre si.
▪ Tornou-se aspecto crítico para a entrega de
softwares, particularmente em sistemas
distribuídos, onde os componentes de um
sistema podem estar espalhados por várias
máquinas, redes e data centers (CLOUD).

MONITORAMENTO DE
BANCOS DE DADOS
EM NUVEM
PORQUE IR PARA A NUVEM?
▪ A opção mais discutida no mercado é a
possibilidade de operar seu banco de dados
em nuvem.
▪ Dentro dos modelos de comercialização
cloud, IaaS, PaaS, SaaS, relembrando, o que
faz mais sentido para o nosso escopo de
atuação de banco de dados é a contratação de
PaaS.
▪ Há algumas vantagens de se adotar este
modelo, veja.
▪ Gerenciamento de banco de dados
simplificado: com a modalidade PaaS, o
provedor de nuvem gerencia a infraestrutura
e o software básico para você, incluindo
atualizações, patches e backups.
▪ Alta disponibilidade e escalabilidade: o
provedor contratado fornece recursos
integrados de alta disponibilidade e
escalabilidade, como failover automático e
dimensionamento horizontal (banco de dados
distribuído).
PORQUE IR PARA A NUVEM?
▪ Economia de custos: a oferta podem ser
mais econômica do que as soluções locais
tradicionais ou IaaS, pois os usuários pagam
apenas pelos recursos que usam, em vez de
provisionar e gerenciar sua própria
infraestrutura de hardware e software.
▪ Porém, sob esta ótica, pode ser um grande
problema pois aplicações não otimizadas
consumirão mais e por este motivo as
funções de monitoramento e
observabilidade são fundamentais!
PORQUE IR PARA A NUVEM?
▪ Segurança e conformidade: normalmente
esta oferta possui recursos integrados de
segurança e conformidade, como
criptografia, controles de acesso e registro
de auditoria.
▪ Isso pode ajudar os usuários a atender aos
requisitos regulamentares e proteger dados
confidenciais.
▪ Reduzimos a mão de obra especializada e o
conhecimento avançado de infra no time.
PORQUE IR PARA A NUVEM?
▪ Implantação rápida: na oferta PaaS
consegue-se implantar o schemas de banco
de dados de forma rápida e fácil, geralmente
com apenas alguns cliques ou chamadas de
API.
▪ Com a implantação das metodologias ágeis
esta escolha apoia os usuários a acelerar os
cronogramas de desenvolvimento e
implantação de aplicativos e responder
rapidamente às necessidades de negócios em
constante mudança.
PORQUE IR PARA A NUVEM?
MAS O MONITORAMENTO MUDA?
▪ Observe que no próprio quadrante do Gartner já
aparecem soluções de monitoramento em nuvem.
▪ O procedimento é o mesmo de configurar um
ambiente on premise.
▪ É mais simples porque a escolha da ferramenta
não precisará ser feita pois será a ofertada pelo
provedor.
▪ A vantagem é a oferta destes dados via API para
que você possa consumir de qualquer ferramenta
o que é uma regra da cloud.
▪ Amazon Web Services (AWS) fornece
Amazon CloudWatch, que pode ser usado
para monitorar métricas para vários serviços
da AWS, incluindo bancos de dados como
Amazon RDS (Relational Database
Service) e Amazon Aurora.
▪ O CloudWatch é um repositório centralizado
para monitoramento e coleta de métricas,
logs e eventos de seus recursos da AWS.
MAS O MONITORAMENTO MUDA?
▪ Microsoft Azure fornece o Azure Monitor,
que pode ser usado para monitorar o Banco de
Dados SQL do Azure, o Banco de Dados do
Azure para MySQL e o Banco de Dados do
Azure para PostgreSQL.
▪ Azure Monitor fornece uma exibição
unificada de métricas de desempenho e logs em
todos os seus recursos do Azure, incluindo
bancos de dados, e pode ser usado para
detectar problemas, solucionar problemas e
otimizar o desempenho.
MAS O MONITORAMENTO MUDA?
▪ Google Cloud Platform fornece o
Stackdriver Monitoring, que pode ser usado
para monitorar métricas e registros de vários
serviços GCP, incluindo Cloud SQL, um
serviço de banco de dados totalmente
gerenciado.
▪ O Stackdriver Monitoring permite monitorar
o desempenho do banco de dados, a utilização
de recursos e a disponibilidade, além de
fornecer uma visão unificada de métricas e
registros em todos os seus recursos do GCP.
MAS O MONITORAMENTO MUDA?
▪ Oracle Cloud Infrastructure Monitoring
fornece monitoramento em tempo real das
principais métricas de desempenho para seu
ambiente de banco de dados, como uso de
CPU, uso de memória, uso de disco e tráfego
de rede.
▪ Suporta configuração de alarmes com base em
limites predefinidos ou métricas personalizadas
para envio de notificações quando condições
específicas forem atendidas.
MAS O MONITORAMENTO MUDA?
▪ Oracle Management Cloud fornece
recursos avançados de monitoramento e
gerenciamento para seu ambiente de banco
de dados Oracle, incluindo monitoramento
proativo, análise de desempenho e análise de
log.
▪ Inclui um painel unificado para monitorar
todo o seu ambiente de TI, incluindo suas
instâncias de banco de dados.
MAS O MONITORAMENTO MUDA?
▪ Oracle Database Performance Monitoring
fornece monitoramento e diagnóstico de
desempenho em tempo real para suas
instâncias de banco de dados Oracle,
incluindo análise SQL e recomendações de
ajuste.
▪ Vejam como é mais especializado.
▪ E tem o autonomus database que é uma
oferta diferenciada para bancos relacionais.
MAS O MONITORAMENTO MUDA?
▪ Oracle Autonomous Database é um serviço
de banco de dados baseado em nuvem
oferecido pela Oracle Cloud que utiliza
algoritmos de aprendizado de máquina e
automação para fornecer um ambiente de
banco de dados autônomo, auto protegido e
autorreparável.
▪ O serviço Autonomous Database inclui as
ofertas Autonomous Transaction
Processing (ATP) e Autonomous Data
Warehouse (ADW).
MAS O MONITORAMENTO MUDA?
▪ É um ambiente de banco de dados totalmente
gerenciado que automatiza muitas das tarefas
de rotina que tradicionalmente requerem
intervenção humana, como correção de
software, ajuste de banco de dados e
gerenciamento de segurança.
▪ O serviço de banco de dados foi projetado
para ser altamente disponível e escalável,
com backups automáticos, replicação e
recursos de failover incorporados.
MAS O MONITORAMENTO MUDA?
E OS BANCOS NOSQL? SÃO A MESMA COISA?
▪ As ferramentas são basicamente as mesmas
porém as estratégias podem ser um pouco
diferentes.
▪ Esses serviços permitem monitorar métricas
como capacidade de leitura e gravação,
latência e erros, replicação e etc.
▪ Posso utilizar CloudWatch para monitorar
Amazon DynamoDB e Azure Monitor para
monitorar Azure Cosmos DB.
▪ São muitas ferramentas e tecnologias, não é?
▪ MongoDB Atlas fornece monitoramento e
alertas em tempo real para bancos de dados
MongoDB na nuvem.
▪ DataStax Enterprise fornece recursos
abrangentes de monitoramento e alerta para
bancos de dados Apache Cassandra.
▪ É possível personalizar soluções para seu
ambiente de banco de dados NoSQL usando
ferramentas de código aberto como
Prometheus, Grafana ou Nagios.
▪ Imagine então quando tivermos tecnologias múltiplas e tivermos que dominar, além dos
recursos que estão sob nossa gestão ambientes com REPLICAÇÃO, SHARDING e
CLUSTERIZAÇÃO de dados!
