# Check if a given number is a multiple of both 3 and 5.
number = int(input(" Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print(number, " is a multiple of 3 and 5")
else:
    print(number, " is not multiple od 3 and 5")