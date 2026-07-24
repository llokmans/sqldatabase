import sqlite3

con = sqlite3.connect('grades.db')
cur = con.cursor()

data = [
    ('Loki', 'Math', 85),
    ('Loki', 'English', 92),
    ('Loki', 'Science', 78),
    ('Sara', 'Math', 90),
    ('Sara', 'English', 88),
    ('Sara', 'Science', 95),
    ('John', 'Math', 60),
    ('John', 'English', 55),
    ('John', 'Science', 70),
]

cur.executemany("INSERT INTO grades (student, subject, grade) VALUES (?, ?, ?)", data)
con.commit()
con.close()

print("Data inserted successfully.")