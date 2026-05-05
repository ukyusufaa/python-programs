def counter(nums):
    inc=0
    dec=0
    eq=0

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            dec+=1
        elif nums[i] < nums[i+1]:
            inc+=1
        else:
            eq+=1
    return inc,dec,eq

def increasing_neighbour(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return i, nums[i], nums[i+1]
    return -1, None, None 

def decreasing_neighbour(nums):
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            return i, nums[i], nums[i+1]
    return -1, nums[i], nums[i+1]

def main():
    while True:
        print("1.Analyse")
        print("2.EXIT")
        choice=input("Enter a choice: ")

        if choice=="1":
            numbers=[int(a) for a in input("Enter the numbers:").split()]

            inc,dec,eq=counter(numbers)
            idx_x1,val_x1,val_x2=increasing_neighbour(numbers)
            idx_y1,val_y1,val_y2=decreasing_neighbour(numbers)

            print("Array",numbers)
            print("\n---Findings---")
            print("Increasing: ",inc)
            print("Decreasing: ",dec)
            print("Equal: ",eq)
            
            if idx_x1==-1:
                print("Sequence is strictly increasing")
            else:
                print(f"Increasing break at Index:{idx_x1} {val_x1} > {val_x2}")
            
            if idx_y1==-1:
                print("Sequence is stritly decreasing")
            else:
                print(f"Decreasing break at Index:{idx_y1} {val_y1} < {val_y2}")
            
            if inc > 0 and dec == 0 and eq == 0:
                print("Stricty Increasing")
            elif dec > 0 and inc == 0 and eq == 0:
                print("Strictly Decreasing")
            else:
                print("Equal")
        
        else:
            print("Good Bye")
            break
main()


