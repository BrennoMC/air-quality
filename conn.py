import mysql.connector

global db
def connection():
    try:
        db = mysql.connector.connect(
            host='us-cdbr-east-06.cleardb.net',
            user='bf56c1e0d42b6c',
            password='4d93483a',
            database='heroku_8a27ec8860e820b',
            # reconnect=True
        )
        print("Conexão bem sucedida!")
    except mysql.connector.Error as error:
        print("Erro ao tentar conectar ao banco de dados:", error)
    return db
