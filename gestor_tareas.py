import json
import os

ARCHIVO_TAREAS = "tareas.json"

# Cargar tareas desde archivo
def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Guardar tareas en archivo
def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

# Agregar nueva tarea
def agregar_tarea(tareas):
    descripcion = input("Escribe la descripción de tu nueva tarea: ")
    tarea = {"descripcion": descripcion, "estado": "Pendiente"}
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea agregada. ¡Vamos sumando tareas por hacer!")

# Ver tareas
def ver_tareas(tareas):
    if not tareas:
        print("Parece que no hay nada en la lista. ¡Buen trabajo!")
        return
    print("\nLista de tareas:")
    for idx, tarea in enumerate(tareas):
        print(f"{idx + 1}. [{tarea['estado']}] {tarea['descripcion']}")

# Marcar tarea como completada
def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("¿Cuál tarea ya terminaste? Ingresa su número: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["estado"] = "Completada"
            guardar_tareas(tareas)
            print("¡Bien hecho! Tarea marcada como completada.")
        else:
            print("Ese número no corresponde a ninguna tarea.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Eliminar tarea
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("¿Qué tarea quieres eliminar? Ingresa su número: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            guardar_tareas(tareas)
            print("Tarea eliminada de la lista.")
        else:
            print("Ese número no está en la lista.")
    except ValueError:
        print("Entrada no válida. Intenta con un número.")

# Menú principal
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("¿Qué quieres hacer? Ingresa el número de opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Gracias por usar el gestor. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Elige un número del menú.")

if __name__ == "__main__":
    menu()
