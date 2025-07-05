# Logica fuzzy

**Sistemas especialistas Fuzzy**

**Tratamento de dados segundo o pensamento do especialista:**
▪ Senso comum para resolver problemas
▪ Impreciso, inconsistente, incompleto, vago
“Embora o transformador esteja *um pouco* carregado, pode-se usá-lo por *um tempo*”
▪ Análise de dados para problemas com limites imprecisos e certo volume de opções para tomada de decisões

**Lógica Fuzzy:**
▪ Ideia: todas as coisas admitem graus (temperatura, altura, velocidade, distância, etc...)
▪ Desenvolvida por Lofti A. Zadeh da Universidade da Califórnia em Berkeley na década de 60


---

**Características: Lógica Fuzzy (1/2)**

* Lógica convencional: sim-ou-não, verdadeiro-ou-falso

* **Lógica Fuzzy** (difusa ou nebulosa):
  ▪ Refletem o que as pessoas pensam
  ▪ Tenta modelar o nosso senso de palavras, tomada de decisão ou senso comum

* Trabalha com uma grande variedade de informações vagas e incertas, as quais podem ser traduzidas por expressões do tipo: *a maioria, mais ou menos, talvez*, etc.


**Antes do surgimento da lógica fuzzy essas informações não tinham como ser processadas;**

**A lógica fuzzy contém como casos especiais não só os sistemas lógicos binários, como também os multi-valorados;**

**A lógica fuzzy vem sendo aplicada nas seguintes áreas:**
• Análise e tratamento de dados;
• Construção de sistemas especialistas;
• Controle e otimização;
• Reconhecimento de padrões, etc.

**Conjunto de princípios matemáticos para a representação do conhecimento baseado no grau de pertinência dos termos**

![image](https://github.com/user-attachments/assets/df0afe91-1c2d-4bf6-9053-40ad52ec70ae)


Um conjunto fuzzy A definido no universo de discurso X é caracterizado por uma **função de pertinência μA**, a qual mapeia os elementos de X para o intervalo [0,1].

μA:X→[0,1]

Desta forma, a função de pertinência associa a cada elemento x pertencente a X um número real μA(x) no intervalo [0,1], que representa o **grau de pertinência** do elemento x ao conjunto A, isto é, o quanto é possível para o elemento x pertencer ao conjunto A.

Uma sentença pode ser parcialmente verdadeira e parcialmente falsa

μA(x) : X → [0,1], μA(x) = 0
                    0 < μA(x) < 1
                    μA(x) = 1


**■ Definição formal**
• Um conjunto fuzzy A em X é expresso como um conjunto de pares ordenados:

A = {(x, μA(x)) | x ∈ X}

**Conjunto fuzzy** ← **Função de pertinência (MF)** → **Universo ou Universo de discurso**

---

**Um conjunto fuzzy é totalmente caracterizado por sua função de pertinência (MF)**

## Como representar um conjunto Fuzzy num computador?

**1. Função de pertinência**

• Reflete o conhecimento que se tem em relação a intensidade com que o objeto pertence ao conjunto fuzzy
• Métodos para adquirir esse conhecimento do especialista
• Ex: Perguntar ao especialista se vários elementos pertencem a um conjunto
