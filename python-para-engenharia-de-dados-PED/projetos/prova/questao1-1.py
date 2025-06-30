import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Produto": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Quantidade": [10, 20, 15, 12, 22, 18, 14, 24, 16],
    "Preço": [5, 10, 7, 5, 10, 7, 5, 10, 7],
    "Data": ["2024-01-01", "2024-01-01", "2024-01-01", 
             "2024-02-01", "2024-02-01", "2024-02-01", 
             "2024-03-01", "2024-03-01", "2024-03-01"]
}
df = pd.DataFrame(data)

df['Faturamento'] = df['Quantidade'] * df['Preço']
faturamento_por_produto = df.groupby('Produto')['Faturamento'].sum()

plt.figure(figsize=(10, 6))
faturamento_por_produto.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Faturamento Total por Produto', fontsize=15)
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
plt.xticks(rotation=45)

for i, valor in enumerate(faturamento_por_produto):
    plt.text(i, valor, f'R$ {valor}', 
             horizontalalignment='center', 
             verticalalignment='bottom')

plt.tight_layout()
plt.show()

print("Faturamento Total por Produto:")
print(faturamento_por_produto)