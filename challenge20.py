# challenge 20

string = input("Enter the string : ")
list = []
dict = {} #to print only distinct upper characters

for char in string :
    if char.isupper() and not(char in dict):
        list.append(char)
        dict[char] = "1"

print(list)
