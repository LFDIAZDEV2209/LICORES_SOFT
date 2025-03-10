from config import DB_FILE
import modules.msg as msg
import modules.validateData as vd
import modules.screenController as sc
import modules.utils.corefiles as cf
import random

def addMenu():
    sc.limpiar_pantalla()
    print(msg.ADD_MENU)
    option = input("= ")
    match option:
        case "1":
            while True:
                sc.limpiar_pantalla()
                idBeer = random.randint(1023, 9876)
                nomBeer = vd.validatetext("Ingrese el nombre de la cerveza: ")
                ml= vd.validateInt("Ingrese los ml: ")
                costBeer = vd.validateInt("Costo: ")
                priceBeer = vd.validateInt("Precio de venta: ")

                CERVEZA = {
                    idBeer:{
                    "Name":nomBeer,
                    "ml":ml,
                    "Cost":costBeer,
                    "Price":priceBeer

                    }
                }
                if not cf.updateJson(CERVEZA,["Beer"]):
                    print("Cerveza agregada exitosamente ✅")
                    cf.printTable("Beer", CERVEZA, idBeer)
                else:
                    print("No se pudo agregar la cerveza ❌ ")
                
                while True:
                    opcion = input("\n¿Desea agregar otra cerveza? (si/no): ").strip().lower()
                    if opcion == "si":
                        break  
                    elif opcion == "no":
                        sc.pausar_pantalla()
                        return addMenu()  
                    else:
                        print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

        case "2":
            while True:
                sc.limpiar_pantalla()
                idVino = random.randint(1023, 9876)
                nomVino = vd.validatetext("Ingrese el nombre del vino: ")
                mlVino= vd.validateInt("Ingrese los ml: ")
                costVino = vd.validateInt("Costo: ")
                priceVino = vd.validateInt("Precio de venta: ")

                VINO= {
                    idVino:{
                    "Name":nomVino,
                    "ml":mlVino,
                    "Cost":costVino,
                    "Price":priceVino

                    }
                }
                if not cf.updateJson(VINO,["Wine"]):
                    print("Vino agregado exitosamente ✅")
                    cf.printTable("Wine", VINO, idVino)
                else:
                    print("No se pudo agregar el vino ❌")
                while True:
                    opcion = input("\n¿Desea agregar otro vino? (si/no): ").strip().lower()
                    if opcion == "si":
                        break  
                    elif opcion == "no":
                        sc.pausar_pantalla()
                        return addMenu()  
                    else:
                        print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

        case "3":
            while True:
                sc.limpiar_pantalla()
                idLiquors = random.randint(1023, 9876)
                nomLiquors = vd.validatetext("Ingrese el nombre del licor: ")
                mlLiquors= vd.validateInt("Ingrese los ml: ")
                costLiquors = vd.validateInt("Costo: ")
                priceLiquors = vd.validateInt("Precio de venta: ")

                LICORES = {
                    idLiquors:{
                    "Name":nomLiquors,
                    "ml":mlLiquors,
                    "Cost":costLiquors,
                    "Price":priceLiquors

                    }
                }
                if not cf.updateJson(LICORES,["Liquors"]):
                    print("Licor agregado exitosamente ✅")
                    cf.printTable("Liquors", LICORES, idLiquors)
                else:
                    print("No se pudo agregar el licor ❌")
                while True:
                    opcion = input("\n¿Desea agregar otro licor? (si/no): ").strip().lower()
                    if opcion == "si":
                        break  
                    elif opcion == "no":
                        sc.pausar_pantalla()
                        return addMenu()  
                    else:
                        print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

        case "4":
            pass
        case _:
            print("Esta opcion no esta")
            sc.pausar_pantalla()
            return addMenu()
    


