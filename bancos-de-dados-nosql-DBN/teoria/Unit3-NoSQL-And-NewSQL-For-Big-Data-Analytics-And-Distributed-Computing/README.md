# Aplicando NoSQL em BigData, casos de uso e tecnologias

## Análise de dados em tempo real

## Análise de straming e fluxos de dados contínuos
• Análise de streaming é a capacidade de calcular constantemente análises estatísticas enquanto se move dentro do fluxo de dados.
• A análise de streaming permite o gerenciamento, monitoramento e análises em tempo real de dados de streaming ao vivo.
• A atividade de negócios e o monitoramento de desempenho são os principais benefícios obtidos coma análise de streaming.


## Edge / Fog Device Analytics
• O volume de dados dos dispositivos IoT está crescendo exponencialmente, pois eles estão interagindo de forma contínua e espontânea uns com os outros para atender a diferentes aspectos pessoais, profissionais e
necessidades sociais.
• Para habilitar análises em tempo real, há uma nova recomendação criar nuvens de dispositivos IoT ad hoc localmente para capturar, armazenar, particionar e analisar todos os tipos de dados IoT.
• Esse novo fenômeno está sendo denominado como neblina ou análise de dispositivo de borda e podem ser aplicados nas situações:
✓Prevenir acidentes e crimes em cidades.
✓Fornecer aos médicos uma visão em tempo real das informações de marcapassos ou biochips.
✓Otimização da produtividade em todos os setores pormeio de manutenção preditiva em equipamentos e máquinas.
✓Criação casas verdadeiramente inteligentes com aparelhos conectados.
✓Fornecer comunicação crítica entre carros autônomos.

## Platafor mas e soluções
• O EMC Greenplum Data Computing Appliance (DCA) éuma plataforma de análise integrada que acelera a análise de ativos de big data em um único dispositivo
integrado.
• IBM PureData System for Analytics integra arquitetonicamente o banco de dados, o servidor e o armazenamento em um sistema único, criado para o propósito e fácil de gerenciar para acelerar a atividade analítica.
• SAP HANA é uma plataforma exemplar para análises em tempo real e big data
• Fornecedores de plataformas estão ligados aos fornecedores de infraestrutura, especialmente os CSPs (Cloud Service Providers), para levar análises para a nuvem
• O objetivo da análise de dados como serviço (DAaaS) permite várias iniciativas com ofertas de produtos inovadores para acelerar e simplificar a parte complexa da análise de dados de última geração.

# Web Crawler

• Web Crawler é um algoritmo que percorre os hiperlinks os indexa.
• Grava as informações em bancos de dados e as utiliza para gerar insights ou classificar os dados encontrados.
• São conhecidos também como Spiders, Robots (bots), Wanderers.
• Possui muitas finalidades, como análise da Web, coleta de endereços de e-mail, embora a principal delas seja a descoberta e indexação de páginas para mecanismos de busca na Web.

Os principais utilitários do Web Crawler incluem:
✓ Execução de mineração de dados que é a primeira etapa do processo de mineração de dados da Web.
✓ Reunir páginas da Web baixando documentos automaticamente de um servidor Web.
✓ Analisar documentos recuperados de um servidor Web e enviar dados de volta para um banco de dados de mecanismo de pesquisa
✓ Apoiar um motor de pesquisa.
✓ Mecanismos de busca, análise de dados, interações automatizadas da Web, espelhamento e validação de HTML/link onde quando um rastreador da Web visita uma página, ele lê o texto visível, os hiperlinks
e o conteúdo das várias tags usadas no site, como meta tags com muitas palavras-chave.

• As coletas são armazenadas geralmente em bancos NoSQL.
• as características:
✓ Distribuído: o que aumenta a disponibilidade.
✓ Facilidade de desenvolvimento de novas APIs.
✓ Escalável: Resolvendo o problema da utilização da banda.
✓ Schemaless: possibilidade de fazermos a estrutura livre de travas possibilitando armazenar diversos documentos com configurações diferentes

# Hadoop

- Map Reduce

# Segurança em bancos NoSQL

• A maioria dos bancos de dados NoSQL não fornece recursos de segurança embutidos no próprio banco de dados e os desenvolvedores precisam programar os requisitos de segurança em seu código.
• Aí está um dos problemas desta nova geração de bancos de dados que se concentram primeiro em questões de escalabilidade horizontal e usam a camada de aplicativo para implementar recursos de segurança.
• O problema deste modelo é a possibilidade de erros, tendo em vista que se a falta de segurança se torna um dos motivos principais da não adoção destes bancos em empresas que tem critérios mais rigorosos de segurança.
• Desta forma, recursos de segurança como autenticação, autorização e integridade, direcionam as escolhas para que os dados confidenciais sejam hospedados de forma mais segura no SGBD relacional.
• Há muitas ameaças de segurança, como cross-site scripts, SQL Injections, root kits e a famosa engenharia social.
• Para as questões eletrônicas que dependem de codificação os bancos relacionais conseguem trabalhar melhor estas vulnerabilidades devido a seus aprimoramentos.
• Os bancos de dados NoSQL estão sempre sujeitos a ataques à segurança devido à natureza não estruturada dos dados e ao ambiente de computação distribuído 


## Problemas de supor te a segurança
1. Suporte de criptografia insuficiente para os arquivos de dados
2. Autenticação fraca entre o cliente e os servidores
3. Controle de acesso granular
4. Autorização muito simples sem o suporte para RBAC (Role-based Access Control)
5. Vulnerabilidade à injeção de SQL
6. Validação / filtragem de entrada de ponto final
7. Armazenamento e comunicação de dados inseguros
8. Mineração e análise de dados preservando a privacidade

• Aponta-se o perigo de confiar na segurança do perímetro, ou seja, do firewall, tendo em vista que Java Script ou JSON podem ser usados para ataca-los obtendo acesso não autorizado aos dados do banco
de dados.
• Outra questão é que os sistemas não fornecem controles de acesso granulares necessários para separar funções e responsabilidades do usuário e esta vulnerabilidade a ataques é alta se a curva de aprendizado do invasor terminar e ele for capaz de identificar fraquezas ocultas do software

## Mitigando os problemas de segurança

• A metodologia de relacionamento de atributos é um método popular para impor segurança em bancos de dados NoSQL.
• Proteger as informações valiosas é o objetivo principal desta metodologia e o atributo com maior relevância considerado o elemento-chave da extração [chave do hash] de informação e recebe mais importância do que os demais atributos.
• Outro método de controle de acesso a dados adequado para bancos de dados NoSQL é a criptografia baseada em atributos.
• O método consiste em permitir aos proprietários de dados criptografar dados sob a política de acesso de forma que apenas os usuários que têm permissão para acessar os dados possam descriptografá-los.
• Lembram-se da topologia Edge /FOG ? Pois bem, uma das soluções de segurança que estão sendo adotadas é o deslocamento deste processamento para as pontas.
• Outro método de controle de acesso a dados adequado para bancos de dados NoSQL é a criptografia baseada em atributos.
• O método consiste em permitir aos proprietários de dados criptografar dados sob a política de acesso de forma que apenas os usuários que têm permissão para acessar os dados possam descriptografá-los.
• Lembram-se da topologia Edge /FOG ? Pois bem, uma das soluções de segurança que estão sendo adotadas é o deslocamento deste processamento para as pontas.

## Riscos de segurança par abancos NoSQL

### Cluster

• Um banco de dados distribuído controlado centralmente sincroniza periodicamente todos os dados e garante que as atualizações e exclusões realizadas nos dados sejam automaticamente refletidas nos dados armazenados em outro lugar.
• Nesta transição de dados é ideal que o aplicativo implemente o controle de acesso no nível de documento (ou coluna) para evitar acessos indevidos de usuários não autorizados viabilizando isto para o processo de replicação.
• São vários nós distribuídos nos quais os bancos de dados NoSQL são executados aumentando a superfície de ataque e tornando o sistema complexo para proteger.
• A possibilidade de acesso não autorizado ao banco de dados aumenta devido a vários pontos de entrada.
• Esses pontos de entrada podem ser de um local remoto ou de um local on-premise do cliente através de algum dos seus clientes
• O ambiente distribuído é geralmente mais sujeito a riscos de segurança devido à falta de um sistema central de gerenciamento de segurança.
• Os bancos de dados Cassandra e Dynamo são vulneráveis a riscos de segurança em ambiente distribuído.

### Autenticação

• Geralmente o mecanismo de autenticação em um banco de dados NoSQL é aplicado no nível do nó local, mas falha em todos os servidores de commodities (distribuídos em nuvem).
• Devido a isso, os bancos de dados NoSQL são expostos a ataques de força bruta, ataques de injeção e ataques de retransmissão, que levam ao vazamento de informações.
• As razões para esses ataques são o mecanismo de autenticação fraco destas soluções.
• Geralmente o mecanismo de autenticação em um banco de dados NoSQL é aplicado no nível do nó local.
• Devido a isso, os bancos de dados NoSQL são expostos a ataques de força bruta, ataques de injeção e ataques de retransmissão, que levam ao vazamento de informações.
• As razões para esses ataques são o mecanismo de autenticação fraco destas soluções mesmo utilizando-se Kerberos para autenticar os clientes e os nós de dados

### Integridade

• Proteger a integridade é um requisito de segurança para garantir a proteção dos dados contra modificações não autorizadas devido à inserção, exclusão ou atualização de dados no banco de dados.
• Como os bancos de dados NoSQL não têm um esquema, as permissões em uma tabela, coluna ou linha não podem ser segregadas.
• Portanto, manter a integridade transacional também é muito difícil em bancos de dados NoSQL.
• Isso pode levar a várias cópias dos mesmos dados, o que torna difícil manter os dados consistentes, especialmente porque as alterações em várias tabelas não podem ser agrupadas em uma transação onde uma unidade lógica de inserção, atualização ou exclusão de operações é executada como um todo.
• Devido à complexidade de impor restrições de integridade aos bancos de dados NoSQL, não é recomendado que estes bancos de dados sejam usados para transações financeiras.

### Autenticação de usuários
• Autenticação desempenha um papel muito importante em qualquer banco de dado e os bancos relacionais permitem autorização no nível da tabela.
• Os bancos de dados NoSQL não têm esquema e armazenam dados heterogêneos juntos.
• Portanto, é difícil implementar a autorização em uma tabela como um todo.
• O controle de acesso refinado não é implementado à característica schemaless dos bancos de dados NoSQL que permitem em sua maioria autorização em nível de família de colunas.

### Dados em repouso e em movimento

• Dados em repouso significam dados que foram eliminados da memória e gravados no disco.
• Possuem duas categorias:
✓ Comunicação cliente-nó
✓ Comunicação entre nós
• A maioria dos bancos de dados NoSQL não emprega nenhuma técnica para proteger os dados em repouso.
• Apenas alguns fornecem mecanismos de criptografia para proteger os dados.

### Dados em repouso e em movimento
• Dados em movimento significam dados que estão em comunicação ou sendo trocados durante uma comunicação.
• Os bancos de dados NoSQL populares oferecem os seguintes serviços de criptografia para proteção de dados.
• Para dados em repouso o Cassandra usa a técnica TDE (Transparent Data Encryption).
• Já o MongoDB não fornece nenhum método para criptografar o arquivo de dados. Os arquivos de dados podem ser criptografados na camada do aplicativo antes de gravar os dados no banco de dados, o que requer forte segurança do sistema.
• Para dados em movimento o Cassandra não criptografada a comunicação cliente-nó e ela é feita gerando certificados de servidor válidos na camada SSL.
• Já o MongoDB não oferece suporte à comunicação no modo cliente SSL sendo que, para criptografar os dados usando a comunicação de nó com o cliente SSL, o MongoDB precisa ser recompilado configurando a omunicação SSL.
• Na comunicação entre nós o Cassandra não oferece suporte para comunicação entre nós criptografados e o MongoDB não oferece suporte para comunicação entre nós.

### Privacidade dos dados de usuário
• NoSQL armazena grande quantidade de informações confidenciais e manter a privacidade dessas informações é a principal preocupação de qualquer administrador de banco de dados.
• Os clientes acessam bancos de dados NoSQL por meio de vários nós e gerenciadores de recursos.
• Mesmo que haja um único local, os dados maliciosos se propagam para todo o sistema, pois não há gerenciamento de segurança central.
• A natureza distribuída do banco de dados também leva ao comprometimento da segurança.
• Os principais problemas de privacidade estão relacionados a:
• Acesso não autorizado,
• Bloqueio de fornecedor,
• Exclusão de dados,
• Backup,
• Vulnerabilidades,
• Falha de isolamento,
• Monitoramento inadequado
• Auditoria.
