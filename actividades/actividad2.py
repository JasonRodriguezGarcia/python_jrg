import sys

#mostrar version de python y algún detalle más

print(sys.version)
print(sys.version_info)

# librerias varias
# OS
# collection

# bucle while
count = 0

while count <10:
    print(f"Contando {count}")
    count +=1

# while True:  # bucle eterno

while True:
    print("Estoy calculando ...")
    action = input("Quieres continuar? (s/n)")
    if action == "n":
        break

action = "s"

while action == "s":
    print("Estoy calculando2 ...")
    action = input("Quieres continuar2? (s/n)")
    if action == "n":
        break
