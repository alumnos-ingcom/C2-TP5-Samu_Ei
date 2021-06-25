########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 7: Distancias
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

#  7. Distancias
# Escriba una funcion que determine la distancia entre dos números.
# Implementar este ejercicio sin utilizar la función valor absoluto abs().
# Ejemplo La distancia entre -6.5 y 6.0 es 12.5

def distancia(valor_a, valor_b):
    
    dista = valor_a - valor_b
    #eventualmente será CERO
    
    if valor_b > valor_a:
        dista = valor_b - valor_a
    
    return dista

def prueba():
    """Toda la interacción con el usuario va acá"""
    
    numero_a = float(input("ingrese un numero --> "))
    numero_b = float(input("ingrese otro num ---> "))
    print(f"la distancia entre ellos es {distancia(numero_a, numero_b)}")
    

if __name__ == "__main__":
    prueba()
