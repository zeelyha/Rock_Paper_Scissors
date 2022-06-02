#Rock, Paper Scissors

import random


options = ["Rock", "Paper", "Scissors"]

#PC Selection function
def pc_option():
    return random.choice(options)


still_playing = True

while still_playing:
    print("Welcome to the Game!!!")
    user_option = input("Select an option: R for Rock, P for Paper and S for Scissors: \n")
    cpu_option = pc_option()
    if user_option.upper() == "R":
        print("Player (Rock) : CPU ( %s)" %cpu_option)

        #Rock beats Scissors
        if cpu_option == options[2]:
            print("Rock beats Scissors, You Win!!!")
            still_playing = False
        elif cpu_option == options[1]:
            print("Paper beats Rock, CPU Wins!!!")
            still_playing = False
        elif cpu_option == options[0]:
            print("It's a tie!!!")  

    elif user_option.upper() == "P":
        print("Player (Paper) : CPU( %s)" %cpu_option)

        #Paper beats Rock
        if cpu_option == options[0]:
            print("Paper beats Rock, You Win!!!")
            still_playing = False
        elif cpu_option == options[2]:
            print("Scissors beats Paper, CPU Wins!!!")
            still_playing = False
        elif cpu_option == options[1]:
            print("It's a tie!!!")  

    elif user_option.upper() == "S":
        print("Player (Scissors) : CPU (%s)" %cpu_option)

        #Scissors beats Paper
        if cpu_option == options[1]:
            print("Scissors beats Paper, You Win!!!")
            still_playing = False
        elif cpu_option == options[0]:
            print("Rock beats Scissors, CPU Wins!!!")
            still_playing = False
        elif cpu_option == options[2]:
            print("It's a tie!!!")   

    else:
        print("Invalid Selection. Try again")             



    




