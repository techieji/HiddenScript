import os
from random import choice, randint
from Tree import Tree
#from Infect import Infect

def HiddenScript():
    filepath = os.getcwd() #note to self: this is how you get a file's location (most of the time, at least)
    while True:
        t = Tree(filepath)
        try:
            break
        except IndexError:
            filepath = os.path.dirname(filepath)