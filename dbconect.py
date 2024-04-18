import mysql.connector
def conn():
    config = {
        'user': 'tester',
        'password': 'admin@123',
        'host': 'localhost',
        'port': 3306,  
        'database': 'dbmonitoramento',
        'raise_on_warnings': True
    }
    
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None
