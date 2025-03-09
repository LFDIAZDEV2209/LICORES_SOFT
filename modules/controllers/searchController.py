
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

            if not data or not data.get("Beer"):
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()

            encontrados = {}  

            for id_producto, detalles in data["Beer"].items():
                nombre_producto = detalles.get("Name", "").lower() 
                
                if filtro in nombre_producto:
                    encontrados[id_producto] = detalles

            if encontrados:
                print(f"\n📋 Productos encontrados con el filtro '{filtro}':\n")
                cf.printFilteredTable("Beer", encontrados) 
            else:
                print(f"⚠️ No se encontró ningún producto con el filtro '{filtro}'.")

            sc.pausar_pantalla()
            return searchMenu()
        
        case "2":
            sc.limpiar_pantalla()

            if not data or not data.get("Wine"):
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()

            encontrados = {}  

            for id_producto, detalles in data["Wine"].items():
                nombre_producto = detalles.get("Name", "").lower() 
                
                if filtro in nombre_producto:
                    encontrados[id_producto] = detalles

            if encontrados:
                print(f"\n📋 Productos encontrados con el filtro '{filtro}':\n")
                cf.printFilteredTable("Wine", encontrados) 
            else:
                print(f"⚠️ No se encontró ningún producto con el filtro '{filtro}'.")

            sc.pausar_pantalla()
            return searchMenu()
        
        case "3":
            sc.limpiar_pantalla()

            if not data or not data.get("Liquors"):
                print("No hay datos para buscar.")
                sc.pausar_pantalla()
                return searchMenu()

            filtro = input("Ingrese el nombre o parte del nombre del producto: ").strip().lower()

            encontrados = {}  

            for id_producto, detalles in data["Liquors"].items():
                nombre_producto = detalles.get("Name", "").lower() 
                
                if filtro in nombre_producto:
                    encontrados[id_producto] = detalles

            if encontrados:
                print(f"\n📋 Productos encontrados con el filtro '{filtro}':\n")
                cf.printFilteredTable("Liquors", encontrados) 
            else:
                print(f"⚠️ No se encontró ningún producto con el filtro '{filtro}'.")

            sc.pausar_pantalla()
            return searchMenu()
        
        case "4":
            pass

        case _:
            print("Opcion no disponible, intente nuevamente")
            sc.pausar_pantalla()
            return searchMenu()
    