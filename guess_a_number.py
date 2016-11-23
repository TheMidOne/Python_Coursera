import simplegui
import random
import math

remainTry = 0
targetNumber = 0
upperLimit = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global targetNumber, remainTry, upperLimit
    print "======New Game======"
    
    print "Upper limit is : " + str(upperLimit)
    
    targetNumber = random.randrange(0, upperLimit)
    print "target number is : " + str(targetNumber)
    
    remainTry = int(math.ceil(math.log(upperLimit, 2)))
    print "remain number is : " + str(remainTry)

def input_range(upper):
    global upperLimit
    upperLimit = int(upper)
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global targetNumber, remainTry
    print "                  "
    print "The number you are guessing is : " + guess
    remainTry -= 1
    guessNum = int(guess)
    if(guessNum > targetNumber):
        print "Lower!"
        print "You have " + str(remainTry) + " more changes."
    elif(guessNum < targetNumber):
        print "Higher!"
        print "You have " + str(remainTry) + " more changes."
    else:
        print "You are correct!"
        print "====== Next Game ======="
        print "                  "
        new_game()
        
    if(remainTry <= 0):
        print "====== Game over ======="
        print "                  "
        new_game()
    

    
# create frame
frame = simplegui.create_frame("Guess the number", 400, 400)

frame.add_input("Enter upper limit", input_range, 100)
frame.add_input("Enter your guess", input_guess, 100)

# register event handlers for control elements and start frame


# call new_game 
#new_game()

frame.start()

# always remember to check your completed program against the grading rubric
