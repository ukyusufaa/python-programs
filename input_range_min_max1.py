min_val=None 
max_val=None 
numbers=[]

for _ in range(7):
    n=int(input("Number:"))
    numbers.append(n)
    for n in numbers:
        if min_val is None or n < min_val:
            min_val=n
        if max_val is None or n > max_val:
            max_val=n

print("Numbers list:",numbers)
print("Minumum number found:",min_val)
print("Maximum number found:",max_val)










