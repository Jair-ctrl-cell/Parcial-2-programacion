class Usuario:

    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario

        # lista de libros prestados
        self._libros_prestados = []

    def get_nombre(self):
        return self._nombre

    def get_id(self):
        return self._id_usuario

    def agregar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):

        for libro in self._libros_prestados:
            if libro.get_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return libro

        return None

    def listar_libros(self):
        return self._libros_prestados

    def __str__(self):
        return f"Usuario: {self._nombre} | ID: {self._id_usuario}"