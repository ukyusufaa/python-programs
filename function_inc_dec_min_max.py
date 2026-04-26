def calculate_average(num):
    total=0

    for i in range(len(num)):
        total+=num[i]
    average=total/len(num)
    return len(num),total,average

def find_min(num):
    min_val=None 
    min_index=-1

    for i, digit in enumerate(num):
        if min_val is None or digit < min_val:
            min_val=digit
            min_index=i
    return min_val,min_index

def find_max(num):
    max_val=None 
    max_index=-1

    for i, digit in enumerate(num):
        if max_val is None or digit > max_val:
            max_val=digit
            max_index=i
    return max_val,max_index

def compare_neighbor(num):
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
        
def count_inc_dec_eq(num):
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
    number=[]

    for _ in range(7):
        x=int(input("Number:"))
        number.append(x)

    count,total,average=calculate_average(number)
    min_val,min_index=find_min(number)
    max_val,max_index=find_max(number)
    result=compare_neighbor(number)
    increase,decrease,equal=count_inc_dec_eq(number)
    print("Array",number)
    print(f"Count={count} Total={total} Average={average}")
    print(f"Minumum Number={min_val} Index={min_index}")
    print(f"Maximum Number={max_val} Index={max_index}")
    print("Increase/Decrease/Mixed?",result)
    print(f"Increase={increase} Decrease={decrease} Equal={equal}")

main()
