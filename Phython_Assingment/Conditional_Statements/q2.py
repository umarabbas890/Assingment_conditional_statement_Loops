# Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int(input(" Enter Your Age: "))
if age < 18 and age > 0:
    print(age, " is a Minor age")
elif age >= 18 and age < 64:
    print(age, " is an aduult")
else:
    print(age, " is Senior citizen")