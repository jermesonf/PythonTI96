import sqlite3 as qt
from sqlite3 import connect

class UserModel:

    #Metodo para banco de dados
    def __init__(self, bd_file):
        self.conn = connect(bd_file)  # Corrected the attribute name here
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.conn.execute("""
              CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  login TEXT NOT NULL,
                  password TEXT NOT NULL
              )
          """)
        self.conn.commit()

    def selectUsers(self):
        self.cursor.execute("""
             SELECT * FROM users
         """)
        return self.cursor.fetchall()

    # Função adicionar usuario
    def addUser(self, login, password):
        self.cursor.execute("""
               INSERT INTO users (login, password) 
               VALUES (?, ?)
           """, (login, password))
        self.conn.commit()
        print("Usuário cadastrado com sucesso!")

    def closeUser(self):
        self.cursor.close()

    #Função deletar usuario
    def deleteUser(self, id):
        self.cursor.execute("""
            DELETE FROM users 
            WHERE id = ?
        """, (id,))
        self.conn.commit()

    def alterUser(self, login, password, id):
        self.cursor.execute("""
             UPDATE users 
             SET login = ?, password = ?
             WHERE id = ?
         """, (login, password, id))
        self.conn.commit()



#METODO PRINCIPAL
if __name__ == "__main__":
    banco = UserModel("bdTarefas.db")
    banco.createTable()  # Cria a tabela se ela não existir
    banco.addUser("Joao", "1234")
    print(banco.selectUsers())