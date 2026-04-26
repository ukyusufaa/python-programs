def analyse_values(nums):
    total=0
    min_val=nums[0]
    max_val=nums[0]
    min_index=0
    max_index=0
    increasing=True
    decreasing=True
    
    inc=dec=eq=0

    for i in range(len(nums)):
        total+=nums[i]

        if nums[i] < min_val:
            min_val=nums[i]
            min_index=i
        if nums[i] > max_val:
            max_val=nums[i]
            max_index=i
        
        if i < len(nums)-1:
            if nums[i] > nums[i+1]:
                increasing=False
                dec+=1
            elif nums[i] < nums[i+1]:
                decreasing=False
                inc+=1
            else:
                increasing=False
                decreasing=False
                eq+=1

    average=total/len(nums)

    return (total,average,min_val,max_val,min_index,max_index,increasing,decreasing,inc,dec,eq)

def main():
    numbers=[]

    n=int(input("Enter, how many numbers?"))

    for i in range(n):
        x=int(input(f"Number {i+1}:"))
        numbers.append(x)
    
    count=len(numbers)

    result=analyse_values(numbers)
    (total,average,min_val,max_val,min_index,max_index,increasing,decreasing,inc,dec,eq)=result

    print("\n---RESULT---")
    print("Array:",numbers)
    print("Count:",count,"Total:",total,"Average:",average)
    print("Minimum number:",min_val,"Index:",min_index)
    print("Maximum number:",max_val,"Index:",max_index)
    print("Increasing:",increasing)
    print("Decreasing",decreasing)
    print(f"Increasing count,{inc} Decreasing count,{dec} Equal count,{eq}")

main()
    

            
