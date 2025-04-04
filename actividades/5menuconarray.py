# Completar esta aplicacion para la gestión de páginas webs
# while True:
#     print("\n--- Gestor de páginas webs - Menú ---")
#     print("1. Añadir página web")
#     print("2. Ver todas las páginas web")
#     print("3. Salir")
    
#     opcion = input("Selecciona una opción (1-3): ")

import os
#borrar pantalla
import time

paginasWeb = []
while True:
    os.system("cls") #clear en linux
    print(f"\n--- Gestor de páginas webs - Menú ---  Páginas [{len(paginasWeb)}]")
    print("1. Añadir página web")
    print("2. Ver todas las páginas web")
    print("3. Borrar página web")
    print("4. Salir")
    
    opcion = int(input("Selecciona una opción (1-3): "))

    if opcion == 1:
        nueva = input("Introduce pagina web: ")
        paginasWeb.append(nueva)
    if opcion == 2:
        for i in paginasWeb:
            print(i)
        time.sleep(2)
    
    if opcion == 3:
        for i in paginasWeb:
            print(i)
        borrar = input("Introduce página a borrar: ")
        if borrar in paginasWeb:
            paginasWeb.remove(borrar)
        else:
            print("página no encontrada")
    if opcion == 4:
        break
