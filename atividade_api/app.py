from flask import Flask, request, jsonify

app = Flask(__name__)

cursos = [
    {"id": 1, "titulo": "Introdução a Python", "descricao": "Curso básico de Python", "carga_horaria": 40},
    {"id": 2, "titulo": "Desenvolvimento Web com Flask", "descricao": "Criação de APIs com Flask", "carga_horaria": 60},
    {"id": 3, "titulo": "Introdução ao JavaScript", "descricao": "Curso básico de JavaScript", "carga_horaria": 30},
    {"id": 4, "titulo": "Desenvolvimento Web com React", "descricao": "Criação de interfaces com React", "carga_horaria": 45}
]

def get_next_id():
   return max(curso["id"] for curso in cursos) + 1 if cursos else 1

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(cursos)

@app.route('/cursos/<int:id>', methods=['GET'])
def obter_curso(id):
    curso = next((c for c in cursos if c['id'] == id), None)
    if curso:
        return jsonify(curso)
    return jsonify({"message": "Curso não encontrado"}), 404

@app.route('/cursos', methods=['POST'])
def criar_curso():
    data = request.get_json()
    if not data or 'titulo' not in data or 'descricao' not in data or 'carga_horaria' not in data:
        return jsonify({"message": "Dados inválidos"}), 400

    new_id = get_next_id()
    novo_curso = {
        "id": new_id,
        "titulo": data['titulo'],
        "descricao": data['descricao'],
        "carga_horaria": data['carga_horaria']
    }
    cursos.append(novo_curso)
    return jsonify(novo_curso), 201

@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    curso = next((c for c in cursos if c['id'] == id), None)
    if not curso:
        return jsonify({"message": "Curso não encontrado"}), 404

    data = request.get_json()
    if not data or 'titulo' not in data or 'descricao' not in data or 'carga_horaria' not in data:
      return jsonify({"message": "Dados inválidos"}), 400

    curso.update(data)
    return jsonify(curso)

@app.route('/cursos/<int:id>', methods=['DELETE'])
def excluir_curso(id):
    global cursos
    cursos = [c for c in cursos if c['id'] != id]
    return jsonify({"message": "Curso excluído"}), 200


if __name__ == '__main__':
    app.run(debug=True)
