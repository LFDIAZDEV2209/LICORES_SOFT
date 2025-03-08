import modules.screenController as sc
import modules.utils.corefiles as cf
import modules.validateData as vd
from typing import Dict, List, Optional
import modules.msg as msg
import json
from config import DB_FILE



def seeMenu():
    sc.limpiar_pantalla()
    data = cf.readJson()
    print(msg.SEE_MENU)
    option = input("Escoge una opcion:")
           
    match option:
        case "1":
            sc.limpiar_pantalla()
            if not data:
                print("No hay productos para mostrar.")
                sc.pausar_pantalla()
                return

            print("=== TODOS LOS PRODUCTOS ===")
            for categoria, productos in data.items():
                print(f"\n--- {categoria} ---")
                for id_producto, detalles in productos.items():
                    print(f"ID: {id_producto}")
                    print(json.dumps(detalles, indent=4))
            sc.pausar_pantalla()
        case "2":
            sc.limpiar_pantalla()
            if not data:
                print("No hay datos para mostrar.")
                sc.pausar_pantalla()
                return
            todos_los_productos = []
            for categoria, productos in data.items():
                for id_producto, detalles in productos.items():
                    detalles["ID"] = id_producto  
                    detalles["Categoria"] = categoria  
                    todos_los_productos.append(detalles)

           
            todos_los_productos.sort(key=lambda x: x["Nombre"])

            print("=== PRODUCTOS EN ORDEN ALFABÉTICO ===")
            for producto in todos_los_productos:
                print(f"\nID: {producto['ID']} | Categoría: {producto['Categoria']}")
                print(json.dumps({k: v for k, v in producto.items() if k not in ["ID", "Categoria"]}, indent=4))
            sc.pausar_pantalla()
        case "3":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para mostrar.")
                sc.pausar_pantalla()
                return seeMenu()
            for categoria in ["Beer"]:
                if categoria in data:  
                    print(f"Producto encontrado en la categoría {categoria}:")
                    for id_producto, detalles in data[categoria].items():
                        
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
                            

            if not encontrado:
                print(f"No se encontró ningún producto.")

            sc.pausar_pantalla()
            return seeMenu()
        case "4":
            
            data = cf.readJson()  
            if not data:
                print("No hay datos para mostrar.")
                sc.pausar_pantalla()
                return seeMenu()
            for categoria in ["Vino"]:
                if categoria in data:  
                    print(f"Producto encontrado en la categoría {categoria}:")
                    for id_producto, detalles in data[categoria].items():
                        
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
            if not encontrado:
                print(f"No se encontró ningún producto.")

            sc.pausar_pantalla()
            return seeMenu()
        case "5":
            sc.limpiar_pantalla()
            data = cf.readJson()  
            if not data:
                print("No hay datos para mostrar.")
                sc.pausar_pantalla()
                return seeMenu()
            for categoria in ["Liquors"]:
                if categoria in data:  
                    print(f"Producto encontrado en la categoría {categoria}:")
                    for id_producto, detalles in data[categoria].items():
                        
                            
                            print(json.dumps(detalles, indent=4))
                            encontrado = True
            if not encontrado:
                print(f"No se encontró ningún producto.")

            sc.pausar_pantalla()
            return seeMenu()
        case _:
            print("Esta opcion no esta")
            sc.pausar_pantalla()
            return seeMenu()