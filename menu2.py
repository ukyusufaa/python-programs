def menu():
    print("1.Prime Numbers")
    print("2.Even & Odd Numbers")
    print("3.Exit")

def prime_numbers(num):
    is_prime = True
    
    if num <= 1:
        is_prime = False
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break 
    
    if is_prime == True:
        return "PRIME"
    else:
        return "NOT A PRIME"

def even_odd(n):
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

def choices():
    while True:
        menu()
        option = int(input("Enter a choice"))
        if option == 1:
            num = int(input("Enter a number"))
            x = prime_numbers(num)
            print(x)
        elif option == 2:
            n = int(input("enter a number"))
            y = even_odd(n)
            print(y)
        elif option == 3:
            print("Goodbye")
            break
        else:
            print("Invalid choice")
choices()





    

        
        

    
