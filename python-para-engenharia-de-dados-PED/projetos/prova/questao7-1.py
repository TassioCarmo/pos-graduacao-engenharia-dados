import matplotlib.pyplot as plt
import numpy as np

vendas = {
    "Norte": {"Eletrônicos": 120000, "Roupas": 80000, "Móveis": 50000},
    "Sul": {"Eletrônicos": 150000, "Roupas": 70000, "Móveis": 60000},
    "Leste": {"Eletrônicos": 100000, "Roupas": 75000, "Móveis": 45000},
    "Oeste": {"Eletrônicos": 130000, "Roupas": 85000, "Móveis": 55000}
}

regioes = list(vendas.keys())
categorias = list(vendas["Norte"].keys())

plt.figure(figsize=(10, 6))

width = 0.25

r1 = np.arange(len(regioes))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

plt.bar(r1, [vendas[regiao]["Eletrônicos"] for regiao in regioes], 
        color='blue', width=width, edgecolor='white', label='Eletrônicos')
plt.bar(r2, [vendas[regiao]["Roupas"] for regiao in regioes], 
        color='green', width=width, edgecolor='white', label='Roupas')
plt.bar(r3, [vendas[regiao]["Móveis"] for regiao in regioes], 
        color='red', width=width, edgecolor='white', label='Móveis')

plt.xlabel('Regiões', fontweight='bold')
plt.ylabel('Vendas (R$)', fontweight='bold')
plt.title('Vendas por Região e Categoria', fontweight='bold')
plt.xticks([r + width for r in range(len(regioes))], regioes)

plt.legend()
plt.tight_layout()
plt.show()
