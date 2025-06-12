from flask import Flask, request, render_template, redirect, url_for, flash
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.optimizers import Adam
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'
MODEL_PATH = 'model/modelo_final.h5'
IMG_SIZE = (100, 100)
CLASSES = ['frutas', 'higiene', 'ropa', 'tecnologia']

# Asegura carpetas necesarias
os.makedirs('model', exist_ok=True)
os.makedirs('static', exist_ok=True)

def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(100,100,3)),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Flatten(),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dense(len(CLASSES), activation='softmax')
    ])
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

@app.route('/', methods=['GET', 'POST'])
def index():
    pred = None
    img_url = None
    entrenado = os.path.exists(MODEL_PATH)

    if request.method == 'POST' and 'imagen' in request.files:
        if not entrenado:
            return render_template('index.html', pred="Modelo no entrenado", entrenado=False)
        model = load_model(MODEL_PATH)
        img = request.files['imagen']
        if not img.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            flash('❌ El archivo debe ser una imagen (.jpg, .png)', 'danger')
            return redirect(url_for('index'))
        path = os.path.join('static', img.filename)
        img.save(path)
        img_url = '/' + path

        image = load_img(path, target_size=IMG_SIZE)
        x = img_to_array(image)
        x = np.expand_dims(x, axis=0) / 255.0
        pred = CLASSES[np.argmax(model.predict(x))]

    return render_template('index.html', pred=pred, img_url=img_url, entrenado=entrenado)

@app.route('/reemplazar_modelo', methods=['POST'])
def reemplazar_modelo():
    archivo = request.files.get('modelo')
    if archivo:
        if not archivo.filename.endswith('.h5'):
            flash('❌ El archivo debe ser un modelo en formato .h5', 'danger')
            return redirect(url_for('index'))

        try:
            if os.path.exists(MODEL_PATH):
                os.remove(MODEL_PATH)
            archivo.save(MODEL_PATH)
            flash('✅ Modelo reemplazado exitosamente.', 'success')
        except Exception as e:
            flash(f'❌ Error al guardar el modelo: {str(e)}', 'danger')
    else:
        flash('⚠️ No se seleccionó ningún archivo.', 'warning')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)