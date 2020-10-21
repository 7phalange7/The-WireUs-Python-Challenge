# challenge 35


def main():

    x = int(input("1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius "))

    temp=float(input("Enter temperature : ")) 

    if x == 1:
        t = (temp*9.0)/5.0  + 32
        print("The temp in fahrenheit is ",t)
    elif x == 2:
        t = 5*(temp - 32.0)/9.0
        print("The temp in celsius is ",t)
    else:
        print("Wrong Choice!!")

    



if __name__ == "__main__":
    main()
