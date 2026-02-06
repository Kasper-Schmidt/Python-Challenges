import random

words = ["apple", "bread", "chair", "table", "house","plant", "river", "stone", "light", "sound", "smile", "laugh", "dream", "sleep", "brain", "heart", "world", "water", "flame", "cloud", "grass", "beach", "storm", "train", "plane", "money", "peace", "power", "sweet", "sharp", "quick", "smart", "clean", "brave", "truth", "happy", "young", "older", "magic", "solid"]

hangman_word = random.choice(words)

hidden = ["_"] * len(hangman_word)

while True:
    guess = input("Guess letter: ").lower()

    for i, c in enumerate(hangman_word):
        if guess == c:
            hidden[i] = guess

    print(" ".join(hidden))

    if "_" not in hidden:
        print("You found the word!")
        break
        

