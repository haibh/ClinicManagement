import sqlite3

conn = sqlite3.connect("lite.db")
cur = conn.cursor()

cur.execute("CREATE TABLE store (item TEXT, quantity INTERGER, price REAL)")
conn.commit()
conn.close()