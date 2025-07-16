# Rock, Paper, Scissors

import random

RED = "\033[1;31m"
GREEN =  "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
ORANGE = "\033[38;5;208m"

RPS = ["Rock", "Paper", "Scissors"]
score = 0
wins = 1
losses = 1

print(f"{ORANGE}Welcome to Rock, Paper, Scissors!")

while score < 100 and score > -50:
    # Computer logic
    comp_choice = random.choice(RPS)
    # Player logic
    play_choice = input(f"{CYAN}Rock, Paper, or Scissors? Please choose one: ").strip().capitalize()
    if play_choice == "Scissor":
        play_choice = "Scissors"
    # Comparison logic
    if comp_choice == play_choice:
        print(f"{BLUE}You and the computer both chose {comp_choice}. This is a tie.")
        print(f"{CYAN}Your current score is {score}.")
        wins = 1
        losses = 1
    elif play_choice == "Rock":
        if comp_choice == "Scissors":
            print(f"{GREEN}You chose {play_choice} and the computer chose {comp_choice}. Rock smashes scissors. You won the round.")
            score += 10 * wins
            wins += 1
            losses = 1
            print(f"{CYAN}Your current score is {score}.")
        elif comp_choice == "Paper":
            print(f"{RED}You chose {play_choice} and the computer chose {comp_choice}. Paper covers rock. You lost the round.")
            score -= 10 * losses
            wins = 1
            losses += 1
            print(f"{CYAN}Your current score is {score}.")
    elif play_choice == "Paper":
        if comp_choice == "Rock":
            print(f"{GREEN}You chose {play_choice} and the computer chose {comp_choice}. Paper covers rock. You won the round.")
            score += 10 * wins
            wins += 1
            losses = 1
            print(f"{CYAN}Your current score is {score}.")
        elif comp_choice == "Scissors":
            print(f"{RED}You chose {play_choice} and the computer chose {comp_choice}. Scissors cut paper. You lost the round.")
            score -= 10 * losses
            wins = 1
            losses += 1
            print(f"{CYAN}Your current score is {score}.")
    elif play_choice == "Scissors":
        if comp_choice == "Paper":
            print(f"{GREEN}You chose {play_choice} and the computer chose {comp_choice}. Scissors cut paper. You won the round.")
            score += 10 * wins
            wins += 1
            losses = 1
            print(f"{CYAN}Your current score is {score}.")
        elif comp_choice == "Rock":
            print(f"{RED}You chose {play_choice} and the computer chose {comp_choice}. Rock smashes scissors. You lost the round.")
            score -= 10 * losses
            wins = 1
            losses += 1
            print(f"{CYAN}Your current score is {score}.")
    else:
        print(f"{ORANGE}Please choose from \"Rock\", \"Paper\", or \"Scissors\".")

if score >= 100:
    print(f"{ORANGE}Congrats! You've won Rock, Paper, Scissors.")
elif score <= -50:
    print(f"{ORANGE}You lost the game of Rock, Paper, Scissors. Better luck next time!")