#合并排序法
def merge(left,right):
    """Assume left and right are sorted lists.Return a new sorted list containing the same elements as (left+right) would contain."""
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    while i<len(left):
        result.append(left[i])
        i=i+1
    while j<len(right):
        result.append(right[j])
        j=j+1
    return result

def mergesort(L):
    """Return a new sorted list with the same elements as L"""
    print(L)
    if len(L)<2:
        return L[:]
    else:
        middle=int(len(L)/2)
        left=mergesort(L[:middle])
        right=mergesort(L[middle:])
        together=merge(left,right)
        print('merged',together)
        return together

def create(smallest,largest):
    intSet=[]
    for i in range(smallest,largest+1): intSet.append(None)
    return intSet

def insert(intSet,e):
    intSet[e]=1

def member(intSet,e):
    return intSet[e]==1

def hashChar(c):
    #c is a char
    #function returns a different integer in the range 0-255
    #for each possible value of c
    return ord(c) #ord()函数是chr()函数（对于8位的ASCII字符串）或unichr()函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值
def cSetCreate():
    cSet=[]
    for i in range(0,255): cSet.append(None)
    return cSet

def cSetInsert(cSet,e):
    cSet[hashChar(e)]=1

def cSetMember(cSet,e):
    return cSet[hashChar(e)]==1

def readFloat(requestMsg,errorMsg):
    while True:
        val=input(requestMsg)
        try:
            val=float(val)
            return val
        except:
            print(errorMsg)
#print(readFloat('Enter float:','Not a float.')

def readVal(valType,requestMsg,errorMsg):
    while True:
        val=input(requestMsg)
        try:
            val=valType(val)
            return val
        except:
            print(errorMsg)
#print(readVal(int,'Enter int:','Not an int.')















    
