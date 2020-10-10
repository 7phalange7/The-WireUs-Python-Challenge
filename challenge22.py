# challenge 22

import random
n = random.randint(0, 50)

x = 5

while x > 0:
    print("You have "+str(x)+" guesses left")
    num = int(input("Enter your guess :"))
    if num == n:
        break
    else:
        x = x-1

if x == 0:
    print("Better Luck Next Time, the number was "+str(n))
else:
    print("You guessed it in " + str(6-x)+" tries.")
