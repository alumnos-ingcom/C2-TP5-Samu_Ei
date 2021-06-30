########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 6: Parésntesis Balanceados
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

# Parentesis balanceado
# Implementar una función que determine si **una** cadena con parentesis está balanceada.

# Es decir, si cada parentesis que abre, tiene su par que cierra.
# El resultado debe ser un valor lógico indicando si esta o no balanceado.

# **Ejemplos**

#   (vacio)      OK
#   []           OK   
#   [][]         OK   
#   [[][]]       OK 
#   ][           NO OK
#   ][][         NO OK
#   []][[]       NO OK
       
# La funcion deberia de ignorar todo lo que no sean parentesis.

# **Extra**: Permitir la modificacion de los caracteres a parentesis,
# llaves, o cualquier otro par de caracteres.

def parentesis_balanceado(cadena):
    
    respuesta = "Obvio"

    if ((len(cadena) % 2) == 1) or (len(cadena) == 0):
        respuesta = "NO, impar"
    else:
        i = 0
        while i < len(cadena):
            if cadena[i] in "{[(":
                i += 1
            else:
                if cadena[i - 1] + cadena[i] in "{}" or \
                        cadena[i - 1] + cadena[i] in "[]" or \
                        cadena[i - 1] + cadena[i] in "()":
                    
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                else:
                    respuesta = "NO, Falta un cierre"
                    break
                    
    return respuesta
    
    
def prueba():
    cad = [x for x in input("Ingrese parentesis: ") if x in "{}[]()"]
    print(f'salida par de parentesis {parentesis_balanceado(cad)}')
    
if __name__ == "__main__":
    prueba() 