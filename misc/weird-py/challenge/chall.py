#!/usr/bin/env python3

from sys import exit

Flag = "shellmates{Le4k_V4r5_AAS_Has_jusT_STaRteD!_73298473204632}"
GLOBALS = globals()
print("---- show_variables_AAS - Everything is a service now ----\n\n")

while True : 
	var = input("Which variable you want to see --> ")
	if var == "Flag":
	    print("NOOO, not that one!")
	elif var ==  "exit" :
		exit()
	else:
	    if var in GLOBALS:
	        print(GLOBALS[var])
	    else:
	        print("Hmmm, doesn't seem to exist")
