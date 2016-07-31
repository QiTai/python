#open a Web page in a system-specific editor

import os
import sys
import urllib

if len(sys.argv) !=3 :
    sys.exit("Incorrect number of arguments.")

#determine operating system and set editor command
if os.name == "nt" or os.name == "dos":
    editor = "notepad.exe"
elif os.name == "posix":
    editor = "vi"
else:
    sys.exit("Unsupported OS")

#obtain Web page and store in file
urllib.urlretrieve(sys.argv[1],sys.argv[2])

#editor expects to receive itself as an argument
os.execvp(editor, (editor, sys.argv[2]))

print("This line never executes.")
