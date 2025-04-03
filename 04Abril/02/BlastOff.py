import time

# Blast Off! Crear un programa en Python que haga una cuenta regresiva desde 10 hasta 1, y luego 
# imprima el mensaje "¡Despegue!" al final, simulando el lanzamiento de un cohete al espacio. Usar
# el módulo time para que cuente más lento.

for i in range(10, 0, -1):
    print(f"{i} ...")
    time.sleep(1)

print("IGNITION ...!!!")
