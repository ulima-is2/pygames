import sys
from library_csv import CSVWriter
from library_sqlite import SQLiteWorker

class DataAdapter:
    def abrir(self, filename):
        pass

    def escribir(self, data):
        pass

class CSVAdapter(DataAdapter):
    def abrir(self, filename):
        self._csv = CSVWriter(filename)
        self._csv.open()

    def escribir(self, data):
        self._csv.write(data)

class SQLiteAdapter(DataAdapter):
    def abrir(self, filename):
        self._sqlite = SQLiteWorker()
        self._sqlite.connect(filename)

    def escribir(self, data):
        self._sqlite.insert('data', data)

class DataAdapterFactory:
    def obtener_data_adapter(self, tipo):
        if tipo == 'sqlite':
            return SQLiteAdapter()
        elif tipo == 'csv':
            return CSVAdapter()
        else:
            return None

def main():
    tipo = sys.argv[1]
    nombre = sys.argv[2]

    factory_adapter = DataAdapterFactory()
    adapter = factory_adapter.obtener_data_adapter(tipo)

    adapter.abrir(nombre)
    plato = {
        "nombre" : "Ceviche",
        "descripcion" : "Plato rico"
    }
    adapter.escribir(plato)

if __name__ == '__main__':
    main()










#
