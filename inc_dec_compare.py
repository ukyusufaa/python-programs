def compare(num):
    inc=0
    decr=0
    eq=0

    for i in range(len(num)-1):
        a=num[i]
        b=num[i+1]

        if a < b:
           inc+=1
        elif a > b:
            decr+=1
        else:
            eq+=1
    return inc,decr,eq

def main():
    numbers=[1,70,30,21,21,45,22]

    inc,decr,eq=compare(numbers)
    print(numbers)
    print("Increasing:",inc)
    print("Decreasing:",decr)
    print("Equal:",eq)
   
main()

















        

        

    













