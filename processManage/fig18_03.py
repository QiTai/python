#Demonstrates the wait function

import os
import sys
import time
import random

#generate random sleep times for child processes
sleepTime1 = random.randrange(1,6)
sleepTime2 = random.randrange(1,6)

#parent ready to fork first child process
try:
	forkPID1 = os.fork() #create first child process
except OSError:
	sys.exit("Unable to create first child.")

if forkPID1 != 0: #am I parent process?
	#parent read to fork second child processes
	try:
		forkPID2 = os.fork() #create second child process
	except OSError:
		sys.exit("Unable to create second child.")
	
	if forkPID2 != 0: #am I parent process?
		print "Parent waiting for child processes... \n" + \
			"\tpid:%d,forkPID1:%d,forkPID2:%d"\
			%(os.getpid(),forkPID1,forkPID2)

		#wait for any child processes
		try:
			child1 = os.wait()[0] #wait return one child's pid
		except OSError:
			sys.exit("No more child processes.")

		print "Parent: Child %d finished first,one child left."\
			%child1

		#wait for another child processes
		try:
			child2 = os.wait()[0] #wait return another child's pid
		except OSError:
			sys.exit("No more child processes.")

		print "Parent: Child %d finished second,no child left."\
			%child2
	elif forkPID2 == 0: #am I second child process?
		print "Child2 sleeping for %d seconds...\t pid:%d, forkPID1:%d,forkPID2:%d" %(sleepTime2,os.getpid(),forkPID1,forkPID2)
		time.sleep(sleepTime2) #sleep to simulate some work

elif forkPID1 == 0: #am I first child process?
	print "Child1 sleeping for %d seconds...\t pid: %d, forkPID1:%d" %(sleepTime1,os.getpid(),forkPID1)


