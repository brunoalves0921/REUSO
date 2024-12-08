from database import Database

# Funções que simulam o acesso ao banco de dados por diferentes serviços
def service_a():
    db = Database.get_instance()
    print(f"Serviço A usando: {db.get_connection()}")

def service_b():
    db = Database.get_instance()
    print(f"Serviço B usando: {db.get_connection()}")

def service_c():
    db = Database.get_instance()
    print(f"Serviço C usando: {db.get_connection()}")

def main():
    # Simulando o uso dos serviços que acessam a mesma instância do banco de dados
    print("Iniciando os serviços...")

    service_a()  # Serviço A
    service_b()  # Serviço B
    service_c()  # Serviço C

    # Verificando se as instâncias são a mesma
    db1 = Database.get_instance()
    db2 = Database.get_instance()
    print(f"As conexões são a mesma? {db1 is db2}")

    # Fechando a conexão
    db1.close()

if __name__ == "__main__":
    main()
