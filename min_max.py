count = 0
total = 0
max_mark=None
min_mark=None

while True:
    name=input("Enter student name:")
    mark=int(input("Enter mark:"))

    if mark <= -1:
        break

    count = count + 1
    total = total + mark

    print(f"{name}, score is {mark}")
    if mark < 30:
        print("FAIL")
    elif mark <= 40:
        print("PASS")
    elif mark <=45:
        print("THIRD CLASS")
    elif mark <=55:
        print("LOWER SECOND")
    elif mark <=70:
        print("HIGHER SECOND")
    else:
        print("FIRST CLASS")


    if max_mark is None or mark > max_mark:
        max_mark=mark
    
    if min_mark is None or mark < min_mark:
        min_mark=mark

#AFTER LOOP

print("Total students:",count)
print("Total marks",total)
print("Highest mark:",max_mark)
print("Lowest mark:",min_mark)

if count > 0:
    average = total / count
    print("Average mark for year group: ",average)
    
    
    








