def validate_marks(marks):
    if 0 <= marks <=100:
        return marks
    else:
        return None 

def find_min(marks):
    min=None 
    min_i=-1
    for i, n in enumerate(marks):
        if min is None or n < min:
            min=n
            min_i=i
    return min,min_i

def find_max(marks):
    max=None 
    max_i=-1
    for i, n in enumerate(marks):
        if max is None or n > max:
            max=n
            max_i=i
    return max,max_i

def main():
    students=[]

    n=int(input("How many students?"))
    for i in range(n):
        name=input("Enter student name:")
        dob=input("Enter student DOB:")

        all_marks=[]

        for j in range(5):
            while True:
                try:
                    one_mark=int(input(f"Mechanical Mathematics Paper {j+1}:"))
                    xyz=validate_marks(one_mark)
                    if xyz is not None:
                        all_marks.append(one_mark)
                        break
                    else:
                        print("Invalid mark entered(0-100 only)")
                except ValueError:
                    print("Error(Enter numbers and not charcters)")
        
        min,min_i=find_min(all_marks)
        max,max_i=find_max(all_marks)

        students.append({
            "Name":name,
            "DOB":dob,
            "Marks":all_marks,
            "min":min,
            "min_i":min_i,
            "max":max,
            "max_i":max_i
        })
    for info in students:
        print(f"Name:{info['Name']}")
        print(f"Dob:{info['DOB']}")
        print(f"marks:{info['Marks']}")
        print(f"min:{info['min']}")
        print(f"min_i:{info['min_i']}")
        print(f"max:{info['max']}")
        print(f"max_i{info['max_i']}")

main()
     
    