# manejando ficheros

# para el manejo de directorios
import os 

print(os.getcwd()) # get current working directory - directorio actual


# with open("output.txt", "w") as f: # queremos abrir archivo para escribir, si no existe lo crea
#     f.write("hola trón2!!")
with open("output.txt", "a") as f: # queremos abrir archivo para anadir, si no existe lo crea
    f.write("hola trón2!!")

with open("output.txt", "r") as f: # queremos abrir archivo para leer
    # s = f.readlines()    # leemos las líneas del archivo y las devolvemos cada línea en una lista
    s = f.read() # lee texto y devuelve líneas

# for line in s:
#     print (line)
print(s)

