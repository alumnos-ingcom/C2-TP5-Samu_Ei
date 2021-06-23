########################################################
# Samuel Sisto - samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 10: Texto binario
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

def dec_to_bin(dec_value):
    bin_value =''
    if dec_value > 1:
        dec_to_bin(dec_value//2)
    print(dec_value % 2,end = '')
    
def bin_to_dec(binary): 
    dec = 0 
    for digit in binary: 
        dec = dec*2 + int(digit)
    print("Representación decimal:\n", dec)

def prueba():
    decimal = int(input("Ingrese un número en base 10.\n"))
    print("Representación binaria:")
    dec_to_bin(decimal)
    binary = input("\n\nIngrese un número en base 2.\n")
    bin_to_dec(binary)
    pass

if __name__ == '__main__':
    prueba()