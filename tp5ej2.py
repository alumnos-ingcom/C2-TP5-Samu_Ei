########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 2: Fibonacci
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

### 2. Fibonacci
#La sucesión de Fibonacci es una sucesión infinita donde
#cada elemento es la suma de los dos anteriores.
#En la misma, los dos primeros términos
#son 1. (En algunos lugares se toma el primer termino en 0 y el segundo en 1)

def fibonacci(indice):
    acumulado = 2
    anterior = 1
    if indice == 1 or indice == 2:
        acumulado = 1
    elif indice > 3:
        for i in range(1, indice - 2):
            acumulado = acumulado + anterior
            anterior = acumulado - anterior
        
    return acumulado


def prueba():
    """Toda la interacción con el usuario va acá"""
    
    posicion = int(input("Averiguando el valor de la posición en la serie de FIBONACCI ---> "))
    print(f"En la posición {posicion} está el {fibonacci(posicion)}")
    
    #sólo para comprobar, imprimo toda la sucesión hasta n
    for i in range(1, posicion + 1):
        print(fibonacci(i))
    
    
if __name__ == "__main__":
    prueba()


