# practicando bucles

for i in range(10):
    print(i)

x = range(10)
print(type(x))


for i in range(10, 30): # segundo parámetro rango final
    print(f"SEgundo for: {i}")

for i in range(10, 30, 2): # tercer parámetro Step (salto)
    print(f"Tercer FOR: {i}")

MAX_ITEMS = 2 # PONEMOS EN MAYUSCULAS PARA IDENTIFICAR CONSTANTES, AUNQUE ES UNA VARIABLE NORMAL
for _ in range(MAX_ITEMS): # _ se podría imprimir pero se pone así porque no es relevante el imprimirlo
    print(f"MAX_ITEMS")

for i in range(10, 1, -1):
    print(f"cuenta atrás: {i}")

