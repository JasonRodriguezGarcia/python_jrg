#diccionarios = objetos en javascript
# archivos

# set  --> miSet = {1, 2, 3, 4}

# objeto
persona1 = {
    "nombre": "Juan",
    "edad": 21,
    "notas": [1, 2, 3, 4]
}

persona2 = {
    "nombre": "maria",
    "edad": 20,
    "notas": [10, 6, 7, 8]
}

print(persona1)

mySet = {3, 7, 6, 5, 2}  # esto es un set no un objeto
print(mySet) # los ordena, pero ojo con texto

personas = []
personas.append(persona1)
personas.append(persona2)

print(personas)

for persona in personas:
    print(persona["nombre"])