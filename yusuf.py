def menu():
    print("TRINITY UPPER SCHOOL 1993")
    print("1.Insert Students")
    print ("2.Display Students")
    print("Exit")

def validate_marks(marks_list):
    for marks in marks_list:
        if marks < 0 or marks > 100:
            return False 
    return True

      
def find_average_marks(marks_list):
    total = 0
    for marks in marks_list:
        total += marks
    average = total / len(marks_list)
    return average

def final_grades(average):
    if average <= 30:
        return "FAIL"
    elif average <= 45:
        return "E"
    elif average <= 50:
        return "D"
    elif average <= 55:
        return "C"
    elif average <=70:
        return "B"
    else:
        return "A"

def insert_students(students_list):
    
    name=input("Name:")
    dob=input("DOB:")

    marks_list = []
    
    while True:
        try:
            user_input = input("Enter 5 marks:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter 5 marks exactly")
                continue
            if not validate_marks(marks_list):
                print("ERROR - input marks between 0 - 100")
                continue 
            break
        except ValueError:
                print("ERROR! - Do not enter charcaters - Only enter NUMBERS!")
                continue
           
    average = find_average_marks(marks_list)
    grade = final_grades(average)

    students_list.append({
        "Name":name,
        "DOB":dob,
        "Average":average,
        "Grade":grade
    })
    print("Student successfully inserted")

def lowest_student_marks(students_list):
    lowest_student = None 

    for student in students_list:
        if lowest_student is None or student["Average"] < lowest_student["Average"]:
            lowest_student = student
    return lowest_student

def highest_student_marks(students_list):
    highest_student = None 

    for student in students_list:
        if highest_student is None or student["Average"] > highest_student["Average"]:
            highest_student = student
    return highest_student

def display_students(students_list):
    if len(students_list) == 0:
        print("No students found! - Please insert students")
        return
    
    for s in students_list:
        print(f"Name:{s['Name']}")
        print(f"DOB:{s['DOB']}")
        print(f"Average:{s['Average']}")
        print(f"Grade:{s['Grade']}")
    
    lwt_std = lowest_student_marks(students_list)
    hgt_std = highest_student_marks(students_list)

    print(f"Name:{lwt_std['Name']} Lowest Student:{lwt_std['Average']}")
    print(f"Name:{hgt_std['Name']} Highest Student:{hgt_std['Average']}")

def choose_an_option(students_list):
    while True:
        menu()
        user_choice = input("Select a number from the menu to continue:")
        if user_choice == "1":
            insert_students(students_list)
        elif user_choice == "2":
            display_students(students_list)
        elif user_choice == "3":
            print("Kind regards Head Master: MSc BSc ICT Yusuf Ahmad Ali\nGOODBYE")
            break
# Most Important
all_students = []
choose_an_option(all_students)


            




    
 








      