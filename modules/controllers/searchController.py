
import modules.screenController as sc
import modules.utils.corefiles as cf
import modules.validateData as vd
from typing import Dict, List, Optional
import modules.msg as msg
import json
from config import DB_FILE

def searchMenu():
    sc.limpiar_pantalla()
    data = cf.readJson()
    print(msg.SEARCH_MENU) 
    option = input("Escoge una opcion:")
    match option:
        case "1":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            id_buscado = input("Ingrese el ID del producto que desea buscar:")
            encontrado = False
            for categoria in ["Beer"]:
                if categoria in data:  
                    for id_producto, detalles in data[categoria].items():
                        if id_buscado == id_producto:
                            print(f"Producto encontrado en la categoría {categoria}:")
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            break

            if not encontrado:
                print(f"No se encontró ningún producto con el ID {id_buscado}.")

            sc.pausar_pantalla()
            return searchMenu()
            
        case "2":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            id_buscado = input("Ingrese el ID del producto que desea buscar:")
            encontrado = False
            for categoria in ["Vino"]:
                if categoria in data:  
                    for id_producto, detalles in data[categoria].items():
                        if id_buscado == id_producto:
                            print(f"Producto encontrado en la categoría {categoria}:")
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            break

            if not encontrado:
                print(f"No se encontró ningún producto con el ID {id_buscado}.")

            sc.pausar_pantalla()
            return searchMenu()
        case "3":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            id_buscado = input("Ingrese el ID del producto que desea buscar:")
            encontrado = False
            for categoria in ["Liquors"]:
                if categoria in data:  
                    for id_producto, detalles in data[categoria].items():
                        if id_buscado == id_producto:
                            print(f"Producto encontrado en la categoría {categoria}:")
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            break

            if not encontrado:
                print(f"No se encontró ningún producto con el ID {id_buscado}.")

            sc.pausar_pantalla()
            return searchMenu()
        case _:
            pass
    