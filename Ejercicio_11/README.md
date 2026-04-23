# 📦 Lector de Códigos de Barras

> Aplicación web para lectura de códigos de barras y QR, construida con **Streamlit**.  
> Consulta productos en la base de datos pública de **OpenFoodFacts** a partir del código detectado.

![Bienvenida](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzI1Y2o3YXJqOHpoNHlndjg4NDl5aXZrbWVqdXd4N25wNTlodTB3diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hr216HOgDKL0dri3cD/giphy.gif)

![Demo animada](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGt0c2VqeGp1bGs4d2puMXYzaHFkMThqYzZvM3Ric2JydjRyd2Z0NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g9M5tnnQTJcgE/giphy.gif)

![App en funcionamiento](image-2.jpg)

---

## Tabla de Contenidos

1. [Descripción general](#descripción-general)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Modos de operación](#modos-de-operación)
5. [Referencia de funciones](#referencia-de-funciones)
6. [Flujo de datos](#flujo-de-datos)
7. [Dependencias externas y APIs](#dependencias-externas-y-apis)
8. [Manejo de errores](#manejo-de-errores)
9. [Limitaciones conocidas](#limitaciones-conocidas)
10. [Estructura del proyecto](#estructura-del-proyecto)
11. [Licencia](#licencia)

---

## Descripción general

`lector_codigos.py` es una aplicación Streamlit que permite al usuario escanear códigos de barras o QR
desde tres fuentes distintas (foto de cámara, ventana local con OpenCV, o stream en el navegador con WebRTC)
y mostrar el nombre e imagen del producto asociado consultando la API de OpenFoodFacts.

```
Usuario → [cámara/webcam] → detección de código → API OpenFoodFacts → nombre + imagen del producto
```

---

## Requisitos

| Paquete | Versión mínima | Necesario para |
|---|---|---|
| `streamlit` | ≥ 1.20 | Interfaz web |
| `requests` | ≥ 2.28 | Llamadas HTTP a APIs |
| `Pillow` | ≥ 9.0 | Manejo de imágenes |
| `numpy` | ≥ 1.23 | Procesamiento de arrays (importado) |
| `opencv-python` | ≥ 4.6 | Modo ventana local *(opcional)* |
| `pyzbar` | ≥ 0.1.9 | Decodificación de barras *(opcional)* |
| `streamlit-webrtc` | ≥ 0.45 | Modo en tiempo real *(opcional)* |
| `av` | ≥ 10.0 | Frames de video WebRTC *(opcional)* |

> **Nota:** `opencv-python`, `pyzbar`, `streamlit-webrtc` y `av` son opcionales.  
> El script los importa dinámicamente según el modo seleccionado y muestra un error descriptivo si no están instalados.

---

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/lector-codigos.git
cd lector-codigos

# Crear entorno virtual (recomendado)
python -m venv env
source env/bin/activate        # Linux/macOS
env\Scripts\Activate.ps1       # Windows (PowerShell)

# Dependencias base
pip install streamlit requests Pillow numpy

# Dependencias opcionales (modo local y tiempo real)
pip install opencv-python pyzbar streamlit-webrtc av

# Ejecución
streamlit run lector_codigos.py
```

La app estará disponible en `http://localhost:8501`.

---

## Modos de operación

El usuario elige uno de tres modos mediante un `st.radio` en la barra principal:

---

### 1. Streamlit (foto única)

**Flujo:**

1. Se activa `st.camera_input` para capturar una foto desde el navegador.
2. Los bytes de la imagen se envían como `multipart/form-data` a la API pública `qrserver.com`.
3. La respuesta JSON devuelve el contenido del código detectado.
4. Se llama a `fetch_product_info()` con ese código para consultar OpenFoodFacts.
5. Se muestra nombre e imagen del producto en la app.

**API externa utilizada:**
```
POST https://api.qrserver.com/v1/read-qr-code/
```

**Limitación:** Detecta principalmente QR. Para códigos de barras EAN/UPC la tasa de éxito
depende de la calidad de la foto y del servicio externo.

---

### 2. Ventana local (OpenCV)

**Flujo:**

1. Al presionar el botón, se abre una ventana nativa de OpenCV en el equipo del usuario.
2. Se captura video en tiempo real desde la webcam (`cv2.VideoCapture(0)`).
3. `pyzbar.decode()` analiza cada frame en busca de códigos.
4. Los códigos detectados se encuadran visualmente y se consultan en OpenFoodFacts.
5. Resultados se muestran también en la interfaz Streamlit.
6. Se cierra presionando `q` dentro de la ventana de OpenCV.

> **Importante:** Este modo bloquea el hilo principal de Streamlit mientras la ventana está abierta.  
> Solo funciona si la app corre localmente (no en servidores remotos ni Streamlit Cloud).

---

### 3. En la página — tiempo real (WebRTC)

**Flujo:**

1. `webrtc_streamer` inicia un stream de video directamente en el navegador.
2. Cada frame pasa por `BarcodeTransformer.recv()`, que corre en el servidor.
3. `pyzbar` detecta el código, lo dibuja sobre el frame y guarda la última detección en `self.last_barcode`.
4. El botón **"Buscar producto detectado"** toma `last_barcode` y llama a `fetch_product_info()`.
5. Resultado se muestra en `product_box` (placeholder dinámico).

> **Nota:** Requiere un servidor STUN/TURN accesible. En entornos con firewall puede requerir configuración adicional.

---

## Referencia de funciones

---

### `fetch_product_info(barcode: str) → dict | None`

Consulta la API de OpenFoodFacts para obtener el nombre e imagen de un producto.

**Parámetros:**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `barcode` | `str` | Código de barras o QR del producto (EAN-13, UPC-A, etc.) |

**Retorna:**

```python
{
    "name":  str | None,   # nombre del producto
    "image": str | None    # URL de la imagen del producto
}
```

Retorna `None` si ocurre un error de red o si el producto no existe en la base de datos.

**Lógica interna:**

1. Construye la URL: `https://world.openfoodfacts.org/api/v0/product/{barcode}.json`
2. Verifica que `status == 1` en la respuesta para confirmar que el producto existe.
3. Extrae `product_name` → `generic_name` → `brands` (en ese orden de preferencia) como nombre.
4. Extrae `image_front_small_url` → `image_small_url` → `image_front_url` como imagen.

**Ejemplo de uso:**

```python
prod = fetch_product_info("7501055300646")

if prod:
    print(prod["name"])   # → "Coca-Cola"
    print(prod["image"])  # → "https://images.openfoodfacts.org/..."
```

---

### `BarcodeTransformer` (clase — modo WebRTC)

Hereda de `VideoTransformerBase` (streamlit-webrtc).

| Atributo / Método | Tipo | Descripción |
|---|---|---|
| `self.last_detection` | `str \| None` | Último texto detectado con tipo, ej: `"123456 (EAN13)"` |
| `self.last_barcode` | `str \| None` | Último código detectado (solo datos, sin tipo) |
| `recv(frame)` | `av.VideoFrame` | Procesa cada frame: decodifica barras, dibuja rectángulos, actualiza atributos |

---

## Flujo de datos

```
                    ┌─────────────────────────────────────────┐
                    │              Usuario (browser)           │
                    └────────────────┬────────────────────────┘
                                     │
              ┌──────────────────────▼──────────────────────────┐
              │              st.radio — selección de modo        │
              └──────┬─────────────────┬──────────────────┬──────┘
                     │                 │                  │
           ┌─────────▼──────┐ ┌────────▼───────┐ ┌───────▼────────┐
           │  st.camera_input│ │ cv2.VideoCapture│ │ webrtc_streamer│
           │  + qrserver API │ │ + pyzbar       │ │ + BarcodeTransf│
           └────────┬───────┘ └────────┬────────┘ └───────┬────────┘
                    │                  │                   │
              ┌─────▼──────────────────▼───────────────────▼──────┐
              │               fetch_product_info(barcode)          │
              └─────────────────────────┬──────────────────────────┘
                                        │
                               ┌────────▼────────┐
                               │  OpenFoodFacts   │
                               │  API v0          │
                               └────────┬─────────┘
                                        │
                               ┌────────▼────────┐
                               │  st.write / img  │
                               │  (resultado)     │
                               └─────────────────┘
```

---

## Dependencias externas y APIs

### OpenFoodFacts API

- **URL base:** `https://world.openfoodfacts.org/api/v0/product/{barcode}.json`
- **Método:** `GET`
- **Autenticación:** No requerida
- **Límite de uso:** Sin límite oficial, pero se recomienda incluir `User-Agent` identificando la app
- **Docs:** [https://world.openfoodfacts.org/data](https://world.openfoodfacts.org/data)

### QR Server API (modo foto única)

- **URL:** `https://api.qrserver.com/v1/read-qr-code/`
- **Método:** `POST` con `multipart/form-data`
- **Autenticación:** No requerida
- **Límite de uso:** Uso razonable, sin SLA público
- **Docs:** [https://goqr.me/api/](https://goqr.me/api/)

---

## Manejo de errores

| Situación | Comportamiento |
|---|---|
| Código no encontrado en OpenFoodFacts | `st.warning` con mensaje descriptivo |
| Error HTTP en la API | `st.error` con el código de estado recibido |
| Error de red / timeout | `st.error` con el mensaje de la excepción |
| `opencv-python` o `pyzbar` no instalados | `st.error` con instrucción de instalación |
| `streamlit-webrtc` o `av` no instalados | `st.error` con instrucción de instalación |
| Cámara no disponible (modo local) | `st.error` indicando que la cámara puede estar en uso |
| Imagen del producto no cargable | `st.info` indicando que el producto fue encontrado sin imagen |
| No hay código detectado al buscar | `st.info` indicando que aún no hay detección |

---

## Limitaciones conocidas

- **Modo local (OpenCV):** Bloquea el hilo principal de Streamlit. No compatible con Streamlit Cloud ni despliegues en servidor remoto sin acceso a webcam física.
- **Modo foto única:** Depende de un servicio externo (`qrserver.com`) para decodificar el QR; no funciona offline.
- **Modo WebRTC:** El atributo `last_barcode` del transformer no se refresca automáticamente en la UI de Streamlit; requiere que el usuario presione el botón para consultar el producto.
- **Base de datos:** OpenFoodFacts tiene cobertura principalmente de productos alimenticios envasados. Productos sin registro devuelven `None`.
- **`numpy` importado pero no utilizado** directamente en el código actual; puede eliminarse del `import` sin consecuencias.

---

## Estructura del proyecto

```
lector-codigos/
├── lector_codigos.py    # Código principal de la app
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Esta documentación
└── image-2.jpg          # Screenshot de la interfaz
```

---

## Licencia

MIT License — libre para usar, modificar y distribuir.
