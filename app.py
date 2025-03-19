from flask import Flask
from controllers import criar_professor, listar_professores, criar_aluno, listar_alunos, criar_turma, listar_turmas

app = Flask(__name__)

@app.route('/professores', methods=['POST'])
def professor_create():
    return criar_professor()

@app.route('/professores', methods=['GET'])
def professor_list():
    return listar_professores()

@app.route('/alunos', methods=['POST'])
def aluno_create():
    return criar_aluno()

@app.route('/alunos', methods=['GET'])
def aluno_list():
    return listar_alunos()

@app.route('/turmas', methods=['POST'])
def turma_create():
    return criar_turma()

@app.route('/turmas', methods=['GET'])
def turma_list():
    return listar_turmas()

if __name__ == '__main__':
    app.run(debug=True)
    