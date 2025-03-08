import modules.screenController as sc
import modules.utils.corefiles as cf
import modules.validateData as vd
from typing import Dict, List, Optional
import modules.msg as msg
import json
from config import DB_FILE

def editMenu():
    sc.limpiar_pantalla()
    data = cf.readJson()
    print(msg.EDIT_MENU)
    option = input("= ")
    match option:
        case "1":
                sc.limpiar_pantalla()
                print(msg.EDIT_MENU)
                data = cf.readJson()  
                if not data["Beer"]:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()
                for id, info in data["Beer"].items():
                    print(f"ID: {id} - Nombre: {info['Nombre']}")

                id_buscado = input("Ingrese el ID del producto que desea editar:")
                encontrado = False
                categoria_encontrada = None
                producto_encontrado = None

                
                for categoria in data:
                    if categoria in data:  
                        if id_buscado in data[categoria]:  
                            producto_encontrado = data[categoria][id_buscado]
                            categoria_encontrada = categoria
                            encontrado = True
                            break

                if not encontrado:
                    print(f"No se encontró ningún producto con el ID {id_buscado}.")
                    sc.pausar_pantalla()
                    return

              
                print(f"Detalles actuales del producto (ID: {id_buscado}):")
                print(json.dumps(producto_encontrado, indent=4))

               
                print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")
                nuevo_nombre = vd.validatetext(f"Nuevo nombre ({producto_encontrado['Nombre']}): ") or producto_encontrado['Nombre']
                nuevo_ml = vd.validateInt(f"Nueva cantidad de ml ({producto_encontrado['ml']}): ") or producto_encontrado['ml']
                nuevo_costo = vd.validateInt(f"Nuevo costo ({producto_encontrado['Costo']}): ") or producto_encontrado['Costo']
                nuevo_precio_venta = vd.validateInt(f"Nuevo precio de venta ({producto_encontrado['precio de venta']}): ") or producto_encontrado['precio de venta']

                
                producto_encontrado["Nombre"] = nuevo_nombre
                producto_encontrado["ml"] = int(nuevo_ml)
                producto_encontrado["Costo"] = int(nuevo_costo)
                producto_encontrado["precio de venta"] = int(nuevo_precio_venta)

             
                data[categoria_encontrada][id_buscado] = producto_encontrado
                cf.updateJson(data)  

                print("\n¡Producto actualizado con éxito!")
                sc.pausar_pantalla()
                return editMenu()
        case "2":
                sc.limpiar_pantalla()
                print(msg.EDIT_MENU)
                data = cf.readJson()  
                if not data["Vino"]:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()
                for id, info in data["Vino"].items():
                    print(f"ID: {id} - Nombre: {info['Nombre']}")

                id_buscado = input("Ingrese el ID del producto que desea editar:")
                encontrado = False
                categoria_encontrada = None
                producto_encontrado = None

                
                for categoria in data:
                    if categoria in data:  
                        if id_buscado in data[categoria]:  
                            producto_encontrado = data[categoria][id_buscado]
                            categoria_encontrada = categoria
                            encontrado = True
                            break

                if not encontrado:
                    print(f"No se encontró ningún producto con el ID {id_buscado}.")
                    sc.pausar_pantalla()
                    return

              
                print(f"Detalles actuales del producto (ID: {id_buscado}):")
                print(json.dumps(producto_encontrado, indent=4))

               
                print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")
                nuevo_nombre = vd.validatetext(f"Nuevo nombre ({producto_encontrado['Nombre']}): ") or producto_encontrado['Nombre']
                nuevo_ml = vd.validateInt(f"Nueva cantidad de ml ({producto_encontrado['ml']}): ") or producto_encontrado['ml']
                nuevo_costo = vd.validateInt(f"Nuevo costo ({producto_encontrado['Costo']}): ") or producto_encontrado['Costo']
                nuevo_precio_venta = vd.validateInt(f"Nuevo precio de venta ({producto_encontrado['precio de venta']}): ") or producto_encontrado['precio de venta']


                
                producto_encontrado["Nombre"] = nuevo_nombre
                producto_encontrado["ml"] = int(nuevo_ml)
                producto_encontrado["Costo"] = int(nuevo_costo)
                producto_encontrado["precio de venta"] = int(nuevo_precio_venta)

             
                data[categoria_encontrada][id_buscado] = producto_encontrado
                cf.updateJson(data)  

                print("\n¡Producto actualizado con éxito!")
                sc.pausar_pantalla()
                return editMenu()
        case "3":
                sc.limpiar_pantalla()
                print(msg.EDIT_MENU)
                data = cf.readJson()  
                if not data["Liquors"]:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()
                for id, info in data["Liquors"].items():
                    print(f"ID: {id} - Nombre: {info['Nombre']}")

                id_buscado = input("Ingrese el ID del producto que desea editar:")
                encontrado = False
                categoria_encontrada = None
                producto_encontrado = None

                
                for categoria in data:
                    if categoria in data:  
                        if id_buscado in data[categoria]:  
                            producto_encontrado = data[categoria][id_buscado]
                            categoria_encontrada = categoria
                            encontrado = True
                            break

                if not encontrado:
                    print(f"No se encontró ningún producto con el ID {id_buscado}.")
                    sc.pausar_pantalla()
                    return

              
                print(f"Detalles actuales del producto (ID: {id_buscado}):")
                print(json.dumps(producto_encontrado, indent=4))

               
                print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")
                nuevo_nombre = vd.validatetext(f"Nuevo nombre ({producto_encontrado['Nombre']}): ") or producto_encontrado['Nombre']
                nuevo_ml = vd.validateInt(f"Nueva cantidad de ml ({producto_encontrado['ml']}): ") or producto_encontrado['ml']
                nuevo_costo = vd.validateInt(f"Nuevo costo ({producto_encontrado['Costo']}): ") or producto_encontrado['Costo']
                nuevo_precio_venta = vd.validateInt(f"Nuevo precio de venta ({producto_encontrado['precio de venta']}): ") or producto_encontrado['precio de venta']


                
                producto_encontrado["Nombre"] = nuevo_nombre
                producto_encontrado["ml"] = int(nuevo_ml)
                producto_encontrado["Costo"] = int(nuevo_costo)
                producto_encontrado["precio de venta"] = int(nuevo_precio_venta)

             
                data[categoria_encontrada][id_buscado] = producto_encontrado
                cf.updateJson(data)  

                print("\n¡Producto actualizado con éxito!")
                sc.pausar_pantalla()
                return editMenu()
        case "4":
            pass
        case _:
            print("Esta opcion no esta")
            sc.pausar_pantalla()
            return editMenu()
    