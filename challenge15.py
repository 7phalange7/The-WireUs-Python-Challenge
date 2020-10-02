# challenge 15

f = open("file.txt","r")

n = 0

for line in f:
    words = line.split()
    for word in words:
        if word == "the":
            n=n+1
            

print("There are "+ str(n) + " 'the' in the file")
