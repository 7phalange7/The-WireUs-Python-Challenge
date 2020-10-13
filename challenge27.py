# challenge 27

class calculator:

    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def calcSum(self):
        return self.num1+self.num2




def main():
    x=int(input("Enter first number : "))
    y=int(input("Enter second number : "))

    obj = calculator(x,y)
    print("The sum of the numbers is ",obj.calcSum())


if __name__ == "__main__":
    main()
