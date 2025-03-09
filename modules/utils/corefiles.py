import os 
import json
from typing import Dict, List, Optional
from config import DB_FILE
from tabulate import tabulate



#FUNCION PARA CARGAR LA BASE DE DATOS SE UTILIZA PARA REALIZAR FUNCIONES Y QUE ME RELACIONE LA INFORMACION CON LA BASE DE DATOS
def readJson()->Dict:
    try:
        with open(DB_FILE, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
#FUNCION PARA QUE ME ESCRIBA Y ME MUESTRE LA BASE DE DATOS ES POSIBLE MODIFICAR QUE ESPACIOS PUEDO IMPRIMIR
def writeJson(data : Dict)->Dict:
    with open(DB_FILE, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)
#FUNCION QUE SE ENCARGA DE ACTUALIZAR LA BASE DE DATOS CON LOS VALORES QUE YO CONSIDERE
def updateJson(data : Dict, path: Optional[List[str]] = None) -> None:
    currentData = readJson()

    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    
    writeJson(currentData)
#FUNCION PARA BORRAR ELEMENTOS DE LA BASE DE DATOS CON LOS VALORES QUE YO CONSIDERE
def deleteJson(path: List[str])->bool:
    data = readJson()
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(data)
        return True
    return False
#ME INICIALIZA LA BASE DE DATOS, MAS PARA VALIDACIONES
def initializeJson(initialStructure:Dict)->None:
    if not os.path.isfile(DB_FILE):
        writeJson(initialStructure)
    else:
        currentData = readJson()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData)

def printTable(category: str, product: Dict, product_id: int) -> None:
    table = [[product_id, product[product_id].get("Name", "N/A"), product[product_id].get("ml", "N/A"), 
              product[product_id].get("Cost", "N/A"), product[product_id].get("Price", "N/A")]]
    headers = ["ID", "Name", "ml", "Cost", "Price"]
    
    print(f"\n📋 ÚLTIMA MODIFICACIÓN EN {category.upper()}:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

def printFilteredTable(category: str, products: Dict[int, Dict]) -> None:
    """
    Imprime una tabla con los productos filtrados.
    """
    if not products:
        print(f"\n⚠️ No se encontraron productos en {category}.")
        return

    headers = ["ID", "Name", "ml", "Cost", "Price"]
    table = [
        [id_producto, detalles.get("Name", "N/A"), detalles.get("ml", "N/A"), 
         detalles.get("Cost", "N/A"), detalles.get("Price", "N/A")]
        for id_producto, detalles in products.items()
    ]

    print(f"\n📋 PRODUCTOS FILTRADOS EN {category.upper()}:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

def show_products_by_category(data, category):
    """ Muestra los productos de una categoría específica en tabla. """
    if not data or category not in data or not data[category]:
        print(f"No hay productos en la categoría {category}.")
        return

    productos_tabla = []
    for id_producto, detalles in data[category].items():
        productos_tabla.append([
            id_producto,
            detalles.get("Name", "N/A"),
            detalles.get("ml", "N/A"),
            detalles.get("Cost", "N/A"),
            detalles.get("Price", "N/A")
        ])

    print(f"=== PRODUCTOS EN CATEGORÍA {category.upper()} ===")
    print(tabulate(productos_tabla, headers=["ID", "Nombre", "ML", "Costo", "Precio"], tablefmt="grid"))