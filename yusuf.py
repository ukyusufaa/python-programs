def find_average(number):
    count=0
    total=0

    for n in number:
        count+=1
        total+=n
    average=total/count
    return count,total,average

def solve_min_max(number):
    min_val=None 
    min_index=-1
    max_val=None 
    max_index=-1

    for i, n in enumerate(number):
        if min_val is None or n < min_val:
            min_val=n
            min_index=i
        if max_val is None or n > max_val:
            max_val=n
            max_index=i
    return min_val,min_index,max_val,max_index

def main():
    nums1=[1,-1,0,99,97,3,5,-12,10]
    count1,total1,average1=find_average(nums1)
    min_val1,min_index1,max_val1,max_index1=solve_min_max(nums1)

    print(nums1)
    print(f"Count:{count1},Total:{total1},Average:{average1}")
    print(f"Min:{min_val1},Index:{min_index1} & Max:{max_val1},Index:{max_index1}")

    for start in range(0,5):
        nums2=list(range(start,start + 10))
        
        count2,total2,average2=find_average(nums2)
        min_val2,min_index2,max_val2,max_index2=solve_min_max(nums2)

        print(f"\nRange:{nums2}")
        print(f"Count:{count2},Total:{total2},Average:{average2}")
        print(f"Min:{min_val2},Index:{min_index2} & Max:{max_val2},Index:{max_index2}")
main()



















        

        

    













