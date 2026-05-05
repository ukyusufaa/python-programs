def increasing_neighbour(nums):
    for i in range(len(nums)-1):
        if nums[i] >= nums[i+1]:
            return i, nums[i], nums[i+1]
    return -1, None, None 

def decreasing_neighbour(nums):
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            return i, nums[i], nums[i+1]
    return -1, None, None

def main():
    numbers=[int(x) for x in input("Enter the numbers: ").split()]

    index_1a,val_1a,val_2a=increasing_neighbour(numbers)
    index_1b,val_1b,val_2b=decreasing_neighbour(numbers)

    print("Array",numbers)

    print("\n---Findings---")

    if index_1a==-1:
        print("No break found:Array is strictly increasing")
    else:
        print(f"Break found at Index:{index_1a} {val_1a} >= {val_2a}")
    
    if index_1b==-1:
        print("No break found: Array is strictly decreasing")
    else:
        print(f"Break found at Index:{index_1b} {val_1b} <={val_2b}")
main()