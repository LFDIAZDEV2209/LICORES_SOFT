import modules.msg as msg
import modules.screenController as sc
def main():
    sc.deleteScreen()
    print(msg.MAIN_MENU)
    option = input("= ")
    match option:
        case"1":
            pass
        case"2":
            pass
        case"3":
            pass
        case"4":
            pass    
        case"5":
            pass
        case"6":            
            print("saliendo")
            pass
        case _:
            print(msg.VALID_ERROR)
            sc.pauseScreen()
            return main()
        
if __name__ =="__main__":
    main()
            