from multiprocessing import Process
import os 
import winsound

def func(n):
    print(os.getpid())
    for n in range(10):
        valor = n*n*+n
        print(valor,"--",n)

if __name__ == '__main__':
    procesos=[]
    cores = os.cpu_count()
    print('tienes ',cores,' cores')

    print('instancia')
    for n in range(cores):
        proceso =Process(target=func,args=(n,))
        procesos.append(proceso)
    
    print('ejecucion')
    for proceso in procesos:
        proceso.start()

    print('espera')
    for proceso in procesos:
        proceso.join()

    print('regreso a la ejecucion inicial')