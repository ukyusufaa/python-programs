def prime():
    num = int(input("Enter a number:"))

    is_prime = True
    i = 2

    if num <= 1:
        is_prime = False
    
    for i in range(i, num):
        if num % i == 0:
            is_prime = False
    
    if is_prime == True:
        print("PRIME")
    else:
        print("NOT A PRIME")

prime()

    
