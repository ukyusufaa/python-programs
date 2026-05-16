import sqlite3

conn = sqlite3.connect("sheerazali.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               s_id INTEGER PRIMARY KEY AUTOINCREMENT,
               s_name TEXT,
               s_dob TEXT,
               s_english_avg REAL,
               s_english_grade TEXT,
               s_maths_avg REAL,
               s_maths_grade TEXT,
               s_overall_avg REAL,
               s_overall_grade TEXT
)
""")

conn.commit()

def menu():
    print("\nTRINITY UPPER SCHOOL\n1993")
    print("1.Insert Student GCSE Grades")
    print("2.Display All Students GCSE Grades")
    print("3.Search Student GCSE Grades")
    print("4.Delete Student GCSE Grades")
    print("5.Update Student GCSE Grades")
    print("6.GCSE Students Summary")
    print("7.EXIT")

def validate_marks(marks_list):
    for marks in marks_list:
        if marks < 0 or marks > 100:
            return False
    return True

def find_average(marks_list):
    total = 0

    for marks in marks_list:
        total += marks
        average = total / len(marks_list)
    return average

def get_grades(avg):
    if avg < 25:
        return "U"
    elif avg < 35:
        return "F"
    elif avg < 40:
        return "E"
    elif avg < 55:
        return "D"
    elif avg < 65:
        return "C"
    elif avg < 75:
        return "B"
    elif avg < 90:
        return "A"
    else:
        return "*A"

def calculate_subject_marks(subject):
    marks_list = []

    while True:
        try:
            student_marks = input(f"Enter 3 {subject} marks spaced out:")
            marks_list = list(map(int, student_marks.split()))
            if len(marks_list) !=3:
                print("Enter exactly 3 marks")
                continue 
            if not validate_marks(marks_list):
                print("Enter marks between 0 - 100")
                continue 
            break 
        except ValueError:
            print("Do not enter characters, for marks enter numbers only")
    
    average = find_average(marks_list)
    grade = get_grades(average)

    return average,grade

def insert_student():
    id = int(input("ID:"))
    name = input("Name:")
    dob = input("DOB:")

    gcse_english_avg, gcse_english_grade = calculate_subject_marks("GCSE English")
    gcse_math_avg, gcse_math_grade = calculate_subject_marks("GCSE Mathematics")

    overall_total = (
        gcse_english_avg +
        gcse_math_avg
    )
    overall_average = overall_total / 2
    overall_grade = get_grades(overall_average)

    cursor.execute("""
    INSERT INTO students(
                   s_id,
                   s_name,
                   s_dob,
                   s_english_avg,
                   s_english_grade,
                   s_maths_avg,
                   s_maths_grade,
                   s_overall_avg,
                   s_overall_grade)
    VALUES(?,?,?,?,?,?,?,?,?)
    """,(id,
         name,
         dob,
         gcse_english_avg,
         gcse_english_grade,
         gcse_math_avg,
         gcse_math_grade,
         overall_average,
         overall_grade))
    
    conn.commit()
    print("Student and their GCSE grades, sucessfully added into database")

def display_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No students found")
    
    for student in rows:
        print(f"ID:{student[0]}")
        print(f"Name:{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"GCSE English Mark(average):{student[3]}")
        print(f"GCSE English GRADE:{student[4]}\n")
        print(f"GCSE Mathematics Mark(average):{student[5]}")
        print(f"GCSE Mathematics GRADE:{student[6]}\n")
        print(f"Overall Average Mark:{student[7]}")
        print(f"Overall GRADE:{student[8]}")

def search_student():
    id = int(input("ID:"))

    cursor.execute("""
    SELECT * FROM students
    WHERE s_id = ?
    """,(id,))

    student = cursor.fetchone()

    if student:
        print(f"Name{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"GCSE English Mark(average):{student[3]}")
        print(f"GCSE English GRADE:{student[4]}")
        print(f"GCSE Mathematics Mark(average):{student[5]}")
        print(f"GCSE Mathematics GRADE:{student[6]}")
        print(f"Overall Average Mark:{student[7]}")
        print(f"Overall GRADE:{student[8]}")
    else:
        print("Student unmatched")

def delete_student():
    id = int(input("ID:"))

    cursor.execute("""
    SELECT * FROM students
    WHERE s_id = ?
    """,(id,))

    student = cursor.fetchone()

    if student:
        print(f"Name{student[1]}")
        print(f"DOB:{student[2]}")
        print(f"GCSE English Mark(average):{student[3]}")
        print(f"GCSE English GRADE:{student[4]}")
        print(f"GCSE Mathematics Mark(average):{student[5]}")
        print(f"GCSE Mathematics GRADE:{student[6]}")
        print(f"Overall Average Mark:{student[7]}")
        print(f"Overall GRADE:{student[8]}")

        delete = input("Are you sure you want to delete this student?").lower()
        if delete == 'y':
            cursor.execute = ("""
            DELETE FROM students
            WHERE s_id = ?
            """,(id,))
        
            conn.commit()

        else:
            print("Student not deleted")
    else:
        print("Student unmatched")

def update_student():
    old_id = int(input("Enter current student ID:"))

    new_id = int(input("Enter new student ID:"))
    name = input("Name:")
    dob = input("DOB:")

    gcse_english_avg, gcse_english_grade = calculate_subject_marks("GCSE English")
    gcse_math_avg, gcse_math_grade = calculate_subject_marks("GCSE Mathematics")

    overall_total = (
        gcse_english_avg +
        gcse_math_avg
    )
    overall_average = overall_total / 2
    overall_grade = get_grades(overall_average)

    cursor.execute("""
    UPDATE students
    SET s_id = ?,
        s_name = ?,
        s_dob = ?,
        s_english_avg = ?,
        s_english_grade =?,
        s_maths_avg = ?,
        s_maths_grade = ?,
        s_overall_avg = ?,
        s_overall_grade = ?
    WHERE s_id = ?
    """,(new_id,
         name,
         dob,
         gcse_english_avg,
         gcse_english_grade,
         gcse_math_avg,
         gcse_math_grade,
         overall_average,
         overall_grade,
         old_id))
    
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student and their GCSE grades, sucessfully updated on database system")
    else:
        print("Student unmatched")

def find_class_average(rows):
    total = 0

    for student in rows:
        total += student[7]
    average = total /len(rows)
    return average

def count_grades(rows):
    count_a_star = 0
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0
    count_u = 0

    for student in rows:
        if student[8] == "*A":
            count_a_star += 1
        elif student[8] == "A":
            count_a += 1
        elif student[8] == "B":
            count_b += 1
        elif student[8] == "C":
            count_c += 1
        elif student[8] == "D":
            count_d += 1
        elif student[8] == "E":
            count_e += 1
        elif student[8] == "F":
            count_f += 1
        elif student[8] == "U":
            count_u += 1
    return count_a_star,count_a,count_b,count_c,count_d,count_e,count_f,count_u
        
def summary():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Student not found")
        return
    
    highest_student = None 
    lowest_student = None
    hgst_eng_stu = None
    lwst_eng_stu = None 
    hgst_mth_stu = None
    lwst_mth_stu = None

    total_students = len(rows)

    for student in rows:

        if highest_student is None or student[7] > highest_student[7]:
            highest_student = student

        if lowest_student is None or student[7] < lowest_student[7]:
            lowest_student = student
        
        if hgst_eng_stu is None or student[3] > hgst_eng_stu[3]:
            hgst_eng_stu = student
        
        if lwst_eng_stu is None or student[3] < lwst_eng_stu[3]:
            lwst_eng_stu = student
        
        if hgst_mth_stu is None or student[5] > hgst_mth_stu[5]:
            hgst_mth_stu = student
        
        if lwst_mth_stu is None or student[5] < lwst_mth_stu[5]:
            lwst_mth_stu = student
    
    avg = find_class_average(rows)
    grade = get_grades(avg)
    count_a_star,count_a,count_b,count_c,count_d,count_e,count_f,count_u = count_grades(rows)
    
    print("\n---SUMMARY---")
    print(f"Grade A*:{count_a_star}")
    print(f"Grade A:{count_a}")
    print(f"Grade B:{count_b}")
    print(f"Grade C:{count_c}")
    print(f"Grade D:{count_d}")
    print(f"Grade E:{count_e}")
    print(f"Grade F:{count_f}")
    print(f"Grade U:{count_u}")
    print()
    print(f"Class Average Mark:{avg}")
    print(f"Class GRADE:{grade}")
    print()
    print(f"Total students:{total_students}")
    print()
    print(f"Highest student name:{highest_student[1]}")
    print(f"Highest Student Mark:{highest_student[7]}")
    print(f"Highest Student Grade:{highest_student[8]}")
    print()
    print(f"Lowest student name:{lowest_student[1]}")
    print(f"Lowest Student Mark:{lowest_student[7]}")
    print(f"Lowest Student Grade:{lowest_student[8]}")
    print()
    print(f"Highest GCSE English Student Name:{hgst_eng_stu[1]}")
    print(f"Highest GCSE English Mark:{hgst_eng_stu[3]}")
    print(f"Highest GCSE English GRADE:{hgst_eng_stu[4]}")
    print()
    print(f"Lowest GCSE English student Name:{lwst_eng_stu[1]}")
    print(f"Lowest GCSE English Mark:{lwst_eng_stu[3]}")
    print(f"Lowest GCSE English GRADE:{lwst_eng_stu[4]}")
    print()
    print(f"Highest GCSE Maths Student Name:{hgst_mth_stu[1]}")
    print(f"Highest GCSE Maths Mark:{hgst_mth_stu[5]}")
    print(f"Highest GCSE Maths GRADE:{hgst_mth_stu[6]}")
    print()
    print(f"Lowest GCSE Maths student Name:{lwst_mth_stu[1]}")
    print(f"Lowest GCSE Maths Mark:{lwst_mth_stu[5]}")
    print(f"Lowest GCSE Maths GRADE:{lwst_mth_stu[6]}")
    print()

def choices():
    while True:
        menu()
        select = input("Select an option from the menu:")

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
            summary()
        elif select == "7":
            print("Goodbye")
            break 
        else:
            print("Invalid Choice")

choices()
    