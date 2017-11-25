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
        print("Se debe de disminuir el consumo")

