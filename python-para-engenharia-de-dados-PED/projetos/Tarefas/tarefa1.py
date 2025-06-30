
# exercicios pagina 12 

# Exercicio 1
print("Hello World!")

#Exercicio 2 
userInput = str(input("Escreve o numero um numero "))
print("O número informado foi", userInput)


# Exercicio 3
V = input("Digite a quantidade do Item 1 (V): ")
W = input("Digite a quantidade do Item 2 (W): ")
Y = input("Digite a quantidade do Item 3 (Y): ")
X = input("Digite a quantidade do Item 4 (X): ")
Z = input("Digite a quantidade do Item 5 (Z): ")

print(f"""
Item 1 – Quantidade: {V}
Item 2 – Quantidade: {W}
Item 3 – Quantidade: {Y}
Item 4 – Quantidade: {X}
Item 5 – Quantidade: {Z}
""")

# exercicio pagina 13

fruta1 = 1.00
fruta2 = fruta1 * 2
fruta3 = fruta1 / 2
fruta4 = fruta3 * 3
fruta5 = fruta4 / 2

frutas = ['Primeira fruta', 'Segunda fruta', 'Terceira fruta', 'Quarta fruta', 'Quinta fruta']

precos = [fruta1, fruta2, fruta3, fruta4, fruta5]

for i in range(len(frutas)):
    print(f"A {frutas[i]} custa {precos[i]:.2f}")

# exercicio pagina 19

dic_pessoa = {
    'Nome': 'Tassio',
    'Ultimo Nome': 'Carmo',
    'Idade': 27,
    'Curso': 'Engenharia de dados',
    'Endereço': 'Rua das Flores, 123, São Paulo'
}

print(dic_pessoa)
print(dic_pessoa.items())
del dic_pessoa['Ultimo Nome']
print(dic_pessoa)
print(dic_pessoa['Endereço'])
dic_novo_pessoa = dic_pessoa.copy()
dic_novo_pessoa['Idade'] = 30
dic_novo_pessoa['Nome'] = "Alan"
print(dic_novo_pessoa)


