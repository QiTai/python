#Use the system function to clear the screen

import os
import sys

def printInstructions(clearCommand):
	os.system(clearCommand) #clear display

print """Type the text that you wish to save in this file.\nType clear on a blank line to delete the contents of the file.\nType quit on a blank line when you are finished.\n"""
#determine operating system
if os.name == "nt" or os.name == "dos": #Windows system
	clearCommand = "cls"
	print "You are using a Windows system."
elif os.name == "posix": #UNIX-compatible system
	clearCommand = "clear"
	print "You are using a UNIX-compatible system."
else:
	sys.exit("Unsupported OS")

filename = raw_input("What file would you like to create?")

#open file 
try:
	file = open(filename, "w+")
except IOError, message:
	sys.exit("Error creating file: %s" %message)

printInstructions(clearCommand)
currentLine = "" 

#write input to file
while currentLine != "quit\n":
	file.write(currentLine)
	currentLine = sys.stdin.readline()

	if currentLine == "clear\n":
		#seek to beginning and truncate file
		file.seek(0,0)
		file.truncate()

		currentLine = ""
		printInstructions(clearCommand)

file.close()


