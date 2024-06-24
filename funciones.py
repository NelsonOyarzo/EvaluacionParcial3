libros=[]

def agregar_libro():
    titulo=input("Ingrese el nombre del libro que desea registrar: ")
    autor=input("Ingrese el nombre del autor: ")
    plublicacion=input("Ingrese el año de publicacion: ")
    genero=input("Ingrese en genero del libro: ")
    
    libro={
        "nombre":titulo,
        "autor":autor,
        "publicacion":plublicacion,
        "genero":genero
    }
    libros.append(libro)
    print("¡Se ha registrado de manera correcta el libro!")

def ver_libros():
    for libro in libros:
        print(libro)
        break
