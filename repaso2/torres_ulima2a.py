'''
Clase que le permitirá tener un registro de todas las veces que se exceda el umbral
de consumo energetico.
'''
class HistoricoUmbrales:
    def __init__(self):
        self.registro_historicos = []

    def agregar_registro(self, registro):
        self.registro_historicos.append(registro)


'''
Clase que notificara que alertara que se debe disminuir el consumo.
'''
class Notificador:
    def alert(self):
        print("Reducir intensidad de focos en 10%")


class Componente:
    def __init__(self):
        self.consumo = 0
        self._hijos = []

    def obtener_consumo(self):
        pass

class Torres(Componente):
    def agregar_hijo(self, componente_hijo):
        self._hijos.append(componente_hijo)

    def obtener_consumo(self):
        consumo = 0
        for componente in self._hijos:
            consumo = consumo + componente.obtener_consumo()
        return consumo

class Torre(Componente):
    def agregar_hijo(self, componente_hijo):
        self._hijos.append(componente_hijo)

    def obtener_consumo(self):
        consumo = 0
        for componente in self._hijos:
            consumo = consumo + componente.obtener_consumo()
        return consumo

class Piso(Componente):
    def agregar_hijo(self, componente_hijo):
        self._hijos.append(componente_hijo)

    def obtener_consumo(self):
        consumo = 0
        for componente in self._hijos:
            consumo = consumo + componente.obtener_consumo()
        return consumo

class Lobby(Componente):
    def obtener_consumo(self):
        return 200

class Salon(Componente):
    def obtener_consumo(self):
        return 200

class Edificio:
    def __init__(self):

        self.torres = Torres()
        self.torreA = Torre()
        self.torreB = Torre()
        piso1A = Piso()
        piso2A = Piso()
        piso3A = Piso()
        piso1B = Piso()
        piso2B = Piso()
        piso3B = Piso()
        lobbyA = Lobby()
        salon1A = Salon()
        salon2A = Salon()
        salonAA = Salon()
        salonBA = Salon()
        salonCA = Salon()
        lobbyB = Lobby()
        salon1B = Salon()
        salonAB = Salon()
        salonBB = Salon()

        #Armamos la estructura
        self.torres.agregar_hijo(self.torreA)
        self.torres.agregar_hijo(self.torreB)
        self.torreA.agregar_hijo(piso1A)
        self.torreA.agregar_hijo(piso2A)
        self.torreA.agregar_hijo(piso3A)
        piso1A.agregar_hijo(lobbyA)
        piso2A.agregar_hijo(salon1A)
        piso2A.agregar_hijo(salon2A)
        piso3A.agregar_hijo(salonAA)
        piso3A.agregar_hijo(salonBA)
        piso3A.agregar_hijo(salonCA)
        self.torreB.agregar_hijo(piso1B)
        self.torreB.agregar_hijo(piso2B)
        self.torreB.agregar_hijo(piso3B)
        piso1B.agregar_hijo(lobbyB)
        piso2B.agregar_hijo(salon1B)
        piso3B.agregar_hijo(salonAB)
        piso3B.agregar_hijo(salonBB)



def main():
    edificio = Edificio()
    print("Consumo de torre A: %d vatios" % edificio.torreA.obtener_consumo())
    print("Consumo de torre B: %d vatios" % edificio.torreB.obtener_consumo())


if __name__ == '__main__':
    main()
