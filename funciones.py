import json


# FUNCIONES DATA JSON
def cargar_tareas(arch_json = "data.json"):
    try:
        with open(arch_json, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("archivo no encontrado")
        return []
    except json.JSONDecodeError:
        print("Error al cargar el archivo")
        return []


def guardar_tareas(tareas: list, arch_json: str = "data.json"):
    with open(arch_json, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)


# FUNCIONES APP
def mostrar_tareas(n):
    if not n:
        print("no hay tareas para mostrar")
        return 
    
    print("TAREAS: ")
    for i,tarea in enumerate(n, start=1):
        print(f'{i}: {tarea["titulo"]}')

def verif_num(x, b):
    try:
        idx = int(x.strip())
    except ValueError:
        print("Debe ingresar un número entero.")
        return None
    
    if 1 <= idx <= b:
        return idx
    else:
        print(f"Número fuera de rango.")
        return None
                    