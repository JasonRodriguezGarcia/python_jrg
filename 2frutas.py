frutas = ["kiwi", "mango", "manzana", "platano", "Melocotón"]

# list comprehension, parecido al filter
# longitud fruta >5
#devolver en fruta en mayúsculas

filtrado = [fruta.upper() for fruta in frutas if len(fruta)>5]

print(filtrado)

frutas.reverse() # ojo mayúsculas, orden según ASCII
print(frutas)

