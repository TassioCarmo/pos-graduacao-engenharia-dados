class Candidato:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.votos = 0

class UrnaEletronica:
    def __init__(self):
        self.candidatos = {}
        self.votos_brancos = 0
        self.votos_nulos = 0
        self.total_votos = 0
        self.inicializar_candidatos()
    
    def inicializar_candidatos(self):
        print("\n=== Cadastro de Candidatos ===")
        n = int(input("Digite o número de candidatos: "))
        
        for i in range(n):
            print(f"\nCandidato {i+1}")
            numero = input("Digite o número do candidato: ")
            nome = input("Digite o nome do candidato: ")
            self.candidatos[numero] = Candidato(numero, nome)
    
    def exibir_menu(self):
        print("\n=== URNA ELETRÔNICA ===")
        print("Candidatos:")
        for numero, candidato in self.candidatos.items():
            print(f"{numero} - {candidato.nome}")
        print("\nOpções especiais:")
        print("B - Voto em Branco")
        print("N - Voto Nulo")
        print("F - Finalizar Votação")
    
    def votar(self):
        while True:
            self.exibir_menu()
            voto = input("\nDigite seu voto: ").upper()
            
            if voto == 'F':
                if self.confirmar_acao("Deseja realmente finalizar a votação? (S/N): "):
                    break
            elif voto == 'B':
                if self.confirmar_acao("Confirma voto em BRANCO? (S/N): "):
                    self.votos_brancos += 1
                    self.total_votos += 1
                    print("Voto em BRANCO computado!")
            elif voto == 'N':
                if self.confirmar_acao("Confirma voto NULO? (S/N): "):
                    self.votos_nulos += 1
                    self.total_votos += 1
                    print("Voto NULO computado!")
            elif voto in self.candidatos:
                candidato = self.candidatos[voto]
                if self.confirmar_acao(f"Confirma voto em {candidato.nome}? (S/N): "):
                    candidato.votos += 1
                    self.total_votos += 1
                    print(f"Voto para {candidato.nome} computado!")
            else:
                print("Opção inválida!")
    
    def confirmar_acao(self, mensagem):
        while True:
            confirmacao = input(mensagem).upper()
            if confirmacao in ['S', 'N']:
                return confirmacao == 'S'
            print("Por favor, digite S para Sim ou N para Não.")
    
    def determinar_vencedor(self):
        if not self.candidatos:
            return None
        
        vencedor = max(self.candidatos.values(), key=lambda c: c.votos)
        
        # Verificar se há empate
        empate = False
        for candidato in self.candidatos.values():
            if candidato.numero != vencedor.numero and candidato.votos == vencedor.votos:
                empate = True
                break
        
        return vencedor if not empate else None
    
    def exibir_resultados(self):
        print("\n=== RESULTADO DA ELEIÇÃO ===")
        print(f"Total de votos: {self.total_votos}")
        print(f"\nVotos Brancos: {self.votos_brancos}")
        print(f"Votos Nulos: {self.votos_nulos}")
        
        print("\nVotos por candidato:")
        for candidato in self.candidatos.values():
            percentual = (candidato.votos / self.total_votos * 100) if self.total_votos > 0 else 0
            print(f"{candidato.nome}: {candidato.votos} votos ({percentual:.1f}%)")
        
        vencedor = self.determinar_vencedor()
        if vencedor:
            print(f"\nVENCEDOR: {vencedor.nome} com {vencedor.votos} votos")
        else:
            print("\nELEIÇÃO EMPATADA")
    
    def gravar_resultados(self):
        with open("resultado_eleicao.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("=== RESULTADO DA ELEIÇÃO ===\n")
            arquivo.write(f"Total de votos: {self.total_votos}\n")
            arquivo.write(f"\nVotos Brancos: {self.votos_brancos}\n")
            arquivo.write(f"Votos Nulos: {self.votos_nulos}\n")
            
            arquivo.write("\nVotos por candidato:\n")
            for candidato in self.candidatos.values():
                percentual = (candidato.votos / self.total_votos * 100) if self.total_votos > 0 else 0
                arquivo.write(f"{candidato.nome}: {candidato.votos} votos ({percentual:.1f}%)\n")
            
            vencedor = self.determinar_vencedor()
            if vencedor:
                arquivo.write(f"\nVENCEDOR: {vencedor.nome} com {vencedor.votos} votos\n")
            else:
                arquivo.write("\nELEIÇÃO EMPATADA\n")

def main():
    urna = UrnaEletronica()
    urna.votar()
    urna.exibir_resultados()
    urna.gravar_resultados()
    print("\nResultados gravados em 'resultado_eleicao.txt'")

if __name__ == "__main__":
    main()