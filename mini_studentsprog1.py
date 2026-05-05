def marks_errorcheck(marks):
    if 0 <= marks <= 100:
        return marks
    else:
        return None 
    
def calculate_mark(marks):
    total=0
    for i in range(len(marks)):
        total+=marks[i]
    avg=total/len(marks)
    return avg

def final_mark(avg):
    if avg <= 20:
        return "FAIL"
    elif avg <= 30:
        return "PASS"
    elif avg <= 55:
        return "THIRD CLASS"
    elif avg <= 70:
        return "SECOND CLASS LOWER DIVISION - BSc(Hons) Computer Communications"
    elif avg <= 90:
        return "SECOND CLASS HIGHER DIVISION - BSc(Hons) Computer Communications"
    else:
        return "FIRST CLASS - BSc(Hons)Computer Communications"


def main():
    students=[]

    n=int(input("How many students?"))
    for i in range(n):
        name=input("Enter student name:")
        dob=input("Enter DOB:")

        all_marks=[]

        for j in range(5):
            while True:
                try:
                    marks=int(input(f"Paper {j+1}: "))
                    xyz=marks_errorcheck(marks)
                    if xyz is not None:
                        all_marks.append(marks)
                        break
                    else:
                        print("Invalid mark entered:(Enter BETWEEN 0-100)")
                except ValueError:
                    print("Error(Enter ONLY numbers, NOT characters)")
        
        avg=calculate_mark(all_marks)
        result=final_mark(avg)

        students.append({
            "Name":name,
            "DOB":dob,
            "Total Marks":all_marks,
            "Average Mark":avg,
            "Grade":result       
        })
    for info in students:
        print(f"Name:{info['Name']}")
        print(f"DOB:{info['DOB']}")
        print(f"Total Marks:{info['Total Marks']}")
        print(f"Average Mark:{info['Average Mark']}")
        print(f"Grade:{info['Grade']}")


main()

      