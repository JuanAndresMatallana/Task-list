import json

import os


ARCHIVO_TAREAS = "tareas.json"

def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
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
    print("6. Editar tarea")



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

            
        elif opcion == "2":
            if not tareas:
                print("No hay tareas registradas")
            else:
                
                pendientes = [t for t in tareas if not t["completada"]]
                completadas = [t for t in tareas if t["completada"]]

                print("\n Tareas pendientes:")

                if pendientes:
                    for t in pendientes:
                        print(f'{t["id"]}. {t["descripcion"]} [❌]')
                else:
                    print("No hay tareas pendientes")

                print("\n Tareas completadas")

                completadas = [t for t in tareas if t["completada"]]

                if completadas:
                    for  t in completadas:
                        print(f'{t["id"]}. {t["descripcion"]} [✅]')

                else:
                    print("No hay tareas completadas")

                print("\n---Resumen---")
                print(f"Pendientes: {len(pendientes)} | Completadas: {len(completadas)} | Total: {len(tareas)}")



        elif opcion == "3":
            id_tarea = int(input("Por favor ingrese el ID de la tarjeta a completar: "))
            for t in tareas:
                if t["id"] == id_tarea:
                    t["completada"] = True
                    guardar_tareas(tareas)
                    print("La tarea ha sido completada")
                    break
            else:
                print("Tarea no encontrada")
        elif opcion == "4":
            print("Saliendo del programa")
            break

        elif opcion == "5":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            #se crea una nueva lista sin el elemento que el usuario desea eliminar
            nueva_lista = [t for t in tareas if t["id"] != id_tarea]

            if len(nueva_lista) != len(tareas):
                
                for i, tarea in enumerate(nueva_lista, start=1):
                    tarea["id"] = i
                
                tareas = nueva_lista
                guardar_tareas(tareas)
                print("Tarea eliminada y ID ordenados")


        elif opcion == "6":
            id_tarea = int(input("ID de la tarea a editar: "))
            for t in tareas:
                if t["id"] == id_tarea:
                    print(f"Descripcion actual: {t['descripcion']}")
                    nueva_desc = input("Nueva descripcion: ").strip()
                    if nueva_desc:
                        t["descripcion"] = nueva_desc
                        guardar_tareas(tareas)
                        print("Tarea actualizada con exito")
                    else:
                        print("No se realizo ningun cambio")
                        break
            else:
                print("No se encontro ninguna tarea con ese ID")
        else:
            print("Opcion invalida intenta de nuevo")


if __name__ == "__main__":
    main()