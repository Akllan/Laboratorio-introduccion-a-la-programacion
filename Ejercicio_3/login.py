##usuario = "admin"
##contrasena = "Admin2026"
def contar_pass(contrasena):
    numero_letras = len(contrasena)
    if numero_letras < 8:
        print("La contrasena debe de tener al menos 8 caracteres")


def numero(contrasena):
    if not contrasena.isdigit():
        print("La contrasena debe de tener al menos un numero")

def letra(contrasena):
    if not contrasena.isalpha():
        print("La contrasena debe de tener al menos una letra")


intentos = 0
print("LOG IN")
while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    
    if usuario == "":
        print("No se permite el user vacio ")
    elif usuario == chr(32):
        print("No se permite espacios en el usuario")
        
    else:
        contrasena = input("Ingrese la contrasena: ")
        contar_pass(contrasena)
        numero(contrasena)
        letra(contrasena)


    if usuario == "admin" and contrasena == "Admin2026":
        
        print("USUARIO VALIDO")
        break
    elif usuario != "admin":
        print("Usuario Invalido")
    else:
        intentos = intentos + 1
        print(f"llevas : {intentos} intentos,  MAXIMO 3 INTENTOS")
     



    

