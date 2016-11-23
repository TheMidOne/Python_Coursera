#rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
import math

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name == "rock"):
        return 0
    elif(name == "Spock"):
        return 1
    elif(name == "paper"):
        return 2
    elif(name == "lizard"):
        return 3
    elif(name == "scissors"):
        return 4
    else:
        print 'Invalid name input!'


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print 'Invalid number input!'
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print "========================="
    # print out the message for the player's choice
    print "player choose: " + player_choice;
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    print "player's choice maps to number: " + str(player_number)
    # compute random guess for comp_number using random.randrange()
    component_number = random.randrange(0,4)
    print "Now, random generate a component number: " + str(component_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print "Component is calling: " + number_to_name(component_number)

    # compute difference of comp_number and player_number modulo five
    smart_count = (player_number - component_number) % 5
    # use if/elif/else to determine winner, print winner message
    if(smart_count == 0):
        print "It's a draw"
    elif(smart_count >= 3):
        print "You lose!"
    else:
        print "You win!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


