import pandas as pd
import matplotlib.pyplot as plt

presenca = {
    "João": [1, 1, 0, 1, 1], 
    "Maria": [1, 1, 1, 1, 1], 
    "Ana": [0, 1, 0, 1, 0], 
    "Pedro": [1, 1, 1, 1, 0], 
    "Lucas": [0, 0, 1, 1, 1]
}

df_presenca = pd.DataFrame.from_dict(presenca, orient='index', columns=['Aula 1', 'Aula 2', 'Aula 3', 'Aula 4', 'Aula 5'])

percentuais_presenca = (df_presenca.sum(axis=1) / len(df_presenca.columns) * 100).round(2)

plt.figure(figsize=(10, 7))
plt.pie(percentuais_presenca, labels=percentuais_presenca.index, 
        autopct='%1.1f%%', startangle=90)
plt.title('Percentual de Presença dos Alunos')
plt.axis('equal')
plt.show()

print("Percentuais de Presença:")
for aluno, percentual in percentuais_presenca.items():
    print(f"{aluno}: {percentual}%")