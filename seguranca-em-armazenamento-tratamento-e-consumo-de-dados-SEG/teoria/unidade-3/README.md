# Auditoria de dados pela Lei de Benford

## Auditoria de sistemas

**Objetivos**

- Validar e avaliar os controles internos de Sistemas
- Validar a eficacia do sistema
- Reunir, agrupar e validar evidencias
- Garantir a segurança (fisica e logica) da inforamção e sistema

**Pode deterctar problemas em**

- Fraudes em e-mail;
- Uso inadequado de hardwares
- Vazamento de informações
- Falta de segurança fisica (acessos indevidos )

**Principais tipos de auditorias de sistemas**

- **Auditoria Legal ou Regulatória:** Atendimento a regulamentações locais e internacionais (Lei Sarbanes-Oxley, Basileia II, Comissão de Valores Mobiliários, etc.).
- **Auditoria de Integridade de Dados:** Classificação dos dados, atualização, bancos de dados, aplicativos, acessos, estudo dos fluxos (entradas e saídas) de transmissão, controles de verificação qualidade e confiabilidade das informações.
- **Auditoria em Segurança da Informação:** Métodos de autenticação, autorização, criptografia, gestão de certificados digitais, segurança de redes, gestão dos usuários, configuração de antivírus, atualizações, políticas, normas, manuais operacionais.
- **Auditoria de Segurança Física:** Avaliação de localidades e riscos ambientais: vidas (capital intelectual), furto/roubo, acesso, umidade, temperatura, acidentes, desastres, etc. e as proteções: perímetros de segurança, câmeras, sensores, guardas, dispositivos, proteções do ambiente.
- **Auditoria de Desenvolvimento de Sistemas:** Validação dos processos de gestão de projetos, cumprimento de metodologia de qualidade, orçamentos previstos e realizados e avaliação de desvios.


**CAAT – Computer Aided Audit Tools**

- **A CAAT ou TAACs - Técnicas de Auditoria Auxiliadas por Computador** - são técnicas ou programas de computador especializados para gerar amostras, importar dados, sumarizar e testar os controles, condições e processos implantados nos sistemas através das amostras que selecionamos.

- **Software Especializado para Auditoria (SEA)**
Permite ao auditor realizar testes em arquivos e bancos de dados.
Ex.: ACL, IDEA, etc.

- **Software de Auditoria Adaptado (SAA)**
Geralmente desenvolvidos por auditores para desempenhar tarefas específicas, são necessários quando os sistemas da empresa não são compatíveis aos SEA, ou quando o auditor quer realizar testes não possíveis com os SEA.
Ex.: Easy Trieve, SQL+, SAS, etc

- **Teste de Dados ou Recálculo de Operações**
O auditor testa os dados para verificar os controles empregados no sistema através de validação nestes dados> Simulação em Paralelo
O auditor utiliza as informações do sistema para mapear e construir os passos a serem simulados em outra ferramenta a fim de chegar ao mesmo resultado do sistema.

- **Testes integrados**
O auditor submete parâmetros de teste com dados reais, sem impactar na rotina normal de processamento do sistema.


- **Aborda os dados contidos em meios de armazenamento eletrônico a fim de se certificar se são íntegros, confiáveis e em conformidade com as leis que regem o Negócio.**

- **Pode ser executado isoladamente ou de forma a complementar outra auditoria (ex.: auditoria de sistemas).**

- **Possibilita a verificação de toda a base de dados auditada.**

- **Permite o cruzamento de informações com outras bases de dados a fim de verificar os registros auditados.**

**Quando realizar?**

- **Existência de um grande volume de dados para analisar.**
- **Possibilidade de se verificar até 100% dos dados armazenados.**
- **Necessidade de se utilizar dados processados por computador para fundamentar achados de auditoria.**
- **Necessidade de determinar se os dados podem ser considerados completos e exatos.**
- **Possibilidade de comparação de informações obtidas em diferentes fontes.**


**Indícios de problemas na confiabilidade dos dados**

• **documentação ausente ou precária;**
• **sistemas antigos, que exigem muita manutenção;**
• **estruturas de dados complexas e desorganizadas;**
• **alta rotatividade de pessoal e treinamento inadequado ou em escala insuficiente;**
• **falta de padrões para o processamento de dados, especialmente quanto à segurança, acesso e controle de mudança de programas.**
• **Os princípios de auditoria exigem que qualquer evidência (independentemente de sua fonte ou formato) seja confiável, relevante e suficiente.**
• **O risco de confiabilidade dos dados é definido como sendo o "risco de que os dados utilizados não sejam suficientemente confiáveis para o fim a que se destinam", ou seja, o risco de que esses não sejam exatos e completos o suficiente para servir de fundamento para achados de auditoria.**


**Exemplo de critérios para auditoria da geração dos dados**

• **O arquivo não deve ser um back-up.**

• **Necessidade de fornecimento de leiaute dos arquivos junto aos dados.**

• **Tipos de formatos possíveis:**

    − **Dados em formato ASCII de comprimento fixo ou**

    − **Dados em formato compatível com Windows (Excel, Word, Access) ou**

    − **Dados em formato separado por vírgulas ou**

    − **Como última alternativa, relatório padrão ou elaborado para fins da auditoria, em meio magnético.**

• **Necessidade de recebimento de "jobs" de execução de geração de dados.**

• **Considerar possibilidade de acompanhamento do processo de geração.**


• **Fórmula da Lei de Newcomb-Benford, onde d é o primeiro dígito significativo.:**

Prob(d) = log₁₀(1 + 1/d), d ∈ {1,2,3,4,5,6,7,8,9}

**Desta forma, para d=1:** Prob(d) = log₁₀(1 + 1/1) = log₁₀(2) = 0.30102999566

• **Hill (1995) considerou uma generalização da lei para os demais dígitos, nos seguintes termos:**

Prob(d₂ = k) = Σ(i=1 to 9) log₁₀(1 + 1/(d₁d₂)), k = {0,1,2,3,4,5,6,7,8,9}

**Então, para k=3:**

Prob(d₂ = 3) = log₁₀(1 + 1/13) + log₁₀(1 + 1/23) + ... log₁₀(1 + 1/93)

**A tabela de frequência do segundo dígito seria:**

| Segundo dígito | 0     | 1     | 2    | 3     | 4    | 5    | 6    | 7     | 8    | 9     | Total |
|----------------|-------|-------|------|-------|------|------|------|-------|------|-------|-------|
| Porcentagem    | 11,67 | 12,00 | 9,00 | 11,00 | 9,00 | 9,00 | 8,00 | 11,00 | 9,33 | 10,00 | 100   |


**Lei de Newcomb-Benford na auditoria de dados**

O estudo inicial de Benford (1938) analisou milhares de registros de diversas variáveis e magnitudes de fenômenos naturais, humanos e científicos. Os resultados demonstraram que o "fenômeno do primeiro dígito" ocorria em várias tabelas de dados, das mais variadas naturezas. Posteriormente, ficou demonstrado que a LNB aplicava-se também aos eventos financeiros, como balanços, preços de ações e demonstrativos contábeis.

Por lidar com os primeiros dígitos dos números, um dos requisitos da LNB é a de que o primeiro dígito possa assumir qualquer valor inteiro entre 1 e 9. Dessa forma, uma tabela de dados de alturas de uma população em metros, por exemplo, não seguirá uma distribuição de Benford, pois não existem pessoas com 3 metros ou mais.

A segunda, e mais importante, limitação, consiste no fato da LNB não se aplicar a números gerados de maneira aleatória, como os números de loterias ou lançamentos de dados. Aqui reside o potencial preditivo e a aplicabilidade forense da técnica: números inventados ou alterados por seres humanos não seguem a distribuição da LNB, mas sim uma tendência a uma distribuição aleatória. Isso implica que números fabricados ou alterados irão fugir da distribuição esperada da LNB, podendo esta ser utilizada como indicativo de alterações ou anomalias que exijam maiores investigações.

