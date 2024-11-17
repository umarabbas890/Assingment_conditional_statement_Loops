# Create a program that evaluates if an inputted number is prime.

number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not prime.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
