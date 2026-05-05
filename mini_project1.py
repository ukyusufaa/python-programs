def validate_mark(marks):
    if 0 <= marks <= 100:
        return marks
    else:
        return None 

def avg_mark(marks):
    total=0
    for mark in marks:
        total+=mark
    avg=total/len(marks)
    return avg

def grade(avg):
    if avg <= 40:
        return "FAIL"
    elif avg <= 59:
        return "THIRD CLASS - 3rd"
    elif avg <= 65:
        return "SECOND CLASS LOWER DIVISION - BSc(HONs) COMPUTER COMMUNICATIONS (2ii)"
    elif avg <= 79:
        return "SECOND CLASS HIGHER DIVISION - BSc(HONs) COMPUTER COMMUNICATIONS (2i)"
    else: 
        return "FIRST CLASS DEGREE- BSc(HONs) COMPUTER COMUNICATIONS (1st)"

def lowest_mark_student(students):
    lowest_mark=None
    for student in students:
        avg=student["Average Mark"]
        if lowest_mark is None or avg < lowest_mark["Average Mark"]:
            lowest_mark=student
    return lowest_mark

def highest_mark_student(students):
    highest_mark=None 
    for student in students:
        avg=student["Average Mark"]
        if highest_mark is None or avg > highest_mark["Average Mark"]:
            highest_mark=student
    return highest_mark

def main():
    students=[]

    n=int(input("How many students?"))
    for i in range(n):
        name=input("Student name:")
        dob=input("DOB:")

        all_marks=[]

        for j in range(7):
            while True:
                    try:
                        marks=int(input(f"Paper {j+1}:"))
                        xyz=validate_mark(marks)
                        if xyz is not None:
                            all_marks.append(marks)
                            break
                        else:
                            print("Invalid mark entered(Enter BETWEEN 0-100)")
                    except ValueError:
                        print("Error(Enter 'Numbers' only)")
        
        avg=avg_mark(all_marks)
        result=grade(avg)
      
        
        students.append({
            "Name":name,
            "DOB":dob,
            "Total Marks":all_marks,
            "Average Mark":avg,
            "Grade":result,
    
        })
    lowest=lowest_mark_student(students)
    highest=highest_mark_student(students)

    for info in students:
        print(f"\nName:{info['Name']}")
        print(f"DOB:{info['DOB']}")
        print(f"Marks:{info['Total Marks']}")
        print(f"Average:{info['Average Mark']}")
        print(f"Final Grade:{info['Grade']}")

    print("\n---SUMMARY---")
    print(f"Lowest Student:{lowest['Name']} ({lowest['Average Mark']})")
    print(f"Highest Student:{highest['Name']} ({highest['Average Mark']})")

main()



      