def show_menu():
    print("\n---MENU---")
    print("1.Add Student")
    print("2.View Student")
    print("3.EXIT")


def are_marks_valid(marks_list):
    for mark in marks_list:
        if mark < 0 or mark > 100:
            return False
    return True

def calculate_average(marks_list):
    total=0
    for mark in marks_list:
        total+=mark
    avg=total/len(marks_list)
    return avg

def get_grade_from_average(avg_mark):
    if avg_mark<= 40:
        return "FAIL"
    elif avg_mark <= 59:
        return "THIRD CLASS - 3rd"
    elif avg_mark <= 65:
        return "SECOND CLASS LOWER DIVISION - BSc(HONs) COMPUTER COMMUNICATIONS (2ii)"
    elif avg_mark <= 79:
        return "SECOND CLASS HIGHER DIVISION - BSc(HONs) COMPUTER COMMUNICATIONS (2i)"
    else: 
        return "FIRST CLASS DEGREE- BSc(HONs) COMPUTER COMUNICATIONS (1st)"

def find_lowest_student(student_list):
    lowest_student=None
    for student in student_list:
        if lowest_student is None or student["Average"] < lowest_student["Average"]:
            lowest_student=student
    return lowest_student

def find_highest_student(student_list):
    highest_student=None 
    for student in student_list:
        if highest_student is None or student["Average"] > highest_student["Average"]:
            highest_student=student
    return highest_student

def add_new_student(student_list):

    student_name=input("Student name:")
    student_dob=input("DOB:")

    marks_list = None 

    while True:
        try:
            user_input = input("Enter 5 marks (space separated):")
            marks_list = list(map(int, user_input.split()))

            if len(marks_list) != 5:
                print("Invalid input, enter only 5 marks")
                continue 
        
            if not are_marks_valid(marks_list):
                print("Invalid mark entered(Enter BETWEEN 0-100)")
                continue
            break 
        
        except ValueError:
            print("Error(Enter 'Numbers' only)")
            continue
        
    average_mark=calculate_average(marks_list)
    student_grade=get_grade_from_average(average_mark)

    student_list.append({
        "Name":student_name,
        "DOB":student_dob,
        "Total Marks":marks_list,
        "Average":average_mark,
        "Grade":student_grade,
    })
    print("Student added succesfully")
    

def display_all_students(student_list):
    if not student_list:
        print("No students found")
        return

    lowest=find_lowest_student(student_list)
    highest=find_highest_student(student_list)

    for student in student_list:
        print("\n---STUDENT---")
        print(f"\nName:{student['Name']}")
        print(f"DOB:{student['DOB']}")
        print(f"Marks:{student['Total Marks']}")
        print(f"Average:{student['Average']}")
        print(f"Final Grade:{student['Grade']}")

        print("\n---SUMMARY---")
        print(f"Lowest Student:{lowest['Name']} ({lowest['Average']})")
        print(f"Highest Student:{highest['Name']} ({highest['Average']})")

def run_program(student_list):
    while True:
        show_menu()
        user_choice = input("Enter a choice: ")
        if user_choice == "1":
            add_new_student(student_list)
        elif user_choice == "2":
             display_all_students(student_list)
        elif user_choice == "3":
             print("Goodbye")
             break
        else:
            print("Invalid choice")

# START PROGRAM
all_students = []
run_program(all_students)




      