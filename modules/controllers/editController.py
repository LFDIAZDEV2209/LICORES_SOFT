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
            while True:
                sc.limpiar_pantalla()
                if not data["Beer"] or not data:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()

                for id, info in data["Beer"].items():
                    print(f"ID: {id} - Nombre: {info['Name']}")

                id = input("Ingrese el ID del producto que desea editar:")

                if str(id) in data["Beer"]:
                    cerveza_actual = data["Beer"][str(id)] 
                    print("\n🔹 Presiona ENTER para mantener el valor actual.")

                    nomBeer = input(f"Ingrese el nuevo nombre de la cerveza ({cerveza_actual['Name']}): ").strip() or cerveza_actual["Name"]
                    ml = input(f"Ingrese los nuevos ml ({cerveza_actual['ml']}): ").strip()
                    costBeer = input(f"Nuevo costo ({cerveza_actual['Cost']}): ").strip()
                    priceBeer = input(f"Nuevo precio de venta ({cerveza_actual['Price']}): ").strip()

                    ml = int(ml) if ml.isdigit() else cerveza_actual["ml"]
                    costBeer = int(costBeer) if costBeer.isdigit() else cerveza_actual["Cost"]
                    priceBeer = int(priceBeer) if priceBeer.isdigit() else cerveza_actual["Price"]

                    CERVEZA = {
                        id: {
                            "Name": nomBeer,
                            "ml": ml,
                            "Cost": costBeer,
                            "Price": priceBeer
                        }
                    }

                    if not cf.updateJson(CERVEZA, ["Beer"]):
                        print("Cerveza editada exitosamente ✅")
                        cf.printTable("Beer", CERVEZA, id)
                    else:
                        print("No se pudo editar la cerveza ❌")

                    while True:
                        opcion = input("\n¿Desea editar otra cerveza? (si/no): ").strip().lower()
                        if opcion == "si":
                            break  
                        elif opcion == "no":
                            sc.pausar_pantalla()
                            return editMenu()  
                        else:
                            print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

                else:
                    print(f"⚠️ No se encontró una cerveza con el ID '{id}'.")
                    sc.pausar_pantalla()
                    return editMenu()
        case "2":
            while True:
                sc.limpiar_pantalla()
                if not data["Wine"] or not data:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()

                for id, info in data["Wine"].items():
                    print(f"ID: {id} - Nombre: {info['Name']}")

                id = input("Ingrese el ID del producto que desea editar:")

                if str(id) in data["Wine"]:
                    wine_actual = data["Wine"][str(id)] 
                    print("\n🔹 Presiona ENTER para mantener el valor actual.")

                    nomWine = input(f"Ingrese el nuevo nombre de la cerveza ({wine_actual['Name']}): ").strip() or wine_actual["Name"]
                    ml = input(f"Ingrese los nuevos ml ({wine_actual['ml']}): ").strip()
                    costWine = input(f"Nuevo costo ({wine_actual['Cost']}): ").strip()
                    priceWine = input(f"Nuevo precio de venta ({wine_actual['Price']}): ").strip()

                    ml = int(ml) if ml.isdigit() else wine_actual["ml"]
                    costWine = int(costWine) if costWine.isdigit() else wine_actual["Cost"]
                    priceWine = int(priceWine) if priceWine.isdigit() else wine_actual["Price"]

                    WINE = {
                        id: {
                            "Name": nomWine,
                            "ml": ml,
                            "Cost": costWine,
                            "Price": priceWine
                        }
                    }

                    if not cf.updateJson(WINE, ["Wine"]):
                        print("Cerveza editada exitosamente ✅")
                        cf.printTable("Wine", WINE, id)
                    else:
                        print("No se pudo editar la cerveza ❌")

                    while True:
                        opcion = input("\n¿Desea editar otra cerveza? (si/no): ").strip().lower()
                        if opcion == "si":
                            break  
                        elif opcion == "no":
                            sc.pausar_pantalla()
                            return editMenu()  
                        else:
                            print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

                else:
                    print(f"⚠️ No se encontró una cerveza con el ID '{id}'.")
                    sc.pausar_pantalla()
                    return editMenu()
        case "3":
            while True:
                sc.limpiar_pantalla()
                if not data["Liquors"] or not data:
                    print("No hay datos para editar.")
                    sc.pausar_pantalla()
                    return editMenu()

                for id, info in data["Liquors"].items():
                    print(f"ID: {id} - Nombre: {info['Name']}")

                id = input("Ingrese el ID del producto que desea editar:")

                if str(id) in data["Liquors"]:
                    liquor_actual = data["Liquors"][str(id)] 
                    print("\n🔹 Presiona ENTER para mantener el valor actual.")

                    nomLiquors = input(f"Ingrese el nuevo nombre de la cerveza ({liquor_actual['Name']}): ").strip() or liquor_actual["Name"]
                    ml = input(f"Ingrese los nuevos ml ({liquor_actual['ml']}): ").strip()
                    costLiquors = input(f"Nuevo costo ({liquor_actual['Cost']}): ").strip()
                    priceLiquors = input(f"Nuevo precio de venta ({liquor_actual['Price']}): ").strip()

                    ml = int(ml) if ml.isdigit() else liquor_actual["ml"]
                    costLiquors = int(costLiquors) if costLiquors.isdigit() else liquor_actual["Cost"]
                    priceLiquors = int(priceLiquors) if priceLiquors.isdigit() else liquor_actual["Price"]

                    LIQUORS = {
                        id: {
                            "Name": nomLiquors,
                            "ml": ml,
                            "Cost": costLiquors,
                            "Price": priceLiquors
                        }
                    }

                    if not cf.updateJson(LIQUORS, ["Liquors"]):
                        print("Cerveza editada exitosamente ✅")
                        cf.printTable("Liquors", LIQUORS, id)
                    else:
                        print("No se pudo editar la cerveza ❌")

                    while True:
                        opcion = input("\n¿Desea editar otra cerveza? (si/no): ").strip().lower()
                        if opcion == "si":
                            break  
                        elif opcion == "no":
                            sc.pausar_pantalla()
                            return editMenu()  
                        else:
                            print("⚠️ Respuesta inválida. Por favor, ingrese 'si' o 'no'.")

                else:
                    print(f"⚠️ No se encontró una cerveza con el ID '{id}'.")
                    sc.pausar_pantalla()
                    return editMenu()
        case "4":
            pass
        case _:
            print("Esta opcion no esta")
            sc.pausar_pantalla()
            return editMenu()
    