import os

def validateint(msg:str)->int:
    try:
        x=input(msg)
        return x
    except ValueError:
        print('ingrese un valor valido')
        return(validateint)

def validatetext(msg):
    x = input(msg).strip(' ')
    if x.isalpha():
        return x
    else:
        print('ingrese un valor valido')
        return validatetext(msg)
    
def validateflot(msg:str)->float:
    try:
        x=input(msg)
        return x
    except ValueError:
        print('ingrese un valor valido')
        return(validateflot)