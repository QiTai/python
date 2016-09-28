def fib(x):
    """"Return fibonacci of x, where x is non-negative int"""
    if x==0 or x==1: return 1
    else: return fib(x-1)+fib(x-2)
