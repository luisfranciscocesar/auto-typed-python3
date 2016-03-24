import sys
from time import sleep
from threading import Thread

speed = 0.1 # velocidad de tipeo
file = 'code_example.py' # ruta del archivo
loop = False # bucle True or False

def typedcode():
    f = open(file, 'r')
    code = f.read()
    f.close()
    words = code
    if loop == True:
        while (True):
            for char in words:
                sleep(speed)
                sys.stdout.write(char)
                sys.stdout.flush()
            print('')
    if loop == False:
        for char in words:
            sleep(speed)
            sys.stdout.write(char)
            sys.stdout.flush()
subproceso = Thread(target=typedcode)
subproceso.start()