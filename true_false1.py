def compare(num):
    for i in range(len(num)-1):
        if num[i]>=num[i+1]:
            return False
    return True

def main():
    number=[1,9,10,11]

    decide=compare(number)

    print(number)
    print(decide)

main()
    
        

















        

        

    













