import sys
import srx
import pp

'''
Este programa se ejecuta con un parametro extra (por el shell).
Ejm :
    $ python pregunta2.py SRX777
    $ python pregunta2.py PP876
'''

def main():
    if sys.argv[1] == 'SRX77':
        data = srx.obtain_data()
        print('La humedad es %i' % data['humidity'])
    elif sys.argv[1] == 'PP876':
        data = pp.get_humidity()
        print('La humedad es %i' % data)
    else:
        print('Debe ingresar un tipo de sensor')

if __name__ == '__main__':
    main()
