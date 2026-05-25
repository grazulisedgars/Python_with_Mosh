# Loops

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

# Guessing game


secret_number = 3
guesses = 0
guess_limit = 3

while guesses < guess_limit:
    guess_number = int(input("Guess: "))

    if guess_number == secret_number:
        print("Well Done! You've guessed the number")
        break
    else:
        print("Not the number. Try again!")
        guesses = guesses + 1

    if guess_number != secret_number:
        print("Sorry you failed!")
