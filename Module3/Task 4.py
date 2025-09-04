import random
random_num=random.randint(1,10)
while True:
    guess_num=int(input("Guess the number between ( 1 and 10): "))
    if guess_num > random_num:
        print("it is high! Better luck next time!")
    elif guess_num < random_num:
        print("it is low! Better luck next time!")
    elif guess_num == guess_num:
        print("well done! you get it!")
