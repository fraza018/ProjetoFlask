from flask import jsonify, request
from models import Professor, Aluno, Turma
import database

# Professores
def criar_professor():
    data = request.get_json()
    novo_professor = Professor(len(database.professores) + 1, data['nome'], data['especialidade'])
    database.professores.append(novo_professor)
    return jsonify({"message": "Professor criado com sucesso", "professor": data}), 201

def listar_professores():
    return jsonify([{"id": p.id, "nome": p.nome, "especialidade": p.especialidade} for p in database.professores])

# Alunos
def criar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(len(database.alunos) + 1, data['nome'], data['idade'], data['turma_id'])
    database.alunos.append(novo_aluno)
    return jsonify({"message": "Aluno criado com sucesso", "aluno": data}), 201

def listar_alunos():
    return jsonify([{"id": a.id, "nome": a.nome, "idade": a.idade, "turma_id": a.turma_id} for a in database.alunos])

# Turmas
def criar_turma():
    data = request.get_json()
    nova_turma = Turma(len(database.turmas) + 1, data['nome'], data['professor_id'])
    database.turmas.append(nova_turma)
    return jsonify({"message": "Turma criada com sucesso", "turma": data}), 201

def listar_turmas():
    return jsonify([{"id": t.id, "nome": t.nome, "professor_id": t.professor_id} for t in database.turmas])
