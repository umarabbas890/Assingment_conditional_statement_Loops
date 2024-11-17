# 15. Print the sum of even and odd numbers separately up to a given number
n = int(input("Enter a number: "))
sum_even = sum(num for num in range(1, n + 1) if num % 2 == 0)
sum_odd = sum(num for num in range(1, n + 1) if num % 2 != 0)
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)