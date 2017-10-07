class EjecutorNivel1:
    def __init__(self):
        self.sucesor = None
    def add_sucesor(self, sucesor):
        self.sucesor = sucesor
    def matar(self, proceso):
        if proceso['prioridad']==3 and proceso['consumo'] > 100:
            print('EjecutorNivel1 matará proceso %s' % proceso['nombre'])
        else:
            self.sucesor.matar(proceso)

class EjecutorNivel2:
    def __init__(self):
        self.sucesor = None
    def add_sucesor(self, sucesor):
        self.sucesor = sucesor
    def matar(self, proceso):
        if proceso['prioridad']==2 and proceso['consumo'] > 100:
            print('EjecutorNivel2 matará proceso %s' % proceso['nombre'])
        else:
            self.sucesor.matar(proceso)

class EjecutorNivel3:
    def __init__(self):
        self.sucesor = None
    def add_sucesor(self, sucesor):
        self.sucesor = sucesor
    def matar(self, proceso):
        if proceso['prioridad']==1 and proceso['consumo'] > 100:
            print('EjecutorNivel3 matará proceso %s' % proceso['nombre'])



def main():
    en1 = EjecutorNivel1()
    en2 = EjecutorNivel2()
    en3 = EjecutorNivel3()

    en1.add_sucesor(en2)
    en2.add_sucesor(en3)

    proceso = {
        "prioridad" : 2,
        "nombre" : "Proceso de prueba",
        "consumo" : 101
    }
    en1.matar(proceso)

if __name__ == '__main__':
    main()
