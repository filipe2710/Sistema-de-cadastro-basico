import sqlite3


def create_tabld():
    conn = sqlite3.connect("database.bd")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS clientes (
                   cod INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nome CHAR(50) NOT NULL,
                            telefone INTEGER(20),
                            cidade CHAR(50) 
                            )
                            """
    )

    conn.commit()
    conn.close()
    print("Tabela criada com sucesso")


def insert_data():
    conn = sqlite3.connect("database.bd")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clientes (nome, telefone, cidade) VALUES ('Filipe', 123456789, 'São Paulo')"
    )
    conn.commit()
    conn.close()
    print("Dados inseridos com sucesso")


def fecth_data():
    conn = sqlite3.connect("database.bd")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes ORDER BY nome ASC")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(row)


# criar tabela
create_tabld()
# inserir dados
insert_data()
# buscar dados
fecth_data()
