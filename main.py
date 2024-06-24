import funciones as funcion

while True:
    print ("1 agregar libro");
    print ("2 ver todos los libros");
    print ("3 modificar un libro");
    print ("4 eliminar un libro ");
    print ("5 guardar coleccion en un libro");
    print ("6 salir del programa");
    try:
        opcion=int(input("** ingrese una opcion --> ")); 
    except ValueError:
        print("debe ser un numero del 1 al 6");
