#Defining our own signal handler

import time
import signal

def stop(signalNumber, frame):
	global keepRunning
	keepRunning -= 1
	print "Crtl -C pressed; keepRunning id " , keepRunning

keepRunning = 3

#set the handler for SIGINT to be function stop 
signal.signal(signal.SIGINT, stop)

while keepRunning:
	print "Executing ..."
	time.sleep(1)

print "Program terminating..."

