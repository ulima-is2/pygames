class Animal:
    instance = None

    def __init__(self):
        self._peso = 0

    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = Singleton()
        return cls.instance

def main ():
    obj1 = Animal.get_instance()
    obj2 = Animal.get_instance()
    obj3 = Animal.get_instance()

    obj1._peso = 30

    print(obj3._peso)

if __name__ == '__main__':
    main()
