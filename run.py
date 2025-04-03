from app.database.data import *
from app.models.main import *


if __name__ == "__main__":
    createDB()
    insertBook("O Hobbit","J. R. R. Tolkien",1937,False)
    insertBook("O Senhor dos Anéis", "J. R. R. Tolkien",1954,True)