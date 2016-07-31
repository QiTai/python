#Using fork to create child process

import os
import sys
import time

processName = "parent" #only the parent is running now

print "Program executing\n\tpid: %d, processName: %s" %(os.getpid(),processName)

#attempt to fork child processName
try:
	forkPID = os.fork() #create child process
	print(processName)
except OSError:
	sys.exit('Unable to create new process.')

if forkPID!=0:	#am I parent process? 
	print "Parent executing\n" + \
			"\tpid: %d, forkPID: %d, processName: %s" \
		 %(os.getpid(), forkPID, processName)
elif forkPID==0: #am I child process?
	processName = "child"
	print "Child executing\n" + \
			"\tpid: %d, forkPID: %d, processName: %s" \
			%(os.getpid(), forkPID, processName)

print "Process finishing \n\tpid:%d,processName:%s"\
		%(os.getpid(),processName)

