import csv

def main():
    with open('contacts.csv') as f:
        data = [row for row in csv.reader(f)]

    data[0][0] = "The"         #A1
    data[1][0] = "WireUs"      #B1
    data[2][1] = "Challenge"   #C2
    
    
    w = csv.writer(open('contacts.csv','w',newline=""))

    w.writerows(data)



if __name__ == "__main__":
    main()
