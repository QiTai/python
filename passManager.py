import string
#define our own exception
class NameException(Exception):
    """For malformed names"""
    pass
class PasswordException(Exception):
    """For bad password"""
    pass
class UserException(Exception):
    '''raise for existing or missing user'''
    pass

def checkPass(passStr,targetStr):
    '''return True, if password contains characters from target'''
    for char in passStr:
        if char in targetStr:
            return True
        return False
    
class passManager(object):
    '''A class to manage a dictionary of password with error checking'''
    def __init__(self,initDict=None):
        if initDict==None:
            self.passDict={}
        else:
            self.passDict=initDict.copy()

    def dumpPasswords(self):
        return self.passDict.copy()

    def addUser(self,user):
        '''add good user name and strong password to password dictionary'''
        if not isinstance(user,str) or not user.isalnum():  ##isinstance,isalnum?
            raise NameException
        if user in self.passDict:
            raise UserException
        passStr=input('New password:')
        if not(checkPass(passStr,string.digits) and\
               checkPass(passStr,string.uppercase) and\
               checkPass(passStr,string.punctuation)):
            raise PasswordException
        
    def validate(self,user):
        '''return true, if valid user and password'''
        if not isinstance(user,str) or not user.isalnum():
            raise NameException
        if user not in self.passDict:
            raise UserException
        passWd=input('Passwd:')
        return self.passDict[user]==passWd


#from pmModule import *

def main():
    pm=passManager({'bill':'$4Donuts','rich':'1234ABC'})

    maxTries=3 #three tries allowed
    cnt=maxTries
    result=False
    while cnt>0 and not result:
        userStr=input('User name:')
        try:
            result=pm.validate(userStr)   #validate prompts for password
        except NameException:
            print('Bad name!')
        except UserException:
            if input('No such name,add as new user(Y or y)?') in 'Yy':
                try:
                    pm.addUser(userStr)
                    #only get here if no exception raised in addUser
                    result=True
                except NameException:
                    print('Bad name!')
                except UserException:
                    print('User already exists!')
                except PasswordException:
                    print('Bad password!')
        finally:
            cnt-=1
        if not result:
            print('Session timed out.')
        else:
            print('Welcome user',userStr)
            
                    

                


    
