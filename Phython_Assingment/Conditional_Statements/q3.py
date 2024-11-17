# Write a program that checks if a given year is a leap year.
leap_year = int(input("Enter a Year: "))
if leap_year %100 == 0 and leap_year % 400 == 0:
    print(leap_year, " is a leap year")
elif leap_year %100 !=0 and leap_year %4 ==0:
       print(leap_year, " is a leap year")
else:
      print(leap_year, " is not a leap year")