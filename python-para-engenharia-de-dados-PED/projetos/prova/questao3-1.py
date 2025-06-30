import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Funcionário": ["Carlos", "Ana", "João", "Pedro", "Maria"],
    "Departamento": ["Vendas", "RH", "TI", "TI", "Vendas"],
    "Avaliação": [4.5, 4.0, 5.0, 3.5, 4.8]
}
df = pd.DataFrame(data)

media_departamento = df.groupby('Departamento')['Avaliação'].mean()

plt.figure(figsize=(8, 4))
media_departamento.plot(kind='barh')
plt.title('Média de Avaliações por Departamento')
plt.xlabel('Nota Média')
plt.ylabel('Departamento')
plt.tight_layout()
plt.show()

print("Média de Avaliações por Departamento:")
print(media_departamento)