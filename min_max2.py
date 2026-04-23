numbers=[5,2,9,1,7]

min_val=None
max_val=None

for n in numbers:
    if min_val is None or n < min_val:
        min_val=n
    if max_val is None or n > max_val:
        max_val=n

print(min_val)
print(max_val)

    
    








