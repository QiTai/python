import os
def check(searchStr,count,fileList,dirList):
    for dirName,dirs,files in os.walk("."):
        for f in files:
            if os.path.splitext(f)[1]=='.txt':
                count=count+1
                aFile=open(os.path.join(dirName,f),'r')
                fileStr=aFile.read()
                if searchStr in fileStr:
                    fileName=os.path.join(dirName,f)
                    fileList.append(fileName)
                    if dirName not in dirList:
                        dirList.append(dirName)
                aFile.close()
    return count

theStr=input('What string to look for:')
fileList=[]
dirList=[]
count=0
count=check(theStr,count,fileList,dirList)

print('Looked at %d text files'%(count))
