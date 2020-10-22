# challenge 36

def main():

    i = 1
    x = 0
    maxStars = 5

    for j in range (0,2*maxStars-1):

        x +=i

        for k in range(0,x):
            print("* ",end=" ")
        
        print("\n")
        if x == maxStars:
            i=-1
            





if __name__ == "__main__":
    main()
