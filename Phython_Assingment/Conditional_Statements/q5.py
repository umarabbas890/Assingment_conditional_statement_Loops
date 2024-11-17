# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

Grade = int(input(" Enter your marks: "))
if Grade >= 90 and Grade <= 100:
    print(" You Get A Grade")
elif Grade >= 80 and Grade <= 89:
    print(" You Get B Grade")
elif Grade >= 70 and Grade <= 79:
    print(" You Get C Grade")
elif Grade >= 60 and Grade <= 69:
    print(" You Get D Grade")
elif Grade >= 50 and Grade <= 59:
    print(" You Get E Grade")
else:
    print("You Got F Grade")
