# Rock-Paper-Scissors-Game

import random


# function to determine the winner
def determine_winner(player, cpu):
    if player == cpu:
        print(f'Both players selected {player}. It\'s a tie!')
    elif player == "R":
        if cpu == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif player == "P":
        if cpu == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif player == "S":
        if cpu == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")


# loop to play the game, loop ends when user select No
while True:
    while True:
        try:
            user_input = input('Enter a choice ("R" for "rock", "P" for "paper", "S" for "scissors"): ')
            if user_input.upper() not in ('R', 'P', 'S'):
                print('Wrong input, please try again')
            else:
                break

        except ValueError:
            print('Wrong input, please try again')
            continue

    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    user_input = user_input.upper()
    computer_action = computer_action.upper()

    determine_winner(user_input, computer_action)

    play_again = input("Play again? ('Y' for Yes/'N' for No): ")
    
    if play_again.lower() not in ('y', 'n'):
        continue
    else:
        if play_again.lower() != "y":
            print("Thank you for playing!")
            break
