from config import DB_FILE
import modules.msg as msg
import modules.validateData as vd
import modules.screenController as sc
import modules.utils.corefiles as cf
import random

def addMenu():
    sc.limpiar_pantalla()
    print(msg.ADD_MENU)
    option = input("Escoja una opcion:")
    match option:
        case "1":
            sc.limpiar_pantalla()
            idBeer = random.randint(1023, 9876)
            nomBeer = vd.validatetext("Ingrese el nombre de la cerveza🍺:")
            ml= vd.validateInt("Ingrese la caltida de mililitros de la cerveza🍺:")
            costBeer = vd.validateInt("Costo de la cerveza🍺:")
            priceBeer = vd.validateInt("Precio de venta de la cerveza🍺:")

            CERVEZA = {
                idBeer:{
                "Nombre":nomBeer,
                "ml":ml,
                "Costo":costBeer,
                "precio de venta":priceBeer

                }
            }
            cf.updateJson(CERVEZA,["Beer"])
            return addMenu()
        case "2":
            sc.limpiar_pantalla()
            idVino = random.randint(1023, 9876)
            nomVino = vd.validatetext("Ingrese el nombre del vino🍷:")
            mlVino= vd.validateInt("Ingrese la caltida de mililitros del vino🍷:")
            costVino = vd.validateInt("Costo del vino🍷:")
            priceVino = vd.validateInt("Precio de venta del vino🍷:")

            VINO= {
                idVino:{
                "Nombre":nomVino,
                "ml":mlVino,
                "Costo":costVino,
                "precio de venta":priceVino

                }
            }
            cf.updateJson(VINO,["Vino"])
            return addMenu()
        case "3":
            sc.limpiar_pantalla()
            idLiquors = random.randint(1023, 9876)
            nomLiquors = vd.validatetext("Ingrese el nombre del licor🥃:")
            mlLiquors= vd.validateInt("Ingrese la caltida de mililitros del licor🥃:")
            costLiquors = vd.validateInt("Costo del licor🥃:")
            priceLiquors = vd.validateInt("Precio de venta del licor🥃:")

            LICORES = {
                idLiquors:{
                "Nombre":nomLiquors,
                "ml":mlLiquors,
                "Costo":costLiquors,
                "precio de venta":priceLiquors

                }
            }
            cf.updateJson(LICORES,["Liquors"])
            return addMenu()
        case "4":
            pass
        case _:
            print("Esta opcion no esta")
            sc.pausar_pantalla()
            return addMenu()
    


