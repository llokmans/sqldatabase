import sqlite3

con = sqlite3.connect("grades.db")
cur = con.cursor()

cur.execute("INSERT INTO grades (student, subject, grade) VALUES ('Claude', 'Coding', 100)")
con.commit()
con.close()

print("Data inserted successfully.")