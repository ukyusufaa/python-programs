import sqlite3

conn = sqlite3.connect("musa.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               s_id INTEGER PRIMARY KEY AUTOINCREMENT,
               s_pupil_id INTEGER,
               s_name TEXT,
               s_eng_avg_mark REAL,
               s_eng_grade TEXT,
               s_math_avg_mark REAL,
               s_math_grade TEXT,
               s_overall_avg_mark REAL,
               s_overall_grade TEXT)
""")

conn.commit()

def menu():
    print("\n" + "=" * 40)
    print("---TRINITY UPPER SCHOOL---".center(40))
    print("=" * 40)
    from datetime import datetime
    now = datetime.now()
    print("\n",now,"\n")
    print("1.Insert Student")
    print("2.Display All Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Update Student")
    print("6.Summary")
    print("7.EXIT")

def grade_validation(marks_list):
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

def get_grade(avg):
    if avg < 40:
        return "FAIL"
    elif avg < 50:
        return "E"
    elif avg < 65:
        return "D"
    elif avg < 75:
        return "C"
    elif avg < 85:
        return "B"
    else:
        return "A"

def a_level_subjects(subject):
    marks_list = []

    while True:
        try:
            student_marks = input(f"Enter 3 {subject} marks spaced out:")
            marks_list = list(map(int, student_marks.split()))
            if len(marks_list) != 3:
                print("Enter Exactly 3 marks!")
                continue 
            if not grade_validation(marks_list):
                print("Enter marks between 0 - 100")
                continue 
            break 
        except ValueError:
            print("Do not enter characters, only enter numbers for marks!")
            continue 
    
    average = find_average(marks_list)
    grade = get_grade(average)

    return average,grade

def insert_student():
    print("---Insert A Student")
    pupil_id = int(input("Enter Student ID:"))
    name = input("Enter Student name: ")

    eng_avg_mark,eng_grade = a_level_subjects("A-LEVEL ENGLISH")
    math_avg_mark,math_grade = a_level_subjects("A-LEVEL MATHEMATICS")

    overall_total = (eng_avg_mark +
                     math_avg_mark)
    overall_avg_mark = overall_total / 2
    overall_grade = get_grade(overall_avg_mark)

    cursor.execute("""
    INSERT INTO students(
                s_pupil_id,
                s_name,
                s_eng_avg_mark,
                s_eng_grade,
                s_math_avg_mark,
                s_math_grade,
                s_overall_avg_mark,
                s_overall_grade)
    VALUES(?,?,?,?,?,?,?,?)
    """,(pupil_id,
         name,
         eng_avg_mark,
         eng_grade,
         math_avg_mark,
         math_grade,
         overall_avg_mark,
         overall_grade))
    
    conn.commit()
    print("Student successfully added onto school database system")
    input("\n Press Enter to continue....")

def display_all():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("INSERT STUDENTS - No students are stored on school database")
        return
    
    for student in rows:
        print(f"Student Primary Key:{student[0]}")
        print(f"Student ID:{student[1]}")
        print(f"Student name:{student[2]}")
        print(f"A-LEVEL English mark(average):{student[3]}")
        print(f"A-LEVEL English GRADE:{student[4]}")
        print(f"A-LEVEL Mathematics mark(average):{student[5]}")
        print(f"A-LEVEL Mathematics GRADE:{student[6]}")
        print(f"Overall average mark:{student[7]}")
        print(f"Oveerall average GRADE:{student[8]}")
    input("Press Enter to continue.......")

def search_student():
    pupil_id = int(input("Enter student ID:"))

    cursor.execute("""
    SELECT * FROM students
    WHERE s_pupil_id = ?
    """,(pupil_id,))

    student = cursor.fetchone()

    if student is None:
        print("INSERT STUDENT- No studensts saved on database")

    if student:
        print(f"Student ID:{student[1]}")
        print(f"Student name:{student[2]}")
        print(f"A-LEVEL English mark(average):{student[3]}")
        print(f"A-LEVEL English GRADE:{student[4]}")
        print(f"A-LEVEL Mathematics mark(average):{student[5]}")
        print(f"A-LEVEL Mathematics GRADE:{student[6]}")
        print(f"Overall average mark:{student[7]}")
        print(f"Oveerall average GRADE:{student[8]}")
        input("Press Enter to continue......")
    else:
        print("Student not found")
        return
        
def delete_student():
    pupil_id = int(input("Enter student ID:"))

    cursor.execute("""
    SELECT * FROM students
    WHERE s_pupil_id = ?
    """,(pupil_id,))

    student = cursor.fetchone()

    if student:
        print(f"Student ID:{student[1]}")
        print(f"Student name:{student[2]}")
        print(f"A-LEVEL English mark(average):{student[3]}")
        print(f"A-LEVEL English GRADE:{student[4]}")
        print(f"A-LEVEL Mathematics mark(average):{student[5]}")
        print(f"A-LEVEL Mathematics GRADE:{student[6]}")
        print(f"Overall average mark:{student[7]}")
        print(f"Oveerall average GRADE:{student[8]}")

        answer = input("Are you sure you want to delete this student?").lower()
        if answer == "y":
            print("Student deleted succesfully")
            input("Press Enter to continue.....")

            cursor.execute("""
            DELETE FROM students
            WHERE s_pupil_id = ?
            """,(pupil_id,))

            conn.commit()

        else:
            print("Student not deleted")
            input("Press Enter to continue.....")
    else:
        print("Student not found")
        return
    
def update_student():
    print("---Update A Student")

    primary_key_id =int(input("Enter Original Primary Key ID:"))

    pupil_id = int(input("Enter Original Pupil ID:"))
    name = input("Enter Student name: ")

    eng_avg_mark,eng_grade = a_level_subjects("A-LEVEL ENGLISH")
    math_avg_mark,math_grade = a_level_subjects("A-LEVEL MATHEMATICS")

    overall_total = (eng_avg_mark +
                     math_avg_mark)
    overall_avg_mark = overall_total / 2
    overall_grade = get_grade(overall_avg_mark)

    cursor.execute("""
    UPDATE students
    SET s_pupil_id = ?,
        s_name = ?,
        s_eng_avg_mark = ?,
        s_eng_grade = ?,
        s_math_avg_mark = ?,
        s_math_grade = ?,
        s_overall_avg_mark = ?,
        s_overall_grade = ?
    WHERE s_id = ?
    """,(pupil_id,
         name,
         eng_avg_mark,
         eng_grade,
         math_avg_mark,
         math_grade,
         overall_avg_mark,
         overall_grade,
         primary_key_id))
    
    conn.commit()
    
    if cursor.rowcount > 0:
        print("Student sucessfully updated")
    else:
        print("Student not found")

def class_average(rows):
    total = 0

    for student_avg in rows:
        total += student_avg[7]
        classroom_average = total / len(rows)
    
    return classroom_average

def grade_counter(rows):
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_fail = 0

    for overall_grade in rows:
        if overall_grade[8] == "A":
            count_a += 1
        if overall_grade[8] == "B":
            count_b += 1
        if overall_grade[8] == "C":
            count_c += 1
        if overall_grade[8] == "D":
            count_d += 1
        if overall_grade[8] == "E":
            count_e += 1
        if overall_grade[8] == "FAIL":
            count_fail += 1

    return count_a,count_b,count_c,count_d,count_e,count_fail

def summary():
    overall_highest_student = None 
    overall_lowest_student = None 
    highest_eng_student = None 
    lowest_eng_student = None 
    highest_math_student = None 
    lowest_math_student = None

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No student records on here")
        return
    
    total_students = len(rows)

    classroom_average = class_average(rows)
    classroom_grade = get_grade(classroom_average)
    count_a,count_b,count_c,count_d,count_e,count_fail = grade_counter(rows)


    for student in rows:

        if overall_highest_student is None or student[7] > overall_highest_student[7]:
            overall_highest_student = student
        if overall_lowest_student is None or student[7] < overall_lowest_student[7]:
            overall_lowest_student = student

        if highest_eng_student is None or student[3] > highest_eng_student[3]:
            highest_eng_student = student
        if lowest_eng_student is None or student[3] < lowest_eng_student[3]:
            lowest_eng_student = student
        
        if highest_math_student is None or student[5] > highest_math_student[5]:
            highest_math_student = student
        if lowest_math_student is None or student[5] < lowest_math_student[5]:
            lowest_math_student = student

    print("---Summary---")
    print(f"Grade A:{count_a}")
    print(f"Grade B:{count_b}")
    print(f"Grade C:{count_c}")
    print(f"Grade D:{count_d}")
    print(f"Grade E:{count_e}")
    print(f"Grade FAIL:{count_fail}")
    print()
    print(f"Total Students:{total_students}")
    print()
    print(f"Classroom Average Mark:{classroom_average}")
    print(f"Clasroom Average GRADE:{classroom_grade} ")
    print()
    print(f"Overall Highest Student Name:{overall_highest_student[2]}")
    print(f"Overall Highest Student Average Mark:{overall_highest_student[7]}")
    print(f"Overall Highest Student Average GRADE:{overall_highest_student[8]}")
    print(f"Overall Lowest Student Name:{overall_lowest_student[2]}")
    print(f"Overall Lowest Student Average Mark:{overall_lowest_student[7]}")
    print(f"Overall Lowest Student Average GRADE:{overall_lowest_student[8]}")
    print()
    print(f"Highest English Student Name:{highest_eng_student[2]}")
    print(f"Highest English Student Average Mark:{highest_eng_student[3]}")
    print(f"Highest English Student Average GRADE:{highest_eng_student[4]}")
    print(f"Lowest English Student Name:{lowest_eng_student[2]}")
    print(f"Lowest English Student Average Mark:{lowest_eng_student[3]}")
    print(f"Lowest English Student Average GRADE:{lowest_eng_student[4]}")
    print()
    print(f"Highest Math Student Name:{highest_math_student[2]}")
    print(f"Highest Math Student Average Mark:{highest_math_student[5]}")
    print(f"Highest Math Student Average GRADE:{highest_math_student[6]}")
    print(f"Lowest Math Student Name:{lowest_math_student[2]}")
    print(f"Lowest Math Student Average Mark:{lowest_math_student[5]}")
    print(f"Lowest Math Student Average GRADE:{lowest_math_student[6]}")
    
def choices():
    while True:
        menu()
        answer = input("Please select an option from the menu:")

        if answer == "1":
            insert_student()
        elif answer == "2":
            display_all()
        elif answer == "3":
            search_student()
        elif answer == "4":
            delete_student()
        elif answer == "5":
            update_student()
        elif answer == "6":
            summary()
        elif answer == "7":
            print("Goodbye")
            break 
        else:
            print("Invalid option")

choices()




