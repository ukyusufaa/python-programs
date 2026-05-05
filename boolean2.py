def increase_number(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return False,i
    return True,-1

def decrease_number(nums):
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            return False,i
    return True,-1

def main():
    numbers=[]

    x=int(input("How many numbers in array?"))
    for i in range(x):
        y=int(input(f"Number {i+1}: "))
        numbers.append(y)
    print("Array",numbers)

    inc_flag,inc_index=increase_number(numbers)
    dec_flag,dec_index=decrease_number(numbers)

    if inc_flag:
        print("Increasing")
    elif dec_flag:
        print("Decreasing")
    else:
        print("Mixed")

    print("\n---RESULTS--")
    if not inc_flag:
        print(f"Increasing breaks at index:{inc_index} {numbers[inc_index]} >= {numbers[inc_index+1]}")
    if not dec_flag:
        print(f"Decreasing breaks at index:{dec_index} {numbers[dec_index]} <= {numbers[dec_index]+1}")

main()

