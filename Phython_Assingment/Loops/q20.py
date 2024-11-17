# 20. Countdown timer from a given number to zero
countdown = int(input("Enter a number to start countdown: "))
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Countdown complete!")