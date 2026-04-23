while True:
    age=int(input("How old are you?"))
    if age==0:
        print("Error")
        break
    print(f"I am {age} years old")

    if age>=60:
        print("Senior")
    elif age>=18:
        print("Adult")
    else:
        print("Child")







