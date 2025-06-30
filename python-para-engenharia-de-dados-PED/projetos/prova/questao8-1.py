import matplotlib.pyplot as plt
import numpy as np

sensores = {
    "Sensor1": {"08:00": 22.5, "12:00": 24.0, "16:00": 23.5, "20:00": 21.0},
    "Sensor2": {"08:00": 18.5, "12:00": 20.0, "16:00": 19.5, "20:00": 17.0},
    "Sensor3": {"08:00": 25.0, "12:00": 27.5, "16:00": 26.5, "20:00": 24.0}
}

horarios = list(list(sensores.values())[0].keys())
cores = ['blue', 'green', 'red']

plt.figure(figsize=(10, 6))

# Dicionário para armazenar valores em cada horário para calcular máximo e mínimo
valores_por_horario = {hora: [] for hora in horarios}

for i, (sensor, leituras) in enumerate(sensores.items()):
    valores = list(leituras.values())
    plt.plot(horarios, valores, marker='o', label=sensor, color=cores[i])
    
    # Preenche o dicionário de valores por horário
    for j, hora in enumerate(horarios):
        valores_por_horario[hora].append(leituras[hora])

# Calcula máximos e mínimos para cada horário
minimos = [min(valores_por_horario[hora]) for hora in horarios]
maximos = [max(valores_por_horario[hora]) for hora in horarios]

# Adiciona área sombreada entre máximo e mínimo
plt.fill_between(horarios, minimos, maximos, alpha=0.2, color='gray')

plt.title('Leituras de Temperatura dos Sensores')
plt.xlabel('Horário')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()