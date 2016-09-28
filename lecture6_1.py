Techs=['MIT','Cal Tech']

print(Techs)
Ivys=['Harvard','Yale','Brown']
print(Ivys)
Univs=[]
Univs.append(Techs)
print (Univs)
Univs.append(Ivys)
input()
print (Univs)
input()
for e in Univs:
    print( e)
    for c in e: print(c)
input()
Univs=Techs+Ivys
print(Univs)
input()
Ivys.remove('Harvard')
print (Univs)
Ivys[1]=-1
print (Ivys)

L1=[1,2,3]
L2=L1
L1[0]=4
print (L2)

def f(L):
    L[0]=4
L1=[1,2,3]
L2=[1,2,3]
L3=L1
print(L1==L2)
y=input()
f(L1)
print(L1==L2)
print(L1)
print(L2)
print(L3)

L1=[1,2,3]
L2=L1[:]
print("::",L2)


EtoF={'one':'un','soccer':'football'}
print(EtoF['soccer'])
#print(EtoF[0])    #This sentence has error,because dictionaries aren't ordered.
print(EtoF)


NtoS={1:'one',2:'two','one':1,'two':2}
print(NtoS.keys())
print(NtoS.keys)
del NtoS['one']
print(NtoS)


L=[ ['un','one'],['deux','two']]
def keySearch(L,k):
    for elem in L:
        if elem[0]==k: return elem[1]
    return 1
print(keySearch(L,'deux'))
      









