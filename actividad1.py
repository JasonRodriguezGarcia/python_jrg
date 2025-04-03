# En Este juego interactivo de personalidad, el usuario responderá algunas preguntas sobre su nombre, edad, 
# altura y sus gustos en programación. El programa utiliza diferentes tipos de datos como cadenas de texto 
# (str), enteros (int), flotantes (float) y booleanos (bool) para recoger y procesar la información. Al final, 
# el programa genera un mensaje personalizado y divertido basado en las respuestas del usuario.

# Por ejemplo: output : 'Hola Juan. Veo que tienes 18 años, mides 176 centimétros, y no te gusta la programacion.'

nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
altura = float(input("Introduce tu altura en cms: "))
programacion = input("Te gusta la progamacion (si/no): ")

print(type(programacion))
if programacion == "si":
    leGusta = True
else:
    leGusta = False
print(f"Hola {nombre}. Veo que tienes {edad} años, mides {altura}cms y {"sí" if leGusta else "no"} te gusta la programación")
fraseAdicional = ""
if nombre == "Nadal":
    fraseAdicional += "Yo Soy tu fan nº1 !!"
elif nombre == "Alcaraz":
    fraseAdicional += "Juegas un poco 'regu' !!"
elif nombre == "Badosa":
    fraseAdicional += "Te has lesionado hace poco !!"
elif nombre == "Muguruza":
    fraseAdicional += "Tienes tus altibajos !!"
else:
    fraseAdicional += "Ere un looser !!"

print(fraseAdicional)


# if (var1 or var2):
#     print("test1")
# elif (var1 and bool2):
#     print("test2")