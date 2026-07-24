import sqlite3

con = sqlite3.connect("grades.db")
cur = con.cursor()




print("\n---LEADERBOARD ---")
cur.execute("SELECT student, AVG(grade) FROM grades GROUP BY student ORDER BY AVG(grade) DESC")
results = cur.fetchall()
for row in results:
    print(f"Student: {row[0]}, Average Grade: {row[1]:.1f}")
    
print("\n--- PASS/FAIL ---")
cur.execute("SELECT student, AVG(grade) FROM grades GROUP BY student HAVING AVG(grade) >= 70")
results = cur.fetchall()
for row in results:
    print(f"Student: {row[0]}, Average Grade: {row[1]:.1f}")

print("\n--- SUBJECT AVERAGES ---")
cur.execute("SELECT subject, AVG(grade) FROM grades GROUP BY subject ORDER BY AVG(grade) ASC")
results = cur.fetchall()
for row in results:
    print(f"Subject: {row[0]}, Average Grade: {row[1]:.1f}")

con.close()