<div align="center">

# 🔢 Calculadora Conversora en Python

**Conversor de números decimales a Binario, Octal y Hexadecimal**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Funcional-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/Licencia-MIT-blue?style=for-the-badge)

</div>

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Cómo funciona](#-cómo-funciona)
  - [Decimal a Binario](#decimal-a-binario-base-2)
  - [Decimal a Octal](#decimal-a-octal-base-8)
  - [Decimal a Hexadecimal](#decimal-a-hexadecimal-base-16)
- [Uso](#-uso)
- [Ejemplos](#-ejemplos)

---

## 📖 Descripción

Este script de Python convierte números decimales enteros a sus representaciones en tres sistemas numéricos distintos: **binario**, **octal** y **hexadecimal**. Cada conversión está implementada manualmente usando el algoritmo de divisiones sucesivas, sin utilizar funciones nativas de Python como `bin()`, `oct()` o `hex()`.

---

## ✨ Características

- ✅ Conversión de decimal a **Binario** (base 2)
- ✅ Conversión de decimal a **Octal** (base 8)
- ✅ Conversión de decimal a **Hexadecimal** (base 16)
- ✅ Manejo del caso especial cuando el número es `0`
- ✅ Implementación manual del algoritmo (sin funciones nativas)
- ✅ Interfaz de entrada por consola

---

## ⚙️ Cómo funciona

### Decimal a Binario (Base 2)

Se declara la función `dec_bin()` que recibe un número entero. Primero se inicializa la variable `binario` como string vacío, lo que facilita construir el resultado al final. Si el número ingresado es `0`, se retorna directamente `"0"`.

```python
def dec_bin(numero):
    binario = ""
    if numero == 0:
        return "0"
```

![Declaración función binario](assets/1.png)

> 💡 La variable `binario` se declara como string vacío para poder concatenar los residuos directamente.

![Inicialización variable](assets/2.png)

Luego se ejecuta un bucle `while` que sigue mientras el número sea mayor a 0. En cada iteración:
1. Se calcula el **residuo** con el operador módulo `% 2` (siempre da `0` o `1`)
2. Se **actualiza el número** con división entera `// 2` para continuar el proceso
3. El residuo se **antepone** al string `binario` para que quede en el orden correcto

![Caso especial cero](assets/3.png)

![Bucle while - algoritmo principal](assets/4.png)

Al terminar el bucle, se retorna `binario` con la representación completa.

![Resultado completo función binario](assets/7.png)

---

### Decimal a Octal (Base 8)

La lógica es **exactamente igual** que para binario, con la única diferencia de que la base cambia de `2` a `8`. El operador módulo `% 8` ahora puede retornar valores del `0` al `7`, y la división entera se hace entre `8`.

![Función decimal a octal](assets/12.png)

> 🔄 Mismo algoritmo, distinta base. Si entendiste binario, ¡ya entendiste octal!

---

### Decimal a Hexadecimal (Base 16)

Esta conversión tiene una particularidad: los valores del `10` al `15` se representan con letras (`A` al `F`). Para resolver esto sin usar múltiples condicionales, se declara una **cadena de caracteres** que mapea cada posición con su símbolo correcto:

```python
hexadecimal = "0123456789ABCDEF"
```

![Cadena hexadecimal](assets/8.png)

De esta forma, si el residuo es `10`, `hexadecimal[10]` devuelve `'A'`; si es `11`, devuelve `'B'`, y así sucesivamente. El algoritmo es el mismo que los anteriores pero usando `% 16` y `// 16`.

![Bucle función hexadecimal](assets/11.png)

> 📝 En esta función **no es necesario** manejar el caso especial del `0` porque el `0` ya está incluido como primer elemento de la cadena `hexadecimal`.

---

## 🚀 Uso

### Requisitos

- Python 3.x

### Ejecución

```bash
python calculadora_conversor.py
```

Al ejecutarlo, el programa pedirá un número entero por consola y mostrará los tres resultados:

![Input y llamada a funciones](assets/10.png)

---

## 📊 Ejemplos

### Entrada de usuario

Al ejecutar el script se muestra un prompt solicitando el número:

![Ejemplo de entrada](assets/9.png)

### Resultado de la conversión

El programa imprime los tres resultados uno debajo del otro:

**Resultado Binario y Octal:**

![Salida binario](assets/6.png)

**Resultado Hexadecimal:**

![Salida hexadecimal](assets/5.png)

**Vista completa del conversor:**

![Resultado final completo](assets/3.png)

---

## 📁 Estructura del Proyecto

```
📦 calculadora-conversora/
├── 📄 calculadora_conversor.py   # Script principal
├── 📄 README.md                  # Documentación
└── 📁 assets/                    # Capturas de pantalla
    ├── 1.png  → 12.png
```

---

<div align="center">

Hecho con ❤️ en Python

</div>