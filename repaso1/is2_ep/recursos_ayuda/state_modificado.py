class EstadoPersona:
    def __init__(self, persona):
        self._persona = persona
    def casar(self):
        pass
    def divorciarse(self):
        pass
    def enviudar(self):
        pass
    def morir(self):
        pass
    def imprimir(self):
        print("Estado Base")

class EstadoSoltero(EstadoPersona):
    def casar(self):
        self._persona._estado = EstadoCasado(self._persona)
    def morir(self):
        self._persona._estado = EstadoDifunto(self._persona)
    def imprimir(self):
        print("Estado Soltero")

class EstadoCasado(EstadoPersona):
    def enviudar(self):
        self._persona._estado = EstadoViudo(self._persona)
    def divorciarse(self):
        self._persona._estado = EstadoDivorciado(self._persona)
    def morir(self):
        self._persona._estado = EstadoDifunto(self._persona)
    def imprimir(self):
        print("Estado Casado")

class EstadoViudo(EstadoPersona):
    def casar(self):
        self._persona._estado = EstadoCasado(self._persona)
    def morir(self):
        self._persona._estado = EstadoDifunto(self._persona)
    def imprimir(self):
        print("Estado Viudo")

class EstadoDivorciado(EstadoPersona):
    def casar(self):
        self._persona._estado = EstadoCasado(self._persona)
    def morir(self):
        self._persona._estado = EstadoDifunto(self._persona)
    def imprimir(self):
        print("Estado Divorciado")

class EstadoDifunto(EstadoPersona):
    def imprimir(self):
        print("Estado Difunto")

class Persona:
    def __init__(self):
        self._estado = EstadoSoltero(self)
    def casar(self):
        self._estado.casar()
    def morir(self):
        self._estado.morir()
    def divorciarse(self):
        self._estado.divorciarse()
    def enviudar(self):
        self._estado.enviudar()
    def imprimir_estado(self):
        self._estado.imprimir()

def main():
    persona = Persona()
    persona.imprimir_estado()
    persona.casar()
    persona.imprimir_estado()
    persona.morir()
    persona.imprimir_estado()
    persona.casar()
    persona.imprimir_estado()

if __name__ == '__main__':
    main()




#
