from os import system
import sys
import json as js

def deleteScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")
def pauseScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        pause = input("Presione una tecla para continuar...")
    else:
        system("pause")
        
def dicOrder(league:dict):
    print(js.dumps(league, indent=4))