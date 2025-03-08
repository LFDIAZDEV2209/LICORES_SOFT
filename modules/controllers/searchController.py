
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
    option = input("= ")
    match option:
        case "1":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()
            if not data["Beer"]:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()

            encontrado = False  
            print(f"Productos encontrados con el filtro {filtro}:")
            for id_producto, detalles in data["Beer"].items():
                
                nombre_producto = detalles.get("Nombre", "").lower()
                if filtro in nombre_producto:
                            
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            

            if not encontrado:
                print(f"No se encontró ningún producto con el filtro {filtro}.")

            sc.pausar_pantalla()
            return searchMenu()

            
        case "2":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()
            if not data["Vino"]:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()

            encontrado = False  
            print(f"Productos encontrados con el filtro {filtro}:")
            for id_producto, detalles in data["Vino"].items():
                        nombre_producto = detalles.get("Nombre", "").lower()
                        if filtro in nombre_producto:
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            

            if not encontrado:
                print(f"No se encontró ningún producto con el filtro {filtro}.")

            sc.pausar_pantalla()
            return searchMenu()
        case "3":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()
            if not data["Liquors"]:
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()
            encontrado = False  
            print(f"Productos encontrados con el filtro {filtro}:")
            for id_producto, detalles in data["Liquors"].items():
                        nombre_producto = detalles.get("Nombre", "").lower()
                        if filtro in nombre_producto:
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            

            if not encontrado:
                print(f"No se encontró ningún producto con el filtro {filtro}.")

            sc.pausar_pantalla()
            return searchMenu()
        case _:
            pass
    