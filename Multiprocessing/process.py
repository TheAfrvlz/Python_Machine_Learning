from concurrent.futures import process
from multiprocessing import Process
import os
import winsound

def Funcion(numero):
    print(os.getpid())
    for n in range(10):
        valor = n*n+n
        print(valor, "-->",numero)
        winsound.Beep(2500,100)

if __name__ == '__main__':
    procesos = []
    cores = os.cpu_count()
    print('Tienes', cores , 'cores')
    print('-------Instanciar')

    for n in range(cores):
        
        proceso = Process(target=Funcion,args=(n,))
        procesos.append(proceso)

    print('-----------ejecutar')
    for proceso in procesos:
        proceso.start()

    print('-----------espera')
    for proceso in procesos:
        proceso.join()

    print('-----------ejecucion inicial')
