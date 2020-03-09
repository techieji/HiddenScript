import os
import threading
from time import sleep
from random import randint, choice
from itertools import chain

class Tree:
    def __init__(self, startpath):
        self.startpath = startpath
        os.chdir(startpath)
        self.dir = []
        self.files = []
        for x in os.listdir(startpath):
            try:
                if os.path.isdir(os.path.join(startpath, x)):
                    self.dir.append(Tree(os.path.join(startpath, x)))
                else:
                    self.files.append(x)
            except PermissionError:
                continue
    def searchExtension(self, ex): # returns a list of all the files
        lis = []
        for x in self.files:
            _, extension = os.path.splitext(x)
            if extension == ex:
                lis.append(x)
        return list(chain.from_iterable([lis] + [x.searchExtension(ex) for x in self.dir]))
    
    def findFile(self, filename): # returns the path of the specified file
        os.chdir(self.startpath)
        for root, dirs, files in os.walk(os.getcwd()):
            for name in files:
                if name == filename:
                    return os.path.abspath(os.path.join(root, name))

def HiddenScript():
    filepath = os.getcwd() #note to self: this is how you get a file's location (most of the time, at least)
    t = Tree(os.path.dirname(filepath))
    open(os.path.dirname(filepath) + "\\" + "Test.txt", mode='x')

def GuessingGame():                            #credits to https://www.codespeedy.com/number-guessing-game-in-python/
    print(os.getcwd())
    print("This is a guessing game. Try your best!")
    sleep(0.1)
    random_number = randint(1, 100)
    win = False
    Turns =0
    while win==False:
        Your_guess = input("Enter a number between 1 and 100: ")
        Turns +=1
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
              
game = threading.Thread(target=GuessingGame)
script = threading.Thread(target=HiddenScript)
game.start()
script.start()
