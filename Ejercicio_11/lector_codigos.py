import streamlit as st
import numpy as np
import requests
from PIL import Image

st.title("Lector de Códigos de Barras")
st.write("Selecciona el modo: foto única, ventana local o detección en la misma página (en vivo).")


def fetch_product_info(barcode: str):
    """Busca información de producto por código de barras en OpenFoodFacts.
    Devuelve dict con 'name' y 'image' (o None si no hay resultado).
    """
    headers = {"User-Agent": "ProductScanner/1.0 (https://github.com/your-repo)"}
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
        resp = requests.get(url, headers=headers, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == 1 and data.get("product"):
                prod = data["product"]
                name = prod.get("product_name") or prod.get("generic_name") or prod.get("brands")
                # Prefer front image
                image = prod.get("image_front_small_url") or prod.get("image_small_url") or prod.get("image_front_url")
                return {"name": name, "image": image}
            else:
                st.warning("Producto no encontrado en la base de datos de OpenFoodFacts.")
                st.write("Respuesta de la API:", data)
        else:
            st.error(f"Error en la API: Código de estado {resp.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error de red al buscar el producto: {e}")
    except Exception:
        return None
    return None

mode = st.radio("Modo:", ("Streamlit (foto única)", "Ventana local (OpenCV)", "En la página (realtime)"))

if mode == "Streamlit (foto única)":
    camera_input = st.camera_input("Activar cámara")

    if camera_input:
        image = Image.open(camera_input)
        img_bytes = camera_input.getvalue()
        
        st.write("Procesando...")
        
        files = {"file": ("image.png", img_bytes, "image/png")}
        
        try:
            response = requests.post("https://api.qrserver.com/v1/read-qr-code/", files=files, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                if result and result[0].get("symbol") and result[0]["symbol"][0].get("data"):
                    barcode_data = result[0]["symbol"][0]["data"]
                    st.success(f"¡Código detectado!\n\n**Datos:** {barcode_data}")
                    # Buscar producto
                    prod = fetch_product_info(barcode_data)
                    if prod:
                        if prod.get("name"):
                            st.write(f"**Producto:** {prod.get('name')}")
                        if prod.get("image"):
                            try:
                                st.image(prod.get("image"), caption=prod.get("name"))
                            except Exception:
                                st.info("Producto encontrado, pero no se pudo cargar la imagen.")
                else:
                    st.warning("No se detectó ningún código. Intenta acercar el código a la cámara.")
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

elif mode == "Ventana local (OpenCV)":
    st.write("Ventana local: se abrirá una ventana de OpenCV en tu equipo. Presiona 'q' dentro de la ventana para cerrar.")
    if st.button("Abrir ventana local (OpenCV)"):
        st.write("Abriendo ventana local...")
        try:
            import cv2
            from pyzbar import pyzbar
        except Exception as e:
            st.error("Faltan dependencias: instala 'opencv-python' y 'pyzbar'.")
            st.error(str(e))
        else:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                st.error("No se pudo abrir la cámara. Verifica que no esté en uso por otra aplicación.")
            else:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    barcodes = pyzbar.decode(frame)
                    for barcode in barcodes:
                        (x, y, w, h) = barcode.rect
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        barcodeData = barcode.data.decode("utf-8")
                        barcodeType = barcode.type
                        text = f"{barcodeData} ({barcodeType})"
                        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        # Buscar producto y mostrar en la página Streamlit
                        prod = fetch_product_info(barcodeData)
                        if prod:
                            # Mostrar nombre e imagen en la app Streamlit
                            if prod.get("name"):
                                st.write(f"**Producto:** {prod.get('name')}")
                            if prod.get("image"):
                                try:
                                    st.image(prod.get("image"), caption=prod.get("name"))
                                except Exception:
                                    st.info("Producto encontrado, pero no se pudo cargar la imagen.")
                    cv2.imshow("Lector en tiempo real - presiona 'q' para salir", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()

else:
    st.write("Detección en la página usando WebRTC. Permite acceder a la cámara en el navegador y procesar frames en Python.")
    try:
        from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
        import av
    except Exception as e:
        st.error("Faltan dependencias: instala 'streamlit-webrtc', 'av' y 'pyzbar'.")
        st.error(str(e))
    else:
        class BarcodeTransformer(VideoTransformerBase):
            def __init__(self):
                try:
                    import cv2
                    from pyzbar import pyzbar
                except Exception:
                    # Lanzar para que el error sea visible en la interfaz
                    raise
                self.cv2 = cv2
                self.pyzbar = pyzbar
                self.last_detection = None
                self.last_barcode = None

            def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
                img = frame.to_ndarray(format="bgr24")
                barcodes = self.pyzbar.decode(img)
                for barcode in barcodes:
                    (x, y, w, h) = barcode.rect
                    self.cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    barcodeData = barcode.data.decode("utf-8")
                    barcodeType = barcode.type
                    text = f"{barcodeData} ({barcodeType})"
                    self.cv2.putText(img, text, (x, y - 10), self.cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    # Guardar la última detección y el código
                    self.last_detection = text
                    self.last_barcode = barcodeData
                return av.VideoFrame.from_ndarray(img, format="bgr24")

        webrtc_ctx = webrtc_streamer(key="barcode-stream", video_transformer_factory=BarcodeTransformer, media_stream_constraints={"video": True, "audio": False})

        info_box = st.empty()
        product_box = st.empty()
        if webrtc_ctx.video_transformer:
            last = webrtc_ctx.video_transformer.last_detection
            if last:
                info_box.success(f"Última detección: {last}")
            else:
                info_box.info("No se ha detectado ningún código aún.")

        # Botón para buscar el producto detectado
        if st.button("Buscar producto detectado"):
            if webrtc_ctx.video_transformer and webrtc_ctx.video_transformer.last_barcode:
                barcode = webrtc_ctx.video_transformer.last_barcode
                product_box.info("Buscando producto...")
                prod = fetch_product_info(barcode)
                if prod:
                    if prod.get("name"):
                        product_box.write(f"**Producto:** {prod.get('name')}")
                    if prod.get("image"):
                        try:
                            product_box.image(prod.get("image"), caption=prod.get("name"))
                        except Exception:
                            product_box.info("Producto encontrado, pero no se pudo cargar la imagen.")
                else:
                    product_box.warning("No se encontró información del producto para ese código.")
            else:
                product_box.info("No hay código detectado todavía.")
                