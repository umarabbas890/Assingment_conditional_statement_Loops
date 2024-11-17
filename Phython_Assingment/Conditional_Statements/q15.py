# Write a program to check if a number is within a specified range.
number = float(input(" Enter a Number: "))
start = float(input(" Enter starting pont nmber: "))
end =  float(input(" Enter tour end number: "))

if number >= start and number <= end:
    print( number, " is in rang")
else:
    print(number, " is not in range")