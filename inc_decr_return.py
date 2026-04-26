def compare(num):
    increase=True
    decrease=True

    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            decrease=False
        elif num[i] > num[i+1]:
            increase=False
        else:
            increase=False
            decrease=False
        
        if increase:
            return "Increase"
        elif decrease:
            return "Decrease"
        else:
            return "Mixed" 

def inc_dec(num):
    increase=0
    decrease=0
    equal=0

    for i in range(len(num)-1):
        if num[i] < num[i+1]:
            increase+=1
        elif num[i] > num[i+1]:
            decrease+=1
        else:
            equal+=1
    return increase,decrease,equal

def main():
    numbers=[]
    for _ in range(6):
        n=int(input("Number:"))
        numbers.append(n)
    print("Numbers:",numbers)

    answer=compare(numbers)
    increase,decrease,equal=inc_dec(numbers)


    print("Result:",answer)
    print(f"Increase={increase} Decrease={decrease}, Equal={equal}")

main()
