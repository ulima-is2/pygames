import sys

class Recetario:
    def __init__(self):
        self._recetas = []

    def listar_recetas(self):
        for receta in self._recetas:
            print(receta)

    def agregar_receta(self, receta):
        self._recetas.append(receta);

class RecetarioMarina(Recetario):
    def listar_recetas(self):
        for receta in self._recetas:
            print("* %s" % receta)

class RecetarioCriolla(Recetario):
    def listar_recetas(self):
        for receta in self._recetas:
            print("- %s" % receta)

class RecetarioFactory:
    def obtener_recetario(self, tipo_comida):
        if tipo_comida == 'marina':
            return RecetarioMarina()
        elif tipo_comida == 'criolla':
            return RecetarioCriolla()
        else:
            raise TypeError("No existe el tipo de comida ingresado")

def main():
    factory = RecetarioFactory()
    recetario = factory.obtener_recetario(sys.argv[1])
    recetario.agregar_receta("Ceviche")
    recetario.listar_recetas();

if __name__ == '__main__':
    main()







#
