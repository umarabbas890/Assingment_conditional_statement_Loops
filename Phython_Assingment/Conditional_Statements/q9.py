# Take three sides of a triangle as input and check if they form a valid triangle.
a = float(input(" Enter first side of tryangle: "))
b = float(input(" Enter second side of tryangle: "))
c = float(input(" Enter third side of tryangle: "))
if a + b > c and a + c > b and b + c > a:
    print(" tryangle is valid triangle")
else:
  print(" is not a valid triangle")