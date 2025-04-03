import sqlite3

def insertBook(titulo:str,autor:str,ano_pub:int,disponivel:bool):
    try:
        conexao = sqlite3.connect("./app/database/Biblioteca.db")
        cursor = conexao.cursor()
        print("Conexão efetuada com sucesso!")

        cursor.execute(f"""INSERT INTO Livros(TITULO, AUTOR, ANO_PUBLICACAO, DISPONIVEL)
                        VALUES(?,?,?,?)""")
        conexao.commit()
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    insertBook("O Hobbit","J. R. R. Tolkien",1937,True)