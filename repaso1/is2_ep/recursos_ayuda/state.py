
ESTADO_SOLTERO = 0
ESTADO_CASADO = 1
ESTADO_DIVORCIADO = 2
ESTADO_VIUDO = 3
ESTADO_DIFUNTO = 4

class Persona:
    def __init__(self):
        self._estado = ESTADO_SOLTERO
    def casar(self):
        if self._estado == ESTADO_SOLTERO
            or self._estado == ESTADO_DIVORCIADO
            or self._estado == ESTADO_VIUDO:

            self._estado = ESTADO_CASADO
    def divorciarse(self):
        if self._estado == ESTADO_CASADO:
            self._estado = ESTADO_DIVORCIADO
    def enviudar(self):
        if self._estado == ESTADO_CASADO:
            self._estado = ESTADO_VIUDO
    def morir(self):
        if self._estado != ESTADO_DIFUNTO:
            self._estado = ESTADO_DIFUNTO
