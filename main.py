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
    print("5. Eliminar tarea")



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
                print("\n Tareas pendientes")
                pendientes = [t for t in tareas if not t["completada"]]

                if pendientes:
                    for t in pendientes:
                        print(f"{t["id"]}. {t["descripcion"]} [❌]")
                else:
                    print("No hay tareas pendientes")

                print("\n Tareas completadas")

                completadas = [t for t in tareas if t["completada"]]

                if completadas:
                    for  t in completadas:
                        print(f"{t["id"]}. {t["descripcion"]} [✅]")

                else:
                    print("No hay tareas completadas")

        if opcion == "3":
            id_tarea = input("Por favor ingrese el ID de la tarjeta a completar")
            for t in tareas:
                if t["id"] == id_tarea:
                    t["completada"] = True
                    guardar_tareas(tareas)
                    print("La tarea ha sido completada")
                    break
                else:
                    print("Tarea no encontrada")
        if opcion == "4":
            print("Saliendo del programa")
            break

        elif opcion == "5":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            #se crea una nueva lista sin el elemento que el usuario desea eliminar
            nueva_lista = [t for t in tareas if t["id"] != id_tarea]

            if len(nueva_lista) == len(tareas):
                tareas = nueva_lista
                guardar_tareas(tareas)
                print("Tarea eliminada con exito")

        else:
            print("Opcion invalida intenta de nuevo")


if __name__ == "__main__":
    main()