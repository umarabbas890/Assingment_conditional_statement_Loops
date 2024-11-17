# 17. Continue asking for a number until the correct number is guessed
correct_number = 5  # you can set any target number
while True:
    guess = int(input("Guess the number: "))
    if guess == correct_number:
        print("Correct guess!")
        break
    else:
        print("Try again.")