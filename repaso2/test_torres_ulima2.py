import unittest
from torres_ulima2 import Edificio

class TestTorresULima(unittest.TestCase):
    def setUp(self):
        self.edificio = Edificio()
        
    def tearDown(self):
        pass
    
    def test_no_envia_alerta(self):        
        self.edificio.actualizar_luminosidad_en(1)
        
        self.assertEqual(self.edificio.obtener_nro_registros(), 0, "Error: envia alerta cuando no debe")

    def test_envia_alerta(self):
        self.edificio.actualizar_luminosidad_en(3)
        
        self.assertEqual(self.edificio.obtener_nro_registros(), 1, "Error: no envia alerta cuando debe")
        
        self.assertEqual(round(self.edificio.obtener_luminosidad(), 2), 2.7, "Error: no disminuye la luminosidad")
        
if __name__ == '__main__':
    unittest.main()