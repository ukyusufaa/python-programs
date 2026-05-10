import sqlite3

conn = sqlite3.connect("trinity.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               dob TEXT,
               average REAL,
               grades TEXT
)
""")

conn.commit()



cursor.execute("""
INSERT INTO students(name,dob,average,grades)
VALUES(?,?,?,?)
""",(name,dob,av,grades))

conn.commit()


cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

cursor.execute("""
SELECT * FROM students
WHERE lower(name) = ?
""",(user_input,))

student = cursor.fetchone()


cursor.execute("""
DELETE FROM students
WHERE lower(name) = ?
""",(user_input,))

conn.commit()

if cursor.rowcount > 0:
    print("Student deleted sucessfully")
else:
    print("Student not found")


cursor.execute("""
UPDATE students
SET name = ?, dob = ?
WHERE lower(name) = ?
""",(new_name,new_dob,old_name,))

conn.commit()

if cursor.rowcount > 0:
    print("Student sucessfully updated")
else:
    print("Student not found")





