def add(x, y):
    return x+y+5

print(add(2,1))

#lamda -  funciones anonimas
abc = lambda x,y: x+y+5
print(abc(2,1))


listaPeliculas = [
    {
        "titulo": "Heat",
        "genero": "Acción",
        "puntuacion": 8.2
    },
    {
        "titulo": "Titanic",
        "genero": "Romántica",
        "puntuacion": 7.2
    },
    {
        "titulo": "John Wick",
        "genero": "Acción",
        "puntuacion": 8.0
    },
    {
        "titulo": "El Señor de los anillos",
        "genero": "Fantasía",
        "puntuacion": 9.0
    },
    {
        "titulo": "Pretty woman",
        "genero": "Romántica",
        "puntuacion": 7.1
    },
    {
        "titulo": "The matix",
        "genero": "Acción",
        "puntuacion": 9.2
    },
    {
        "titulo": "La boda de mi mejor amigo",
        "genero": "Romántica",
        "puntuacion": 5.2
    },
    {
        "titulo": "La Historia interminable",
        "genero": "Fantasía",
        "puntuacion": 7.8
    },
    {
        "titulo": "Harry Potter",
        "genero": "Fantasía",
        "puntuacion": 8.4
    }
]

print("Lista de peliculas")
print("Titulo \t\t\t Genero \t Puntuacion")
for pelicula in listaPeliculas:
    print(f" {pelicula["titulo"]} \t\t\t {pelicula["genero"]} \t {pelicula["puntuacion"]}")
genero = input("Selecciona un genero(Fantasía/Romántica/Acción): ").lower()

#list comprehension = español ¿?
seleccionPeliculas = [pelicula for pelicula in listaPeliculas if pelicula["genero"].lower() == genero]
ordenadas = sorted(seleccionPeliculas,key=lambda x:x['puntuacion'], reverse=True)
for i in range(0, 2):
    peli = ordenadas[i]
    print (f"{peli['titulo']} {peli['puntuacion']}")

# seleccionPeliculas=[]
# for pelicula in listaPeliculas:
#     if pelicula["genero"].lower() == genero:
#         # agregamos el que coincida con el género
#         seleccionPeliculas.append(pelicula)
# indice=1

# for pelicula in ordenados:
#     if indice != 1:
#         print(f" {pelicula["titulo"]} \t\t\t {pelicula["genero"]} \t {pelicula["puntuacion"]}")
#     indice +=1

