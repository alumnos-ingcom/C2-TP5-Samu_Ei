########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 3: Tribonacci
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

### 3. ¡Tribonacci!
# La secuencia de Tribonacci es el mismo concepto que la de Fibonacci común,
# pero acá en lugar de sumar dos terminos; se suman de a tres.
# [Tribonacci - OEIS](http://oeis.org/A000213) 

# Los tres primeros terminos son uno y el termino 4 es la suma de los tres anteriores.
# Implementar una funcion que permita obtener el n-esimo termino
# de la suceción Tribonacci, siendo este termino un numero entero positivo mayor a 3.


def tribonacci(indice):
    acumulado = 3
    anterior = 1
    pos_anterior = 1
    
    if indice == 1 or indice == 2 or indice == 3:
        acumulado = 1
    elif indice > 4:
        for i in range(1, indice - 2):
            acumulado = acumulado + anterior + pos_anterior
            pos_anterior = anterior
            anterior = acumulado - (pos_anterior + anterior)
        
    return acumulado

# 1 1 1 3 5 9 17 31 57

def prueba():
    """Toda la interacción con el usuario va acá"""
    
    posicion = int(input("Averiguando el valor de la posición en la serie de FIBONACCI ---> "))
    print(f"En la posición {posicion} está el {tribonacci(posicion)}")
    
    #sólo para comprobar, imprimo toda la sucesión hasta n
    for i in range(1, posicion + 1):
        print(tribonacci(i))
    
    
if __name__ == "__main__":
    prueba()


