min_val=None 
min_index=None 
max_val=None 
max_index=None 
count=0
total=0
avgA_addup=0
avgB_addup=0

name=input("Name:")
number=[]
for _ in range(3):
    mark=int(input("Mark:"))
    number.append(mark)
    count=count+1
    total=total+mark
average=total/count
print(number)

if average < 30:
    print("FAIL")
elif average <=40:
    print("PASS")
elif average <=50:
    print("THIRD CLASS")
elif average <=60:
    print("SECOND CLASS LOWER")
elif average <=70:
    print("SECOND CLASS HIGHER")
else:
    print("FIRST CLASS")

for i, n in enumerate(number):
    if min_val is None or n < min_val:
        min_val=n
        min_index=i
    if max_val is None or n > max_val:
        max_val=n
        max_index=i

for mark in number:
    if mark < average:
        avgA_addup+=1
    
    if mark > average:
        avgB_addup+=1

print(f"Name:{name}")
print(f"Average Mark:{average}")
print(f"Lowest Mark:{min_val} (Index:{min_index})")
print(f"Highest Mark:{max_val} (Index:{max_index})")
print(f"Marks below average:{avgA_addup}")
print(f"Marks above average:{avgB_addup}")
















        

        

    













