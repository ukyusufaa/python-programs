def validate_mark(m):
    if 0 <= m <= 100:
        return m
    else:
        return None 

def main():
    students = {}
    overall_marks = []

    n=int(input("Enter the number of students:"))

    for i in range(n):
        name=input("Enter student name:")
        dob=input("Enter student DOB:")
    
        while True:
            try:
                marks=int(input("Enter student marks:"))
                xyz=validate_mark(marks)

                if xyz is not None:
                    break
                else:
                    print("Invalid mark(Re-Enter a mark between 0-100 only)")
            except ValueError:
                print("Invalid input(Do not enter characters, only enter numbers)")
    
        overall_marks.append(marks)

        students[name]={
            "DOB":dob,
            "Marks":marks
        }
    for name, info in students.items():
        print(f"\nName:{name}")
        print(f"DOB:{info['DOB']}")
        print(f"Marks:{info['Marks']}")

main()



        



