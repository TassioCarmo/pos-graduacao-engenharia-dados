import pandas as pd
import matplotlib.pyplot as plt
data = { 
    "Estudante": ["Alice", "Bob", "Carlos", "Diana", "Eduardo"], 
    "Horas de Estudo": [10, 8, 12, 6, 9], 
    "Notas": [8.5, 7.0, 9.0, 6.5, 7.5]
}

df = pd.DataFrame(data)

correlacao = df["Horas de Estudo"].corr(df["Notas"])
print(f"Correlação entre Horas de Estudo e Notas: {correlacao}")

plt.figure(figsize=(8, 6))
plt.scatter(df['Horas de Estudo'], df['Notas'], color='b', marker='o')

plt.title('Relação entre Horas de Estudo e Notas')
plt.xlabel('Horas de Estudo')
plt.ylabel('Notas')

plt.text(6, 9, f'Correlação: {correlacao:.2f}', fontsize=12, color='red')

plt.grid(True)
plt.show()