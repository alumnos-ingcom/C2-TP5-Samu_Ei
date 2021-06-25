########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 1: pares e impares
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

# 1. Pares e impares
# Escribir una función que retorne True cuando un número entero es par
# y False cuando no lo sea, sin utilizar módulo. (%)

def es_par(numero):
    bandera = True
    if pow(-1, numero) == -1:
        bandera = False

    return bandera


def prueba():
    """Toda la interacción con el usuario va acá"""
    
    valor = int(input("Determinando si el sig valor es par o impar ---> "))
    texto = "IMPAR"
    if es_par(valor):
        texto = "PAR"
        
    print(f"Comprobado que {valor} es {texto}")
    
    
if __name__ == "__main__":
    prueba()