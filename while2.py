count = 0
total = 0

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

#AFTER LOOP

print("Total students:",count)
print("Total marks",total)

if count > 0:
    average = total / count
    print("Average mark for year group: ",average)
 
    
    
    








