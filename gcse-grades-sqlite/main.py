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
               s_urdu_grade TEXT,
               s_overall_avg REAL,
               s_overall_grade TEXT
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
    print("6.Summary")
    print("7.EXIT")

def validate_marks(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def get_grades(average):
    if average < 25:
        return "U"
    elif average < 30:
        return "E"
    elif average < 45:
        return "D"
    elif average < 60:
        return "C"
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

    overall_total = (
        english_lan_avg +
        english_lit_avg +
        math_avg +
        biology_avg +
        chemistry_avg +
        physics_avg +
        geography_avg +
        history_avg +
        pe_avg +
        urdu_avg 
    )
    overall_avg = overall_total / 10
    overall_grade = get_grades(overall_avg)

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
                s_urdu_grade,
                s_overall_avg,
                s_overall_grade)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
        urdu_grade,
        overall_avg,
        overall_grade))

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
        print(f"GCSE History - GRADE:{student[18]}\n")
        print(f"GCSE Physical Education - Average Mark:{student[19]}")
        print(f"GCSE Physical Education - GRADE:{student[20]}\n")
        print(f"GCSE Urdu - Average Mark:{student[21]}")
        print(f"GCSE Urdu - GRADE:{student[22]}\n")
        print("***************************************\n")
        print(f"Overall GCSE Average Mark:{student[23]}")
        print(f"Overall GCSE Grade:{student[24]}")

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
        print(f"GCSE History - GRADE:{student[18]}\n")
        print(f"GCSE Physical Education - Average Mark:{student[19]}")
        print(f"GCSE Physical Education - GRADE:{student[20]}\n")
        print(f"GCSE Urdu - Average Mark:{student[21]}")
        print(f"GCSE Urdu - GRADE:{student[22]}\n")
        print("*****************************************")
        print(f"Overall GCSE Average Mark:{student[23]}")
        print(f"Overall GCSE Grade:{student[24]}")
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
        print(f"GCSE History - GRADE:{student[18]}\n")
        print(f"GCSE Physical Education - Average Mark:{student[19]}")
        print(f"GCSE Physical Education - GRADE:{student[20]}\n")
        print(f"GCSE Urdu - Average Mark:{student[21]}")
        print(f"GCSE Urdu - GRADE:{student[22]}\n")
        print("****************************************\n")
        print(f"Overall GCSE Average Mark:{student[23]}")
        print(f"Overall GCSE Grade:{student[24]}")

    
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

    student_id = int(input("Enter Student ID:"))

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

    overall_total = (
        english_lan_avg +
        english_lit_avg +
        math_avg +
        biology_avg +
        chemistry_avg +
        physics_avg +
        geography_avg +
        history_avg +
        pe_avg +
        urdu_avg
    )
    overall_avg = overall_total / 10
    overall_grade = get_grades(overall_avg)

    cursor.execute("""
    UPDATE students
    SET s_english_lan_avg = ?,
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
        s_urdu_grade = ?,
        s_overall_avg  = ?,
        s_overall_grade = ?
    WHERE s_id = ?
    """,(english_lan_avg,
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
        overall_avg,
        overall_grade,
        student_id))

    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully updated on school database system")
    else:
        print("Student unmatched, re-enter correct student name to update")

def summary():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Student not found")
        return
    
    highest_student = None 
    lowest_student = None 

    for student in rows:
        if highest_student is None or student[23] > highest_student[23]:
            highest_student = student
        
        if lowest_student is None or student[23] < lowest_student[23]:
            lowest_student = student

    print("\n---SUMMARY")
    print(f"Highest Student:{highest_student[1]}")
    print(f"Highest Average:{highest_student[23]:.2f}")
    print(f"Highest Grade:{highest_student[24]}")

    print()
    print(f"Lowest Student:{lowest_student[1]}")
    print(f"Lowest Average:{lowest_student[23]:.2f}")
    print(f"Lowest Grade:{lowest_student[24]}")

    
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
        elif select == "6":
            summary()
        elif select == "7":
            print("Goodbye\n")
            break
        else:
            print("ERROR - Please re-enter only a number from the menu:")

choices()
    