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

    
    

