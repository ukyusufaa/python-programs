def menu():
    print("1:Fnd Odd & Even numbers")
    print("2:Exit")

def numbers():
    num=int(input("Enter a number:"))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def choose():
    while True:
        menu()
        choice = input("Enter a choice:")
        if choice == "1":
            result = numbers()
            print(result)
        elif choice == "2":
            print("Goodbye")
            break 
        else:
            print("Error - Invalid option")
        
choose()
