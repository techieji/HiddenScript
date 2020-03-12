import os
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
