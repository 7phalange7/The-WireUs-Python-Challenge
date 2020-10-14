# challenge 28

def main():
    balance = 0
    exit = False

    while not exit :
        c = int(input("\n\n Enter Choice :\n 1. Balance \n 2. Withdraw \n 3. Deposit \n 4. Quit\n\n"))

        if c == 1:
            print("\n Balancen: ",balance)
        elif c == 2:
            w = int(input("\n Enter the amount to withdraw : "))
            if w > balance:
                print("\nNot enough balance !!")
            else:
                balance-=w
        elif c == 3:
            d = int(input("\n Enter the amount to deposit : "))
            balance+=d
        elif c == 4:
            exit = True
        else:
            print("\n Wrong Input!!!")




if __name__ == "__main__":
    main()
