import json
from funciones import mostrar_tareas, verif_num, guardar_tareas, cargar_tareas


print("Bienvenido al ToDoList")
tareas = cargar_tareas()
bucle = True



while bucle: 
    print("\n--- LISTA DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Marcar tarea como completada")
    print("0. Salir")
        
    opcion = input("Seleccione una opcion (0-4): ")

    if opcion == "1":
        titulo = input("ingrese el titulo: ")
        descripcion = input("ingrese descripcion: ")
        tarea = {"titulo": titulo, "descripcion" : descripcion, "completada" : False}
        tareas.append(tarea)
        guardar_tareas(tareas)
        print("tarea Agregada")
        
    
    elif opcion =="2" :
        
        if not tareas:
            print("no hay tareas para eliminar")
            continue
        
        mostrar_tareas(tareas)
        
        n = verif_num(input("ingrese el numero de la tarea a eliminar:"), len(tareas))
        
        if n is not None:
            tareas.pop(n - 1)
            guardar_tareas(tareas)
            print(f"tarea eliminada")
            
                    
         
    elif opcion == "3":
        mostrar_tareas(tareas)
    
    
    elif opcion == "4":
        mostrar_tareas(tareas)
        n = verif_num(input("ingrese el numero de la tarea completada:"), len(tareas))
        if n is not None:
            tareas[n-1]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea completada")
    
    elif opcion == "0":
        bucle = False
        print("hasta la proxima")
    
    else:
        print("opcion no valida")
        continue