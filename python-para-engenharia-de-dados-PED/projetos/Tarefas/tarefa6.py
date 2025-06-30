def analise_expectativa_vida(input_data):

    expectativa_vida = []
    for line in input_data.strip().split('\n'):
        Cidade, expectativa = line.split(';')
        expectativa_vida.append((Cidade, float(expectativa)))
    
    sorted_data = sorted(expectativa_vida, key=lambda x: x[1], reverse=True)
    
    top_10 = sorted_data[:10]
    bottom_10 = sorted_data[-10:]
    
    with open('maiores_expectativas.txt', 'w', encoding='utf-8') as f:
        f.write("Os 10 expectativa com maior expectativa de vida:\n\n")
        for i, (Cidade, expectativa) in enumerate(top_10, 1):
            f.write(f"{i}. {Cidade}: {expectativa:.2f} anos\n")
    
    with open('menores_expectativas.txt', 'w', encoding='utf-8') as f:
        f.write("Os 10 municípios com menor expectativa de vida:\n\n")
        for i, (Cidade, expectativa) in enumerate(bottom_10, 1):
            f.write(f"{i}. {Cidade}: {expectativa:.2f} anos\n")
    
    return top_10, bottom_10

with open('MunicipiosExpectativa.txt', 'r', encoding='utf-8') as f:
    data = f.read()

top_10, bottom_10 = analise_expectativa_vida(data)

print("Os 10 municípios com maior expectativa de vida:")
for i, (Cidade, expectativa) in enumerate(top_10, 1):
    print(f"{i}. {Cidade}: {expectativa:.2f} anos")

print("\nOs 10 municípios com menor expectativa de vida:")
for i, (Cidade, expectativa) in enumerate(bottom_10, 1):
    print(f"{i}. {Cidade}: {expectativa:.2f} anos")
