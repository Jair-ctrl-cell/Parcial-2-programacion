class VisitaServicio:
    def __init__(self):
        self._visitantes = []

    def registrar_visitante(self, visitante):
        # Validar duplicados por cédula
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False
        self._visitantes.append(visitante)
        return True

    def obtener_visitantes(self):
        return self._visitantes

    def eliminar_visitante(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False