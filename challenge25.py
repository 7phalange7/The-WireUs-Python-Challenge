# challenge 25

x = input("Enter the string : ")
a = e = i = o = u = 0
for char in x:
    if char == 'a' or char == 'A':
        a += 1
    elif char == 'e' or char == 'E':
        e += 1
    elif char == 'i' or char == 'I':
        i += 1
    elif char == 'o' or char =='O':
        o += 1
    elif char == 'u' or char =='U':
        u += 1

print(f"{{'a': {a}, 'e': {e},'i': {i},'o': {o},'u': {u}}} ")
