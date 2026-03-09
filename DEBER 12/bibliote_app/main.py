from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    print("\n===== SISTEMA BIBLIOTECA DIGITAL =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar por titulo")
    print("8. Buscar por autor")
    print("9. Buscar por categoria")
    print("10. Libros prestados de usuario")
    print("0. Salir")


def main():

    biblioteca = BibliotecaServicio()

    while True:

        menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")

            biblioteca.anadir_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")

            biblioteca.quitar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre usuario: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID usuario: ")

            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")

            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "6":

            isbn = input("ISBN del libro: ")
            id_usuario = input("ID usuario: ")

            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "7":

            titulo = input("Titulo: ")

            biblioteca.buscar_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor: ")

            biblioteca.buscar_autor(autor)

        elif opcion == "9":

            categoria = input("Categoria: ")

            biblioteca.buscar_categoria(categoria)

        elif opcion == "10":

            id_usuario = input("ID usuario: ")

            biblioteca.libros_usuario(id_usuario)

        elif opcion == "0":

            print("Saliendo del sistema")
            break

        else:

            print("Opcion invalida")


if __name__ == "__main__":
    main()