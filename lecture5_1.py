def squareRootBi(x,epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon>0, 'epsilon must be positive, not'+str(epsilon)
    low=0
    high=max(x,1)
    guess=(low+high)/2.0
    ctr=1
    while abs(guess**2-x)>epsilon and ctr<=100:
        if guess**2<x:
            low=guess
        else:
            high=guess
        guess=(low+high)/2.0
        ctr+=1
    assert ctr <= 100, 'Iteration count exceed'
    print ('Bi method. Num. iterations:',ctr,'Estimate:',guess)
    return guess
