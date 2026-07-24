import sqlite3

con = sqlite3.connect("grades.db")
cur = con.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student TEXT NOT NULL,
                subject TEXT NOT NULL,
                grade REAL NOT NULL     
            )           
''')

con.commit()
con.close()

print("Database and table created successfully.")
