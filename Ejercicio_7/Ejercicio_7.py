#accion= int(input("Ingrese la opcion que quieras hacer:"))
edad = 0
numero = 0
##palabra = input("Ingresa la palabra que vas a repetir 10 veces")
def mostrar_palabra_10_veces(palabra):
    veces = 1
    while veces < 11 and veces >0:  
        veces = veces +1
        print(palabra)


""" Ejercicio 2 
Escribir un programa que pregunte al usuario su edad y 
muestre por pantalla todos los años que ha cumplido (desde 1 
hasta su edad). """

def edad(edad):
    edad = int(input("Ingresa tu edad:  "))
    ano = 0
    for ano in range(ano, edad):
        
        ano = ano + 1
        print(f"Año de vida que has vivido:", ano)
       
""" 
Ejercicio 3 
Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas. 
"""

def numero_impares(numero):
    numero = int(input("Ingresa el numero que se va mostrar todos los numeros impares hacsta tu numero : "))
    for numero in range(1,numero, 2):
        print(numero)
    

""" 
Ejercicio 4 
Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla la cuenta atrás desde ese 
número hasta cero separados por comas. 
""" 

def cuenta_atras(numero):
    numero = int(input("Ingresa el numero que vas a hacer la cuenta regresiva: "))
    for numero in range(numero, -1, -1):
        print(numero)

##cuenta_atras(numero)


"""  
Ejercicio 5 
Escribir un programa que pregunte al usuario una cantidad a 
invertir, el interés anual y el número de años, y muestre por 
pantalla el capital obtenido en la inversión cada año que dura 
la inversión. 

""" 
invertir = 0
interes = 0
anos = 0 
def invertir(invertir, interes, anos):
    invertir = int(input("Ingrese la cantida que desea invertir: "))
    interes = int(input("Ingrese la cantida del interes: : "))
    anos = int(input("Ingrese la cantida de anos: : "))

    capital_mas_interes = invertir + (0.1 * interes)
    capital_anos = anos * capital_mas_interes / 12

    capital_final = invertir + capital_anos

    print(f"Tu capital final es de {capital_final} con un plazo de {anos} anos + {interes}% de intereses")


###invertir(invertir, interes, anos)


""" 
Ejercicio 6 
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más 
abajo, de altura el número introducido.
""" 
rango = 0

def triangulo(rango):
    rango = int(input("Ingresa el rango de asteriscos para el triangulo: "))
    for i in range(1, rango):
        corchete = "*"
        corchete_mas = corchete * i
        print(corchete_mas)

##triangulo(rango)    


""" 
Ejercicio 7 
Escribir un programa que muestre por pantalla la tabla de 
multiplicar del 1 al 10. 
""" 

def tabla_multiplicar():
   
    for i in range(1, 11, +1):
        print(f"\nTabla del {i}:")
        for numero in range (1, 11):
            tabla = numero * i
            print(tabla)


##tabla_multiplicar()

""" 
Ejercicio 8 
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más 
abajo.
""" 

def piramide_numeros(numero):
    numero = int(input("Ingresa el numero entero : "))
    for i in range(1, numero + 1):
        for j in range(2*i - 1, 0, -2):
            print(j, end=" ")
        print()
        
##piramide_numeros(numero)

""" 
Ejercicio 9 
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta. 
""" 
contrasena = ""
def contrasena(contrasena):
    contrasena = str(input("Ingresa ru contrasena:"))
    print(f"Tu contrasena es {contrasena}")
    print("Ahora ingresa tu contrasena correctamente")
    poner_contra = ""
    while True:
        poner_contra = input("Ingresa tu contrasena: ")
        if poner_contra == contrasena:
            print("contrasena correcta")
            break
        else:
            print("Contrasena incorrecta")
            

##contrasena(contrasena)

""" 
Ejercicio 10 
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla si es un número primo o no.
""" 

def primos(numero):
    numero = int(input("Ingresa el numero: "))
    if numero % 2 == 0:
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")


##primos(numero)
"""
Ejercicio 11 
Escribir un programa que pida al usuario una palabra y luego 
muestre por pantalla una a una las letras de la palabra 
introducida empezando por la última.
"""
palabra = ""
def letras(palabra):
    palabra = input("Ingresa la palabra: ")
    for i in palabra:
        print(i)


##letras(palabra)

""""
Ejercicio 12 
Escribir un programa en el que se pregunte al usuario por una 
frase y una letra, y muestre por pantalla el número de veces 
que aparece la letra en la frase.

"""
letra = ""
frase = ""
def palabra(letra):
    frase = input("Ingresa la frase")
    letra = input("Ingrese la letra que quieres contar: ")

    contador = frase.count(letra)
    print(f"La letra" f" {letra} " f" aparece {contador} veces")
##palabra(letra)

def eco(palabra):
    while palabra != "salir":
        palabra = input("Ingresa una palabra: ")
        salida = palabra.lower()
        if salida == "salir":
            palabra = "salir"
        print(palabra)

        
        

###eco(palabra)


print("Opciones: 0 salir, [1] mostrar palabras 10 veces, [2] mostrar anos vividos, [3] mostrar numeros impares, [4] cuenta atras, [5] invertir capital, [6] triangulo de asteriscos, [7] tablas de multiplicar, [8] piramide de numeros, [9] comprobar contrasena, [10] comprobar numero primo, [11] mostrar letras de una palabra, [12] contar letra en frase, [13] eco")
while True:
    opcion = int(input("Ingrese la opción: "))

    match opcion:
        case 0:
            break
        case 1:
            palabra = input("Ingresa la palabra que vas a repetir 10 veces: ")
            mostrar_palabra_10_veces(palabra)
        case 2:
            edad(0)
        case 3:
            numero_impares(0)
        case 4:
            cuenta_atras(0)
        case 5:
            invertir(0, 0, 0)
        case 6:
            triangulo(0)
        case 7:
            tabla_multiplicar()
        case 8:
            piramide_numeros(0)
        case 9:
            contrasena("")
        case 10:
            primos(0)
        case 11:
            letras("")
        case 12:
            palabra("")
        case 13:
            eco("")
        case _:
            print("Opción no reconocida.")