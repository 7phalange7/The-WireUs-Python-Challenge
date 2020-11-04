# challenge 49

list = [3, 6, 4, 5, 1, 9]

max = max(list)

for i in range(0, max):
    for e in list:
        if e >= max - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

for e in list:
    print(e, end=" ")

# output :
#           *
#           *
#           *
#   *       *
#   *   *   *
#   * * *   *
# * * * *   *
# * * * *   *
# * * * * * *
# 3 6 4 5 1 9
