####### CONVERSOR DECIMAL A BINARIO, OCTAL Y HEXADECIMAL #######


def dec_bin(numero):
    binario = ""

    if numero == 0:
        return "0"

    while numero > 0:
        residuo = numero % 2
        numero = numero // 2
        binario = str(residuo) + binario
   
    
    return binario


def dec_octal(numero):
    octal = ""

    if numero == 0:
        return "0"
    
    while numero > 0:
        residuo = numero % 8
        numero = numero // 8
        octal = str(residuo) + octal

    return octal

def dec_hex(numero):
    hexa = ""
    hexadecimal = "0123456789ABCDEF"

    while numero > 0:
        residuo = numero % 16
        numero = numero // 16
        hexa = hexadecimal[residuo] + hexa

    return hexa
        
numero = int(input("ingrese el numero que deseas convertir a binario(solo enteros)"))
print(dec_bin(numero))
print(dec_octal(numero))
print(dec_hex(numero))

