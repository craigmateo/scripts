# Rock-paper-scissors-lizard-Spock game


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random 

# helper functions

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Sorry, not a valid entry!'


def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Sorry, number not in range 0-4!'
    

def rpsls(player_choice): 
    print
    print('You chose ' + player_choice +'!')
    player_number = name_to_number(player_choice)  # convert the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0,4)  # compute random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)   # convert comp_number to comp_choice using the function number_to_name()
    print('The computer choses '+comp_choice +'!')  # print out the message for computer's choice
    difference = (comp_number - player_number)%5 # compute difference of comp_number and player_number modulo five
    if difference == 0:
        print('tie...play again') # use if/elif/else to determine winner, print winner message
    elif difference < 2:
        print('computer wins!')
    else:
        print('you win!')
        
        
    
    
# test code 
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
