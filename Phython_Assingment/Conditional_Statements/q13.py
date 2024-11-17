# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operater = input( "Enter operater (+,-,*,/)")
if operater == "+" :
    print(num1 + num2)
elif operater == "-":
    print(num1 - num2)
elif operater == "*" :
    print(num1 * num2)
else:
    print(num1 / num2)