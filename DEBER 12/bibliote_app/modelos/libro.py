class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # tupla inmutable (titulo, autor)
        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    def get_titulo(self):
        return self._info[0]

    def get_autor(self):
        return self._info[1]

    def get_categoria(self):
        return self._categoria

    def get_isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self._info[0]} - {self._info[1]} | Categoria: {self._categoria} | ISBN: {self._isbn}"