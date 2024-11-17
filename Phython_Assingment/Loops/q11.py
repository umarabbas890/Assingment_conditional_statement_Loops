# 11. Print the reverse of a given number
number = int(input("Enter a number to reverse: "))
reverse = 0
while number > 0:
    reverse = reverse * 10 + number % 10
    number //= 10
print("Reversed number:", reverse)