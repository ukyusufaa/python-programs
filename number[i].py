def process(num):
    count=0
    total=0
    for i in range(len(num)):
        count+=1
        total+=num[i]
    average=total/count
    return count,total,average

def main():
    n=[10,20,30,60]

    count,total,average=process(n)
    print(n)
    print(count)
    print(total)
    print(average)


main()

















        

        

    













