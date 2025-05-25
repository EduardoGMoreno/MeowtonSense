from flask import Flask, render_template, request, jsonify, send_from_directory, Response
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import os
import uuid
import cv2
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

model = YOLO("best.pt")

def detectar_objetos(imagen_path):
    results = model.predict(source=imagen_path, save=False)
    detections = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls]
            detections.append({'name': name, 'confidence': round(conf * 100, 2)})

    result_name = f"result_{uuid.uuid4().hex[:6]}.jpg"
    save_path = os.path.join(RESULT_FOLDER, result_name)
    results[0].save(filename=save_path)

    return result_name, detections

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            result_image, detections = detectar_objetos(filepath)
            os.remove(filepath)
            return render_template('index.html', result_image=result_image, detections=detections)

    return render_template('index.html')

# STREAMING CON CAMARA EN TIEMPO REAL CADA 2 SEGUNDOS
def gen_frames():
    cap = cv2.VideoCapture(0)
    last_time = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        current_time = time.time()
        if current_time - last_time >= 2:
            # Forzar confianza baja y detectar
            results = model(frame, conf=0.1)

            # Mostrar detecciones en consola
            print("Detecciones:", results[0].boxes)

            # Dibujar cajas y etiquetas si hay resultados
            frame = results[0].plot()
            last_time = current_time

            # Guardar solo si hay detecciones
            if results[0].boxes:
                filename = f"cam_result_{uuid.uuid4().hex[:6]}.jpg"
                cv2.imwrite(os.path.join("static", filename), frame)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Para validación SSL si la necesitas después
@app.route('/.well-known/acme-challenge/<filename>')
def certbot_static(filename):
    return send_from_directory('/var/www/letsencrypt/.well-known/acme-challenge/', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
