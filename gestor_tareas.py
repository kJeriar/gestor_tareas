# gestor_tareas.py

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
    descripcion = input("Descripción de la nueva tarea: ")
    tarea = {"descripcion": descripcion, "estado": "Pendiente"}
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada correctamente.")

# Ver tareas
def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return
    for idx, tarea in enumerate(tareas):
        print(f"{idx + 1}. [{tarea['estado']}] {tarea['descripcion']}")

# Marcar tarea como completada
def marcar_completada(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Número de la tarea a marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["estado"] = "Completada"
            guardar_tareas(tareas)
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Entrada no válida.")

# Eliminar tarea
def eliminar_tarea(tareas):
    ver_tareas(tareas)
    try:
        indice = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            guardar_tareas(tareas)
            print("🗑️ Tarea eliminada.")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Entrada no válida.")

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
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
