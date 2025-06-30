import matplotlib.pyplot as plt

filmes = {
    "2021": {"Ação": 7.5, "Comédia": 6.8, "Drama": 8.2},
    "2022": {"Ação": 7.8, "Comédia": 7.0, "Drama": 8.0},
    "2023": {"Ação": 8.0, "Comédia": 7.2, "Drama": 8.5}
}

plt.figure(figsize=(10, 6))
plt.title('Pontuação Média de Filmes por Gênero (2021-2023)', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Pontuação Média', fontsize=12)

estilos = {
    'Ação': {'cor': 'red', 'marcador': 'o'},
    'Comédia': {'cor': 'green', 'marcador': 's'},
    'Drama': {'cor': 'blue', 'marcador': '^'}
}

for genero, estilo in estilos.items():
    pontuacoes = [filmes[ano][genero] for ano in filmes.keys()]
    anos = list(filmes.keys())
    
    plt.plot(anos, pontuacoes, 
             label=genero, 
             color=estilo['cor'], 
             marker=estilo['marcador'],
             linestyle='-',
             linewidth=2,
             markersize=8)

plt.legend(title='Gêneros', loc='best')

plt.grid(True, linestyle='--', alpha=0.7)

plt.ylim(6.5, 8.7)

plt.tight_layout()
plt.show()