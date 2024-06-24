import funciones as funcion

while True:
    print ("_.Bienvenido a su Bibloteca personal._");
    print ("_.----------------------------------._");
    print ("1.-Agregar libro");
    print ("2.-Ver todos los libros");
    print ("3.-Modificar un libro");
    print ("4.-Eliminar un libro ");
    print ("5.-Guardar coleccion en un libro");
    print ("6.-Salir del programa");
    print ("_.----------------------------------._");
    try:
        opcion=int(input("** ingrese una opcion --> ")); 
    except ValueError:
        print("debe ser un numero del 1 al 6");
    else:
        if opcion == 1:
            print("Ingresaste a la opcion 1: ");
            funcion.agregar_libro();
        elif opcion==2:
            print("Ingresaste a la opcion 2");
            funcion.ver_libros();
        elif opcion == 3:
            print("Ingresaste a la opcion 3");
            funcion.modificar_libro();
        elif opcion == 4:
            print("Ingresaste a la opcion 4");
            funcion.eliminar_libro();
        elif opcion == 5:
            print("Ingresaste a la opcion 5");
            funcion.guardar_archivo();
        elif opcion == 6:
            print("saliendo del programa");
            break;
