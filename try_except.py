valueStr=input("Input an integer:")
try:
    if valueStr.isdigit():
        valueInt=int(valueStr)
    else:
        raise ValueError

except ValueError:
    print("Conversion to int Error:",valueStr)



while True:
    try:
        valueStr=input("Input integer: ")
        valueInt=int(valueStr)
        break
    except ValueError:
        print("Bad input")

while True:
    try:
        fileName=input("Open file:")
        dataFile=open(fileName,"r")
        break
    except IOError:
        print("Bad file name")
        


def processFile(dataFile):
    count=1
    for line in dataFile:
        print('Line'+str(count)+':'+line.strip())
        count=count+1

while True:
    filename=input('Input a file to open:')
    try:
        dataFile=open(fileName)
    except IOError:
        print('Bad file name;try again')
    else:
        print('Processing file',filename)
        processFile(dataFile)
        break
    finally:
        try:
            dataFile.close()
        except NameError:
            print('Going around again')
print('Line after the try-except group')

##LBYL, test for the problematic conditions:
##    if not isinstance(s,str) or not s.isdigit:
##        return None
##    elif len(s)>10:
##        return None
##    else:
##        return int(str)

##EAFP, just try it,clean up any mess with handlers
##    try:
##        return int(str)
##    except (TypeError, ValueError, OverflowError):
##        return None
