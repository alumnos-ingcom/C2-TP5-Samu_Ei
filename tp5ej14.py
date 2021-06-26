########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 14: capicúa
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

### 14. Números capicúa
#Escribir una función que determine si un numero entero positivo es capicúa.

def capicua(numero):
    """
    Esta función determina con ´True´ o ´False´ si un número
    entero positivo es capicúa o no.
    """
    separo_digitos = list(str(numero))
    longitud = len(separo_digitos) - 1
    bandera = True
    
    for i in range(len(separo_digitos)//2):
        if not(separo_digitos[i] == separo_digitos[longitud]):
            bandera = False
            break
        longitud = longitud - 1
        
    return bandera


def prueba():
    valor = int(input("ingrese el supuesto capicúa: "))
    
    print(f"será capicúa?? ---> {capicua(valor)}")
    

if __name__ == "__main__":
    prueba()