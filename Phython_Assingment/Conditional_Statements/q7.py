# Write a program to find the largest of three numbers.

num1 = int(input(" Enter your first number: "))
num2 = int(input(" Enter your second number: "))
num3 = int(input(" Enter your third number: "))

if num1 > num2 and num1 > num3:
    print(num1, " is greater then ", num2, " and ", num3)
elif num2 > num1 and num2 > num3:
    print(num2, " is greater then ", num1, " and ", num3)
else:
    print(num3," is greater then ", num1, " and ", num2)
