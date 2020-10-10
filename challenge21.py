# challenge 21

operator = input("Enter the operator : ")
op1 = int(input("Enter first number :"))
op2 = int(input("Enter second number :"))

switch = {
    "+":op1+op2,
    "*":op1*op2,
    "-":op1-op2,
    "%":op1%op2,
    "/":op1/op2,
    "^":op1**op2,
    "//":op1//op2,
}


ans = switch.get(operator,"not defined")

print(str(op1) + " " + operator + " " + str(op2) + " = " + str(ans))
