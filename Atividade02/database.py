class Database:
    # Atributo estático que armazenará a única instância da conexão
    _instance = None

    # Construtor privado que simula a conexão com o banco de dados
    def __init__(self):
        if Database._instance is not None:
            raise Exception("Já existe uma instância de conexão com o banco de dados!")
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        # Simulação de conexão com o banco de dados
        return "Conectado ao banco de dados"

    @staticmethod
    def get_instance():
        # Verifica se a instância já foi criada, caso contrário, cria uma nova
        if Database._instance is None:
            Database._instance = Database()
        return Database._instance

    def get_connection(self):
        return self.connection

    def close(self):
        # Simulação de fechamento da conexão
        self.connection = None
        print("Conexão fechada.")
