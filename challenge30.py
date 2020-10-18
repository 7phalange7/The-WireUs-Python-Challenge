#challenge 30

def main():
    n =int(input("Enter length of list : "))

    list=[]

    print("Enter the elements : ")

    for i in range(0,n):
        e = int(input())
        list.append(e)

    # swap list
   
    for i in range(0,n//2):
        list[i],list[n-1-i]=list[n-1-i],list[i]
    

    print("Swapped list : ",list)



if __name__ == "__main__":
    main()
