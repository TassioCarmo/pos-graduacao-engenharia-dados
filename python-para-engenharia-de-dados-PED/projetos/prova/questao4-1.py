import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"], 
    "Produção": [150, 200, 170, 220, 180, 210]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['Mês'], df['Produção'], marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)

plt.title('Evolução da Produção Mensal', fontsize=16, fontweight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Produção', fontsize=12)

for x, y in zip(df['Mês'], df['Produção']):
    plt.text(x, y, str(y), ha='center', va='bottom', fontweight='bold')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()