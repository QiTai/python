def main(fName):
    '''
    >>>main('')
    File named not found
    >>>main('x')
    Traceback(most recent call last):
    ...
    IOError: bad file format, line was: this is a bad life
    >>>main('player_career.csv')
    The top 10 palers in efficency are
    ******************
                 Eilt Chab:41.50
                 ...

    '''
    try:
        fd=open(fName)
    except IOError:
        print('File named %s not found',fName)
    else:
        nbaDict={}
        line=fd.readline()
        if line[0:5]!='ilkid':
            raise IOError('bad file format,line was: %s', line)
        for line in fd:
            calcEfficiency(line,nabDict)
        results=findMOstEfficient(nbaDict,10)
        printResults(results)
        fd.close()
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
