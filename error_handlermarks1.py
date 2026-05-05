def error_handler():
    while True:
        try:
            m = int(input("Enter Student Mark"))
            if 0 <= m <= 100:
                return m
            else:
                print("Invalid figure entered (Please enter a mark between 0-100:")
        except ValueError:
            print("Invalid Entry(Please Enter integers and not charcaters ")

def main():
    students={}

    n = int(input("How many students?"))

    for i in range(n):
        name=input("Enter student name:")
        dob=int(input("Enter student dob:"))
        address=input("Enter student UK address:")
        nationality=input("Enter student nationality:")
        mark=error_handler()
        students[name]={
        "address":address,
        "DOB":dob,
        "nationality":nationality,
        "mark": mark
    }

    print("\n---Student Records---")
    for name, info in students.items():
        print(name, " ",info)

    
main()






        



