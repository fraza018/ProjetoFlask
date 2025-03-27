from flask import Flask, jsonify, request

app = Flask(__name__)

# Bancos de dados simples (listas)
alunos = []
professores = []

# Reseta os dados
@app.route('/reseta', methods=['POST'])
def reseta():
    global alunos, professores
    alunos = []
    professores = []
    return jsonify({'status': 'ok'}), 200

# Rotas de alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    nome = data.get('nome')
    id = data.get('id')

    if not nome:
        return jsonify({'erro': 'aluno sem nome'}), 400
    if any(a['id'] == id for a in alunos):
        return jsonify({'erro': 'id ja utilizada'}), 400

    aluno = {'id': id, 'nome': nome}
    alunos.append(aluno)
    return jsonify(aluno), 200

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({'erro': 'aluno nao encontrado'}), 404

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if not aluno:
        return jsonify({'erro': 'aluno nao encontrado'}), 404

    data = request.get_json()
    nome = data.get('nome')
    if not nome:
        return jsonify({'erro': 'aluno sem nome'}), 400

    aluno['nome'] = nome
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        alunos.remove(aluno)
        return jsonify({'status': 'ok'}), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 404

# Rotas de professores
@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

@app.route('/professores', methods=['POST'])
def add_professor():
    data = request.get_json()
    nome = data.get('nome')
    id = data.get('id')

    if not nome:
        return jsonify({'erro': 'professor sem nome'}), 400
    if any(p['id'] == id for p in professores):
        return jsonify({'erro': 'id ja utilizada'}), 400

    professor = {'id': id, 'nome': nome}
    professores.append(professor)
    return jsonify(professor), 200

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        return jsonify(professor)
    return jsonify({'erro': 'professor nao encontrado'}), 404

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if not professor:
        return jsonify({'erro': 'professor nao encontrado'}), 404

    data = request.get_json()
    nome = data.get('nome')
    if not nome:
        return jsonify({'erro': 'professor sem nome'}), 400

    professor['nome'] = nome
    return jsonify(professor)

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        professores.remove(professor)
        return jsonify({'status': 'ok'}), 200
    return jsonify({'erro': 'professor nao encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
