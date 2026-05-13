import sqlite3

conn = sqlite3.connect("abdulaziz.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               s_id INTEGER PRIMARY KEY AUTOINCREMENT,
               s_name TEXT,
               s_dob TEXT,
               s_average REAL,
               s_grade TEXT
)
""")

conn.commit()

def menu():
    print("\n---St Georges---")
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

def find_average_mark(marks_list):
    total = 0

    for mark in marks_list:
        total += mark
    avg = total / len(marks_list)
    return avg

def get_grades(average):
    if average < 40:
        return "FAIL"
    elif average < 60:
        return "PASS"
    elif average < 75:
        return "MERIT"
    else:
        return "DISTINCTION"

def insert_student():
    print("\n---INSERT A STUDENT---")
    id = int(input("Student ID:"))
    name = input("Student Name:")
    dob = input("Student DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks separated by space:\n")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("Re-enter excatly 5 marks")
                continue 
            if not validate_marks(marks_list):
                print("Re-enter marks between 0 - 100")
                continue 
            break  
        except ValueError:
            print("Re-enter marks using numbers")
        
    average = find_average_mark(marks_list)
    grade = get_grades(average)

    cursor.execute("""
    INSERT INTO students(s_id,s_name,s_dob,s_average,s_grade)
    VALUES(?,?,?,?,?)
    """,(id,name,dob,average,grade))

    conn.commit()
    print("Student sucesfully added to school database system\n")

def display_all():
    print("\n---DISPLAY ALL STUDENTS---")

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found\n")
    else:
        print("Students listed on school database system are shown here below:\n")

    for student in rows:
        print(f"Student ID:{student[0]}")
        print(f"Student Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average Mark:{student[3]}")
        print(f"Grade:{student[4]}")

def search_student():
    print("\n---SEARCH FOR A STUDENT---")

    id = int(input("Student ID:"))
    cursor.execute("""
    SELECT * FROM students
    WHERE s_id = ?
    """,(id,))

    student = cursor.fetchone()
    
    if student:
        print(f"Student Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average Mark:{student[3]}")
        print(f"Grade:{student[4]}")
    else:
        print("Search failed, student not found")

def delete_student():
    id = int(input("Student ID:"))
    cursor.execute("""
    SELECT * FROM students
    WHERE s_id = ?
    """,(id,))

    student = cursor.fetchone()
    
    if student:
        print(f"Student ID:{student[0]}")
        print(f"Student Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"Average Mark:{student[3]}")
        print(f"Grade:{student[4]}")
    
        delete = input("Are you sure, you want to delete:Y/N?\n").lower()
        if delete == "y":
            cursor.execute("""
            DELETE FROM students
            WHERE s_id = ?
            """,(id,))

            conn.commit()
            print("Student sucessfully deleted from school database system\n")
        else:
            print("Student has not been deleted")
    else:
        print("Student not found")

def update_student():
    print("\n---UPDATE A STUDENT--")

    old_id = int(input("Enter current Student ID:"))

    new_id = int(input("Enter new Student ID:"))
    new_name = input("Student Name:")
    new_dob = input("DOB:")
    
    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks separated by space")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("Re-enter excatly 5 marks:")
                continue 
            if not validate_marks(marks_list):
                print("Re-enter marks between 0 - 100:")
                continue 
            break  
        except ValueError:
            print("Re-enter marks using numbers:")
        
    new_average = find_average_mark(marks_list)
    new_grade = get_grades(new_average)

    cursor.execute("""
    UPDATE students
    SET s_id = ?,
        s_name = ?,
        s_dob = ?,
        s_average = ?,
        s_grade = ?
    WHERE s_id = ?
    """,(new_id,new_name,new_dob,new_average,new_grade,old_id))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully updated on school database system")
    else:
        print("Student unmatched, re-enter correct student name to update")
    
def choices():
    while True:
        menu()
        select = input("Please enter a number from the menu to proceed:\n")
        if select == "1":
            insert_student()
        elif select == "2":
            display_all()
        elif select == "3":
            search_student()
        elif select == "4":
            delete_student()
        elif select == "5":
            update_student()
        elif select == "5":
            print("Goodbye\n")
            break
        else:
            ("ERROR - Please re-enter only a number from the menu:")

choices()
    