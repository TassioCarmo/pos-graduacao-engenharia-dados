UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOS
A IMPORTÂNCIA
DO PROJETO OU DESIGN
▪ Trabalhar com performance é entender profundamente do aplicativo, do SGBD que você
escolheu, sua interação com o sistema operacional e o funcionamento físico do tipo de
hardware escolhido.
▪ A maior parte das teorias de tunning (otimização) te mostram as regras práticas mas não
informam as limitações.
▪ Uma regra simples que precisa ser observada é que transações longas que acessam
grandes conjuntos de dados compartilhados podem atrasar transações on-line
simultâneas!
▪ O desempenho do aplicativo depende de muitos fatores, mas a causa evitável mais
frequente de baixo desempenho é o banco de dados.
PORQUE O TRABALHO DE PERFORMANCE É DIFÍCIL!?
▪ A movimentação de dados do disco para o
SGBD e dele para o aplicativo envolve os
componentes mais lentos da infraestrutura
do aplicativo – as unidades de disco e a rede.
▪ Passa a ser fundamental que o código do
aplicativo que interage com o banco de dados
e o próprio banco de dados seja ajustado
para desempenho premium.
Fonte: SHARMA, 2021.
A MOVIMENTAÇÃO DOS DADOS
▪ O foco do projeto de um banco de dados
tem que ser a recuperação deste dado.
▪ Se você projetar um banco de dados
incorretamente, será difícil recuperar certos
tipos de informações e você correrá o risco
de que suas pesquisas produzam informações
imprecisas.
▪ Hoje os bancos de dados influenciam como
as empresas viabilizam seus negócios! Fonte: GHISLENI, 2021.
Fonte: BRASIL PARALELO, 2022.
A IMPORTÂNCIA DO DESIGN
▪ O design lógico do banco de dados descreve
o tamanho, a forma e os sistemas necessários
para um banco de dados
▪ Atende às necessidades informacionais e
operacionais do negócio.
▪ Em seguida, você constrói a implementação
física do projeto de banco de dados lógico.
▪ Cria a estrutura, configurar relacionamentos
e estabelece os níveis apropriados de
integridade de dados. Fonte: BOTTURA, 2014.
A IMPORTÂNCIA DO DESIGN: RELEMBRANDO OS PASSOS
▪ Conhecer as teorias é ter a possibilidade de prever o que acontecerá se você executar uma
determinada ação ou série de ações.
▪ No caso dos SGBDs o conhecimento de seu funcionamento baseando-se na teoria como
ele funciona te permite extrair os dados da forma mais performática possível.
▪ Os banco de dados relacionais baseiam-se em dois ramos da matemática conhecidos
como teoria dos conjuntos e lógica de predicados de primeira ordem.
▪ Bancos de dados não relacionais aproveitam parte destas teorias e utilizam outras como
teoria dos grafos além de modificar a forma de organização dos registros como orientação
a documentos ficando livres dos esquemas fixos e definição de tipos de dados.
TEORIAS E O QUE ELAS PODEM AJUDAR NO PROCESSO
▪ Uma boa metodologia o ajuda a reconhecer
erros em seu projeto e fornece as ferramentas
para corrigi-los.
▪ E como sempre falamos: Ferramenta certa
para cada tipo de problema!
▪ Metodologias de Design podem ser vistas
como estas ferramentas que irão apoiá-lo.
▪ Focando a longo prazo, você não precisará
alterar estrutura mal projetada quando estiver
em momentos críticos. Fonte: https://www.recadosface.com/img-1261.html
A IMPORTÂNCIA DO DESIGN: METODOLOGIAS▪ Uma boa metodologia o ajuda a reconhecer
erros em seu projeto e fornece as ferramentas
para corrigi-los.
▪ E como sempre falamos: Ferramenta certa
para cada tipo de problema!
▪ Metodologias de Design podem ser vistas
como estas ferramentas que irão apoiá-lo.
▪ Focando a longo prazo, você não precisará
alterar estrutura mal projetada quando estiver
em momentos críticos. Fonte: https://www.recadosface.com/img-1261.html


UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOSPERFORMANCE DE
AMBIENTES DE DADOS
TIPOS DE BANCO
E OS CURSORES
A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE
▪ Os tipos de bancos de dados irão nos dizer
como funcionam os mecanismos para
recuperação de dados de nosso interesse.
▪ A natureza do negócio e a necessidade de
atendimento ao requisito do cliente, (VIDE
DESIGN) indicam que a escolha do tipo de
banco de dados faz toda a diferença.
▪ Evoluindo de arquiteturas centralizadas como
o Mainframe até a cloud há mudanças.
Fonte: AUTOR, 2021.
▪ O QUE ME INDICA UMA MELHOR ESCOLHA DO TIPO DE BANCO DE
DADOS QUE IREI UTILIZAR?
▪ A funcionalidade básica que irá atender ao negócio.
▪ O momento da operação não é um bom momento para tentar fazer tunning de banco de
dados para resolver um problema que não é o especialista em resolver.
▪ Mais que isto, temos os recursos ofertados que podem não atender ao requisito do
negócio.
▪ É importante conhecer as principais funções de cada tipo para não perder tempo na
operação!
A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE
▪ Banco de dados Relacional: armazena dados em colunas com a sua descrição nas linhas
e atributos; segue regras de normalização de dados que remetem a relacionamentos.
▪ Banco de dados Não-Relacional: recomendado para dados não estruturados como
vídeos, imagens e/ou gráficos, que não podem ser dispostos em tabelas; não é necessário o
uso de um sistema de relacionamento.
▪ Banco de dados orientado para objetos: a estrutura do banco de dados é voltada para
objetos; as informações são dispostas em blocos e têm identificadores.
▪ Banco de dados distribuído: cada um dos nós representa um computador, que está em
local físico diferente (ou não); são conectados pela Internet e compartilham dados.
A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE▪ Banco de dados Relacional: armazena dados em colunas com a sua descrição nas linhas
e atributos; segue regras de normalização de dados que remetem a relacionamentos.
▪ Banco de dados Não-Relacional: recomendado para dados não estruturados como
vídeos, imagens e/ou gráficos, que não podem ser dispostos em tabelas; não é necessário o
uso de um sistema de relacionamento.
▪ Banco de dados orientado para objetos: a estrutura do banco de dados é voltada para
objetos; as informações são dispostas em blocos e têm identificadores.
▪ Banco de dados distribuído: cada um dos nós representa um computador, que está em
local físico diferente (ou não); são conectados pela Internet e compartilham dados.
A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE
▪ Banco de dados gráfico: as estruturas complexas são armazenadas e as informações
ficam interligadas por grafos de conexão; a informação importa mais que a própria
estrutura.
▪ Banco de dados em modelo de rede: trabalham com uma estrutura de lista invertida que
contém arquivos, registros e campos; não segue e nem exige regras de normalização.
▪ Banco de dados em cloud: precisamos do acesso à Internet para acessar os dados; há uma
mudança arquitetural enorme pois os dados ficam no provedor e são gerenciados por
ele.
A ORGANIZAÇÃO ESTRUTURAL É IMPORTANTE
▪ CURSOR é um recurso importante
oferecido pelo SGBD.
▪ NA PRÁTICA: cursores são áreas de
memória que armazenam o resultado de
uma consulta.
▪ Podem ser implícitos: quando não precisam
ser declarados no código ou explícitos:
quando precisam ser descritos no código.
JÁ OUVIU FALAR DISTO, MAS SABE O QUE É?
Fonte: DEVMEDIA, 2006.
Fonte: SILVA, 2016.
Fonte: MONGO, 2022.
Fonte: REDIS, 2022.▪ CURSOR é um recurso importante
oferecido pelo SGBD.
▪ NA PRÁTICA: cursores são áreas de
memória que armazenam o resultado de
uma consulta.
▪ Podem ser implícitos: quando não precisam
ser declarados no código ou explícitos:
quando precisam ser descritos no código.
JÁ OUVIU FALAR DISTO, MAS SABE O QUE É?
Fonte: DEVMEDIA, 2006.
Fonte: SILVA, 2016.
Fonte: MONGO, 2022.
Fonte: REDIS, 2022.
▪ Os cursores somente leitura ajudam os
usuários a navegar pelo conjunto de
resultados, e os cursores de leitura/gravação
podem implementar atualizações de linha
individuais.
▪ Os cursores devem ser uma das últimas
técnicas escolhida para recuperar os dados, e
você deve escolher o cursor com o impacto
mais baixo possível.
▪ VERIFIQUE O CLIENT DE CONEXÃO!
JÁ OUVIU FALAR DISTO, MAS SABE O QUE É?
Fonte: DEVMEDIA, 2006.
Fonte: SILVA, 2016.
Fonte: MONGO, 2022.
Fonte: REDIS, 2022.▪ Os cursores somente leitura ajudam os
usuários a navegar pelo conjunto de
resultados, e os cursores de leitura/gravação
podem implementar atualizações de linha
individuais.
▪ Os cursores devem ser uma das últimas
técnicas escolhida para recuperar os dados, e
você deve escolher o cursor com o impacto
mais baixo possível.
▪ VERIFIQUE O CLIENT DE CONEXÃO!
JÁ OUVIU FALAR DISTO, MAS SABE O QUE É?
Fonte: DEVMEDIA, 2006.
Fonte: SILVA, 2016.
Fonte: MONGO, 2022.
Fonte: REDIS, 2022.
OS RECURSOS PRECISAM SER AVALIADOS
▪ A utilização de cursores nem sempre é uma
boa alternativa, principalmente em aplicações
que precisam de atualização em tempo real
ou seja, que possuem muita concorrência.
▪ Conforme observamos cada SGBD possui
características de funcionamento específicas
que precisam ser observadas.
▪ Tipos de chave, estruturação, método de
acesso e plano de execução são algumas. Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.OS RECURSOS PRECISAM SER AVALIADOS
▪ A utilização de cursores nem sempre é uma
boa alternativa, principalmente em aplicações
que precisam de atualização em tempo real
ou seja, que possuem muita concorrência.
▪ Conforme observamos cada SGBD possui
características de funcionamento específicas
que precisam ser observadas.
▪ Tipos de chave, estruturação, método de
acesso e plano de execução são algumas. 


UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOS
INDEXAÇÃO
COMO O BANCO ARMAZENA OS DADOS?
▪ Os princípios que iremos mostrar nesta
conversa se aplicam aos bancos de dados
relacionais.
▪ Quando utilizamos outros tipos de bancos de
dados precisaremos fazer uma pequena
adaptação conceitual mas podemos verificar
que todos eles são plenamente aplicáveis.
▪ Vamos falar da organização do
armazenamento e do mecanismo de
recuperação índice! Fonte: DEVMEDIA, 2007.
▪ Registros são armazenados em
páginas de 8Kb, que tem um header
que contém links para as outras
páginas e hash.
▪ São agrupados de 8 em 8 formando
este conjunto de extensão.
▪ Os registros de dados não são armazenados em uma ordem específica, e não existe uma
ordenação sequente para as páginas de dados.
▪ É utilizado um conceito de organização que se chama pilha, e quando a capacidade das
páginas de dados se esgota estabelece-se um link que as liga.
▪ Vamos a duas formas básicas de método de acesso para recuperação de dados:
▪ Exame de tabela: examina todas as páginas de dados das tabelas, começando do início da
tabela passando por todos os registros, extraindo aqueles que satisfazem aos critérios da
consulta.
▪ Usando índices: percorrendo a estrutura da árvore do índice para localizar os registros.
UM RECURSO MUITO PODEROSO
▪ Um índice para uma tabela é uma organização de dados que permite que permite acelerar
o processamento de consultas, por comparação, extraindo somente aqueles registros
necessários para satisfazerem os critérios passados pela consulta.
Fonte: PEDROZO & VAZ, 2007.
▪ Uma árvore B+ é uma árvore
balanceada cujas folhas contêm
uma sequência de pares chaves-
ponteiro.
▪ As chaves são ordenadas pelo seu
valor.
UM RECURSO MUITO PODEROSO
▪ Esta árvore é do tipo balanceada e projetada
para facilitar a interação com dispositivos de
armazenamento secundário como disco
magnético.
▪ A ideia é tentar melhorar a questão do I/O
nestes dispositivos diminuindo o tempo de
acesso.
▪ Se o braço puder apontar para o lugar certo
de recuperação do registro, agiliza-se a
leitura. Fonte: GHISLENI, 2021.
UM RECURSO MUITO PODEROSO▪ Esta árvore é do tipo balanceada e projetada
para facilitar a interação com dispositivos de
armazenamento secundário como disco
magnético.
▪ A ideia é tentar melhorar a questão do I/O
nestes dispositivos diminuindo o tempo de
acesso.
▪ Se o braço puder apontar para o lugar certo
de recuperação do registro, agiliza-se a
leitura. Fonte: GHISLENI, 2021.
UM RECURSO MUITO PODEROSO
UM OLHO NAS MÉTRICAS E OUTRO NO OTIMIZADOR
▪ Então vamos supor que eu seja chamado para
diagnosticar um problema, observe o cenário:
▪ Olho para as métricas críticas de desempenho
do sistema operacional, duas coisas se
destacam: a CPU e o I/O no disco primário.
Tanto a média de carga da CPU quanto as
latências de E/S do disco sugerem que o
sistema precisa de mais capacidade de CPU e
I/O. Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
UM OLHO NAS MÉTRICAS E OUTRO NO OTIMIZADOR
▪ Um componente de subsistema muito
importante é o otimizador de consultas que é
quem define qual o método será mais
eficiente para recuperar os dados.
▪ Entra aqui um recurso que quase todos os
bancos tem que é o EXPLAIN ainda não
vamos entrar neste assunto.
▪ Vamos apenas nos ater aos índices e seus
tipos.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022
TIPOS DE ÍNDICES
▪ Índices clusterizados, não clusterizados e de
hashing
▪ Índice de árvore B*
▪ Índice de bitmap
▪ Índice TTL (Time To Live)
▪ Índice Geoespacial
▪ Índice de várias tabelas
▪ Índice booleano
▪ Índice funcional
Fonte: REIS, 2019
VOLTANDO AO PROBLEMA...
▪ Então vamos supor que eu seja chamado para
diagnosticar um problema, observe o cenário:
▪ Olho para as métricas críticas de desempenho
do sistema operacional, duas coisas se
destacam: a CPU e o I/O no disco primário.
Tanto a média de carga da CPU quanto as
latências de E/S do disco sugerem que o
sistema precisa de mais capacidade de CPU e
I/O. Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
UTILIZAÇÃO DE ÍNDICES
▪ Lembrem-se novamente das dicas de
DESIGN, conheçam o problema de negócio.
▪ Uma pergunta simples seria a quantidade de
transações de gravação e quantas de
recuperação teremos nas funcionalidades
principais.
▪ Qual a prioridade do negócio?
▪ Índice é uma das ferramentas de otimização
mais conhecidas e utilizadas pelos
desenvolvedores de bancos de dados.
Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
▪ A indexação em tabelas pode aumentar
significativamente a performance em
consultas ao banco de dados.
▪ Só que pode diminuir a velocidade de
transações como inserts e updates.
▪ Porque é necessário balancear a árvore!
▪ Senão não faz sentido manter o índice,
concorda?
▪ Reorganização de índices devem ser feitos
periodicamente por este motivo!

UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOS
INDEXAÇÃO
COMO O BANCO ARMAZENA OS DADOS?
▪ Os princípios que iremos mostrar nesta
conversa se aplicam aos bancos de dados
relacionais.
▪ Quando utilizamos outros tipos de bancos de
dados precisaremos fazer uma pequena
adaptação conceitual mas podemos verificar
que todos eles são plenamente aplicáveis.
▪ Vamos falar da organização do
armazenamento e do mecanismo de
recuperação índice! Fonte: DEVMEDIA, 2007.
▪ Registros são armazenados em
páginas de 8Kb, que tem um header
que contém links para as outras
páginas e hash.
▪ São agrupados de 8 em 8 formando
este conjunto de extensão.
▪ Os registros de dados não são armazenados em uma ordem específica, e não existe uma
ordenação sequente para as páginas de dados.
▪ É utilizado um conceito de organização que se chama pilha, e quando a capacidade das
páginas de dados se esgota estabelece-se um link que as liga.
▪ Vamos a duas formas básicas de método de acesso para recuperação de dados:
▪ Exame de tabela: examina todas as páginas de dados das tabelas, começando do início da
tabela passando por todos os registros, extraindo aqueles que satisfazem aos critérios da
consulta.
▪ Usando índices: percorrendo a estrutura da árvore do índice para localizar os registros.
UM RECURSO MUITO PODEROSO
▪ Um índice para uma tabela é uma organização de dados que permite que permite acelerar
o processamento de consultas, por comparação, extraindo somente aqueles registros
necessários para satisfazerem os critérios passados pela consulta.
Fonte: PEDROZO & VAZ, 2007.
▪ Uma árvore B+ é uma árvore
balanceada cujas folhas contêm
uma sequência de pares chaves-
ponteiro.
▪ As chaves são ordenadas pelo seu
valor.
UM RECURSO MUITO PODEROSO
▪ Esta árvore é do tipo balanceada e projetada
para facilitar a interação com dispositivos de
armazenamento secundário como disco
magnético.
▪ A ideia é tentar melhorar a questão do I/O
nestes dispositivos diminuindo o tempo de
acesso.
▪ Se o braço puder apontar para o lugar certo
de recuperação do registro, agiliza-se a
leitura. Fonte: GHISLENI, 2021.
UM RECURSO MUITO PODEROSO▪ Esta árvore é do tipo balanceada e projetada
para facilitar a interação com dispositivos de
armazenamento secundário como disco
magnético.
▪ A ideia é tentar melhorar a questão do I/O
nestes dispositivos diminuindo o tempo de
acesso.
▪ Se o braço puder apontar para o lugar certo
de recuperação do registro, agiliza-se a
leitura. Fonte: GHISLENI, 2021.
UM RECURSO MUITO PODEROSO
UM OLHO NAS MÉTRICAS E OUTRO NO OTIMIZADOR
▪ Então vamos supor que eu seja chamado para
diagnosticar um problema, observe o cenário:
▪ Olho para as métricas críticas de desempenho
do sistema operacional, duas coisas se
destacam: a CPU e o I/O no disco primário.
Tanto a média de carga da CPU quanto as
latências de E/S do disco sugerem que o
sistema precisa de mais capacidade de CPU e
I/O. Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
UM OLHO NAS MÉTRICAS E OUTRO NO OTIMIZADOR
▪ Um componente de subsistema muito
importante é o otimizador de consultas que é
quem define qual o método será mais
eficiente para recuperar os dados.
▪ Entra aqui um recurso que quase todos os
bancos tem que é o EXPLAIN ainda não
vamos entrar neste assunto.
▪ Vamos apenas nos ater aos índices e seus
tipos.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022
TIPOS DE ÍNDICES
▪ Índices clusterizados, não clusterizados e de
hashing
▪ Índice de árvore B*
▪ Índice de bitmap
▪ Índice TTL (Time To Live)
▪ Índice Geoespacial
▪ Índice de várias tabelas
▪ Índice booleano
▪ Índice funcional
Fonte: REIS, 2019
VOLTANDO AO PROBLEMA...
▪ Então vamos supor que eu seja chamado para
diagnosticar um problema, observe o cenário:
▪ Olho para as métricas críticas de desempenho
do sistema operacional, duas coisas se
destacam: a CPU e o I/O no disco primário.
Tanto a média de carga da CPU quanto as
latências de E/S do disco sugerem que o
sistema precisa de mais capacidade de CPU e
I/O. Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
UTILIZAÇÃO DE ÍNDICES
▪ Lembrem-se novamente das dicas de
DESIGN, conheçam o problema de negócio.
▪ Uma pergunta simples seria a quantidade de
transações de gravação e quantas de
recuperação teremos nas funcionalidades
principais.
▪ Qual a prioridade do negócio?
▪ Índice é uma das ferramentas de otimização
mais conhecidas e utilizadas pelos
desenvolvedores de bancos de dados.
Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
Fonte: https://livecoins.com.br/permissao-para-bancos-guardarem-
bitcoin-pode-ser-sinal-de-desespero-do-sistema-financeiro/.
▪ A indexação em tabelas pode aumentar
significativamente a performance em
consultas ao banco de dados.
▪ Só que pode diminuir a velocidade de
transações como inserts e updates.
▪ Porque é necessário balancear a árvore!
▪ Senão não faz sentido manter o índice,
concorda?
▪ Reorganização de índices devem ser feitos
periodicamente por este motivo!

UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOS
OTIMIZAÇÃO
DE CONSULTAS
▪ O principal motivo da utilização de SGBDs é a recuperação de dados.
▪ A escolha do SGBD mais adequado ao atendimento dos requisitos de negócio é o ponto
de partida mas que nem sempre acontece.
▪ A organização e estruturação dos arquivos de dados além da forma como o SGBD os
gerencia são parte fundamental para a análise e o bom desempenho da entrega.
▪ Esta entrega é feita através das consultas que são escritas.
▪ Utilização de índices são boas inciativas que devem ser utilizadas com cuidado para não
prejudicar ainda mais o desempenho
EM RESUMO...▪ O principal motivo da utilização de SGBDs é a recuperação de dados.
▪ A escolha do SGBD mais adequado ao atendimento dos requisitos de negócio é o ponto
de partida mas que nem sempre acontece.
▪ A organização e estruturação dos arquivos de dados além da forma como o SGBD os
gerencia são parte fundamental para a análise e o bom desempenho da entrega.
▪ Esta entrega é feita através das consultas que são escritas.
▪ Utilização de índices são boas inciativas que devem ser utilizadas com cuidado para não
prejudicar ainda mais o desempenho
EM RESUMO...
A OTIMIZAÇÃO DE CONSULTAS
▪ A otimização de consulta é a arte de
encontrar a maneira mais eficiente de
recuperar um dado em um SGBD.
▪ Executando-se esta técnica é possível
melhorar o desempenho das consultas ao
banco de dados, com foco na redução de
tempo e dos recursos necessários para
executá-las.
▪ Envolve análise de consultas e seus planos de
execução para identificar ineficiências. Fonte: DEVMEDIA, 2007.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022
▪ Trabalhar na otimização de consultas nos permitirá melhorar o SGBD nos quesitos:
✓ Aumentar a concorrência de acessos a consultas
✓ Reduzir os custos associados à infraestrutura e manutenção do SGBD
✓ Melhorar a confiabilidade e a escalabilidade
✓ Ajuda a decidir sobre a utilização de técnicas como particionamento,
clustering e balanceamento de carga
✓ Pode apontar o uso de unidades de disco mais performáticas como SSD e
ou bancos de dados na memória
A OTIMIZAÇÃO DE CONSULTAS
MAS COMO COMEÇAR A FAZER ISTO?
▪ PLANO DE EXECUÇÃO é um conjunto de
etapas que o algoritmo do SGBD, através do
seu subsistema otimizador de consultas, usa
para executar uma consulta.
▪ Determina a rapidez com que uma consulta
será executada e pode melhorar
significativamente o desempenho da
consulta.
▪ Plano mal projetado gera lentidão ou falha
na resposta a uma consulta. Fonte: DEVMEDIA, 2007.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022MAS COMO COMEÇAR A FAZER ISTO?
▪ PLANO DE EXECUÇÃO é um conjunto de
etapas que o algoritmo do SGBD, através do
seu subsistema otimizador de consultas, usa
para executar uma consulta.
▪ Determina a rapidez com que uma consulta
será executada e pode melhorar
significativamente o desempenho da
consulta.
▪ Plano mal projetado gera lentidão ou falha
na resposta a uma consulta. Fonte: DEVMEDIA, 2007.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022
O QUE É O PLANO DE EXECUÇÃO?
▪ A otimização de consulta é a arte de
encontrar a maneira mais eficiente de
recuperar um dado em um SGBD.
▪ Executando-se esta técnica é possível
melhorar o desempenho das consultas ao
banco de dados, com foco na redução de
tempo e dos recursos necessários para
executá-las.
▪ Envolve análise de consultas e seus planos de
execução para identificar ineficiências. Fonte: DEVMEDIA, 2007.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022O QUE É O PLANO DE EXECUÇÃO?
▪ A otimização de consulta é a arte de
encontrar a maneira mais eficiente de
recuperar um dado em um SGBD.
▪ Executando-se esta técnica é possível
melhorar o desempenho das consultas ao
banco de dados, com foco na redução de
tempo e dos recursos necessários para
executá-las.
▪ Envolve análise de consultas e seus planos de
execução para identificar ineficiências. Fonte: DEVMEDIA, 2007.
Fonte: HARRISON, 2017
Fonte: ORACLE, 2022
▪ Existem métricas que o SGBD utiliza para criar um plano de execução baseado em cálculo
de custo, que tem peso em cada uma das variáveis utilizadas para calcular:
✓ Tamanho das tabelas envolvidas na consulta, número de índices nessas
tabelas e processamento da consulta
✓ Bloqueio de registros de log
✓ Recursos de sistema computacional disponíveis armazenamento, memória,
CPU
▪ ENTÃO QUER DIZER QUE OS SGBDS POSSUEM MONINTORAMENTO EM
TEMPO REAL PARA PODER GERAR ESTAS INFORMAÇÕES?
FATORES CONSIDERADOS PELO PLANO DE EXECUÇÃO
ESTATÍSTICAS DE BANCO DE DADOS
▪ ESTATÍSTICAS são utilizadas para
alimentar os cálculos do otimizador de
consultas, gerando meta-dados e suportando
o cálculo da seleção do melhor plano de
execução.
▪ Elas fornecem informações sobre a
distribuição dos dados no banco de dados e
podem incluir um inclui um histograma que
exibe a distribuição de valores na primeira
coluna Fonte: SIQUEIRA, 2021.
A PARTE SOBRE O HISTOGRAMA
▪ HISTOGRAMA é um demonstrativo de
distribuição de frequências.
▪ É utilizado para resumir grandes conjuntos
de dados, comparar os resultados e oferecer
uma possibilidade de demonstração gráfica.
▪ Imaginem o otimizador de query do SGBD
fazendo esta análise em tempo real para todas
as colunas, linhas, índices e consultas em
tempo real.
Fonte: SIQUEIRA, 2021.
COMO CONFIGURAR AS ESTATISTICAS NO BANCO
▪ Geralmente os DBAs habilitam as opções de
auto generate e auto update para as
estatísticas do banco.
▪ CONFIRAM SEMPRE A ATUALIZAÇÃO!
▪ Os apontamentos da estatística podem
apontar ajustes de parâmetros físicos do
SGBD, da alteração das configurações de
dispositivos, da alteração de parâmetros do
sistema operacional e de outras atividades
similares.
Fonte: https://br.freepik.com/vetores-premium/conceito-de-estatisticas-
de-banco-de-dados-com-personagem_11050128.htm

UNIDADE II – TÉCNICAS DE OTIMIZAÇÃO
DE BANCOS DE DADOS
PERFORMANCE DE
AMBIENTES DE DADOS
TUNNING
DOS AMBIENTES DE
SGBD
COMO REFINAR O AMBIENTE
▪ Vamos para a prática!
▪ Adquirimos um SGBD caríssimo e contamos
com as técnicas implementadas em seus
subsistemas para abstrair a questão de
desempenho das entregas.
▪ Mas ele não está entregando
satisfatoriamente o que precisamos.
▪ PRECISAMOS ATUAR EM OUTROS
NÍVEIS!
OS GARGALOS DE SISTEMA E COMO ESCOLHER O QUE ATACAR
▪ A ação em caso de mais problemas é
localizar o gargalo: pode ser um ou vários
componentes que estão limitando o
desempenho global do sistema.
▪ Exemplo de atuação:
▪ Uma função que represente 80% do tempo
total de sua execução, se atuarmos no ajuste
dessa função melhora de forma
significativa o andamento do sistema.
▪ Se essa função for melhorada em 50 % do
seu desempenho, então o seu ajuste irá
representar 40% do desempenho total da
aplicação.
▪ Mas se prepare para a SURPESA!
Geralmente quando resolvemos o primeiro
gargalo outros aparecem.
▪ O processo de localização e eliminação de
gargalos é continuo até que o sistema esteja
equilibrado.
OS GARGALOS DE SISTEMA E COMO ESCOLHER O QUE ATACAR
▪ A complexidade em um ambiente de SGBD é grande, são várias etapas e vários
componentes que não o SGBD envolvidos tais quais:
✓ Como entrada de processos no servidor
✓ Leitura de discos
✓ Ciclos de CPU
✓ Controle de concorrência
▪ Tudo isto fica amarrado em uma fila de concorrência e a soma de atuação de todos é o
tempo total das transações.
O DESEMPENHO DO BANCO DE DADOS
PARÂMTEROS AJUSTÁVEIS
▪ São três níveis em que o DBA pode realizar
interferência em um SGBD:
▪ 1º Nível: o hardware, que engloba decisões
como utilização de um ou mais discos,
aumento da memória e aumento do buffer de
disco entre outros.
▪ 2º Nível: parâmetros do SGBD e cada
fornecedor tem o seu próprio conjunto de
ajuste de parâmetros.
PARÂMTEROS AJUSTÁVEIS
▪ 3º Nível: ajuste de esquemas e transações e
esse nível é em parte independente do
sistema, pois passam por ajuste no projeto
do esquema e transações, criação de
índices de pesquisa entre outros.
▪ O ajuste perfeito se deve ao conjunto
associado dos três níveis além da observância
que precisamos ter do crescimento e
utilização do sistema.PARÂMTEROS AJUSTÁVEIS
▪ 3º Nível: ajuste de esquemas e transações e
esse nível é em parte independente do
sistema, pois passam por ajuste no projeto
do esquema e transações, criação de
índices de pesquisa entre outros.
▪ O ajuste perfeito se deve ao conjunto
associado dos três níveis além da observância
que precisamos ter do crescimento e
utilização do sistema.
▪ Ajuste de Hardware: garante a robustez do subsistema de disco e da memória utilizada
para armazenamento de todas as páginas;
▪ Ajuste de Esquema: modificações nas relações entre tabelas (no caso dos bancos de
dados relacionais), alteram a forma como as mesmas são acessadas. Lembre-se do
catálogo e das estatísticas que alimentam o plano de execução;
▪ Ajuste de Índices: os índices são a referência sobre os dados armazenados para que se
consiga uma melhora no desempenho;
▪ Visões Materializadas: armazenam um conteúdo calculado, o que facilita e agiliza a
requisição desta consulta;
OBSERVEM OS IMPACTOS DE CADA ATUAÇÃO
▪ Ajuste Automatizado do Projeto Físico: é realizado por ferramentas ou subsistemas
presentes nos SGBDs com o objetivo de criação de índices, visão materializada,
particionamento de tabelas e etc (geralmente disponíveis nas versões Enterprise);
▪ Ajuste de Transações: utiliza a técnica da melhoria da orientação do conjunto, que tenta
minimizar a alta sobrecarga de comunicação no envio de múltiplas consultas no caso
dos bancos de dados relacionais;
▪ Simulação de Desempenho ou teste de carga: utilizada pelo administrador do banco de
dados (DBA) com o objetivo de analisar o comportamento do sistema sobre várias
condições de carga de trabalho e tempo de serviço. Praticamente todos os SGBDs já
oferecem alguns programas para simular carga em esquemas de exemplo.
OBSERVEM OS IMPACTOS DE CADA ATUAÇÃO
FERRAMENTAS
▪ Os próprios SGBDs oferecem as ferramentas
básicas para observância dos parâmetros
principais para que possamos executar o
tunning dos nossos ambientes.
▪ Fique atento aos marcadores de
fragmentação dos dados com a sua
utilização dos esquemas que me direciona
para uso de recursos inadequados.
▪ Fique atento também ao nível de
compartilhamento da instância!
DICAS DE OURO!
▪ Nunca mude mais um parâmetro ao mesmo
tempo!
▪ Verifique se as áreas de paginação e SWAP
estão de acordo com a realidade do banco de
dados.
▪ Fique atento também ao espaço em disco
pois ele pode ser utilizado por completo não
existindo assim espaço para execução de um
processo do banco de dados.
▪ ATUALIZE AS ESTATÍSTICAS!













-------------------
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
