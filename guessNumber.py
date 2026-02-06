import random

random_number = random.randint(1, 100)
guess_amount = 0

while True:
    guess = int(input("What do you guess? "))
    guess_amount += 1

    if guess > random_number:
        print("You guessed too high")

    elif guess < random_number:
        print("You guessed too low")

    else:
        print("You guessed correctly!") 
        print(f"It took you {guess_amount} guesses")
        break