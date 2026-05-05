def marks_validater(m):
    if 0 <= m <= 100:
        return m
    else:
        return None 

def main():
    students={}

    n=int(input("How many students?"))
    for i in range(n):
        name=input("Enter student name:")
        dob=input("Enter DOB:")

        while True:
            try:
                marks=int(input("Enter student marks"))
                points=marks_validater(marks)
                if points is not None:
                    break 
                else:
                    print("Invalid input(0-100 only)")
            except ValueError:
                print("Invalid input(Enter numbers only)")

        students[name]={
            "Dob":dob,
            "Marks":points
        }
    for name, info in students.items():
        print(f"Name:{name}")
        print(f"DOB:{info['Dob']}")
        print(f"Marks:{info['Marks']}")

main()


