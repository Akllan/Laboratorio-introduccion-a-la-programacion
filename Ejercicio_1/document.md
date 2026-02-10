# Creación de un Entorno Virtual en Python

Este documento describe el proceso de creación y activación de un entorno virtual en Python utilizando el módulo `venv`. El objetivo es trabajar de manera ordenada y evitar conflictos entre librerías, aplicando buenas prácticas de desarrollo.

---

## 1. Verificación de la versión de Python

Antes de comenzar, es necesario comprobar que Python esté correctamente instalado en el sistema.

```bash
py --version
```

Resultado de la verificación:

![Verificación de Python](assets/1-verificacion-python.png)

También se puede consultar la versión instalada desde el sistema operativo:

---

## 2. Acceso a la carpeta del proyecto

Se abre la terminal y se accede a la ruta donde se encuentra el proyecto.

```bash
cd ruta/del/proyecto
```

Ejemplo del acceso a la ruta:

![Acceso a la ruta](assets/2-acceso-ruta.png)

---

## 3. Creación del entorno virtual

Una vez ubicada la carpeta del proyecto, se crea el entorno virtual con el siguiente comando:

```bash
py -m venv env
```

Ejecución del comando:

![Creación del entorno virtual](assets/3-creacion-venv.png)

---

## 4. Estructura del entorno virtual

Al ejecutarse correctamente el comando, se crea la carpeta `env`, la cual contiene los archivos y subcarpetas necesarios para el entorno virtual.

Contenido interno del entorno virtual:

![Estructura del entorno virtual](assets/4-estructura-venv.png)

---

## 5. Activación del entorno virtual

Para comenzar a trabajar dentro del entorno virtual, se debe activar desde PowerShell con el siguiente comando:

```bash
.\env\Scripts\Activate.ps1
```

Proceso de activación:

![Activación del entorno virtual](assets/5-activacion-venv.png)

Cuando el entorno se encuentra activo, el nombre `(env)` aparece al inicio de la línea de comandos.

---

## Conclusión

El uso de entornos virtuales en Python es una práctica fundamental para el desarrollo de proyectos, ya que permite mantener las dependencias aisladas, mejorar la organización del código y facilitar el trabajo académico y profesional.
