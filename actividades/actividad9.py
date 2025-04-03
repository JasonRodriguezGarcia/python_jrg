# Podrias terminar este programa usando un diccionario para gestionar los contactos:

# libro_de_contactos = [] # se guardará cada contacto como un diccionario dentro una lista


# def main():
#     while True:
#         print("\nMenú del Libro de Contactos:")
#         print("1. Agregar Contacto")
#         print("2. Ver Todos los Contactos")
#         print("3. Salir")
        
#         opcion = input("Elige una opción (1-3): ")
        
#         if opcion == "1":
#             agregar_contacto()
#             # pista: hay que usar libro_de_contactos.append()
#         elif opcion == "2":
#             ver_todos_los_contactos()
#         elif opcion == "3":
#             print("¡Adiós!")
#             break
#         else:
#             print("Opción no válida, por favor intenta de nuevo.")


libro_de_contactos = [] # se guardará cada contacto como un diccionario dentro una lista
ARCHIVO = "contactos.txt"

def agregar_contacto(nuevoContacto = ""):
    libro_de_contactos.append(nuevoContacto)

def ver_todos_los_contactos():
    for contacto in libro_de_contactos:
        print(f"-- Nombre: {contacto["nombre"]} Teléfono: {contacto["telefono"]}")

def guardar_permanente():
    resultado = ""
    for contacto in libro_de_contactos:
        resultado = resultado + 'contacto: '+ contacto["nombre"] + ", " + 'telefono: ' + contacto["telefono"] + '\n'
    with open(ARCHIVO, "a") as f: # queremos abrir archivo para anadir, si no existe lo crea
        f.writelines(resultado)


def main():
    while True:
        print("\nMenú del Libro de Contactos:")
        print("1. Agregar Contacto")
        print("2. Ver Todos los Contactos")
        print("3. Guarda y Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            nombre = input("Introduce contacto: ")
            telefono = input("Introduce teléfono: ")
            nuevoContacto = {}
            nuevoContacto["nombre"] = nombre
            nuevoContacto["telefono"] = telefono
            # nuevoContacto = {"nombre" : nombre, "telefono" : telefono}

            agregar_contacto(nuevoContacto)
            # pista: hay que usar libro_de_contactos.append()
        elif opcion == "2":
            ver_todos_los_contactos()
        elif opcion == "3":
            guardar_permanente()
            print("¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

main()