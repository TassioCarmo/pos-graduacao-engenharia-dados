#  Criptografia e gestão de chaves criptográficas

O que é criptografia?
● Criptografia pode ser entendido como o estudo e desenvolvimento de técnicas de transformação de texto de sua forma normalizada e legível para uma linguagem decodificada, não legível para quem não possui o modelo de conversão, o procedimento de decodificação;
● Deriva do grego, ‘KRIPTOS’, que significa escondido e ‘GRAPHO’, que significa escrit

## Conceitos gerais
- ● Texto simples, texto plano, texto claro: mensagem a ser cifrada;
- ● Texto cifrado: texto resultante do processo criptográfico;
- ● Criptoanálise: técnicas para solucionar mensagens cifradas;
- ● Criptografia: técnicas para a criação de mensagens cifradas;
- ● Algoritmo Criptográfico: modelo matemático utilizado para criptografar e descriptografar mensagens;
- ● Chave: String que seleciona a forma de criptografia que deve ser usada para criptografar e descriptografar mensagens;
- ● O sigilo está na chave e no algoritmo, portanto, para que uma mansagem criptografada seja decodificada é necessário descobrir o algoritmo e a chave criptográfica.

Entre os objetivos centrais da criptografia, inclue-se:
- ● **Confidencialidade** – mantém o conteúdo da informação secreto para todos excepto para as pessoas que tenham acesso à mesma.
- ● **Integridade da informação** – assegura que não há alteração, intencional ou não, da informação por pessoas não autorizadas.
- ● **Autenticação de informação** – serve para identificar pessoas ou processos com quem se estabelece comunicação.
- ● **Não repudiação** – evita que qualquer das partes envolvidas na comunicação negue o envio ou a recepção de uma informação

| Característica               | Criptografia Simétrica                                  | Criptografia de Chave Pública                                                               |
| ---------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Formas de Criptografia**   | Técnicas de Substituição e de Permutação                | Funções matemáticas                                                                         |
| **Velocidade**               | Rápida                                                  | Lenta                                                                                       |
| **Distribuição de Chaves**   | Complexa                                                | Simples                                                                                     |
| **Assinatura digital**       | Não necessita                                           | Necessita                                                                                   |
| **Segurança**                | Na chave                                                | Na complexidade matemática                                                                  |
| **Troca de chaves**          | Frequente                                               | Raramente                                                                                   |
| **Comprometimento da chave** | Arriscado                                               | Difícil                                                                                     |
| **Direção**                  | Pode ser utilizada nos dois sentidos (A → B) ou (B → A) | Somente é usada em um sentido:<br> A → B usando a chave de B <br> B → A usando a chave de A |


## Criptografia Simétrica (1)
- ● O critério e classificação de métodos criptográficos é o número de chaves, que denomina-se criptografia simétrica e assimétrica;
- ● Criptografia SIMÉTRICA a mesma chave é utilizada para criptografar e descriptografar a mensagem;
- ● A chave deve ser compartilhada entre o emissor e o receptor da mensagem;
- ● A maior complexidade deste tipo de criptografia é manter a chave privada secreta.

## Uma chave única

m < c(m) > d(c(m))

- ● Criptografia simétric é utilizada para processo que envolvem grandes volumes de dados;
- ● Frequentemente a criptografia simétrica é combinada com a assimétrica, para que se possa alcançar um balanceamento entre segurança e velocidade;
- ● Na criptografia simétrica existem cinco componentes: [1] o texto simples, [2] o algoritmo de criptografia, [3] a chave secreta, [4] o texto cifrado e [5] o algoritmo de descriptografia. (SILVA, 2021);
- ● É comum os algoritimos de criptografia simétricos seja orientados a bits, e não a caracteres. Isso permite que qualquer arquivo digital como texto, video, musicas ou até mesmo imagens sejam criptografado

| **Tamanho da Chave**           | **Número de Chaves** | **Tempo Requerido** | **Tempo Requerido** |
| ------------------------------ | -------------------- | ------------------- | ------------------- |
|                                |                      | *Cenário 1*         | *Cenário 2*         |
| **32 bits**                    | 2³² = 4,3 × 10⁹      | 35,8 minutos        | 2,15 milissegundos  |
| **56 bits**                    | 2⁵⁶ = 7,2 × 10¹⁶     | 1.142 anos          | 10,01 horas         |
| **128 bits**                   | 2¹²⁸ = 3,4 × 10³⁸    | 5,4 × 10²⁴          | 5,4 × 10¹⁸ anos     |
| **26 caracteres (permutação)** | 26! = 4 × 10²⁶       | 6,4 × 10¹²          | 6,4 × 10⁶           |

- ● A criptorafia simétrica pode se basear em funções matemáticas que efetuam permutas ou combinações;
- ● Seja S um conjunto finito. A Permutação p sobre S é uma bijeção de S sobre ele mesmo, ou seja, p : S → S.
- ● Exemplo: Seja S ={1, 2, 3, 4, 5}. Uma permutação p : S → S definida por p(1) = 3 ; p(2) = 5 ; p(3) = 4 ; p(4) = 2 ; p(5) = 1 pode ser representada pela seguinte forma matricia
- ● Um dos modelos básicos da criptografia simétrica é o sistema de transformação de bits
- ● Uma pessoa A deseja enviar uma mensagem sigilosa para outra pessoa B, que deverá ser cifrada substituindo-se cada letra por um número, que será convertido por meio da aplicação da função f(x) = 3x − 2, obtendo assim a mensagem cifrada. Por exemplo, a letra m corresponde ao número 13, que é transformado pela função em f(13) = 3 × 13 − 2 = 37, ou seja, a letra m é cifrada pelo número 37 (m → 37)
PARA DECIFRAR:

## Data Encryption Standart(DES)

## Criptografia Assimétrica 
- ● Neste modelo, são utilizadas duas chaves, uma chave pública e outra privada (que é a chave secreta);
- ● A criptografia assimétrica também é conhecida como criptografia de chave pública, mas nos sistemas criptográficos assimétricos, a garantia da confidencialidade está contida na chave privada;
- ● O método criptográfico assimétrico foi definido pelos pesquisadores Whitfield Diffie e Martin Hellman no artigo, “New directions in cryptography”, no qual estimaram que a progressão da vlocidade e volume da transmissão de mensagens em rede exigiria processos criptográficos mais eficazes (DIFFIE; HELLMAN, 1976);
- ● A criptografia assimétrica é o método padrão atualmente adotado;
- ● A maior vantagem da criptografia assimétrica é que a chave pública pode ser distribuída livremente, e apenas o destinatário poderá descritografar a mensagem usando sua chave privada, que é o segredo do processo;
- ● Entre os elementos fundamentais de segurança relativos às chaves pública e privada, vale salientar:
- ● Deve ser computacionalmente inviável descobrir a chave de descriptografia a partir do simples conhecimento do algoritmo de criptografia utilizado;
- ● Deve ser inviável a obtenção da chave privada conhecendo-se a chave pública;
- ● Em termos de criptoanálise, um documento cifrado pode ser considerado computacionalmente seguro quando atende e dois critérios:
- ● O custo para quebrar o texto cifrado excede ao valor da informação cifrada;
- ● O tempo requerido para quebrar o texto cifrado excede o tempo de vida útil da informação.
Processo de funcionamento da criptografia e descriptografia nos ambientes assimétricos:
Suponha que um usuário “A” digite uma mensagem em texto claro, em que cada letra do texto claro pode ser presentada em um conjunto X (X = [x1, x2, ..., xn]). Os “n” elementos de X são
letras em algum alfabeto finito (a, b, c, d, e, f, ... z). A mensagem do usuário A é direcionada para o usuário B.
- 1) O computador do cliente e o servidor trocam suas chaves públicas;
- 2) O computador do cliente usa a chave pública enviada pelo servidor e efetua a critopgrafia da mensagem;
- 3) Depois que o cliente envia a mensagem criptografada ao servidor, o servidor utiliza a sua chave privada e descriptografa a mensagem do cliente;
- 4) Logo após descriptografar a mensagem, o servidor faz o devido uso do texto original e novamente efetua a criptografia da mensagem que deve ser devolvida ao cliente, usando a chave pública do cliente;
- 5) Para encerrar o processo, o cliente deve descriptografar a mensagem usando sua chave privada.

### Algoritmo RSA 

- ● O Método RSA foi criado por Ron Rivest, Adi Shamir e Leonard Adlema, que hoje é usado na internet;
- ● É baseado na Teoria dos Números, nas propriedades dos números primos e na aritmética modular;
- ● O algoritmo funciona nos seguintes termos:
- 1) O algoritmo se inicia com uma pré-codificação. Para que o RSA codifique uma mensagem, ela deve estar em formato numérico.
Portanto, alguma forma de conversão das mensagens textuais em números inteiros deve ser utilizada. Poderia ser usada, por
exemplo, uma função como demonstrado anteriormente.
2) Realizada a pr ́s-codificação, o algoritmo solicita que se escolha dois números primos. Geralmente, são escolhidos números muito
grandes, com mais de 100 dígitos (170141183460469231731687303715884105727 que é um Primos de Mersenne, números primos
que tem a forma ). Estes números serão as variáveis p e q, cujos valores serão:
p = 3, q = 11
3) Multiplicamos p e q para se obtermos a variável n:
n = p * q
n = 33
4) Calculamos a variável z, nos seguintes termos
z = (p-1)(q-1)
z = (3-1)(11-1)

Criptografia Assimétrica (4) – Algoritmo RSA
5) Escolher o número E, que deve ser menor que Z e primo. Esta escolha é condicionada à seguinte regra:
m.d.c(E,n) = 1
 m.d.c(E,33) = 1
Ou seja, deve obrigatoriamente ser um número cujo máximo divisor comum entre ele e n seja 1. O número E escolhido foi 7.
Então, m.d.c (7,33) = 1, portanto E = 7
6) Escolher o número D, que deve estar entre p e q, nos seguintes termos
E x D = 1 mod (p-1)(q-1)
Ou seja,o número D deve ser tal que o produto de E x D, quando dividido por (p-1)(q-1) precisa ter resto 1. O número D será 3, pois
7 x 3 = 1 mod(20), pois
21 = 1 + 20
Neste ponto já possuímos os valores das variáveis p, q, n, E e D, que são do conhecimento do site de origem do processo. Estas variáveis não serão
todas divulgadas em rede, mas somente os valores de n e E

) Funcionamento do processo de criptografia no lado do servidor
O usuário faz uma compra e informa seu número de cartão de crédito, que no nosso caso será 2. O algoritmo no site de compras enviará para a loja os valores de n e E. O seguinte processo é realizado pelo
site, antes de enviar os dados:
- determinaremos o número a nos seguintes termos:
Ou seja, elevamos a a E, dividimos por n e obtemos o resto da divisão, que é o valor b. Considerando n=33, E=7, e a=2, teremos b=29, pois:
O site de compras no lado do servidor recebe o número 29 (2 criptografado)
8) Como obter o número original do cartão de crétido?
O site de compras, do lado do cleinte, possui várias informações: p = 3; E = 7; b = 29; q = 11; D = 3; n = 33. Para que o valor original do cartão seja obtido, é necessário realizar o seguinte cálculo:
Ou seja, eleva b a D, divide por n e obtem-se o resto da divisão, que será o valor original do cartão, que é 2.
aE=d mod (n)
27=29+3 x 33
bD=a mod (n)→293=2+739 x 33


## Ataques em sistemas computacionais
O ataque a uma organização é, de maneira geral, qualquer ação que compromete a segurança de uma informação que esta organização possui. Isso pode ocorrer de várias formas, como o acesso não autorizado a uma rede de computadores ou a uma informação codifi cada (quando o atacante
decifra o código), por exemplo. Há vários modos de ataques e serviços utilizados para preveni-los. Nesta aula, veremos os tipos gerais e o que cada um destes ataques objetiva.
Se o ataque é uma ação que busca acesso não autorizado de uma organização ou indivíduo, a segurança da informação possui como metas essenciais detectar e prevenir os ataques.
Uma defesa eficiente exige conhecimento completo dos objetivos e técnicas de ataque.
A seguir, veremos alguns exemplos de ataques e condutas que comprometem a segurança da informação. Muitos deles não são “ataques” no sentido usual do termo, mas formas de “trapaça”, maneiras de subverter as regras de um sistema e a confiança de outros.
### Violação de segredo ou privacidade
É o acesso não autorizado à informação. Acontece, por exemplo, se alguma pessoa ler um email, tiver acesso aos arquivos pessoais de um indivíduo etc. Pode ocorrer em uma rede
de computadores quando alguém se coloca e passa a “ouvir” toda a comunicação dentro dela.
### Passar-se por outra pessoa
Acontece quando alguém usa documentos de outro para fins fraudulentos. Alguém pode, por exemplo, usar um cartão de crédito e realizar compras, ou ainda roubar um talão de
cheques e usá-los, falsificando a assinatura.
### Negar responsabilidade por informação originada
Acontece quando alguém origina uma informação e depois nega que o fez. Um exemplo é quando uma pessoa faz uma compra com cartão e depois liga para a administradora,
dizendo que este foi roubado antes que a compra tivesse sido feita. Outro exemplo é quando uma pessoa envia um email, depois arrepende-se e alega que foi outra.
### Negar recebimento de informação
Ocorre quando alguém recebe uma informação e depois nega que a recebeu. Um exemplo: quando uma pessoa age incorretamente, ela é avisada, permanece no erro, e depois nega que tenha sido alertada ### Falsear informação recebida
Uma pessoa pode receber informação de alguém, mas divulgar para terceiros outra como sendo a recebida.
### Troca de informação
Acontece quando um atacante intercepta uma mensagem entre duas pessoas e consegue modificá-la sem que isto seja percebido por seu receptor.
### Impedir que uma informação seja disponibilizada ou transmitida entre duas pessoas.
Há vários exemplos: muitas vezes hackers atacam de forma organizada sites na internet com o objetivo de tirá-lo do ar (talvez para desacreditar a segurança do site). Outro exemplo ocorre quando uma comunicação é interrompida em trânsito, como acontece durante as guerras, em
que as correspondências das pessoas são monitoradas e qualquer informação “suspeita” é impedida de continuar. Nestes casos, o receptor pode não saber que a informação foi transmitida.

## Categorias de ataques

Para classificar as diversas formas de ataque é necessário entender um sistema que armazena uma informação como um provedor, uma fonte desta informação. Toda informação tem seus destinatários autorizados, isto é, pessoas para as quais ela se
destina.
O esquema pode ser representado pela figura a seguir.
O fluxo de informação acontece na forma de comunicação entre duas pessoas ou organizações, na transmissão de um arquivo, em uma informação divulgada em um site na internet ou no acesso de uma pessoa autorizada a um banco de dados, por exemplo

Interrupção
Ataque em que a informação é impedida de chegar ao destinatário, poisfoi interceptada ou destruída.
Este é um ataque à disponibilidade da informação.
Acontece quando, por exemplo, um servidor contendo a informação é fi sicamente destruído, uma linha
de comunicação (cabo de rede, linha telefônica etc.) é interrompida, um servidor de internet recebe um
ataque e fica “fora do ar”, entre outros.

Para classificar as diversas formas de ataque é necessário entender um sistema que armazena uma
informação como um provedor, uma fonte desta
informação. Toda informação tem seus destinatários autorizados, isto é, pessoas para as quais ela se
destina.
O esquema pode ser representado pela figura a seguir.
O fluxo de informação acontece na forma de comunicação entre duas pessoas ou organizações, na
transmissão de um arquivo, em uma informação divulgada em um site na internet ou no acesso de uma
pessoa autorizada a um banco de dados, por exemplo.
