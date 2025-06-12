# 🧠 Clasificador de Imágenes de Productos (Flask + Keras)

Esta aplicación web permite **cargar, reemplazar y utilizar modelos entrenados** para clasificar imágenes en categorías como **frutas, higiene, ropa y tecnología**. Funciona con modelos en formato `.h5` generados previamente con TensorFlow/Keras.

---

## 📌 Características principales

- Subida de imágenes desde el navegador para clasificación.
- Carga dinámica de modelos `.h5` (ya entrenados).
- Reemplazo del modelo actual desde la interfaz (sin reiniciar la app).
- Validación y mensajes de error ante formatos incorrectos.
- Interfaz limpia basada en Bootstrap 5.

---

## 🗂️ Estructura del proyecto

```
Flask_ImagenApp/
├── app.py                 # Backend principal de la aplicación
├── requirements.txt       # Dependencias necesarias
├── model/
│   └── modelo_final.h5    # Modelo actual en uso (sobrescribible)
├── static/                # Imágenes subidas por el usuario
├── templates/
│   └── index.html         # Interfaz de usuario (HTML + Bootstrap)
```

---

## ⚙️ Requisitos

- Python 3.8+
- TensorFlow 2.x
- Flask
- NumPy
- Pillow

Instala todo con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo usar la aplicación

### 1. Ejecutar localmente

```bash
python app.py
```

Luego, abre tu navegador en:  
👉 `http://127.0.0.1:5000`

---

### 2. Subir y reemplazar el modelo

1. En la parte superior de la interfaz, selecciona tu modelo `.h5` entrenado (por ejemplo, `modelo_mobilenetv2.h5`).
2. Haz clic en **"Reemplazar Modelo"**.
3. Verás un mensaje de confirmación si fue exitoso (`✅ Modelo reemplazado correctamente`).

⚠️ Solo se aceptan archivos con extensión `.h5`. Si se intenta subir una imagen o un archivo inválido, se mostrará un error.

---

### 3. Clasificar una imagen

1. Selecciona una imagen `.jpg`, `.jpeg` o `.png`.
2. Haz clic en **"Clasificar Imagen"**.
3. Verás el resultado y la imagen en pantalla.

---

## 🧪 Entrenamiento del modelo (externo)

Puedes usar Google Colab o tu entorno local para entrenar modelos CNN o Transfer Learning y luego exportarlos como `.h5`. Ejemplo:

```python
model.save("modelo_final.h5")
```

Luego, súbelo en la interfaz web para reemplazar el actual.

---

## 🎨 Clases soportadas (predefinidas)

```python
CLASSES = ['frutas', 'higiene', 'ropa', 'tecnologia']
```

Estas clases se usan para mapear la salida `softmax` del modelo. Asegúrate de entrenar tu modelo con estas etiquetas.

---

## ✅ Validaciones incluidas

- ✔ Verifica que el modelo sea `.h5` antes de reemplazar.
- ✔ Verifica que la imagen sea `.jpg`, `.jpeg` o `.png` antes de clasificar.
- ✔ Muestra mensajes de confirmación o error en pantalla para todas las acciones.

---

## 📎 Autor

Kevin Santiago Martínez Molina
Estudiante de Ingeniería de Sistemas - ITM Medellín  
Proyecto académico integrador – Clasificación de imágenes con redes neuronales