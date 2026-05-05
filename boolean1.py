def increasing_number(nums):
    increase=True
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            increase=False
    return increase

def decreasing_number(nums):
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            return False
    return True


def main():
    numbers=[]

    x=int(input("How many numbers in array do you want?"))
    for i in range(x):
        y=int(input(f"Number {i+1}:"))
        numbers.append(y)
    print("Array:",numbers)

    inc_flag=increasing_number(numbers)
    dec_flag=decreasing_number(numbers)

    if inc_flag:
        print("Type:Increasing")
    elif dec_flag:
        print("Type:Decreasing")
    else:
        print("Type:Mixed")
    
main()

