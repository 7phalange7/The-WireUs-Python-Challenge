import csv


def main():
    f = open('contacts.csv')
    reader = csv.reader(f)

    i=1

    for row in reader:
        if(i==3):
            print("third cell of the second coloumn : ",row[1])
        i+=1
    



if __name__ == "__main__":
    main()
