class Professor:
    def __init__(self, id, nome, especialidade):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade

class Aluno:
    def __init__(self, id, nome, idade, turma_id):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id

class Turma:
    def __init__(self, id, nome, professor_id):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id
