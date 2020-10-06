#challenge 19

import math


def perfectSquares(start, end):
    for z in range(start, end+1):
       root = math.sqrt(z)
       if root - int(root) == 0:
          print(z)


x = int(input("Enter starting value : "))
y = int(input("Enter end value : "))

perfectSquares(x,y)
