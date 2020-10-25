# challenge 39

import csv


def main():
    f = open('contacts.csv')
    reader = csv.reader(f)

    i=1

    print("The Third Row :")

    for row in reader:
        if(i==3):
            print(row)
            break
        i+=1


    f = open('contacts.csv')
    reader = csv.reader(f)

    print("\nThe second coloumn :\n")
    for row in reader:
        print(row[1])

    



if __name__ == "__main__":
    main()
