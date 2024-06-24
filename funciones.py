libros=[]

def agregar_libro():
    titulo=input("Ingrese el nombre del libro que desea registrar: ");
    autor=input("Ingrese el nombre del autor: ");
    plublicacion=input("Ingrese el año de publicacion: ");
    genero=input("Ingrese en genero del libro: ");
    
    libro=["Nombre: ",{titulo},
           "Autor",{autor},
           "publicacion",{plublicacion},
           "Genero",{genero}
           ];
    libros.append(libro);
    print("Se ha registrado de manera correcta el libro!");


def ver_libros():
    for libro in libros:
        return libro


def eliminar_libro(libros):
    libro_eliminar = input("Ingrese el nombre del libro que desea eliminar: ")
    encontrado = False
    
    for libro in libros:
        if libro['Nombre'].lower() == libro_eliminar.lower():
            libros.remove(libro)
            print(f"Se eliminó el libro '{libro['Nombre']}' con éxito.")
            encontrado = True
            
    if not encontrado:
        print("Libro no encontrado.")


def guardar_archivo(libros):
    with open('Archivo_nuevo.txt', 'w', encoding='utf-8') as archivo:
        for libro in libros:
            nombre = libro['Nombre']
            autor = libro['Autor']
            publicacion = libro['Publicacion']
            genero = libro['Genero']
            archivo.write(f"{nombre} {autor} {publicacion} {genero}\n")
    print("Archivo nuevo.txt ha sido generado correctamente con la información de los libros.")
