import sqlite3 as sq
import string

db = sq.connect("short_url.db")
cur = db.cursor()

letters = string.ascii_letters + string.digits
        
q = "SELECT * FROM links"
cur.execute(q)
b = cur.fetchall()
b = [i[1] for i in b]
print(b)
        