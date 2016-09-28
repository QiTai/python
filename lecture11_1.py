def silly():
    res=[]
    done=False
    while not done:
        elem=input('Enter element. Return when done. ')
        if elem=='':
            done=True
        else:
            res.append(elem)
    print('res should be[1,''a'',2]',res)  #debugging right
    tmp=res
    tmp.reverse()
    print("tmp",tmp,'res',res)  #dubugging to these two sentence, tmp=res[:]
    isPal=(res==tmp)
    #print("tmp",tmp,'res',res)    #debugging wrong
    if isPal:
        print('is a palindrome')
    else:
        print('is NOT a palindrome')
