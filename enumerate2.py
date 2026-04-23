min_val=None 
min_index=None 
max_val=None 
max_index=None 

numbers=[]
for _ in range(7):
    n=int(input("Number:"))
    numbers.append(n)
print(numbers)

for i, n in enumerate(numbers):
    print("Numbers Listed:",i,n)
    if min_val is None or n < min_val:
        min_val = n
        min_index = i
    if max_val is None or n > max_val:
        max_val = n
        max_index = i
print(f"Minimum Index:{min_index} & Value:{min_val}")
print(f"Maximum Index:{max_index} & Value:{max_val}")













