O mascaramento de dados é uma técnica de segurança de dados que embaralha os dados para criar uma cópia inautêntica para vários fins de não produção. O mascaramento de dados retém as características e a integridade dos dados de produção originais e ajuda as organizações a minimizar os problemas de segurança de dados ao utilizar os dados em um ambiente de não produção. Esses dados mascarados podem ser usados para análise, treinamento ou teste

## Por que as organizações devem efetuar mascaramento de dados?

Nos últimos anos, os regulamentos de segurança de dados tornaram-se muito rigorosos. A
introdução de regulamentos como o Regulamento Geral de Proteção de Dados (GDPR) forçou as
organizações a proteger seus dados ferozmente. Isso colocou uma restrição significativa no uso
dos dados da organização para teste ou análise.
Suponha que uma empresa de saúde queira analisar e estudar o comportamento de seus clientes.
Eles podem querer terceirizar o trabalho de análise para um fornecedor terceirizado. Se eles
passarem as informações de saúde autênticas de seus clientes para um fornecedor, há uma chance
de violação de dados. O mascaramento de dados ajuda nesses cenários.
Os dados são um dos ativos mais importantes de uma organização. O mascaramento ajuda as
organizações a extrair o máximo de benefícios dos dados sem comprometer a segurança.



# Operações de Tratamento de Dados
-  ACESSO - ato de ingressar, transitar, conhecer ou consultar a informação, bem como possibilidade de usar os ativos de informação de um órgão ou entidade, observada
eventual restrição que se aplique;
- ARMAZENAMENTO - ação ou resultado de manter ou conservar em repositório um dado;
- ARQUIVAMENTO - ato ou efeito de manter registrado um dado em qualquer das fases do ciclo da informação, compreendendo os arquivos corrente, intermediário e permanente, ainda que tal informação já tenha perdido a validade ou esgotado a sua vigência;
- AVALIAÇÃO - analisar o dado com o objetivo de produzir informação;
- CLASSIFICAÇÃO - maneira de ordenar os dados conforme algum critério estabelecido;
- COLETA - recolhimento de dados com finalidade específica;
- COMUNICAÇÃO - transmitir informações pertinentes a políticas de ação sobre os dados;
- CONTROLE - ação ou poder de regular, determinar ou monitorar as ações sobre o dado;
-  DIFUSÃO - ato ou efeito de divulgação, propagação, multiplicação dos dados;
-  DISTRIBUIÇÃO - ato ou efeito de dispor de dados de acordo com algum critério estabelecido;
-  ELIMINAÇÃO - ato ou efeito de excluir ou destruir dado do repositório;
-  EXTRAÇÃO - ato de copiar ou retirar dados do repositório em que se encontrava;
- MODIFICAÇÃO - ato ou efeito de alteração do dado;
-  PROCESSAMENTO - ato ou efeito de processar dados visando organizá-los para obtenção de um resultado determinado;
- PRODUÇÃO - criação de bens e de serviços a partir do tratamento de dados;
-  RECEPÇÃO - ato de receber os dados ao final da transmissão;
-  REPRODUÇÃO - cópia de dado preexistente obtido por meio de qualquer processo;
- TRANSFERÊNCIA - mudança de dados de uma área de armazenamento para outra, ou para terceiro;
- TRANSMISSÃO - movimentação de dados entre dois pontos por meio de dispositivos elétricos, eletrônicos, telegráficos, telefônicos, radioelétricos, pneumáticos, etc.;
- UTILIZAÇÃO - ato ou efeito do aproveitamento dos dados

| **Hipótese de Tratamento**                                                                    | **Dispositivo Legal para o Tratamento de Dados Pessoais** | **Dispositivo Legal para o Tratamento de Dados Pessoais Sensíveis** |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- |
| **Hipótese 1:** Mediante consentimento do titular                                             | LGPD, art. 7º, I                                          | LGPD, art. 11, I                                                    |
| **Hipótese 2:** Para o cumprimento de obrigação legal ou regulatória                          | LGPD, art. 7º, II                                         | LGPD, art. 11, II, *"a"*                                            |
| **Hipótese 3:** Para a execução de políticas públicas                                         | LGPD, art. 7º, inciso III                                 | LGPD, art. 11, II, *"b"*                                            |
| **Hipótese 4:** Para a realização de estudos e pesquisas                                      | LGPD, art. 7º, inciso IV                                  | LGPD, art. 11, II, *"c"*                                            |
| **Hipótese 5:** Para a execução ou preparação de contrato                                     | LGPD, art. 7º, inciso V                                   | **Não se aplica**                                                   |
| **Hipótese 6:** Para o exercício de direitos em processo judicial, administrativo ou arbitral | LGPD, art. 7º, inciso VI                                  | LGPD, art. 11, II, *"d"*                                            |
| **Hipótese 7:** Para a proteção da vida ou da incolumidade física do                          |                                                           |                                                                     |


# Bases Legais da LGPD
O tratamento de dados pessoais sensíveis pode ser realizado em quais condições?
Sem fornecimento de consentimento do titular, nas hipóteses em que for indispensável para:
- Cumprimento de obrigação legal ou regulatória pelo controlador;
- Pela administração pública, de políticas públicas previstas em leis ou regulamentos;
- Estudos por órgão de pesquisa;
- Exercício regular de direitos, inclusive em contrato e em processo judicial, administrativo e arbitral;
- Proteção da vida;
- Tutela da saúde;
- Garantia da prevenção à fraude e à segurança do titular..

## Modalidade de Dados

 “Estáticos” se referem ao facto de os dados estarem totalmente disponíveis no momento da anonimização; isto contrasta com dados em fluxo, nos quais, as
relações entre os dados podem não estar totalmente estabelecidas porque o fluxo fornece constantemente novos dados. Logo, é possível que os dados em
fluxo precisem de outras técnicas de anonimização além daquelas que são descritas nesta Guia.
 “Estruturados” se referem ao facto de que a técnica de anonimização é aplicada a dados dentro de um formato conhecido e a uma localização conhecida
dentro da base de dados. “Estruturados” não se limitam, portanto, a dados em formato tabular tais como uma folha de cálculo ou uma base de dados relacional,
mas podem ser guardados ou divulgados em outros formatos definidos, como por exemplo XML, CSV, JSON, etc. Nesta Guia, se descrevem as técnicas e fornecem
exemplos no formato tabular mais comum, mas isto não implica que as técnicas apenas se aplicam a esse formato, ou seja, formato tabular.
 “Bem definidos” se referem ao facto de o conjunto de dados original estar em conformidade com regras pré-definidas. Por exemplo, os dados derivados de
bases de dados relacionais tendem a ser mais bem definidos. Anonimizar conjuntos de dados que não sejam bem definidos pode provocar desafios adicionais à
anonimização, e está fora do âmbito desta Guia.
 “Em formato textual” se referem a texto, números, datas, etc., ou seja, dados alfanuméricos já em formato digital. As técnicas de anonimização para dados
em fluxo como áudio, vídeo, imagem, mega dados (no seu formato em bruto), geolocalização, dados biométricos, etc., criam desafios adicionais e requerem
técnicas de anonimização completamente diferentes, as quais estão fora do âmbito desta Guia.
 “De nível único” se referem a dados que relativos a indivíduos diferentes. Conjuntos de dados que contenham entradas múltiplas para os mesmos indivíduos
(por exemplo, diferentes transações efetuadas por um indivíduo) podem ainda utilizar algumas das técnicas explicadas nesta Guia, mas é necessário aplicar
critérios adicionais; os quias estão fora do âmbito desta Guia.

## Escolha das técnicas de anonimização

- Competência no processo de anonimização e as suas técnicas: A anonimização é complexa. Além de ter conhecimento do assunto em questão
(como explicado em cima), as organizações que pretendam partilhar dados anonimizados devem também assegurar que o processo de
anonimização em si é realizado por pessoas familiarizadas com técnicas e princípios de anonimização. Se o conhecimento necessário não for
encontrado dentro da organização, deve-se procurar ajuda externa.
- O receptor: Fatores como o conhecimento do receptor sobre o assunto em questão, controlos implementados para limitar os receptores e para
evitar que os dados sejam partilhados com partes não autorizadas, desempenham um papel importante na escola de técnica de anonimização. Em
particular, o uso expectável dos dados anonimizados pelo receptor pode impor limitações nas técnicas aplicadas, porque a utilidade dos dados
pode ser perdida além de limites aceitáveis. É necessário usar muita precaução ao fazer uma publicação dos dados, e o mesmo requer uma forma
muito mais forte de anonimização quando comparada com dados partilhados sob um formato contratual.
- Ferramentas: Devido à complexidade e computação necessária, as ferramentas de software podem ser muito úteis como apoio na execução de
técnicas de anonimização. Existem algumas ferramentas4 dedicadas disponíveis, mas a Guia não fornece qualquer avaliação ou recomendação de
ferramentas de anonimização e re-identificação. Nota-se que mesmo as melhores ferramentas precisam de entradas adequadas (ex. parâmetros
adequados para ser utilizados), ou podem conter limitações, daí que a supervisão e a familiaridade do elemento humano com as ferramentas e
dados continuam a ser necessárias.

# Artigos relevantes a proteção de dados

Os trechos a seguir foram extraídos da Lei Brasileira nº 13.709 (LGPD), de 14 de agosto de 2018.¹
Aplicação
Art. 3. Esta Lei aplica-se a qualquer operação de tratamento realizada por pessoa naturalou por pessoa jurídica de direito público ou privado,
independentemente do meio, do país de sua sede ou do país onde estejam localizados os dados ....
Dados anonimizados
Art. 5. Para fins desta Lei, aplicam-se as seguintes definições:
ou por pessoa jurídica de direito público ou privado, independentemente do meio, do país de sua sede ou do país onde estejam localizados os
dados ....
III - dado anonimizado: dado relativo ao titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis
na ocasião de seu tratamento;
XI - anonimização: utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um
dado perde a possibilidade de associação, direta ou indireta, a um indivíduo

## Artigos relevantes a proteção de dados

Tratamento de dados
Art. 6. As atividades de tratamento de dados pessoais deverão observar a boa-fé e os seguintes princípios:
VII - segurança: utilização de medidas técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações
acidentais ou ilícitas de destruição, perda, alteração, comunicação ou difusão;
VIII - prevenção: adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento de dados pessoais;
X - responsabilização e prestação de contas: demonstração, pelo agente, da adoção de medidas eficazes e capazes de comprovar a observância e o
cumprimento das normas de proteção de dados pessoais e, inclusive, da eficácia dessas medidas.
Dados anonimizados não considerados dados pessoais
Art. 12. Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei, salvo quando o processo de anonimização ao qual
foram submetidos for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido.
§ 1º A determinação do que seja razoável deve levar em consideração fatores objetivos, tais como custo e tempo necessários para reverter o
processo de anonimização, de acordo com as tecnologias disponíveis, e a utilização exclusiva de meios próprios.
Art. 13. §4º. “Para os efeitos deste artigo, a pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta
ou indireta, a um indivíduo, senão pelo uso deinformação adicional mantida separadamente pelo controlador emambiente controlado e seguro”
Responsabilidade e registro de acesso
Art. 37. O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem,
especialmente quando baseado no legítimo interesse.
Art. 38. A autoridade nacional poderá determinar ao controlador que elabore relatório de impacto à proteção de dados pessoais,
inclusive de dados sensíveis, referente a suas operações de tratamento de dados, nos termos de regulamento, observados os
segredos comercial e industrial.
Parágrafo único. Observado o disposto no caput deste artigo, o relatório deverá conter, no mínimo, uma descrição dos tipos de
dados coletados, a metodologia utilizada para a coleta e para a garantia da segurança das informações e análise do controlador
com relação às medidas, salvaguardas e mecanismos de mitigação de risco adotados.
esponsabilidade do controlador e dos processadores
Art. 42. O controlador ou o operador que, em razão do exercício de atividade de tratamento de dados pessoais, causar a outrem dano patrimonial,
moral, individual ou coletivo, em violação à legislação de proteção de dados pessoais, é obrigado a repará-lo.
Da segurança e do sigilo de dados
Art. 46. Os agentes de tratamento devem adotar medidas de segurança, técnicas e administrativas aptas a proteger os dados pessoais de acessos
não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento
inadequado ou ilícito.
Notificação de vazamento de dados
Art. 48. O controlador deverá comunicar à autoridade nacional e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou
dano relevante aos titulares.
Melhores práticas de segurança de dados.
Art. 49. Os sistemas utilizados para o tratamento de dados pessoais devem ser estruturados de forma a atender aos requisitos de segurança, aos
padrões de boas práticas e de governança e aos princípios gerais previstos nesta Lei e às demais normas regulamentares
Sanções administrativas
Art. 52. Os agentes de tratamento de dados, em razão das infrações cometidas às normas previstas nesta Lei, ficam sujeitos às seguintes
sanções administrativas aplicáveis pela autoridade nacional:
• advertência, com indicação de prazo para adoção de medidas corretivas;
• multa simples, de até 2% (dois por cento) do faturamento da pessoa jurídica de direito privado, grupo ou conglomerado no Brasil no seu
último exercício, excluídos os tributos, limitada, no total, a 50 milhões de reaispor infração;
• multa diária, observado o limite total a que se refere o inciso II;
• publicização da infração após devidamente apurada e confirmada a sua ocorrência;
• bloqueio dos dados pessoais a que se refere a infração até a sua regularização;
• eliminação dos dados pessoais a que se refere a infração;
| **Direitos dos Titulares de Dados que Decorrem dos Princípios**                                                                                                                                 | **Princípio Correspondente**     | **Referência Legislativa (LGPD)** |

| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------------- |
| Direito ao tratamento adstrito aos propósitos legítimos, específicos, explícitos e informados ao titular, sem possibilidade de tratamento posterior de forma incompatível com essas finalidades | Princípio da finalidade          | Art. 6º, I                        |
| Direito ao tratamento adequado, compatível com as finalidades informadas ao titular, de acordo com o contexto do tratamento                                                                     | Princípio da adequação           | Art. 6º, II                       |
| Direito à limitação do tratamento ao mínimo necessário para a realização de suas finalidades, com abrangência dos dados pertinentes, proporcionais e não excessivos em relação às finalidades   | Princípio da necessidade         | Art. 6º, III                      |
| Direito à consulta facilitada e gratuita sobre a forma e a duração do tratamento, bem como sobre a integralidade de seus dados pessoais                                                         | Princípio do livre acesso        | Art. 6º, IV                       |
| Direito à exatidão, clareza, relevância e atualização dos dados, de acordo com a necessidade para o cumprimento da finalidade de seu tratamento                                                 | Princípio da qualidade dos dados | Art. 6º, V                        |
| Direito a informações claras, precisas e facilmente acessíveis sobre a realização do tratamento e os respectivos agentes de tratamento, observados os segredos comercial e industrial           | Princípio da transparência       | Art. 6º, VI                       |
Aqui está a transcrição da tabela da imagem com os **direitos dos titulares de dados conforme os princípios da LGPD (continuação):**

| **Direitos dos Titulares de Dados que Decorrem dos Princípios**                                                                                                                                                                               | **Princípio Correspondente**                         | **Referência Legislativa (LGPD)** |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------- |
| Direito à segurança dos dados, ao qual se contrapõe o dever, por parte dos agentes de tratamento, de utilização de medidas técnicas e administrativas para proteger os dados de acessos não autorizados e de situações acidentais ou ilícitas | Princípio da segurança                               | Art. 6º, VII                      |
| Direito à adequada prevenção de danos, ao qual se contrapõe o dever de adoção de medidas para prevenir a ocorrência de danos em virtude do tratamento de dados                                                                                | Princípio da prevenção                               | Art. 6º, VIII                     |
| Direito de não ser discriminado de forma ilícita ou abusiva                                                                                                                                                                                   | Princípio da não discriminação                       | Art. 6º, IX                       |
| Direito de exigir a adequada responsabilização e a prestação de contas pelos agentes de tratamento                                                                                                                                            | Princípio da responsabilização e prestação de contas | Art. 6º, X                        |

