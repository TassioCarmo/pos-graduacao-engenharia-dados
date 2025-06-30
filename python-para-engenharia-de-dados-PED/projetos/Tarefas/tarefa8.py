from typing import List, Optional
from datetime import datetime

class Aluno:
    def __init__(self, nome: str, matricula: str, sexo: str, idade: int):
        self.nome = nome
        self.matricula = matricula
        self.sexo = sexo
        self.idade = idade

class Disciplina:
    def __init__(self, nome: str, periodo: str, ano: int, professor: str):
        self.nome = nome
        self.periodo = periodo
        self.ano = ano
        self.professor = professor

class GerenciadorAlunos:
    def __init__(self):
        self.alunos: List[Aluno] = []

    def criar_aluno(self, nome: str, matricula: str, sexo: str, idade: int) -> Aluno:
        aluno = Aluno(nome, matricula, sexo, idade)
        self.alunos.append(aluno)
        return aluno

    def buscar_aluno(self, matricula: str) -> Optional[Aluno]:
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def listar_alunos(self) -> List[Aluno]:
        return self.alunos

    def atualizar_aluno(self, matricula: str, nome: str = None, sexo: str = None, idade: int = None) -> bool:
        aluno = self.buscar_aluno(matricula)
        if aluno:
            if nome:
                aluno.nome = nome
            if sexo:
                aluno.sexo = sexo
            if idade:
                aluno.idade = idade
            return True
        return False

    def deletar_aluno(self, matricula: str) -> bool:
        aluno = self.buscar_aluno(matricula)
        if aluno:
            self.alunos.remove(aluno)
            return True
        return False

class GerenciadorDisciplinas:
    def __init__(self):
        self.disciplinas: List[Disciplina] = []

    def criar_disciplina(self, nome: str, periodo: str, ano: int, professor: str) -> Disciplina:
        disciplina = Disciplina(nome, periodo, ano, professor)
        self.disciplinas.append(disciplina)
        return disciplina

    def buscar_disciplina(self, nome: str, periodo: str, ano: int) -> Optional[Disciplina]:
        for disciplina in self.disciplinas:
            if disciplina.nome == nome and disciplina.periodo == periodo and disciplina.ano == ano:
                return disciplina
        return None

    def listar_disciplinas(self) -> List[Disciplina]:
        return self.disciplinas

    def atualizar_disciplina(self, nome: str, periodo: str, ano: int, 
                           novo_nome: str = None, novo_periodo: str = None, 
                           novo_ano: int = None, novo_professor: str = None) -> bool:
        disciplina = self.buscar_disciplina(nome, periodo, ano)
        if disciplina:
            if novo_nome:
                disciplina.nome = novo_nome
            if novo_periodo:
                disciplina.periodo = novo_periodo
            if novo_ano:
                disciplina.ano = novo_ano
            if novo_professor:
                disciplina.professor = novo_professor
            return True
        return False

    def deletar_disciplina(self, nome: str, periodo: str, ano: int) -> bool:
        disciplina = self.buscar_disciplina(nome, periodo, ano)
        if disciplina:
            self.disciplinas.remove(disciplina)
            return True
        return False

# Exemplo de uso:
def main():
    # Criando gerenciadores
    gerenciador_alunos = GerenciadorAlunos()
    gerenciador_disciplinas = GerenciadorDisciplinas()

    # Criando alguns alunos
    aluno1 = gerenciador_alunos.criar_aluno("João Silva", "2024001", "M", 20)
    aluno2 = gerenciador_alunos.criar_aluno("Maria Santos", "2024002", "F", 19)

    # Criando algumas disciplinas
    disciplina1 = gerenciador_disciplinas.criar_disciplina("Programação", "1º", 2024, "Prof. Carlos")
    disciplina2 = gerenciador_disciplinas.criar_disciplina("Banco de Dados", "1º", 2024, "Profa. Ana")

    # Exemplos de operações
    # Listando alunos
    print("Lista de Alunos:")
    for aluno in gerenciador_alunos.listar_alunos():
        print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}")

    # Atualizando um aluno
    gerenciador_alunos.atualizar_aluno("2024001", idade=21)

    # Buscando um aluno
    aluno = gerenciador_alunos.buscar_aluno("2024001")
    if aluno:
        print(f"\nAluno encontrado: {aluno.nome}, Idade: {aluno.idade}")

    # Listando disciplinas
    print("\nLista de Disciplinas:")
    for disciplina in gerenciador_disciplinas.listar_disciplinas():
        print(f"Disciplina: {disciplina.nome}, Professor: {disciplina.professor}")

    # Deletando uma disciplina
    gerenciador_disciplinas.deletar_disciplina("Programação", "1º", 2024)

if __name__ == "__main__":
    main()