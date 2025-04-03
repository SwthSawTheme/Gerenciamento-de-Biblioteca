import sqlite3

def insertBook(titulo:str,autor:str,ano_pub:int,disponivel:bool):
    try:
        conexao = sqlite3.connect("Biblioteca.db")
        cursor = conexao.cursor()
        print("Conexão efetuada com sucesso!")
        cursor.execute("SELECT * FROM Livros WHERE TITULO = ?",(titulo,))
        if cursor.fetchone():
            print(f"O livro {titulo} já existe no Banco de Dados!")
        else:
            cursor.execute(f"""INSERT INTO Livros(TITULO, AUTOR, ANO_PUBLICACAO, DISPONIVEL)
                            VALUES(?,?,?,?)""", (titulo,autor, ano_pub, disponivel))
            conexao.commit()
            print(f"Livro {titulo} inserido com sucesso!")
    except Exception as e:
        print(f"Error:{e}")
    finally:
        if conexao:
            conexao.close()
            print("Conexão fechada com sucesso!")

if __name__ == "__main__":
    insertBook("O Hobbit","J. R. R. Tolkien",1937,False)