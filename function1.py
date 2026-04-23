def get_number():
    name=input("Name:")
    number=[]
    for _ in range(5):
        mark=int(input("Mark:"))
        number.append(mark)
    print(name,number)
    return name,number

def calculate_average(number):
    total=0
    count=0

    for mark in number:
        count=count+1
        total=total+mark
    return total/count

def find_min_max(number):
    min_val=None 
    min_index=-1
    max_val=None 
    max_index=-1

    for i, n in enumerate(number):
        if min_val is None or n < min_val:
            min_val=n
            min_index=i

        if max_val is None or n > max_val:
            max_val=n
            max_index=i
    return min_val,min_index,max_val,max_index

def count_relative(number,average):
    avgA_addup=0
    avgB_addup=0

    for mark in number:
        if mark < average:
            avgA_addup+=1
    
        if mark > average:
            avgB_addup+=1
    return avgA_addup,avgB_addup

def classify(average):
    if average < 30:
        return "FAIL"
    elif average <=40:
        return "PASS"
    elif average <=50:
        return "THIRD CLASS"
    elif average <=60:
        return "SECOND CLASS LOWER"
    elif average <=70:
        return "SECOND CLASS HIGHER"
    else:
        return "FIRST CLASS"

def main():
    name,number=get_number()
    average=calculate_average(number)
    min_val,min_index,max_val,max_index=find_min_max(number)
    below,above=count_relative(number,average)
    grade=classify(average)

    print(f"Name:{name}")
    print(f"Average Mark:{average}")
    print(f"Grade:{grade}")
    print(f"Lowest Mark:{min_val} (Index:{min_index})")
    print(f"Highest Mark:{max_val} (Index:{max_index})")
    print(f"Marks below average:{below}")
    print(f"Marks above average:{above}")

main()














        

        

    













