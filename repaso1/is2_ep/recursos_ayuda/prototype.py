import copy

class Animal:
    def __init__(self):
        self._tamano = 0

    def __clone__(self):
        return copy.deepcopy(self)

def main():
    obj1 = Animal()
    obj1._tamano = 140
    obj2 = obj1.__clone__()
    obj1._tamano = 190
    print(obj1._tamano) #190
    print(obj2._tamano) #140

if __name__ == '__main__':
    main()
