#Demonstrates the waitpid function

import os
import sys
import time

#parent about to fork first child process
try:
    forkPID1 = os.fork() #create the first child process
except OSError:
    sys.exit("Unable to create first child.")

if forkPID1 != 0:   #am I parent process?

    #parent about to fork second child process
    try:
        forkPID2 = os.fork()
    except OSError:
        sys.exit("Unable to create second child.")

    if forkPID2 > 0: #am I parent process?
        print ("Parent waiting for child processes...\n"\
               "\tpid:%d,forkPID1:%d,forkPID2:%d"\
               %(os.getpid(),forkPID1,forkPID2))
        #wait for second child process explicitly
        try:
            child2 = os.waitpid(forPID2,0)[0] #child pid
        except OSError:
            sys.exit("No child process with pid %d." %(forkPID2))
        print("Parent : Child %d finished."\
              % child2)

    elif forkPID2 == 0: #am I second child process?
        print("Child2 sleeping for 4 seconds ...\n" + \
              "\tpid:%d forkPID1:%d, forkPID2: %d" \
              %(os.getpid(),forkPID1,forkPID2))
        time.sleep(4)
elif forPID1 == 0: # am I first child process?
    print("Child1 sleeping for 2 seconds ...\n" + \
              "\tpid:%d forkPID1:%d" \
              %(os.getpid(),forkPID1))
    time.sleep(2)
