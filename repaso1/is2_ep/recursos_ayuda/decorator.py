def ejecutar(func, numero):
    def func2():
        return func(numero)
    return func2

def cuadrado(x):
    return x * x

def main():
    f = ejecutar(cuadrado, 10)
    resp = f()
    print(resp)

if __name__ == '__main__':
    main()
