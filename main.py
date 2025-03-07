import modules.msg as msg 
import modules.screenController as sc

def main(): 
    sc.limpiar_pantalla() 
    print(msg.MAIN_MENU) 
    option = input("= ") 
    match option:
        case "1":          
            pass
        case "2":
            pass
            return main()
        case "3":
            pass
            return main()
        case "4":
            pass
            return main()
        case "5":
            pass
            return main()
        case "6":
            pass
            return main()
        case "8":
            print("Saliendo...")
            pass
        case _:
            print("ERROR, INTENTE NUEVAMENTE")
            sc.pausar_pantalla()
            return main()
            
if __name__ == "__main__":
    main()
    