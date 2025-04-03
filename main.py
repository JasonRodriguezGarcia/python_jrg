print("Hola Youseff, cómo etámo?")
print("Llo vién")
edad = int(input("Cuántos años tienes si es indiscreto? "))
# print("Hola Pepe. Tienes"+edad*5+"años  <---mal")
print(f"Hola Pepe. Tienes {edad} años") # para insertar variables {}

nombre = "Pepe"
print(nombre)
print(type(nombre))
altura = 120
print(type(altura))
isLoggedIn = True
peso = 56.7
print(type(isLoggedIn))
print(type(peso))

# procesar datos
edad = edad + 5

if edad >= 21:
    print("Eres viejo")   # indent 4 spaces
    print("Dentro")
else:
    print("Eres JOVEN")
print("fuera")

if edad < 10:
    print("eres Joven")
elif edad <20:
    print("Eres no tan joven")
elif edad <40:
    print("Eres viejuno")
else:
    print("Jubilaoo")