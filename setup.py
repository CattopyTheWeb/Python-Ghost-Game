import os, winshell
from win32com.client import Dispatch
import requests
dir = os.path.join("C:\\","ProgramData\\","GhostGame")

if not os.path.exists(dir):
    # file deepcode ignore UpdateAPI: don't need that
    os.mkdir(dir)

yesorno = input("Do you want to enter your name? (Y/N)")
print("Don't worry your name will only be used in this game.\n Keep in mind it will be stored in C:\ProgramData so you can amend it there.")
if yesorno == "Y":
    name = input("What is your name?")
    
elif yesorno == "N":
    print("No worries, we will not take note of your name.")

else:
    print("Please enter Y or N.")
    exit()

version = 2.0

#info file
f = open("name.txt", "w")
f.write(name)
f.close()

#other files
f = open("version.txt", "w")
f.write(version)
f.close()

#Ghost game
ghost_game = requests.get("https://github.com/MesVisiDraugai/Python-Ghost-Game/releases/download/v2.0.0/Ghost_game.exe")
f = open(r"C:\ProgramData\GhostGame\Ghost_game.exe", "w")
f.write(ghost_game)
f.close()


#desktop icon

desktop = winshell.desktop()
path = os.path.join(desktop, "Ghost Game")
target = r"C:\ProgramData\GhostGame\Ghost_game.exe"
wDir = r"C:\ProgramData\GhostGame"
icon = r"C:\ProgramData\GhostGame\Ghost_game.exe"
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
