import json

import os


ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if os.path.exits(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r") as f:
        return json.load(f)
    

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)




def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Salir")



def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            descripcion = input("Descripcion de la tarea: ")
            #Se crea un diccionario para almacenar la tarea
            nueva_tarea = {
                "id": len(tareas)+1,
                "descripcion": descripcion,
                "completada": False

            }
            tareas.append(nueva_tarea)
            guardar_tareas(tareas)

            print("Tarea agregada")

            
        if opcion == "2":
            if not tareas:
                print("No hay tareas registradas")
            else:
                for t in tareas:
                    estado = "✅" if t["completada"] else "❌"
                    print(f"{t["id"]}. {t["descripcion"]} [{estado}]")




        if opcion == "3":
            print("Completar las tareas")
        if opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opcion invalida intenta de nuevo")

