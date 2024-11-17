# Write a program that checks if a given number is positive, negative, or zero.
num = int(input(" Enter Your Number: "))

if num < 0:
    print(num, " Is a Negtive Number")
elif num > 0:
    print(num, " is a Positive number")
else:
    print(num, " is a Zero")