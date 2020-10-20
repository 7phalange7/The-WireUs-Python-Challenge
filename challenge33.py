# challenge 33

import re


def main():

    
    a = "dfjlksix@rediffmail.comdfkdfjdfkjf*om@gmail.commmddlxlxad@gmail.com_dkfjfkk@gmail.comdfddf dfdf bbgkdf^dfkdf!xxxf@gmail.com@gmail.com,sfdkfd@red.comddg@gmail.com"
    a.lower() # a is raw string

    b = re.split("(?!\.)(?!\@)\W", a)  # (?!\x) ignores x while splitting

    d = ".com"
    c = []
    for line in b:
        c = c + [e+d for e in line.split(d) if e[-6:] == "@gmail" and e[:-6]]    # will not split for yahoomail.com
   
    
    f = open("Allgmail.txt",'w')
    
    for gmail in c :
        f.write(gmail)
        f.write("\n")

    print("All the gmail are collected in Allgmail.txt")



if __name__ == "__main__":
    main()




# Content of Allgmail.txt after running program :-

# om@gmail.com
# mmddlxlxad@gmail.com
# _dkfjfkk@gmail.com
# xxxf@gmail.com
# ddg@gmail.com
