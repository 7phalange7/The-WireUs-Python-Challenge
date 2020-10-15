# challenge 29


currYear = 2020

def main():
    choice = int(input(" What do you want to enter, 1. Your current age,  2. Birth Year ? "))


    if choice == 1:
        age = int(input("Enter your age : "))

        if age in range(0,99):
            print("You'll be 100 in the year ",(100-age + currYear))
        elif age >= 100:
            print("You already passed the 100 mark in ",(100-age + currYear))
        else:
            print("Invalid Age!!")
    elif choice == 2:
        yr =int(input("Enter birth year : "))

        if yr >= 0:
            print("You will be/were 100 in the year ",(yr +100))
        else:
            print("Invalid Birth Year!!")
    else:
        print("Invalid Choice!!")




if __name__ == "__main__":
    main()
