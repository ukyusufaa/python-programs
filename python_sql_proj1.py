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

def menu():
    print("TRINITY UPPER SCHOOL")
    print("1.Insert Students")
    print("2.Display Students")
    print("3.Search Students")
    print("4.Delete Students")
    print("5.Update Students")
    print("6.EXIT")

def marks_checker(marks_list):
    for marks in marks_list:
        if marks < 0 or marks > 100:
            return False
    return True

def find_average(marks_list):
    total = 0

    for marks in marks_list:
        total += marks
    av = total/len(marks_list)
    return av
    
def final_grades(average):
    if average < 40:
        return "FAIL"
    elif average < 60:
        return "PASS"
    elif average < 80:
        return "MERIT" 
    else:
        return "DISTINCTION"

def insert_students():
    print("Insert students")
    name = input("Name:")
    dob = input("DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks spaced out:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter exactly 5 marks")
                continue 
            if not marks_checker(marks_list):
                print("ERROR - Enter marks between 0 - 100")
                continue 
            break 
        except ValueError:
            print("ERROR - Enter numbers only and not chracters")
            continue 

    av = find_average(marks_list)
    grades = final_grades(av)

    cursor.execute("""
    INSERT INTO students(name,dob,average,grades)
    VALUES(?,?,?,?)
    """,(name,dob,av,grades))
    
    conn.commit()

    print("Student inserted sucessfully")

def display_students():

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found")
        return
    for s in rows:
        print(f"Name:{s[1]}")
        print(f"DOB:{s[2]}")
        print(f"Average:{s[3]}")
        print(f"Grades:{s[4]}")

def search_students():
    print("Search a student")
    user_input = input("Name:").strip().lower()
        
    cursor.execute("""
        SELECT * FROM students
        WHERE lower(name) = ?
        """,(user_input,))
    
    student = cursor.fetchone()

    if student:
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average:{student[3]}")
        print(f"Grades:{student[4]}")

def delete_students():

    print("Search a student")
    user_input = input("Name:").strip().lower()

    cursor.execute("""
    DELETE FROM students
    WHERE lower(name) = ?
    """,(user_input,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student sucessfully deleted")
    else:
        print("Student not found")
  

def update_students():
    old_name = input("Enter name to update:").strip().lower()

    new_name = input("Enter new name:")
    new_dob = input("Enter new DOB:")

    cursor.execute("""
    UPDATE students
    SET name = ?, dob = ?
    WHERE lower(name) = ?
    """,(new_name,new_dob,old_name,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Student succesfully updated")
    else:
        print("Student not found")

def choose():
    while True:
        menu()
        user_input = input("Enter a choice:")
    
        if user_input == "1":
            insert_students()
        elif user_input == "2":
            display_students()
        elif user_input == "3":
            search_students()
        elif user_input == "4":
            delete_students()
        elif user_input == "5":
            update_students()
        elif user_input == "6":
            print("Goodbye")
            break 
        else:
            print("ERROR - Incorrect choice")

choose()


 








      