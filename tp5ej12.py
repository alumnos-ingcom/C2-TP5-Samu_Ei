########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 12: Comparar listas
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

### 12. Comparación de listas
# Escribir una función que que determine retornando True si un par de listas contienen
# los mismos elementos que pueden estén ubicados en diferentes posiciones.

from random import randint

def lista_random(cantidad, numero_minimo=0, numero_maximo=100):
    """
    Esta función genera una lista de `cantidad` 
    con valores entre `número_minimo` y `número_maximo`
    Con valores por defecto sensibles para su uso rápido
        (10 elementos, entre 0 y 100)
    """
    milista = list()
    for i in range(cantidad):
        milista.append(randint(numero_minimo, numero_maximo))
    return milista


def comparo_listas(lista_uno, lista_dos):
    
    flag = False

    if len(lista_uno) == len(lista_dos):
        for i in range(len(lista_uno)):
            posicion = 0
            while posicion < len(lista_dos):
                if lista_uno[i] == lista_dos[posicion]:
                    lista_dos[posicion] = -1
                    posicion = len(lista_dos)
                    if i == len(lista_uno) - 1:
                        flag = True
                
                posicion = posicion + 1

    return flag


def prueba():
    
    aleatoria1 = lista_random(15)
    aleatoria2 = lista_random(15)
    
    print(f"son {aleatoria1} +++ \n   {aleatoria2}")
    print(f"\n{comparo_listas(aleatoria1, aleatoria2)}")
    
    #me fijo qué cambió y qué valores encontró similares (marcados con -1)
    print(f"VER {aleatoria1} +++ \n   {aleatoria2}")
    
    
if __name__ == "__main__":
    prueba()