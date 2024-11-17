# 7. Find the factorial of a number using a while loop
n = int(input("Enter a number to find factorial: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"Factorial of {n} is {factorial}")