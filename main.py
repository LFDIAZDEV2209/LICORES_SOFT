import modules.msg as msg
def main():
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
            return main()
        
if __name__ =="__main__":
    main()
            