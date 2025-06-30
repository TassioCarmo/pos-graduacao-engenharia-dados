class Pais:

    def __init__(self, codigo_iso, nome_pais, dimensao):
        self.codigo_iso = codigo_iso 
        self.nome_pais = nome_pais
        self.dimensao = dimensao
        self.populacao = None    
        
    def validar_pais(self, lista_paises, codigo_iso):                   
        for pais in lista_paises:
            if(codigo_iso == pais.codigo_iso):
                return True
                break
        
        return False

    def densidade(self):
        return self.populacao / self.dimensao 

    def imprimir(self):
        print("Pais ........:" + self.nome_pais)
        print("Codigo ISO ..:" + self.codigo_iso)
        print("Dimensao ....:" + str(self.dimensao))
        print("Populacao ...:" + str(self.populacao))
        print("Densidade ...:" + str(self.densidade()))

lista_paises = []
while(True):
    opcao = int(input("Menu " + "\n" + "1) Cadastrar Pais" + "\n" + "2) Densidade "
                      +"\n" + "3) Imprimir " + "\n" + "4) Finalizar " + "\n"))
    
    if(opcao < 1 or opcao > 4):
        print("Opção Invalida!")
        continue
    
    if(opcao == 4):
        break
    
    if(opcao == 1):
        codigo_iso = input("Digite o codigo iso do Pais:")
        nome_pais = input("Digite o nome do Pais:")
        dimensao = float(input("Digite a dimensão do Pais:"))
        pais = Pais(codigo_iso, nome_pais, dimensao)
        pais.populacao = float(input("Digite a população do Pais:"))
                
        if(len(lista_paises) > 0):
            if(pais.validar_pais(lista_paises, pais.codigo_iso)):
                print("Pais " + pais.nome_pais + " já cadastrado")
                continue          
        lista_paises.append(pais)
        
    if(opcao == 2):
        for pais in lista_paises:
            print("Pais ..: " + pais.nome_pais + " Densidade ..:" + str(pais.densidade()))
            
    if(opcao == 3):
        for pais in lista_paises:
            print(pais.imprimir())
while(True):
    opcao = int(input("Menu " + "\n" + "1) Cadastrar Pais" + "\n" + "2) Densidade "
                    +"\n" + "3) Imprimir " + "\n" + "4) Finalizar " + "\n"))
    
    if(opcao < 1 or opcao > 4):
        print("Opção Invalida!")
        continue
    
    if(opcao == 4):
        break
    
    if(opcao == 1):
        codigo_iso = input("Digite o codigo iso do Pais:")
        nome_pais = input("Digite o nome do Pais:")
        dimensao = float(input("Digite a dimensão do Pais:"))
        pais = Pais(codigo_iso, nome_pais, dimensao)
        pais.populacao = float(input("Digite a população do Pais:"))
                
        if(len(lista_paises) > 0):
            if(pais.validar_pais(lista_paises, pais.codigo_iso)):
                print("Pais " + pais.nome_pais + " já cadastrado")
                continue 
        lista_paises.append(pais)
        
    if(opcao == 2):
        for pais in lista_paises:
            print("Pais ..: " + pais.nome_pais + " Densidade ..:" + str(pais.densidade()))
            
    if(opcao == 3):
        for pais in lista_paises:
            print(pais.imprimir())