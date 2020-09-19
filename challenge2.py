#challange 2

x = int(input("Enter the number : "))
digits = 0
while x > 0:
    digits = 1 + digits
    x = int(x/10)
print("The number of digits are : ", digits)
