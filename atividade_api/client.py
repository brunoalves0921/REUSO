import requests

BASE_URL = "http://127.0.0.1:5000/cursos"

def listar_cursos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao listar cursos: {response.status_code}")
        return None

def obter_curso(id):
    response = requests.get(f"{BASE_URL}/{id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Curso com ID {id} não encontrado.")
        return None
    else:
       print(f"Erro ao obter curso: {response.status_code}")
       return None


def criar_curso(titulo, descricao, carga_horaria):
    data = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao criar curso: {response.status_code} - {response.json()}")
        return None

def atualizar_curso(id, titulo, descricao, carga_horaria):
    data = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.put(f"{BASE_URL}/{id}", json=data)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print(f"Curso com ID {id} não encontrado.")
        return None
    else:
       print(f"Erro ao atualizar curso: {response.status_code} - {response.json()}")
       return None

def excluir_curso(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    if response.status_code == 200:
        print("Curso excluído com sucesso.")
    elif response.status_code == 404:
        print(f"Curso com ID {id} não encontrado.")
    else:
        print(f"Erro ao excluir curso: {response.status_code}")


if __name__ == "__main__":
    while True:
        print("\nEscolha uma ação:")
        print("1. Listar cursos")
        print("2. Obter detalhes de um curso")
        print("3. Adicionar novo curso")
        print("4. Atualizar um curso")
        print("5. Excluir um curso")
        print("0. Sair")

        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            cursos = listar_cursos()
            if cursos:
               for curso in cursos:
                   print(curso)

        elif escolha == "2":
            curso_id = input("Digite o ID do curso: ")
            curso = obter_curso(int(curso_id))
            if curso:
              print(curso)

        elif escolha == "3":
            titulo = input("Digite o título do curso: ")
            descricao = input("Digite a descrição do curso: ")
            carga_horaria = input("Digite a carga horária do curso: ")
            novo_curso = criar_curso(titulo, descricao, int(carga_horaria))
            if novo_curso:
              print("Curso criado com sucesso:", novo_curso)
        elif escolha == "4":
            curso_id = input("Digite o ID do curso a ser atualizado: ")
            titulo = input("Digite o novo título do curso: ")
            descricao = input("Digite a nova descrição do curso: ")
            carga_horaria = input("Digite a nova carga horária do curso: ")
            atualizado = atualizar_curso(int(curso_id), titulo, descricao, int(carga_horaria))
            if atualizado:
               print("Curso atualizado com sucesso:", atualizado)
        elif escolha == "5":
            curso_id = input("Digite o ID do curso a ser excluído: ")
            excluir_curso(int(curso_id))
        elif escolha == "0":
          print("Saindo...")
          break
        else:
          print("Opção inválida.")