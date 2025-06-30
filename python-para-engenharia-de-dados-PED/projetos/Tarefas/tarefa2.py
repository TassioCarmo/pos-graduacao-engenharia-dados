## exercicio 1  ####

temperaturas_celsius = [22.5, 40, 13, 29, 34]

def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

temperaturas_fahrenheit = [celsius_para_fahrenheit(temp) for temp in temperaturas_celsius]

print("Temperaturas em Fahrenheit:", temperaturas_fahrenheit)

### exercicio 2 ###

def calcular_faixa_etaria(idades):
    media_idades = sum(idades) / len(idades)
    
    if 0 <= media_idades <= 25:
        return "Turma jovem"
    elif 26 <= media_idades <= 60:
        return "Turma adulta"
    else:
        return "Turma idosa"

n = int(input("Digite o número de pessoas: "))
idades = []

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)

resultado = calcular_faixa_etaria(idades)
print(f"Média de idades: {sum(idades)/len(idades):.2f}")
print(resultado)


#### exercicio 3 ####

def calcular_media_notas(notas):
    melhor_nota = max(notas)
    pior_nota = min(notas)
    
    notas.remove(melhor_nota)
    notas.remove(pior_nota)
    
    media = sum(notas) / len(notas)
    
    return melhor_nota, pior_nota, media

atleta = input("Digite o nome do atleta: ")
notas = []

for i in range(7):
    nota = float(input(f"Digite a nota do jurado {i+1}: "))
    notas.append(nota)

melhor_nota, pior_nota, media = calcular_media_notas(notas[:])

print(f"\nResultado final:\nAtleta: {atleta}")
print(f"Melhor nota: {melhor_nota}")
print(f"Pior nota: {pior_nota}")
print(f"Média: {media:.2f}")