# Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
celsius = int(input(" Enter you temprature in Celsius: "))
if celsius <= 0:
    print(celsius, " is a freezing")
elif celsius >= 1 and celsius <= 30:
    print(celsius, " is a moderate")
else:
    print(celsius, " is a hot!")