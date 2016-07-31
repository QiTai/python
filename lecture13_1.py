numCalls=0
def fib(n):
    global numCalls
    numCalls+=1
    if n<=1:
        print('fib of',n)
        return 1
    else:
        print('fib of',n)
        return fib(n-1)+fib(n-2)
    print(numCalls)

memo={0:0,1:1}
def fib1(n):
    global memo
    global numCalls
    numCalls+=1
    if not n in memo:
        memo[n]=fib1(n-1)+fib1(n-2)
    return memo[n]



##：以下程序就是采用了”用空间Dictionaries换时间“


##def fastFib(n,memo):
    global numCalls
    numCalls+=1
    print('fib1 called with',n)
    if not n in memo:
        memo[n]=fastFib(n-1,memo)+fastFib(n-2,memo)
    return memo[n]
def fib1(n):
    memo={0:1,1:1}
    return fastFib(n,memo)
numCalls=0


def maxVal(w,v,i,aW):
    #print('maxVal called with:',i,aW)
    global numCalls
    numCalls+=1
    if i==0:
        if w[i]<=aW: return v[i]
        else: return 0
    without_i=maxVal(w,v,i-1,aW)
    if w[i]>aW: return without_i
    else: with_i=v[i]+maxVal(w,v,i-1,aW-w[i])
    return max(with_i,without_i)
weights=[2,2,6,5,4]
vals=[6,3,5,4,6]
numCalls=0
res=maxVal(weights,vals,len(vals)-1,10)


##:下面01背包问题都是采用Dynamic Programming,而上面仅仅用了递归；通过对比两个程序的调用次数numCalls，我们可以看到如果我们采用“Dictionaries",将一些已经算好的子问题的结果存起来，则会节省很多时间，“用空间换时间”。 
def fastMaxVal(w,v,i,aW,m):
    global numCalls
    numCalls+=1
    try: return m[(i,aW)]
    except KeyError:
        if i==0:
            if w[i]<=aW:
                m[(i,aW)]=v[i]
                return v[i]
            else:
                m[(i,aW)]=0
                return 0
        without_i=fastMaxVal(w,v,i-1,aW,m)
        if w[i]>aW:
            m[(i,aW)]=without_i
            return without_i
        else: with_i=v[i]+fastMaxVal(w,v,i-1,aW-w[i],m)
        res=max(with_i,without_i)
        m[(i,aW)]=res
        return res
    
def maxVal0(w,v,i,aW):
    m={}
    return fastMaxVal(w,v,i,aW,m)

weights=[2,2,6,5,4]
vals=[6,3,5,4,6]
numCalls=0
m={}
res=fastMaxVal(weights,vals,len(vals)-1,8,m)        
