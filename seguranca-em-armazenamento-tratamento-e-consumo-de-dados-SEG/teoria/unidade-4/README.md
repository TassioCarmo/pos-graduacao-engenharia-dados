# Logica fuzzy

Sistemas Autônomos Inteligentes
Lógica Fuzzy
Profs. João Alberto FabroProfs. João Alberto Fabro
André Schneider de OliveiraAndré Schneider de Oliveira
Adaptado de material dos profs. Mauro Roisenberg e
Luciana Rech - UFSC
IntroduçãoIntrodução
● A Lógica Fuzzy é baseada na teoria dos conjuntos
fuzzy.
● Tradicionalmente, uma proposição lógica tem dois
extremos: ou é completamente verdadeiro ou é
completamente falso.
● Entretanto, na lógica Fuzzy, uma premissa varia em
grau de verdade de 0 a 1, o que leva a ser
parcialmente verdadeira ou parcialmente falsa.
● Surgiu com Lofti A. Zadeh, Berkeley (1965).
– para tratar do aspecto vago da informação;
– 1978 – desenvolveu a Teoria das Possibilidades
● menos restrita que a noção de probabilidade
– ligar a linguística e a inteligência humana, pois muitos conceitos
são melhores definidos por palavras do que pela matemática.
● É uma técnica baseada em graus de pertinência (verdade).
– os valores 0 e 1 ficam nas extremidades
– inclui os vários estados de verdade entre 0 e 1
– idéia: todas as inf. admitem graus (temperatura, altura,
velocidade, distância, etc...)
IntroduçãoIntrodução
IntroduçãoIntrodução
● Considerando a seguinte sentença: Joãozinho é alto.
● A proposição é verdadeira para uma altura de Joãozinho 1.65m?
● O termo linguístico “alto” é vago, como interpretá-lo?
● A teoria de conjuntos Fuzzy (semântica para lógica fuzzy) permite
especificar quão bem um objeto satisfaz uma descrição vaga
(predicado vago)
IntroduçãoIntrodução
● Lógica convencional: sim/não, verdadeiro/falso
● Lógica Fuzzy (difusa ou nebulosa):
● Refletem o que as pessoas pensam
● Tenta modelar o nosso senso de palavras, tomada de
decisão ou senso comum
● Trabalha com uma grande variedade de informações vagas e
incertas, as quais podem ser traduzidas por expressões do
tipo: a maioria, mais ou menos, talvez, etc.
IntroduçãoIntrodução
● Sistemas baseados em lógica fuzzy podem ser
usado para gerar estimativas, tomadas de decisão,
sistemas de controle mecânico...
● Ar condicionado.
● Controles de automóveis.
● Casas inteligentes.
● Controladores de processo industrial.
● etc...
IntroduçãoIntrodução
● O Japão é um dos maiores utilizadores e difusores da lógica
fuzzy.
● O metrô da cidade de Sendai utiliza desde 1987 um sistema de controle
fuzzy.
● Aspiradores de pó e máquinas de lavar da empresa Matsushita -
carrega e ajusta automaticamente à quantidade de detergente
necessário, a temperatura da água e o tipo de lavagem.
● TVs da Sony utilizam lógica fuzzy para ajustar automaticamente o
contraste, brilho, nitidez e cores.
● A Nissan utiliza lógica fuzzy em seus carros no sistema de transmissão
automática e freios antitravamento.
● Mitsubishi tem um ar condicionado industrial que usa um controlador
fuzzy. Economiza 24% no consumo de energia.
● Câmeras e gravadoras usam fuzzy para ajustar foco automático e
cancelar os tremores causados pelas mãos trêmulas.
Conjuntos FuzzyConjuntos Fuzzy
Conjuntos com limites imprecisos
Altura
(m)
1.75
1.0
Conjunto Clássico
1.0
Função de
pertinência
Altura
(m)
1.60 1.75
0.5
0.9
Conjunto Fuzzy
A = Conjunto de pessoas altas
0.8
1.70
Conjuntos FuzzyConjuntos Fuzzy
● Um conjunto fuzzy A definido no universo X é caracterizado por uma
função de pertinência uA, a qual mapeia os elementos de X para o
intervalo [0,1].
uA:X  [0,1]
● Desta forma, a função de pertinência associa a cada elemento y
pertencente a X um número real no intervalo [0,1], que representa o
grau de pertinência do elemento y ao conjunto A, isto é, o quanto é
possível para o elemento y pertencer ao conjunto A.
● Uma sentença pode ser parcialmente verdadeira e parcialmente falsa.
Conjuntos FuzzyConjuntos Fuzzy
A função de pertinência A(X) indica o grau de compatibilidade entre x
e o conceito expresso por A:
A(x) = 1 indica que x é completamente compatível com A;
A(x) = 0 indica que x é completamente incompatível com A;
0 < A(x) < 1 indica que x é parcialmente compatível com A, com
grau A(x) .
crisp
pode ser visto como um conjunto nebuloso específico (teoria de
conjuntos clássica)
A {0,1} pertinência do tipo “tudo ou nada”, “sim ou não” e não gradual
como para os conjuntos nebulosos
Conjuntos FuzzyConjuntos Fuzzy
Definição formal: Um conjunto fuzzy A em X é expresso
como um conjunto de pares ordenados:
A={( x , u A ( x ))|x ∈ X }
UniversoConjunto
Fuzzy
Função de
Pertinência
Um conjunto fuzzy é totalmente caracterizado
por sua função de pertinência.
Função de PertinênciaFunção de Pertinência
● Reflete o conhecimento que se tem em relação a
intensidade com que o objeto pertence ao conjunto
fuzzy.
● Várias formas diferentes.
● Características das funções de pertinência:
● Medidas subjetivas.
● Funções não probabilísticas monotonicamente crescentes,
decrescentes ou subdividida em parte crescente e parte
decrescente.
Função de PertinênciaFunção de Pertinência
Altura (m)
“alto” no Brasil
1.75
0.5
0.8
0.1
“alto” nos Estados Unidos
“alto” na Itália
Função de PertinênciaFunção de Pertinência
● Função Triangular:
● Função Trapezoidal:
● Função Gaussiana:
● Função Sino Generalizada:
gbellmf ( x ; a , b , c )= 1
1+| x −c
b |
2 b
gaussmf ( x ; a , b , c )=e
− 1
2 ( x −c
σ )
2
trapmf ( x ; a , b , c ,d )=max ( min ( x−a
b−a , 1, d −x
d−c ) , 0 )
trimf ( x ; a , b , c )=max ( min ( x −a
b−a , c−x
c−b ) , 0 )
Função de PertinênciaFunção de Pertinência
0 20 40 60 80 100
0
0.2
0.4
0.6
0.8
1
Grau de Pertinência
(a) Triangular
0 20 40 60 80 100
0
0.2
0.4
0.6
0.8
1
Grau de Pertinência
(b) Trapezoidal

Grau de Pertinência
(c) Gaussiana

Grau de Pertinência
(d) Sino Gerneralizada
Função de Pertinência: Universo DiscretoFunção de Pertinência: Universo Discreto

X = Número de filhos
Grau de Pertinência
Universo Discreto
Função de Pertinência: Universo ContínuoFunção de Pertinência: Universo Contínuo
Função de Pertinência: Universo ContínuoFunção de Pertinência: Universo Contínuo
Variável LinguísticaVariável Linguística
Grau de Pertinência Jovem Adulto Idoso
Variáveis LinguísticasVariáveis Linguísticas
● Uma variável linguística possui valores que não são números, mas
sim palavras ou frases na linguagem natural.
● Idade = idoso
● Um valor linguístico é um conjunto fuzzy.
● Todos os valores linguísticos formam um conjunto de termos:
● T(idade) = {Jovem, velho, muito jovem,...
Adulto, não adulto,...
Velho, não velho, muito velho, mais ou menos velho...}
● Permitem que a linguagem da modelagem fuzzy expresse a
semântica usada por especialistas. Exemplo:
Se duração_do_projeto == não muito longo então
risco = ligeiramente reduzidoVariáveis LinguísticasVariáveis Linguísticas
● Uma variável linguística possui valores que não são números, mas
sim palavras ou frases na linguagem natural.
● Idade = idoso
● Um valor linguístico é um conjunto fuzzy.
● Todos os valores linguísticos formam um conjunto de termos:
● T(idade) = {Jovem, velho, muito jovem,...
Adulto, não adulto,...
Velho, não velho, muito velho, mais ou menos velho...}
● Permitem que a linguagem da modelagem fuzzy expresse a
semântica usada por especialistas. Exemplo:
Se duração_do_projeto == não muito longo então
risco = ligeiramente reduzido
● Uma sentença modificada pela palavra “não” é dita
“negação” da sentença original.
● NÃO-fuzzy(x) = 1 - x
● A palavra “e” é usada para juntar duas sentenças
formando uma “conjunção” de duas sentenças.
● E-fuzzy(x,y) = Mínimo(x,y)
● De maneira similar a sentença formada ao conectarmos
duas sentenças com a palavra “ou” é dita “disjunção” das
duas sentenças.
● OU-fuzzy(x,y) = Máximo(x,y)
Operações sobre conjuntos
fuzzy● Uma sentença modificada pela palavra “não” é dita
“negação” da sentença original.
● NÃO-fuzzy(x) = 1 - x
● A palavra “e” é usada para juntar duas sentenças
formando uma “conjunção” de duas sentenças.
● E-fuzzy(x,y) = Mínimo(x,y)
● De maneira similar a sentença formada ao conectarmos
duas sentenças com a palavra “ou” é dita “disjunção” das
duas sentenças.
● OU-fuzzy(x,y) = Máximo(x,y)
Operações sobre conjuntos
fuzzy
Operadores Fuzzy
● Suponha que desejássemos representar de forma fuzzy a altura de Alice
(1,65 m), Bob (1,75 m), Carlos(2,0m) e Denise(1,45 m). Nossas
proposições serão da forma "X é alto", e serão:
– A = Alice é alta, μ(A)=0,55
– B = Bob é alto, μ(B)=0,75
– C = Carlos é alto, μ(C) = 1,0
– D = Denise é alta, μ(D) = 0,0
● Usando os operadores fuzzy, podemos escrever sentenças como:
– Carlos não é alto, NÃO(C), μ(NÃO(C))= 1,0 - μ(C) = 0,0
– Bob não é alto, NÃO(B), μ(NÃO(B))= 1,0 - μ(B) = 0,25
– Denise é alta e Alice é Alta, D e A, μ(D e A)= mínimo (μ(D), μ(A)) =0,0Operadores Fuzzy
● Suponha que desejássemos representar de forma fuzzy a altura de Alice
(1,65 m), Bob (1,75 m), Carlos(2,0m) e Denise(1,45 m). Nossas
proposições serão da forma "X é alto", e serão:
– A = Alice é alta, μ(A)=0,55
– B = Bob é alto, μ(B)=0,75
– C = Carlos é alto, μ(C) = 1,0
– D = Denise é alta, μ(D) = 0,0
● Usando os operadores fuzzy, podemos escrever sentenças como:
– Carlos não é alto, NÃO(C), μ(NÃO(C))= 1,0 - μ(C) = 0,0
– Bob não é alto, NÃO(B), μ(NÃO(B))= 1,0 - μ(B) = 0,25
– Denise é alta e Alice é Alta, D e A, μ(D e A)= mínimo (μ(D), μ(A)) =0,0
● A lógica está claramente associada a teoria dos conjuntos.
Cada afirmação (do tipo "Carlos é alto") representa na verdade
o grau de pertinência de Carlos ao conjunto de pessoas altas.
● Isso permite que conjuntos como "alto" e "baixo" sejam
tratados de forma separadas e afirmações como "Carlos é alto
0,75" e "Carlos é baixo 0,5" sejam válidas simultaneamente,
ao contrário do que seria esperado em um modelo crisp.
● Esse tipo de afirmação é facilmente encontrada na descrição,
por humanos, na forma como entendem certo conceito, e a
lógica difusa é uma ótima forma de tratar essa forma de
incerteza.
23
Controle Fuzzy
● Sistema de controle fuzzy baseado no
modelo de Mamdani.
Componentes de um
sistema de controle fuzzy
 Definição das variáveis fuzzy de
entrada e de saída: forma e valores das
variáveis
 Regras fuzzy
 Técnica de defuzzificaçãoComponentes de um
sistema de controle fuzzy
 Definição das variáveis fuzzy de
entrada e de saída: forma e valores das
variáveis
 Regras fuzzy
 Técnica de defuzzificação
26
Definição das variáveis
● Etapa na qual as variáveis linguísticas são definidas de forma
subjetiva, bem como as funções membro (funções de pertinência)
● Engloba
– Análise do Problema
– Definição das Variáveis
– Definição das Funções de pertinência
– Criação das Regiões
● Na definição das funções de pertinência para cada variável,
diversos tipos de espaço podem ser gerados:
– Triangular, Trapezoidal, Gaussiana, ...
27
Temperatura (oC)
Frio Normal Quente
Velocidade(m/s)
Lento Rápido
Exemplos de variáveis fuzzy
1 1
Regras Fuzzy
SE condição ENTÃO conclusão , mas com variáveis
linguísticas (fuzzy)
Exemplo:
Se a fruta é verde então o gosto é azedo
Se a fruta é amarela então o gosto é pouco-doce
Se a fruta é vermelha então o gosto é doceRegras Fuzzy
SE condição ENTÃO conclusão , mas com variáveis
linguísticas (fuzzy)
Exemplo:
Se a fruta é verde então o gosto é azedo
Se a fruta é amarela então o gosto é pouco-doce
Se a fruta é vermelha então o gosto é doce
29
Regras Fuzzy
● E o raciocínio?
– Avaliar o antecedente
– Aplicar o resultado ao consequente
– As regras são ativadas parcialmente, dependendo
do antecedente
● Ex: Se a altura é alta, o peso é pesado (altura =1.85, peso = ?)
.5
.75
.1
Alto
.5
.75
.1
Pesado
Operações BásicasOperações Básicas
0
0.2
0.4
0.6
0.8
1
A está contido em B
Grau de Pertinência
B
A
(a) Conjuntos Fuzzy A e B (b) Conjunto Fuzzy não “A”
0
0.2
0.4
0.6
0.8
1 A B
0
0.2
0.4
0.6
0.8
1
0
0.2
0.4
0.6
0.8
1
(c) Conjunto Fuzzy "A ou B"
0
0.2
0.4
0.6
0.8
1
(d) Conjunto Fuzzy "A e B"
Exemplo: União e InterseçãoExemplo: União e Interseção
● X = {a, b, c, d, e}
● A = {1/a, 0.7/b, 0.3/c, 0/d, 0.9/e}
● B = {0.2/a, 0.9/b, 0.4/c, 1/d, 0.4/e}
● União
● C = {1/a, 0.9/b, 0.4/c, 1/d, 0.9/e}
● Interseção
● D = {0.2/a, 0.7/b, 0.3/c, 0/d, 0.4/e}Exemplo: União e InterseçãoExemplo: União e Interseção
● X = {a, b, c, d, e}
● A = {1/a, 0.7/b, 0.3/c, 0/d, 0.9/e}
● B = {0.2/a, 0.9/b, 0.4/c, 1/d, 0.4/e}
● União
● C = {1/a, 0.9/b, 0.4/c, 1/d, 0.9/e}
● Interseção
● D = {0.2/a, 0.7/b, 0.3/c, 0/d, 0.4/e}
Regras - ExemplosRegras - Exemplos
Regras CRISP(Não Fuzzy):
1.Se velocidade > 100 Então
DPP é 30 metros
2.Se velocidade < 40 Então
DPP é 10 metros
Regras Fuzzy:
1.Se velocidade é alta Então
DPP é longa
2. Se velocidade é baixa
Então DPP é curta
Etapas do Raciocínio FuzzyEtapas do Raciocínio Fuzzy
1ª Fuzzificação
2ª Inferência
Agregação
3ª Defuzzificação
ComposiçãoEtapas do Raciocínio FuzzyEtapas do Raciocínio Fuzzy
1ª Fuzzificação
2ª Inferência
Agregação
3ª Defuzzificação
Composição
Etapas do Raciocínio FuzzyEtapas do Raciocínio Fuzzy
Linguístico
Numérico
Nível
Variáveis Calculadas
Variáveis Calculadas
(Valores Numéricos)
(Valores Linguísticos)
Inferência
Variáveis de Comando
Defuzzificação
Fuzzificação
(Valores Linguísticos)
Variáveis de Comando
(Valores Numéricos)
Nível
FuzzificaçãoFuzzificação
● Etapa na qual as variáveis linguísticas e as funções de pertinência
são definidas de forma subjetiva.
● Engloba
● Análise do Problema
● Definição das Variáveis
● Definição das Funções de pertinência
● Criação das Regiões
● Na definição das funções de pertinência para cada variável, diversos
tipos de espaço podem ser gerados:
● Triangular, Trapezoidal, ...
FuzzificaçãoFuzzificação
Triangular
Frio Normal Quente
Trapezoidal
Lento Rápido
Inferência FuzzyInferência Fuzzy
● Etapa na qual as proposições (regras) são definidas
e depois são examinadas paralelamente
● Engloba:
● Definição das proposições
● Análise das Regras
● Criação da região resultante
Inferência FuzzyInferência Fuzzy
● O mecanismo chave do modelo Fuzzy é a proposição.
● A proposição é o relacionamento entre as variáveis do
modelo e regiões Fuzzy.
● Na definição das proposições, deve-se trabalhar com:
● Proposições Condicionais:
Se W == Z então X = Y
● Proposições Não-Condicionais:
X = Y
Inferência FuzzyInferência Fuzzy
Agregação: Calcula a importância de uma
determinada regra para a situação corrente
Composição: Calcula a influência de cada regra
nas variáveis de saída.
DefuzzificaçãoDefuzzificação
● Etapa no qual as regiões resultantes são convertidas em
valores para a variável de saída do sistema.
● Esta etapa corresponde a ligação funcional entre as regiões
Fuzzy e o valor esperado.
● Dentre os diversos tipos de técnicas de defuzzificação
destaca-se:
● Centróide
● First-of-Maxima
● Middle-of-Maxima
● Critério Máximo
DefuzzificaçãoDefuzzificação
Exemplos:
z0 z0 z0
Centróide First-of-Maxima Critério Máximo
Exemplo Inferência FuzzyExemplo Inferência Fuzzy
● Exemplo:
● Um analista de projetos de uma empresa quer determinar o
risco de um determinado projeto.
● Variáveis: Quantidade de dinheiro e de pessoas envolvidas
no projeto.
● Base de conhecimento:
● Se dinheiro é adequado ou o número de pessoas é pequeno
então risco é pequeno.
● Se dinheiro é médio e o numero de pessoas é alto, então
risco é normal.
● Se dinheiro é inadequado, então risco é alto.
Exemplo Inferência FuzzyExemplo Inferência Fuzzy
Passo 1: Fuzzificar
μ i ( d )=0, 25∧μ m ( d )=0,75
Dinheiro
Inadequado Médio Adequado
35
0.25
0.75
Número de Pessoas
60
Baixo Alto
0.2
0.8
μ b ( p)=0,2∧μa ( p )=0,8Exemplo Inferência FuzzyExemplo Inferência Fuzzy
Passo 1: Fuzzificar
μ i ( d )=0, 25∧μ m ( d )=0,75
Dinheiro
Inadequado Médio Adequado
35
0.25
0.75
Número de Pessoas
60
Baixo Alto
0.2
0.8
μ b ( p)=0,2∧μa ( p )=0,8
Exemplo Inferência FuzzyExemplo Inferência Fuzzy
Passo 2: Avaliação das regras
Ou  máximo e  mínimo
Adequado
Regra 1:
Baixo0,0
ou
0,2
Risco
médio
Regra 2:
Alto
0,25 e
0,8
Risco
Exemplo Inferência FuzzyExemplo Inferência Fuzzy
Risco
Inadequado
Regra 3:
0,75
Exemplo Inferência FuzzyExemplo Inferência Fuzzy
Passo 3: Defuzzificação
Cálculo do Centróide
Risco
0.75
0.25
C=( 10+ 20+30 +40 )∗0,2+( 50+60 +70 )∗0, 25 +(80 +90+ 100)∗0, 75
0,2+0,2+0,2+ 0,2+0, 25+ 0, 25+0, 25+ 0, 75+0, 75+ 0,75 =267 , 5
3,8 =70 , 4
10 20 30 40 706050 1009080
Outro ExemploOutro Exemplo
● O sistema tem como objetivo determinar a
gorjeta que um cliente deve dar.
● Esse sistema possui três variáveis
(serviço, comida e gorjeta).
● As variáveis comida e serviço são
variáveis de entrada e gorjeta é a variável
de saída.
Outro ExemploOutro Exemplo
Bibliotecas FuzzyBibliotecas Fuzzy
● Softwares para auxílio a projeto e
implementação de Sistemas Fuzzy:
– Fuzzy Toolbox do Matlab
– SciFLT for Scilab (free)
– X-Fuzzy (free)
– FuzzyClips (free, API para Java)
– FLIE (Fuzzy Logic Inference Engine) do Fabro...
50
Exemplos
 Softwares para auxílio a projeto e implementação de
Sistemas Fuzzy:
 InFuzzy (desenvolvido na UNISC)
 Fuzzy Toolbox do Matlab
 NEFCON, NEFCLASS e NEFPROX... (desenvolvidos pela
Universidade de Magdeburg)
 disponível para download em
 http://fuzzy.cs.uni-magdeburg.de/
 http://fuzzy.cs.uni-magdeburg.de/wiki/pmwiki.php?n=Forschung.Software
 SciFLT for Scilab (free)
 UnFuzzy (free)
 FuzzyTech
 FuzzyClips (free, API para Java)

## Conjuntos Fuzzy



## Função de Pertinência

### Triangular

### Trapezoidal

### Função de Pertinência: Universo Discreto

### Função de Pertinência: Universo Contínuo

### Variável Linguística

Um valor linguístico é um conjunto fuzzy.
● Todos os valores linguísticos formam um conjunto de termos:
● T(idade) = {Jovem, velho, muito jovem,...
Adulto, não adulto,...
Velho, não velho, muito velho, mais ou menos velho...}
● Permitem que a linguagem da modelagem fuzzy expresse a
semântica usada por especialistas. Exemplo:
Se duração_do_projeto == não muito longo então
risco = ligeiramente reduzido

especialista que cria aas regras


### Controle Fuzzy

### Componentes de um sistema de controle fuzzy

### Definição das variáveis

- dentro da estrutura lógica do do de fase instruções, elas não têm as variáveis, elas não precisam respeitar a mesma escala, está elas pode respeitar escalas completamente diferentes.

## Operadores Fuzzy

<img width="1186" height="313" alt="image" src="https://github.com/user-attachments/assets/3c57be61-c816-4b9d-9193-8076498926d5" />


- AO sistema fase esse gráfico, ele é o tira teima que a gente faz para ver se essas essas regras estão certas, OK? Elas estão estão todas em um processo crescente.


<img width="1118" height="579" alt="image" src="https://github.com/user-attachments/assets/50dee26c-c98a-448e-811b-60802dc6d14f" />

<img width="1102" height="453" alt="image" src="https://github.com/user-attachments/assets/18678b20-2c1f-4406-a410-0a3f2133e3ef" />



-----------------------


classificação em cluster 

<img width="1101" height="741" alt="image" src="https://github.com/user-attachments/assets/19c80c0f-b8ac-4c2c-8dfe-53bada754930" />

" A rede da a Google gastou. 200000000 de dólares para treinar o seu gemini."
Isso tudo porque ela teve que pegar um imenso conjunto de dados. 
Ela teve que ela teve que fazer a engenharia de features , né? Ela teve que determinar por meio de testes, quais eram as fichas necessárias, quais eram os atributos necessários.
Que a rede deve os atributos que a rede deveria aprender.


E aí ela tinha que colocar para treinar uma rede e aí ela pode ter definido milhares de features, milhares para rodar esses milhares de futuros para a rede aprender esses milhares de futuros. Ela deve. Ela tem que ter provavelmente reservado, imenso espaço numa numa rede computacional de al.
Carlos Murilo da Silva Valadares 2 horas 43 minutos 24 segundos
Desempenho.
Para ficar lá, dias ou semanas com a rede aprendendo aquilo, então é onde se gasta dinheiro com a rede, né
