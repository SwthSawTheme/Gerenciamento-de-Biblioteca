import sqlite3

def createDB():
    
    tabela = """
    CREATE TABLE IF NOT EXISTS Livros (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TITULO VARCHAR(25) UNIQUE NOT NULL,
    AUTOR VARCHAR(25) NOT NULL,
    ANO_PUBLICACAO INTEGER,
    DISPONIVEL BOOLEAN
    )
"""
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        
        cursor.execute(tabela)
        conexao.commit()
        print("Tabela Livros criada com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão fechada com sucesso!")

if __name__ == "__main__":
    createDB()
    print("Banco de dados criado com sucesso!")
        