import os
import pyautogui as py
a = [1135, 470]
b = [1250, 471]
c = [1139, 580]
d = [1245, 584]
while True:
	while True:
		x = input("Enter option ---> ")
		if x=="a":
			py.moveTo(a)
		elif x=="b":
			py.moveTo(b)
		elif x=="c":
			py.moveTo(c)
		elif x=="d":
			py.moveTo(d)
		elif x in ["nav","Nav","NAV","clear","Clear"]:
			print("")
			print("")
			print("")
			print("Good Luck!")
			break
		else:
			print("Incorrect Response")
			break
		os.system("xdotool click --delay 10 --repeat 1500 1-")
