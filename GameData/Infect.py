import threading
import os
from shutil import move

def RunFile(exepath):
    os.startfile(exepath)

def Infect():
    pass

OrgExePath = ""
VirusExePath = ""

orgfile = threading.Thread(target=RunFile, args=(OrgExePath))
ViralScript = threading.Thread(target=RunFile, args=(VirusExePath))
orgfile.start()
ViralScript.start()