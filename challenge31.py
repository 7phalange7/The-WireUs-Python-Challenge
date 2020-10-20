#challenge 31

def isPal(x):
    n = len(x)//2
    flag=True
    for i in range(0,n):
        if(x[i]!=x[-1-i]):
            flag=False
    
    return flag
    



def main():

    t = int(input("Enter the no. of test cases : "))
    while t>0:
        t-=1

        x = input("Enter the number : ")
        y = int(x)
        z = x
        y+=1
        while True:
            x = str(y)
            if isPal(x):
                break
            y+=1
        print(f"The next pallindrome after {z} is {x}")



if __name__ == "__main__":
    main()
