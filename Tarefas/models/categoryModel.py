import sqlite3 as qt
from sqlite3 import connect

class CategoryModel:

    def __init__(self,bdfile):
        self.conn = connect(bdfile)
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS category (
            cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cat_descript TEXT,
            cat_date DATA NOT NULL
        """)

    def selectCategory(self):
        self.cursor.execute("""
            SELECT * FROM category
        """)

    def addCategory(self, date, descript):
        self.cursor.execute("""
            INSERT INTO category(cat_date, cat_descript)
            VALUES (?, ?)
        """, (date, descript))
        self.conn.commit()
        print("Adicionado categoria com sucesso!")

    def closeCategory(self):
        self.cursor.close()

    def deleteCategory(self, id):
        self.cursor.execute("""
            DELETE FROM category
            WHERE cat_id = ?
        """, (id,))
        self.conn.commit()

    def alterCategory(self, date, descript, id):
        self.cursor.execute("""
            UPDATE category
            SET cat_date = ?, cat_descript = ?,
            WHERE cat_id = ? 
        """, (date, descript, id))
        self.conn.commit()

if __name__ == "__main__":
    banco = CategoryModel("bdCategory.db")
    banco.createTable()
    banco.addCategory(6062024, "Teste")
    print(banco.selectCategory())