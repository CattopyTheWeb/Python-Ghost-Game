#!/usr/bin/env python3
# Ghost Game
from random import randint
from io import StringIO
import sys
import urllib.request
import requests
import time
 
#updator
currentVersion = "2.0.0"
URL = urllib.request.urlopen('https://raw.githubusercontent.com/MesVisiDraugai/Python-Ghost-Game/main/version.txt')

data = URL.read()
if (data == currentVersion):
    print("Ghost Game is up to date!\n", "Current version: ", currentVersion)
else:
    print("Ghost Game is not up to date! App is on version " + currentVersion + " but could be on version " + data + "!")
    print("Downloading new version now!")
    newVersion = requests.get("https://github.com/MesVisiDraugai/Python-Ghost-Game/releases/download/",data,"Ghost_game.exe")
    # file deepcode ignore MissingClose: <please specify a reason of ignoring this>
    open("ghost_game.exe", "wb").write(newVersion.content)
    print("New version downloaded, restarting the app in 5 seconds!")
    time.sleep(5)
    quit()

buffer = StringIO()
sys.stdout = buffer
with open(r"C:\ProgramData\GhostGame\name.txt", "rb") as thefile:
	name = thefile.read()

with open(r"C:\ProgramData\GhostGame\score.txt", "rb") as thefile:
	past_score = thefile.read()
print("Ghost Game")
print("Welcome ", name," !" )
print("Your past score: ", past_score)
lvl = input("What level of difficulty? easy, medium, hard or custom?")
feeling_brave = True
score = 0
if lvl == "easy":
	while feeling_brave:
		ghost_door = randint(1,3)
		print("Three doors ahead...")
		print("A ghost behind one.")
		print("Which door do you open?\n")
		door = input("1, 2 or 3?\n")
		door_num = int(door)
		if door_num == ghost_door:
			print("GHOST!")
			feeling_brave = False
		else:
			print("No ghost!")
			print("You enter the next room.")
			score = score + 1
	print ("Run away!")
	print("Game over! You scored", score)
	input()
elif lvl == "medium":
	while feeling_brave:
		ghost_door = randint(1,5)
		print("Five doors ahead...")
		print("A ghost behind one.")
		print("Which door do you open?\n")
		door = input("1, 2, 3, 4 or 5?\n")
		door_num = int(door)
		if door_num == ghost_door:
			print("GHOST!")
			feeling_brave = False
		else:
			print("No ghost!")
			print("You enter the next room.")
			score = score + 1
	print ("Run away!")
	print("Game over! You scored", score)
	input()
elif lvl == "hard": 
	while feeling_brave:
		ghost_door = randint(1,10)
		print("Ten doors ahead...")
		print("A ghost behind one.")
		print("Which door do you open?\n")
		door = input("1, 2, 3, 4, 5, 6, 7, 8, 9 or 10?\n")
		door_num = int(door)
		if door_num == ghost_door:
			print("GHOST!")
			feeling_brave = False
		else:
			print("No ghost!")
			print("You enter the next room.")
			score = score + 1
	print ("Run away!")
	print("Game over! You scored", score)
	input()
elif lvl == "custom":
	while feeling_brave:
		number = int(input("how many doors do you want? Integer only"))
		ghost_door = randint(1,number)
		print(number," doors ahead...")
		print("A ghost behind one.")
		print("Which door do you open?\n")
		for i in range(number):
			print(i)
		number_range = buffer.getvalue()
		door = input(number_range, "?\n")
		door_num = int(door)
		if door_num == ghost_door:
			print("GHOST!")
			feeling_brave = False
		else:
			print("No ghost!")
			print("You enter the next room.")
			score = score + 1
	print ("Run away!")
	print("Game over! You scored", score)
	input()
else:
    print("Please choose a valid option.")
    sys.exit
f = open("score.txt", "w")
f.write(score)
f.close()
