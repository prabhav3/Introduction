# Guess the number

import random

guess_number = random.randint(1, 100)
chances = 6
score = 10

while chances:
    player = int(input("Guess a number between 1-100: "))
    if not player in range(1, 101):
        print("Please choose a number between 1-100")
        continue
    if guess_number == player:
        print(f"Congratulations! The correct number was {player}.\nYou got it correct in {7-chances} attempts.")
        score *= chances
        break
    elif player > guess_number:
        print("The correct number is less than your guess. Please try again.")
    else:
        print("The correct number is larger than your guess. Please try again.")
    chances -= 1
    print(f"You have {chances} attempts left.")

if chances > 0:
    print(f"Your score is {score}.")
else:
    print(f"Sorry, you've run out of attempts, the correct number was {guess_number}.")