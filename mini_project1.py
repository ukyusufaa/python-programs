def menu():
    print("TRINITY UPPER SCHOOL")
    print("1.Insert Students")
    print("2.Display Students")
    print("3.Serach students")
    print("4.Delete students")
    print("5.EXIT")

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

def lowest_students(students_list):
    lowest = None 

    for students in students_list:
        if lowest is None or students['Average'] < lowest['Average']:
            lowest = students
    return lowest

def highest_students(students_list):
    highest = None 

    for students in students_list:
        if highest is None or students['Average'] > highest ['Average']:
            highest = students
    return highest

def insert_students(students_list):
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

    students_list.append({
        "Name":name,
        "DOB":dob,
        "Average":av,
        "Grades":grades
    })
    print("Student inserted sucessfully")

def display_students(students_list):
    for s in students_list:
        print(f"Name:{s['Name']}")
        print(f"DOB:{s['DOB']}")
        print(f"Average:{s['Average']}")
        print(f"Grades:{s['Grades']}")
    
    lt_students = lowest_students(students_list)
    hg_students = highest_students(students_list)

    print(f"Name:{lt_students['Name']} Lowest Mark:{lt_students['Average']}")
    print(f"Name:{hg_students['Name']} Highest Mark:{hg_students['Average']}")

def search_students(students_list):
    found = False 

    print("Search a student")
    user_input = input("Name:").strip().lower()
    for students in students_list:
        if students['Name'].strip().lower() == user_input:
            found = True
            print(students)
    if found == True:
        print("Student sucessfully found")
    else:
        print("Student not found")

def delete_students(students_list):
    found = False

    print("Search a student")
    user_input = input("Name: ").strip().lower()
    for students in students_list:
        if students['Name'].strip().lower() == user_input:
            students_list.remove(students)
            found = True
            print(f"Student:{students['Name']} sucessfully deleted")
        
    if not found:
        print("ERROR - Please re-enter correct name\nor\nList Empty")


def choose(students_list):
    while True:
        menu()
        user_input = input("Enter a choice:")
        if len(students_list) == 0:
            print("No students found")
    
        
        if user_input == "1":
            insert_students(students_list)
        elif user_input == "2":
            display_students(students_list)
        elif user_input == "3":
            search_students(students_list)
        elif user_input == "4":
            delete_students(students_list)
        elif user_input == "5":
            print("Allah Hafiz")
            break 
        else:
            print("ERROR - Incorrect choice")
# IMPORTANT
all_students = []
choose(all_students)


 








      