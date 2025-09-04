import random

secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break
# Ai assisted