import time
#Importamos esta clase para poder modificar el limite de recursiones en python
#Ya que si no añadiamos esto nos daba un error y no se podia ejecutar
import  sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    #Factorial recursivo
    if n == 1:
        return 1

    return n * factorial_r(n - 1)


if __name__ == '__main__':
    #Aqui modificamos el limite
    sys.setrecursionlimit(1000000)
    n = 2000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final -comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final -comienzo)

