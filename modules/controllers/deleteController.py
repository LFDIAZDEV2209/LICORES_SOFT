from config import DB_FILE
import modules.utils.corefiles as cf
import modules.screenController as sc
import modules.validateData as vd
from modules.msg import DELETE_MENU


def deleteController():
    sc.limpiar_pantalla()
    print(DELETE_MENU)
    option = input("= ")
    data = cf.readJson()

    match option:
        case "1":
            if "Beer" not in data or not data["Beer"]:
                print("NO HAY CERVEZAS PARA ELIMINAR")
                sc.pausar_pantalla()
                return deleteController()
            
            print("\n🍺 CERVEZAS DISPONIBLES:")
            for id, info in data["Beer"].items():
                print(f"ID: {id} - Nombre: {info['Nombre']}")
            
            id = input("Ingrese el ID de la cerveza a eliminar: ")

            if str(id) in data["Beer"]:
                if cf.deleteJson(["Beer", str(id)]):
                    print("🍺 Cerveza eliminada exitosamente.")
                else:
                    print("❌ No se pudo eliminar la cerveza.")
            else:
                print(f"⚠️ No se encontró una cerveza con el ID '{id}'.")

            sc.pausar_pantalla()
            return deleteController()
        case "2":
            if "Vino" not in data or not data["Vino"]:
                print("NO HAY VINOS PARA ELIMINAR")
                sc.pausar_pantalla()
                return deleteController()
            
            print("\n🍷 VINOS DISPONIBLES:")
            for id, info in data["Vino"].items():
                print(f"ID: {id} - Nombre: {info['Nombre']}")
            
            id = input("Ingrese el ID del vino a eliminar: ")
            
            if str(id) in data["Vino"]:
                if cf.deleteJson(["Vino", str(id)]):
                    print("🍷 Vino eliminado exitosamente.")
                else:
                    print("❌ No se pudo eliminar el vino.")
            else:
                print(f"⚠️ No se encontró un vino con el ID '{id}'.")

            sc.pausar_pantalla()
            return deleteController()
        case "3":
            if "Liquors" not in data or not data["Liquors"]:
                print("NO HAY LICORES PARA ELIMINAR")
                sc.pausar_pantalla()
                return deleteController()
            
            print("\n🥃 LICORES DISPONIBLES:")
            for id, info in data["Liquors"].items():
                print(f"ID: {id} - Nombre: {info['Nombre']}")
            
            id = input("Ingrese el ID del licor a eliminar: ")

            if str(id) in data["Liquors"]:
                if cf.deleteJson(["Liquors", str(id)]):
                    print("🥃 Licor eliminado exitosamente.")
                else:
                    print("❌ No se pudo eliminar el licor.")
            else:
                print(f"⚠️ No se encontró un licor con el ID '{id}'.")

            sc.pausar_pantalla()
            return deleteController()
        case "4":
            pass
        case _:
            print("⚠️ Opción no válida")
            sc.pausar_pantalla()
            return deleteController()
