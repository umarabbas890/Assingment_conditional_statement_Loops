# Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 == side2 and side1 == side3 and side2 == side3:
    print(" triangle is a Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print(" triangle is a isosceles")
else:
    print(" trianle is scalene")
