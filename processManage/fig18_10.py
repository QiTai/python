#using os.pipe to communicate with a child process

import os 
import sys

#open parent and child read/write pipes
fromParent, toChild = os.pipe()
fromChild, toParent = os.pipe()

#parent about to fork child process
try:
	pid = os.fork()	#create child process
except OSError:
	sys.exit("Unable to create child process")

if pid!=0:	#am I parent process?
	
	#close unnecessary pipe ends
	os.close( toParent )
	os.close(fromParent)

	#write values from 1-10 to parent's write pipe and read 10 values from child's read pipe
	for i in range(1,11):
		os.write(toChild, str(i))
		print "Parent: %d" % i
		print "child: %s" %\
			os.read(fromChild, 64)
	#close pipes
	os.close(toChild)
	os.close(fromChild)

elif pid == 0: #am I child process?
	
	#close unnecessary pipe ends 
	os.close(toChild)
	os.close(fromChild)

	#read value from parent pipe
	currentNumber = os.read(fromParent, 64)

	#if we receive number from parent, write number to child write pipe'
	while currentNumber:
		newNumber = int(currentNumber)*20
		os.write(toParent,str(newNumber))
		currentNumber = os.read(fromParent, 64)

	#close pipes
	os.close(toParent)
	os.close(fromParent)
	os._exit(0) #terminate child process
