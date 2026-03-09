from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # diccionario de libros disponibles
        self.libros = {}

        # diccionario de usuarios
        self.usuarios = {}

        # set para controlar ids unicos
        self.ids_usuarios = set()

    # añadir libro
    def anadir_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro añadido correctamente")

    # quitar libro
    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # registrar usuario
    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El ID ya existe")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente")

    # eliminar usuario
    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado")

        else:
            print("Usuario no encontrado")

    # prestar libro
    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:
            print("Libro no disponible")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        libro = self.libros.pop(isbn)
        usuario = self.usuarios[id_usuario]

        usuario.agregar_libro(libro)

        print("Libro prestado correctamente")

    # devolver libro
    def devolver_libro(self, isbn, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[id_usuario]

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros[isbn] = libro
            print("Libro devuelto correctamente")
        else:
            print("El usuario no tiene ese libro")

    # buscar por titulo
    def buscar_titulo(self, titulo):

        for libro in self.libros.values():

            if libro.get_titulo().lower() == titulo.lower():
                print(libro)

    # buscar por autor
    def buscar_autor(self, autor):

        for libro in self.libros.values():

            if libro.get_autor().lower() == autor.lower():
                print(libro)

    # buscar por categoria
    def buscar_categoria(self, categoria):

        for libro in self.libros.values():

            if libro.get_categoria().lower() == categoria.lower():
                print(libro)

    # listar libros de usuario
    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.listar_libros():
            print(libro)