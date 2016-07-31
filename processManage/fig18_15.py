#sending signals to child processes using kill

import os
import signal
import time
import sys

#handle both SIGALRM and SIGINT signals
def parentInterruptHandler(signum, frame):
	global pid 
	global parentKeepRunning

	#send kill signal to child process and exit
	os.kill(pid, signal.SIGKILL) #send kill signal 
	print "Interrupt received. Child process killed."

	#allow parent process to terminate normally
	parentKeepRunning = 0

#set parent's handler for SIGINT
signal.signal(signal.SIGINT, parentInterruptHandler)

#keep parent running until child process is killed 
parentKeepRunning = 1

#parent ready to fork child processes
try:
	pid = os.fork()
except OSError:
	sys.exit("Unable to create child process")

if pid!=0: #am I parent process?
	while parentKeepRunning:
		print "Parent Running. Press Ctrl-C to terminate child."
		time.sleep(1)
elif pid==0: #am I child process?
	#ignore interrupt in child processes
	signal.signal(signal.SIGINT, signal.SIG_IGN)

	while 1:
		print "Child still executing."
		time.sleep(1)

print "Parent terminated child process"
print "Parent terminating normally"

