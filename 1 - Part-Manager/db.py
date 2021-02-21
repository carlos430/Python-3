import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, partNumber text, loteNumber text, cantidad text, status text) ") 
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

    def insert(self, partNumber, loteNumber, cantidad, status):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?)", (partNumber, loteNumber, 
        cantidad, status))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM products WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id, partNumber, loteNumber, cantidad, status):
        self.cur.execute("UPDATE products SET loteNumber = ?, loteNumber = ?, cantidad = ?, status = ? WHERE id = ?",(partNumber, loteNumber, cantidad, status, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
