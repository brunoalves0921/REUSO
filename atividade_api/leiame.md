# API de Gestão de Cursos

Este projeto consiste em uma API RESTful simples para gerenciar informações de cursos e um cliente para interagir com essa API.

## Como Utilizar

### Pré-requisitos

1.  **Python:** Certifique-se de ter o Python instalado (versão 3.6 ou superior).
2.  **Pip:** O gerenciador de pacotes `pip` deve estar instalado.

### Configuração do Ambiente

1.  **Instale as dependências:**
    ```bash
    pip install flask requests
    ```

### Backend (API)

1.  **Navegue até o diretório da API:**
    ```bash
    cd api_cursos  # ou o nome do diretório onde você salvou o app.py
    ```

2.  **Execute a API:**
    ```bash
    python app.py
    ```
    A API estará disponível em `http://127.0.0.1:5000`.

### Cliente

1.  **Navegue até o diretório do cliente:**
    ```bash
    cd client  # ou o nome do diretório onde você salvou o client.py
    ```

2.  **Execute o cliente:**
    ```bash
    python client.py
    ```

3. **Interaja:** O cliente mostrará um menu com as seguintes opções:
    - Listar os cursos
    - Obter detalhes de um curso pelo ID
    - Adicionar um novo curso
    - Atualizar um curso existente
    - Excluir um curso
    - Sair

    Siga as instruções para interagir com a API.

### Endpoints da API

*   **Listar todos os cursos:**
    *   `GET /cursos`
*   **Obter detalhes de um curso específico:**
    *   `GET /cursos/{id}`
*   **Criar um novo curso:**
    *   `POST /cursos` (Corpo da requisição: JSON com `titulo`, `descricao` e `carga_horaria`)
*   **Atualizar um curso existente:**
    *   `PUT /cursos/{id}` (Corpo da requisição: JSON com `titulo`, `descricao` e `carga_horaria`)
*   **Excluir um curso:**
    *   `DELETE /cursos/{id}`
