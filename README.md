# 🐾 MeowtonSense

**MeowtonSense** es una aplicación web de visión artificial diseñada para ayudarte a monitorear a tu mascota en tiempo real mediante detección inteligente usando YOLOv8.

🎥 Puedes subir imágenes para detectar objetos o activar tu cámara para monitoreo en vivo con procesamiento automático. ¡Ideal para proteger y observar a tu peludo favorito!

---

## 🖼️ Capturas de pantalla

### Interfaz principal
![UI](https://raw.githubusercontent.com/EduardoGMoreno/MeowtonSense/main/MeowtonSenseUI.png)

### Detección en tiempo real
![LiveCam](https://raw.githubusercontent.com/EduardoGMoreno/MeowtonSense/main/LiveCamMeowtonSense.png)

---

## 🚀 ¿Cómo ejecutar?

1. **Clona el repositorio:**

En el Bash
git clone https://github.com/EduardoGMoreno/MeowtonSense.git
cd MeowtonSense
python -m venv venv
venv\\Scripts\\activate       # En Windows
pip install -r requirements.txt
Ejecuta la aplicación:

En el Bash Ejecuta
python app.py
Y abre tu navegador en:
http://localhost:5000

🔧 Tecnologías utilizadas
Python 3.12

Flask

YOLOv8 (Ultralytics)

OpenCV

HTML5 + CSS3

👨‍💻 Desarrollado por:

Jesus Eduardo García Moreno

Andrik Calderón Macías

Oscar David Rosales Gómez

🐶 ¿Por qué MeowtonSense?
Vigila a tu peludo favorito desde cualquier lugar.
Descubre quién anda husmeando y mantén a tu mascota siempre a la vista con detección inteligente en tiempo real.
---

## ✨ Funciones futuras

- 🌐 **Subir el proyecto a la web:** desplegar MeowtonSense en un servidor (como Render, Railway o un VPS) para que esté disponible desde cualquier navegador sin necesidad de instalar nada localmente.
- 📱 **Interfaz móvil responsiva:** adaptar la interfaz para que funcione perfectamente en teléfonos y tabletas.
- 💬 **Notificaciones inteligentes:** enviar alertas si se detecta movimiento o una mascota en áreas específicas.
- 🧠 **Entrenamiento personalizado:** permitir al usuario subir sus propias imágenes para entrenar nuevas clases fácilmente.
- 📊 **Historial de detecciones:** guardar las detecciones con fecha y hora para su revisión posterior.
- 🔒 **Acceso con contraseña:** agregar autenticación para proteger la vista de la cámara en tiempo real.

