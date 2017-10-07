class Ejecutor:
    def matar(self, proceso):
        if proceso['prioridad']==3 and proceso['consumo'] > 100:
            print('EjecutorNivel1 matará proceso %s' % proceso['nombre'])
        elif proceso['prioridad']==2 and proceso['consumo'] > 100:
            print('EjecutorNivel2 matará proceso %s' % proceso['nombre'])
        elif proceso['prioridad']==1 and proceso['consumo'] > 100:
            print('EjecutorNivel3 matará proceso %s' % proceso['nombre'])

def main():
    proceso = {
        "prioridad" : 2,
        "nombre" : "Proceso de prueba",
        "consumo" : 101
    }
    en = Ejecutor()
    en.matar(proceso)

if __name__ == '__main__':
    main()
