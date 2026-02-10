# Documentación: Entorno Virtual en Python (venv)

## ¿Qué es un entorno virtual?
Un entorno virtual en Python es una forma de crear un espacio aislado donde se pueden instalar librerías y dependencias sin afectar a otros proyectos ni al sistema principal.

Cada proyecto puede tener su propio entorno virtual, lo que ayuda a evitar conflictos entre versiones de librerías.

---

## ¿Para qué sirve?
- Evita conflictos entre librerías
- Mantiene los proyectos organizados
- Permite trabajar con diferentes versiones de paquetes
- Es una buena práctica en programación profesional

---

## Requisitos
- Sistema operativo: Windows
- Python instalado
- Uso de PowerShell o CMD

Para comprobar que Python está instalado:
```bash
py --version
Crear el entorno virtual
Entrar a la carpeta del proyecto:

cd "C:\Users\aklla\OneDrive\Documentos\UNIVERSIDAD\Laboratio de programacion\EntornovirtualENV"
Crear el entorno virtual:

py -m venv env
Esto crea una carpeta llamada env que contiene el entorno virtual.

Problema común: scripts bloqueados en PowerShell
Por seguridad, PowerShell bloquea la ejecución de scripts, lo que impide activar el entorno virtual.

Solución
Ejecutar una sola vez el siguiente comando:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Esto permite ejecutar scripts locales sin comprometer la seguridad del sistema.

Activar el entorno virtual
Desde la carpeta del proyecto:

.\env\Scripts\Activate.ps1
Si el entorno se activa correctamente, aparecerá (env) al inicio de la línea de comandos.

Instalar librerías
Con el entorno virtual activo:

pip install nombre_libreria
Ejemplo:

pip install numpy
Las librerías se instalan únicamente dentro del entorno virtual.

Ejecutar un programa
Con el entorno activado:

py main.py
Salir del entorno virtual
Cuando ya no se necesite:

deactivate
Guardar dependencias del proyecto
Para guardar las librerías instaladas:

pip freeze > requirements.txt
Para instalarlas en otro equipo o entorno:

pip install -r requirements.txt
Conclusión
El uso de entornos virtuales en Python es fundamental para trabajar de forma ordenada, evitar errores y facilitar el desarrollo de proyectos. Es una práctica recomendada tanto en el ámbito académico como profesional.


---
