#Demonstrating popen and popen2

import os

#determine operating system, then set directory-listing and reverse-sort commands
if os.name =="nt" or os.name == "dos":
	fileList = "dir /B"
	sortReverse = "sort /R"
elif os.name =="posix":
	fileList = "ls -l"
	sortReverse = "sort -r"
else:
	sys.exit("OS not supported by this program")

#obtain stdout of directory-listing commands
dirOut = os.popen(fileList,"r")

#obtain stdin, stdout of reverse-sort commands
sortIn,sortOut = os.popen2(sortReverse)

filenames = dirOut.read()

#display output from directory-listing commands
print "Before sending to sort"
print "(Output from '%s'):" % fileList
print filenames

sortIn.write(filenames) #send to stdin of sort commands

dirOut.close()
sortIn.close()
	
#display output from sort commands
print "After sending to sort"
print "(Output from '%s'):" % sortReverse
print sortOut.read() 

sortOut.close()


