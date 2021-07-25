import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
textt = "hi"
cur.execute(f"SELECT answers FROM Exam WHERE qnames='{textt}'")
rows = cur.fetchall()
print(rows[0][0])