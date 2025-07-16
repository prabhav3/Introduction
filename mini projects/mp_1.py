# Flip the coin
# In the flip the coin game, if you win continuously your score added will increase. Example: 10, 20, 30, etc.
# If you lose, your score will decrease by 10 and so on: Example: -10, -20, -30
# To win, you require a score of 100, and to lose it will be -50

import random

score = 0
wins = 1
losses = 1
sides = ["Heads", "Tails"]

RED = "\033[1;31m"
GREEN =  "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"


while score < 100 and score > -50:
    comp_flip = random.choice(sides)
    player_flip = input(f"{BLUE}Heads/Tails? Guess the coin side: ").strip().capitalize()
    if player_flip == comp_flip:
        print(f"{GREEN}Congrats! You got it right, you and the computer chose {comp_flip}.")
        score += 10 * wins
        wins += 1
        losses = 1
        print(f"{CYAN}Your score is {score}")
    elif player_flip not in sides:
        print(f"{YELLOW}Please only enter \"Heads\" or \"Tails\"")
        print(f"{CYAN}Your score is {score}")
    else:
        print(f"{RED}Oh no! You guessed {player_flip} but the computer chose {comp_flip}.")
        score -= 10 * losses
        losses += 1
        wins = 1
        print(f"{CYAN}Your score is {score}")

if score >= 100:
    print(f"{GREEN}Congratulations! You won the game of Coin Flip!")
else:
    print(f"{RED}You lost the game of Coin Flip. Better luck next time!")