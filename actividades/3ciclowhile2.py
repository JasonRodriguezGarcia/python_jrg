# HTML img Simulacro Vamos a simular la carga de imagenes 6 veces en una página (imprimir el resultado en
#  HTML con print). AL pasar una variable i, conseguimos imagenes aleatorias.

# <img src="https://picsum.photos/200/300?random={i}" 

counter = 1
while True:
    # print("Estoy generando imágenes ...")
    print(f"<p><img src='https://picsum.photos/200/300?random={counter}/></p>")
    pregunta = input("Quieres continuar? (s/n)")
    if pregunta == "n":
        break
    counter += 1

