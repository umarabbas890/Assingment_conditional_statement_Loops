# 4. Print the multiplication table of a given number
n = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")