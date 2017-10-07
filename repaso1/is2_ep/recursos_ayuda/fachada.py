import sys
from factory import *

class RecetarioManager:
    def listar_recetas(self, tipo):
        factory = RecetarioFactory()
        recetario = factory.obtener_recetario(tipo)
        recetario.agregar_receta("Comida 1")
        recetario.listar_recetas()


def main():
    manager = RecetarioManager()
    manager.listar_recetas(sys.argv[1])

if __name__ == '__main__':
    main()
