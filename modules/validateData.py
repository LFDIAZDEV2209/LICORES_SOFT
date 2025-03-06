import os 
import modules.screenController as sc
def validateInt(rqs:str)->int:
    try:
        x = int(input(rqs))
    except ValueError:
        print("ERROR: VALOR INVALIDO")
        sc.pauseScreen()
        return validateInt(rqs)
    else:
        return x
def validateFormat(rqs:str):
    x = input(rqs)
    if all(c.isalpha() or c.isspace() for c in x):
        return x
    elif x.isdigit():
        print("ERROR: VALOR INVALIDO")
        sc.pauseScreen()
        return validateFormat(rqs)
    elif x.isalnum():
        print("ERROR: VALOR INVALIDO")
        sc.pauseScreen()
        return validateFormat(rqs)
    else:
        print("ERROR: VALOR INVALIDO")
        sc.pauseScreen()    
        return validateFormat(rqs)
        