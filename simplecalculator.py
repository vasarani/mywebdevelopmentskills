
# simple calculator with the operator

num1 = int(input("enter the a value: "))
num2 = int(input("enter the b value: "))
operator = input("give the operator: ")

if operator == "+":
    print(f"Addition of 2 numbers is: {num1+num2}")
elif operator == "-":
    print(f"subtraction of 2 numbers is: {num1-num2}")
elif operator == "*":
    print(f"multiplication of 2 numbers is: {num1*num2}")
elif operator == "/":
    print(f"division of 2 numbers is: {num1/num2}")
else:
    print("this operator will not works so well")
















