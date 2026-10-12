# Python calculator

operator = input("enter an operator (+-*/):")
num1 =float(input("enter first num"))
num2 =float(input("enter second number"))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))