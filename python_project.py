import sqlite3

conn = sqlite3.connect("ali.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               student_id INTEGER PRIMARY KEY AUTOINCREMENT,
               student_name TEXT,
               student_dob TEXT,
               student_avg_mark REAL,
               student_grade TEXT
)
""")

conn.commit()

def menu():
    print("TRINITY UPPER SCHOOL")
    print("1.Insert A Student")
    print("2.Display All Students")
    print("3.Search A Student")
    print("4.Delete A Student")
    print("5.Update A Student")
    print("6.EXIT")

def validate_marks(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def average_mark(marks_list):
    total = 0

    for mark in marks_list:
        total += mark
    avg = total / len(marks_list)
    return avg

def get_grade(average):
    if average < 35:
        return "U"
    elif average < 45:
        return "F"
    elif average < 50:
        return "E"
    elif average < 55:
        return "D"
    elif average < 70:
        return "C"
    elif average < 75:
        return "B"
    elif average < 85:
        return "A"
    else:
        return "*A"

def insert_student():
    print("Insert a student")
    id = int(input("ID:"))
    name = input("Name:")
    dob = input("DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter exactly 5 marks spaced out")
                continue 
            if not validate_marks(marks_list):
                print("ERROR - Enter marks between 0 - 100")
                continue 
            break 
        except ValueError:
            print("ERROR - Enter numbers only not characters")
    
    average = average_mark(marks_list)
    grade = get_grade(average)

    cursor.execute("""
    INSERT INTO students
                   (student_id, student_name, student_dob,
                   student_avg_mark, student_grade)
    VALUES(?,?,?,?,?)
    """,(id,name,dob,average,grade))

    conn.commit()
    print("Student sucessfully inserted")

def display_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found")

    for student in rows:
        print(f"ID:{student[0]}")
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average{student[3]}")
        print(f"Grade:{student[4]}")

def search_student():
    print("Search a student")
    user_input = int(input("ID:"))
    cursor.execute("""
    SELECT * FROM students
    WHERE student_id = ?
    """,(user_input,))

    student = cursor.fetchone()

    if student:
        print(f"Name:{student[0]}")
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average{student[3]}")
        print(f"Grade:{student[4]}")

    if cursor.rowcount > 0:
        print("Student found")
    else:
        print("Student not found")


def delete_student():
    print("Delete student")
    user_input = int(input("ID:"))

    cursor.execute("""
    DELETE FROM students
    WHERE student_id = ?
    """,(user_input,))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully deleted")
    else:
        print("Student not found")

def update_student():
    print("Search student")

    old_id = int(input("Enter current ID:"))

    new_id = int(input("Enter updated ID"))
    new_name = input("Enter updated name:")
    new_dob = input("Enter updated DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter exactly 5 marks spaced out")
                continue 
            if not validate_marks(marks_list):
                print("ERROR - Enter marks between 0 - 100")
                continue 
            break 
        except ValueError:
            print("ERROR - Enter numbers only not characters")
    
    new_average = average_mark(marks_list)
    new_grade = get_grade(new_average)

    cursor.execute("""
    UPDATE students
    SET student_id = ?,
        student_name = ?, 
        student_dob = ?,
        student_avg_mark = ?,
        student_grade = ?
    WHERE lower(student_name) = ?
    """,(new_id,new_name,new_dob,new_average,new_grade,old_id))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully updated")
    else:
        print("Student not found")

def make_choices():
    while True:
        menu()
        select = input("Choose an operation:")

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
        else:
            print("ERROR - choose again")

make_choices()




    


