import os 
import json
from typing import Dict, List, Optional

DB_FILE = "data/dbmain.json"

#FUNCION PARA CARGAR LA BASE DE DATOS SE UTILIZA PARA REALIZAR FUNCIONES Y QUE ME RELACIONE LA INFORMACION CON LA BASE DE DATOS
def readJson(DB_FILE : str)->Dict:
    try:
        with open(DB_FILE, "r", encoding="utf-8") as cf:
            return json.load(cf)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
#FUNCION PARA QUE ME ESCRIBA Y ME MUESTRE LA BASE DE DATOS ES POSIBLE MODIFICAR QUE ESPACIOS PUEDO IMPRIMIR
def writeJson(DB_FILE : str, data : Dict)->Dict:
    with open(DB_FILE, "w", encoding="utf-8") as cf:
        json.dump(data, cf, indent=4)
#FUNCION QUE SE ENCARGA DE ACTUALIZAR LA BASE DE DATOS CON LOS VALORES QUE YO CONSIDERE
def updateJson(DB_FILE : str, data : Dict, path: Optional[List[str]] = None) -> None:
    currentData = readJson(DB_FILE)

    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    
    writeJson(DB_FILE, currentData)
#FUNCION PARA BORRAR ELEMENTOS DE LA BASE DE DATOS CON LOS VALORES QUE YO CONSIDERE
def deleteJson(DB_FILE: str,path: List[str])->bool:
    data = readJson(DB_FILE)
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(DB_FILE, data)
        return True
    return False
#ME INICIALIZA LA BASE DE DATOS, MAS PARA VALIDACIONES
def initializeJson(DB_FILE: str, initialStructure:Dict)->None:
    if not os.path.isfile(DB_FILE):
        writeJson(DB_FILE, initialStructure)
    else:
        currentData = readJson(DB_FILE)
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(DB_FILE, currentData)