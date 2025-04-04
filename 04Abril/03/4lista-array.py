# arrays son listas en python

frutas = ["kiwis", "mangos", "plátanos", True, 10]

print(frutas[2])

# añadir a una lista (osea array) in python
frutas.append("manzana")
frutas.append("manzana")
print(f"Longitud frutas: {len(frutas)}")

for f in frutas:
    print(f)

frutas.remove("manzana") # si está repetido solo borrar el primero

for f in frutas:
    print(f)

# tupla con (), es inmutable
frutas2 = ("naranja", "melocotón", "uvas", True, 10)
