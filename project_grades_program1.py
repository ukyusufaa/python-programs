import sqlite3

conn = sqlite3.connect("mariam.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               s_id INTEGER PRIMARY KEY AUTOINCREMENT,
               s_name TEXT,
               s_dob TEXT,
               s_english_lan_avg REAL,
               s_english_lan_grade TEXT,
               s_english_lit_avg REAL,
               s_english_lit_grade TEXT,
               s_math_avg REAL,
               s_math_grade TEXT,
               s_biology_avg REAL,
               s_biology_grade TEXT,
               s_chemistry_avg REAL,
               s_chemistry_grade TEXT,
               s_physics_avg REAL,
               s_physics_grade TEXT,
               s_geography_avg REAL,
               s_geography_grade TEXT,
               s_history_avg REAL,
               s_history_grade TEXT,
               s_pe_avg REAL,
               s_pe_grade TEXT,
               s_urdu_avg REAL,
               s_urdu_grade TEXT
)
""")

conn.commit()

def menu():
    print("\n---St Thomas Beckett---")
    print("-------GCSE GRADES 2026---------\n")
    print("1.Insert Student GCSE Grades")
    print("2.Display All Students GCSE Grades")
    print("3.Search Student GCSE Grades")
    print("4.Delete Student GCSE Grades")
    print("5.Update Student GCSE Grades")
    print("6.EXIT")

def validate_marks(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def get_grades(average):
    if average < 25:
        return "U"
    elif average < 30:
        return "F"
    elif average < 45:
        return "E"
    elif average < 60:
        return "D"
    elif average < 70:
        return "B"
    elif average < 75:
        return "A"
    else:
        return "*A"

def get_subject_marks(subject):
    marks_list = []

    while True:
        try:
            user_input = input(f"Enter 3 {subject} marks separated by space:\n")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 3:
                print("Re-enter excatly 3 marks")
                continue 
            if not validate_marks(marks_list):
                print("Re-enter marks between 0 - 100")
                continue 
            break  
        except ValueError:
            print("Re-enter marks using numbers")

    total = 0

    for mark in marks_list:
        total += mark
    average = total / len(marks_list)
        
    grade = get_grades(average)
    return average, grade

def insert_student():
    print("\n---INSERT A STUDENT---")
    id = int(input("Student ID:"))
    name = input("Student Name:")
    dob = input("Student DOB:")


    english_lan_avg,english_lan_grade = get_subject_marks("GCSE English Language")
    english_lit_avg,english_lit_grade = get_subject_marks("GCSE English Literature")
    math_avg,math_grade = get_subject_marks("GCSE Mathematics")
    biology_avg,biology_grade = get_subject_marks("GCSE Biology")
    chemistry_avg, chemistry_grade = get_subject_marks("GCSE Chemistry")
    physics_avg,physics_grade = get_subject_marks("GCSE Physics")
    geography_avg, geography_grade = get_subject_marks("GCSE Geography")
    history_avg,history_grade = get_subject_marks("GCSE History")
    pe_avg,pe_grade = get_subject_marks("GCSE Physical Education")
    urdu_avg,urdu_grade = get_subject_marks("GCSE Urdu")
         

    cursor.execute("""
    INSERT INTO students(
                s_id,
                s_name,
                s_dob,
                s_english_lan_avg,
                s_english_lan_grade,
                s_english_lit_avg,
                s_english_lit_grade,
                s_math_avg,
                s_math_grade,
                s_biology_avg,
                s_biology_grade,
                s_chemistry_avg,
                s_chemistry_grade,
                s_physics_avg,
                s_physics_grade,
                s_geography_avg,
                s_geography_grade,
                s_history_avg,
                s_history_grade,
                s_pe_avg,
                s_pe_grade,
                s_urdu_avg,
                s_urdu_grade)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """,(id,
        name,
        dob,
        english_lan_avg,
        english_lan_grade,
        english_lit_avg,
        english_lit_grade,
        math_avg,
        math_grade,
        biology_avg,
        biology_grade,
        chemistry_avg,
        chemistry_grade,
        physics_avg,
        physics_grade,
        geography_avg,
        geography_grade,
        history_avg,
        history_grade,
        pe_avg,
        pe_grade,
        urdu_avg,
        urdu_grade))

    conn.commit()
    print("Student GCSE grades for all subjects\nsuccessfully added to school database system\n")

def display_all():
    print("\n---DISPLAY ALL STUDENTS---")

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found\n")
    else:
        print("Students listed on school database system are shown here below:\n")

    for student in rows:
        print(f"\nStudent ID:{student[0]}")
        print(f"Student Name:{student[1]}")
        print(f"DOB:{student[2]}\n")
        print(f"GCSE English Language - Average Mark:{student[3]}")
        print(f"GCSE English Language - GRADE:{student[4]}\n")
        print(f"GCSE English Literature - Average Mark:{student[5]}")
        print(f"GCSE English Literature - GRADE:{student[6]}\n")
        print(f"GCSE Mathematics - Average Mark:{student[7]}")
        print(f"GCSE Mathematics - GRADE:{student[8]}\n")
        print(f"GCSE Biology - Average Mark:{student[9]}")
        print(f"GCSE Biology - GRADE:{student[10]}\n")
        print(f"GCSE Chemistry - Average Mark:{student[11]}")
        print(f"GCSE Chemistry - GRADE:{student[12]}\n")
        print(f"GCSE Physics - Average Mark:{student[13]}")
        print(f"GCSE Physics - GRADE:{student[14]}\n")
        print(f"GCSE Geography - Average Mark:{student[15]}")
        print(f"GCSE Geography - GRADE:{student[16]}\n")
        print(f"GCSE History - Average Mark:{student[17]}")
        print(f"GCSE History - GRADE:{student[17]}\n")
        print(f"GCSE Physical Education - Average Mark:{student[18]}")
        print(f"GCSE Physical Education - Average Mark:{student[19]}\n")
        print(f"GCSE Urdu - Average Mark:{student[20]}")
        print(f"GCSE Urdu - Average Mark:{student[21]}\n")

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

    english_lan_avg,english_lan_grade = get_subject_marks("GCSE English Language")
    english_lit_avg,english_lit_grade = get_subject_marks("GCSE English Literature")
    math_avg,math_grade = get_subject_marks("GCSE Mathematics")
    biology_avg,biology_grade = get_subject_marks("GCSE Biology")
    chemistry_avg, chemistry_grade = get_subject_marks("GCSE Chemistry")
    physics_avg,physics_grade = get_subject_marks("GCSE Physics")
    geography_avg, geography_grade = get_subject_marks("GCSE Geography")
    history_avg,history_grade = get_subject_marks("GCSE History")
    pe_avg,pe_grade = get_subject_marks("GCSE Physical Education")
    urdu_avg,urdu_grade = get_subject_marks("GCSE Urdu")

    cursor.execute("""
    UPDATE students
    SET s_id = ?,
        s_name = ?,
        s_dob = ?,
        s_english_lan_avg = ?,
        s_english_lan_grade = ?,
        s_english_lit_avg = ?,
        s_english_lit_grade = ?,
        s_math_avg = ?,
        s_math_grade = ?,
        s_biology_avg = ?,
        s_biology_grade = ?,
        s_chemistry_avg = ?,
        s_chemistry_grade = ?,
        s_physics_avg = ?,
        s_physics_grade = ?,
        s_geography_avg = ?,
        s_geography_grade = ?,
        s_history_avg = ?,
        s_history_grade = ?,
        s_pe_avg = ?,
        s_pe_grade = ?,
        s_urdu_avg = ?,
        s_urdu_grade =?
    WHERE s_id = ?
    """,(new_id,
        new_name,
        new_dob,
        english_lan_avg,
        english_lan_grade,
        english_lit_avg,
        english_lit_grade,
        math_avg,
        math_grade,
        biology_avg,
        biology_grade,
        chemistry_avg,
        chemistry_grade,
        physics_avg,
        physics_grade,
        geography_avg,
        geography_grade,
        history_avg,
        history_grade,
        pe_avg,
        pe_grade,
        urdu_avg,
        urdu_grade,
        old_id))

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
    