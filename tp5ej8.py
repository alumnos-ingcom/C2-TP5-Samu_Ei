########################################################
# Samuel Sisto - @samusisto
# Eimi Saiz - @EimiSaiz
# TP 5 - Eje. 8: El Cifrado del César
# UNRN Andina - Introducción a Ingeniería en Computación
########################################################

# Funcion codificadora:
def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): # chequeá si es una mayúscula
            c_index = ord(c) - ord('A')
            # cambiá el caracter actual por posiciones "key"
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): # chequeá si es una minúscula
            # restá el unicode de 'a' para obtener el índice en el rango [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # si es numérico, cambiá su valor real
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # si no es alfabético ni numérico, dejalo así
            encrypted += c
    return encrypted

# Función decodificadora:
def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            # cambiá el caracter actual a la izquierda por posiciones "key" para obtener su posición original
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower(): 
            c_index = ord(c) - ord('a') 
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # si es numérico, cambiá su valor real
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # si no es alfabético ni numérico, dejalo así
            decrypted += c
    return decrypted

def prueba():
    plain_text = input("Ingrese un texto a codificar.\n")    
    key = int(input("Ingrese la cantidad de posiciones.\n"))   
    ciphertext = cipher_encrypt(plain_text, key)  
    print("Texto codificado:",ciphertext)   
    plain_text = cipher_decrypt(ciphertext, key)   
    print("Texto decodificado:",plain_text) 
    pass

if __name__ == "__main__":
    prueba()