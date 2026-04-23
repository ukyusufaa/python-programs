min_val=None 
min_index=None 
max_val=None 
max_index=None 
count=0
total=0
count_avgA=0
count_avgB=0

number=[]
name=input("Name:")
for _ in range(9):
    mark=int(input("Mark:"))
    number.append(mark)
print(name,number)

for mark in number:
    count=count+1
    total=total+mark
average=total/count
if average<30:
    print("Grade U(UNGRADED)")
elif average<=35:
    print("Grade F")
elif average<=40:
        print("Grade E")
elif average<=60:
        print("Grade D")
elif average<=65:
        print("Grade C")
elif average<=75:
        print("Grade B")
elif average<=85:
        print("Grade A")
else:
        print("Grade A*")

print(average)

for i, n in enumerate(number):
    if min_val is None or n < min_val:
        min_val = n
        min_index=i

for i, n in enumerate(number):
    if max_val is None or n > max_val:
        max_val = n
        max_index=i

print(f"Student:{name}")
print(f"Average Mark:{average}")
print(f"Lowest Mark:{min_val} (Index{min_index})")
print(f"Highest Mark:{max_val} (Index{max_index}) ")

for mark in number:
    if mark > average:
        count_avgA=count_avgA+1

    if mark < average:
        count_avgB=count_avgB+1
print(f"Above Average marks:{count_avgA}")
print(f"Below Average marks:{count_avgB}")












        

        

    













