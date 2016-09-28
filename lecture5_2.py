def squareRootNR(x, epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon>0, 'epsilon must be positive, not'+str(epsilon)
    x=float(x)
    guess=x/2.0
    guess=0.001
    diff=guess**2-x
    ctr=1
    while abs(diff)>epsilon and ctr<=100:
        guess=guess-diff/(2.0*guess)
        diff=guess**2-x
        ctr+=1
    assert ctr<=100,'Iteration count exceed'
    print('NR method. Num. itrations:',ctr,'Estimate:',guess)
    return guess
