# challenge 26

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    year = int(input("Enter the year : "))

    if(isLeapYear(year)):
        print(year, " is a leap year")
    else:
        print(year, " is NOT a leap year")


if __name__ == "__main__":
    main()
