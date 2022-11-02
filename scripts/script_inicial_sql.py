import psycopg2
from os import getenv

password = getenv("PASS")

if password:
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format("localhost", "postgres", "postgres", password, "disable")
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users;")
    print("excluido tabela")
    
    cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, nome VARCHAR(50) NOT NULL, idade INTEGER);")
    print("Tabela criada com sucesso!")
    
    cursor.execute("INSERT INTO users (nome, idade) VALUES (%s, %s);", ("Alexandre Santos", 30))
    cursor.execute("INSERT INTO users (nome, idade) VALUES (%s, %s);", ("Mikaela Santos", 27))
    print("inserido 2 linhas com sucesso")
    
    print("fechando conexão")
    conn.commit()
    cursor.close()
    conn.close()