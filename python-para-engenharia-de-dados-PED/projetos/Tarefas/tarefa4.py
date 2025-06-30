# Classe mãe 
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def emitir_som(self):
        pass
    
    def dormir(self):
        return f"{self.nome} está dormindo..."

# Classes filhas 
class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo, tipo_rabo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo
        self.tipo_rabo = tipo_rabo
        self.tipo = "Gato"
        
    def emitir_som(self):
        return "Miau!"
    
    def arranhar(self):
        return f"{self.nome} está arranhando!"

class Coelho(Animal):
    def __init__(self, nome, idade, tamanho_orelha, tipo_pelagem):
        super().__init__(nome, idade)
        self.tamanho_orelha = tamanho_orelha
        self.tipo_pelagem = tipo_pelagem
        self.tipo = "Coelho"
        
    def emitir_som(self):
        return "Sniff!"
    
    def pular(self):
        return f"{self.nome} está pulando!"

class Cachorro(Animal):
    def __init__(self, nome, idade, raca, porte):
        super().__init__(nome, idade)
        self.raca = raca
        self.porte = porte
        self.tipo = "Cachorro"
        
    def emitir_som(self):
        return "Au au!"
    
    def buscar_bola(self):
        return f"{self.nome} está buscando a bola!"

def exibir_animal(animal):
    print(f"\nTipo: {animal.tipo}")
    print(f"Nome: {animal.nome}")
    print(f"Idade: {animal.idade}")
    
    if isinstance(animal, Gato):
        print(f"Cor do pelo: {animal.cor_pelo}")
        print(f"Tipo do rabo: {animal.tipo_rabo}")
    elif isinstance(animal, Coelho):
        print(f"Tamanho da orelha: {animal.tamanho_orelha}")
        print(f"Tipo de pelagem: {animal.tipo_pelagem}")
    elif isinstance(animal, Cachorro):
        print(f"Raça: {animal.raca}")
        print(f"Porte: {animal.porte}")
    
    print(f"Som: {animal.emitir_som()}")

def cadastrar_animal(lista_animais):
    while True:
        print("\n=== Menu do Sistema ===")
        print("1 - Cadastrar Gato")
        print("2 - Cadastrar Coelho")
        print("3 - Cadastrar Cachorro")
        print("4 - Exibir Animais Cadastrados")
        print("5 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "5":
            break
            
        if opcao == "4":
            if not lista_animais:
                print("\nNenhum animal cadastrado ainda!")
            else:
                print("\n=== Animais Cadastrados ===")
                for i, animal in enumerate(lista_animais, 1):
                    print(f"\n--- Animal {i} ---")
                    exibir_animal(animal)
            continue
            
        nome = input("Digite o nome do animal: ")
        while True:
            try:
                idade = int(input("Digite a idade do animal: "))
                break
            except ValueError:
                print("Por favor, digite um número válido para a idade.")
        
        if opcao == "1":
            cor_pelo = input("Digite a cor do pelo do gato: ")
            tipo_rabo = input("Digite o tipo do rabo do gato: ")
            animal = Gato(nome, idade, cor_pelo, tipo_rabo)
            lista_animais.append(animal)
            print("\nGato cadastrado com sucesso!")
            exibir_animal(animal)
            
        elif opcao == "2":
            tamanho_orelha = input("Digite o tamanho da orelha do coelho: ")
            tipo_pelagem = input("Digite o tipo de pelagem do coelho: ")
            animal = Coelho(nome, idade, tamanho_orelha, tipo_pelagem)
            lista_animais.append(animal)
            print("\nCoelho cadastrado com sucesso!")
            exibir_animal(animal)
            
        elif opcao == "3":
            raca = input("Digite a raça do cachorro: ")
            porte = input("Digite o porte do cachorro: ")
            animal = Cachorro(nome, idade, raca, porte)
            lista_animais.append(animal)
            print("\nCachorro cadastrado com sucesso!")
            exibir_animal(animal)
            
        else:
            print("Opção inválida!")

# Executando o programa
if __name__ == "__main__":
    lista_animais = []  # Lista para armazenar os animais cadastrados
    print("Bem-vindo ao sistema de cadastro de animais!")
    cadastrar_animal(lista_animais)
    print("\nPrograma encerrado!")