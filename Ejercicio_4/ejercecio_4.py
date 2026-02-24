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
        acceso = 1

        print("Bienvenido", usuario)
        print("MENU DEL USUARIO", usuario)
        print("Selecciona lo que quieres hacer")
        print("[1] Clasificar numeror(positivo,negativo, cero, par/impar)")
        print("[2] Categoria por edad")  
        print("[3] Calcular Tarifa final(descuento multiples)")
        print("[4] Cerrar sesion volver al login")
        print("[5] Salir completamente")
        while acceso == 1:
            accion_user = int(input("Selecciona tu opcion: "))
            if accion_user == 1:
                print("Clasificacion de numeros")
            elif accion_user == 2:
                print("Categoria por edad")
            elif accion_user ==3:
                print("Calculo de tarifa para descuatos")
            elif accion_user == 4:
                print("Cerrando sesion ...")
                acceso = 0
            elif accion_user == 5:
                acceso = -1
                break
                
            else:
                print("Opcion invalida")
        if acceso == -1:
            break
                
        
    
    elif usuario != "admin":
        print("Usuario Invalido")
    else:
        intentos = intentos + 1
        print(f"llevas : {intentos} intentos,  MAXIMO 3 INTENTOS")
     



    

