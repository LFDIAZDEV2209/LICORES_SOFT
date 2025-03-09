import modules.screenController as sc
import modules.utils.corefiles as cf
import modules.validateData as vd
from typing import Dict, List, Optional
import modules.msg as msg
import json
from config import DB_FILE
from tabulate import tabulate



def seeMenu():
    sc.limpiar_pantalla()
    data = cf.readJson()
    print(msg.SEE_MENU)
    option = input("= ")
           
    match option:
        case "1":
            sc.limpiar_pantalla()

            if not data:
                print("No hay productos para mostrar.")
                return seeMenu()

            productos_tabla = []
            for categoria, productos in data.items():
                for id_producto, detalles in productos.items():
                    productos_tabla.append([
                        id_producto,
                        categoria,
                        detalles.get("Name", "N/A"),
                        detalles.get("ml", "N/A"),
                        detalles.get("Cost", "N/A"),
                        detalles.get("Price", "N/A")
                    ])

            if productos_tabla:
                print("=== TODOS LOS PRODUCTOS ===")
                print(tabulate(productos_tabla, headers=["ID", "Categoría", "Nombre", "ML", "Costo", "Precio"], tablefmt="grid"))
            else:
                print("No hay productos disponibles.")
            sc.pausar_pantalla()
            return seeMenu()
        case "2":
            sc.limpiar_pantalla()
            if not data:
                print("No hay productos para mostrar.")
                return

            productos_tabla = []
            for categoria, productos in data.items():
                for id_producto, detalles in productos.items():
                    productos_tabla.append([
                        id_producto,
                        categoria,
                        detalles.get("Name", "N/A"),
                        detalles.get("ml", "N/A"),
                        detalles.get("Cost", "N/A"),
                        detalles.get("Price", "N/A")
                    ])

            productos_tabla.sort(key=lambda x: x[2])  

            if productos_tabla:
                print("=== PRODUCTOS EN ORDEN ALFABÉTICO ===")
                print(tabulate(productos_tabla, headers=["ID", "Categoría", "Nombre", "ML", "Costo", "Precio"], tablefmt="grid"))
            else:
                print("No hay productos disponibles.")
            sc.pausar_pantalla()
            return seeMenu()
        case "3":
            sc.limpiar_pantalla()
            cf.show_products_by_category(data, "Beer")
            sc.pausar_pantalla()
            return seeMenu()
        case "4":
            sc.limpiar_pantalla()
            cf.show_products_by_category(data, "Wine")
            sc.pausar_pantalla()
            return seeMenu()
        case "5":
            sc.limpiar_pantalla()
            cf.show_products_by_category(data, "Liquors")
            sc.pausar_pantalla()
            return seeMenu()
        case "6":
            pass
        case _:
            print("Opcion no disponible, intente nuevamente")
            sc.pausar_pantalla()
            return seeMenu()