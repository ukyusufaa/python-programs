import sqlite3

conn = sqlite3.connect("nsb.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               student_name TEXT,
               student_dob TEXT,
               student_average REAL,
               student_grade TEXT
)
""")

conn.commit()

def menu():
    print("NORTHAMPTON SCHOOL FOR BOYS")
    print("1.Insert Student")
    print("2.Display All Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Update Student")
    print("6.EXIT")

def validate_marks(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def find_average_marks(marks_list):
    total = 0

    for mark in marks_list:
        total += mark
    average = total / len(marks_list)
    return average

def final_grade(average):
    if average < 25:
        return "U"
    elif average < 30:
        return "F"
    elif average < 40:
        return "E"
    elif average < 55:
        return "D"
    elif average < 60:
        return "C"
    elif average < 70:
        return "B"
    elif average < 85:
        return "A"
    else:
        return "*A"

def insert_student():
    print("Insert a student")
    name = input("Name:")
    dob = input("DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks spaced out:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter exactly 5 marks only!")
                continue 
            if not validate_marks(marks_list):
                print("ERROR - Enter marks between 0 - 100 only!")
                continue 
            break 
        except ValueError:
            print("ERROR - Do not enter characters, only numbers!")
            continue 

    average = find_average_marks(marks_list)
    grade = final_grade(average)

    cursor.execute("""
    INSERT INTO students(student_name,student_dob,student_average,student_grade)
    VALUES(?,?,?,?)
    """,(name,dob,average,grade))

    conn.commit()
    print("Student sucessfully inserted")

def display_all_students():
    print("All students displayed")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No student found")
    
    for student in rows:
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average:{student[3]}")
        print(f"Grade:{student[4]}")
    
    print("All students are displayed")

def search_student():
    print("Search a student")
    user_input = input("Name:").strip().lower()
    
    cursor.execute("""
    SELECT * FROM students
    WHERE lower(student_name) = ?
    """,(user_input,))

    student = cursor.fetchone()

    if student:
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average{student[3]}")
        print(f"Grade{student[4]}")

def delete_student():
    print("Delete a student")
    user_input = input("Name:").strip().lower()

    cursor.execute("""
    DELETE FROM students
    WHERE lower(student_name) = ?
    """,(user_input,))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student deleted sucessfully")
    else:
        print("Student not found")

def update_student():
    print("Update a student")

    old_name = input("What name would you like to update?").strip().lower()
    new_name = input("New name: ")
    new_dob = input("New DOB: ")

    cursor.execute("""
    UPDATE students
    SET student_name = ?, student_dob = ?
    WHERE lower(student_name) = ?
    """,(new_name,new_dob,old_name,))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully updated")
    else:
        print("student not found ")

def choices():
    while True:
        menu()
        select = input("Enter a choice?")

        if select == "1":
            insert_student()
        elif select == "2":
            display_all_students()
        elif select == "3":
            search_student()
        elif select == "4":
            delete_student()
        elif select == "5":
            update_student()
        elif select == "6":
            print("Goodbye")
            break 
        else:
            print("Invalid selectiion")

choices()





      