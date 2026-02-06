import random

player = 0
pc = 0

signs = ["rock", "paper", "scissors"]
wins_against = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    sign = input("Rock, paper or scissors? ").strip().lower()
    pc_choose = random.choice(signs)

    print(f"You choose {sign} and pc choose {pc_choose}")

    if sign == pc_choose:
        print("Draw!")
    elif wins_against[sign] == pc_choose:
        print("You win!")
        player += 1
    else:
        print("PC wins!")
        pc += 1

    print(f"you: {player} and pc: {pc}")

    if player == 3 or pc == 3:
        print("We have a winner!")
        print(f"player: {player} and pc: {pc}")
        break
