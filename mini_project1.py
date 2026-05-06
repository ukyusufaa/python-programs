def menu():
    print("\nTRINITY UPPER SCHOOL 1993\nNORTHAMPTON")
    print("1:Insert Students")
    print("2:Display Students")
    print("3:Search Students")
    print("4.Delete Students")
    print("5.Exit")

def validate_marks(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def find_average_mark(marks_list):
    total = 0

    for mark in marks_list:
        total += mark
    average = total /len(marks_list)
    return average

def final_grade(avg):
    if avg < 10:
        return "U"
    elif avg < 25:
        return "F"
    elif avg < 30:
        return "E"
    elif avg < 40:
        return "D"
    elif avg < 50:
        return "C"
    elif avg < 65:
        return "B"
    elif avg < 75:
        return "A"
    else:
        return "A*"

def find_lowest_student(students_list):
    lowest = None

    for student in students_list:
        if lowest is None or student["Average"] < lowest["Average"]:
            lowest = student
    return lowest

def find_highest_student(students_list):
    highest = None 

    for student in students_list:
        if highest is None or student["Average"] > highest["Average"]:
            highest = student
    return highest

def insert_student(students_list):
    name = input("Name:")
    dob = input("DOB:")

    marks_list = []

    while True:
        try:
            user_input = input("Enter 5 marks:")
            marks_list = list(map(int, user_input.split()))
            if len(marks_list) != 5:
                print("ERROR - Enter exactly 5 marks")
                continue 
            if not validate_marks(marks_list):
                print("ERROR - Enter marks between 0 - 100")
                continue 
            break
        except ValueError:
            print("ERROR - Do NOT enter characters - Enter ONLY numbers")
            continue 
    
    av = find_average_mark(marks_list)
    grade = final_grade(av)

    students_list.append({
        "Name":name,
        "DOB": dob,
        "Average":av,
        "Grade":grade
    })
    print("Student inserted sucessfully")

def display_students(students_list):
    if len(students_list) == 0:
        print("No students found - Please first insert students and then search")
        return
    
    for s in students_list:
        print(f"Name:{s['Name']}")
        print(f"DOB:{s['DOB']}")
        print(f"Final Mark(Average):{s['Average']}")
        print(f"Grade:{s['Grade']}")
    
    lwt_student = find_lowest_student(students_list)
    hgt_student = find_highest_student(students_list)

    print(f"Name:{lwt_student['Name']} Lowest Mark:{lwt_student['Average']}")
    print(f"Name:{hgt_student['Name']} Highest Mark:{hgt_student['Average']}")

def search_students(students_list):
    found = False

    print("Student search engine")
    user_input = input("Student name:").strip().lower()
    for student in students_list:
        if student["Name"].strip().lower() == user_input:
            found = True
            print(student)
    if found == True:
        print("Student sucessfully found")
    else:
        print("No student found")

def delete_students(students_list):
    found = False

    print("Delete a student")
    user_input = input("Student name:").strip().lower()

    for student in students_list:
        if student['Name'].strip().lower() == user_input:
            students_list.remove(student)
            found = True
            print(f"Student:{student['Name']},successfully deleted")
            break 
    if not found:
        print("ERROR - Please re-enter correct name\nor\nList Empty ")
        
def choosing(students_list):
    while True:
        menu()

        user_choice = input("Enter a choice from the menu:")

        if user_choice == "1":
            insert_student(students_list)
        elif user_choice == "2":
            display_students(students_list)
        elif user_choice == "3":
            search_students(students_list)
        elif user_choice == "4":
            delete_students(students_list)
        elif user_choice == "5":
            print("Kindest Regards, GoodBye.\nHead Master MSc BSc DipICT Yusuf Ahmad Ali ")
            break 
        else:
            print("ERROR - Invalid selection- Try again")
            
# IMPORTANT WITHOUT THIS PROGRAM WILL NOT RUN
all_students = []
choosing(all_students)
        






            




    
 








      