def formatear_xml(diccionario):
    cad = '<data>\n'
    for key, value in diccionario.items():
        cad = cad + '\t<%s>%s</%s>' % (key, value, key)
    cad = cad + '</data>'
    return cad

def p_decorator(func):
    def func_wrapper(param):
        cadena = func(param)
        return cadena.upper()
    return func_wrapper

def main():
    persona = {"nombre": "Billy", "edad": 30}

    # funcion sin decorar
    print(formatear_xml(persona))

    #funcion decorada
    f_decorada = p_decorator(formatear_xml)
    print(f_decorada(persona))


if __name__ == '__main__':
    main()
