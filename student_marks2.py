def marks_validater(m):
    if 0 <= m <= 100:
        return m
    else:
        return None 

def main():
    students= []

    n=int(input("How many students?"))

    for i in range(n):
        name=input("Enter student name:")
        dob=input("Enter DOB:")

        marks_list = []

        for j in range(2):
            while True:
                try:
                    marks=int(input(f"Enter Marks {j+1}:"))
                    xyz= marks_validater(marks)
                    if xyz is not None:
                        marks_list.append(marks)
                        break 
                    else:
                        print("Invalid marks entered(Enter 0-100 marks only)")
                except ValueError:
                    print("Invalid entry(Enter only numbers)")
            
        students.append(
        {"Name":name,
        "DOB":dob,
        "Marks":marks_list})
        
    for info in students:
        print(f"Name:{info['Name']}")
        print(f"DOB:{info['DOB']}")
        print(f"Marks:{info['Marks']}")

main()


