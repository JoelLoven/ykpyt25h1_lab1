import random
import os

WIN = "You win!"
LOSE = "You lose!"
TIE = "It's a tie!"

class round_result:
     def __init__(self,outcome, oponent_pick):
        self.outcome = outcome
        self.oponent_pick = oponent_pick


def get_user_pick_input():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input. Try again using rock, paper or scissors.")

def get_oponent_pick():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return TIE
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return WIN
    else:
        return LOSE

def clear_consol():
    os.system('cls' if os.name=='nt' else 'clear')

def play_roud():
            computer_pick = get_oponent_pick()
            user_pick = get_user_pick_input()
            result = determine_winner(user_pick, computer_pick)
            return round_result(result, computer_pick)

def main():
    print(
        '\033[4m\033[96m' + "Let's play Rock Paper Scissors\033[0m")
    while True:
        result = play_roud()
        while result.outcome == TIE:
            print(TIE + ", let's play again")
            result = play_roud()

        result_print_color = '\033[92m' if result.outcome == WIN else '\033[91m'

        print(f"\nOponent picked: {result.oponent_pick}, \033[1m{result_print_color}{result.outcome}\033[0m")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing.")
            break
        else:
            clear_consol()

if __name__ == "__main__":
    main()
