# 📊 Calculadora de Precio de Seguro - Flask

Aplicación web desarrollada con **Flask** que utiliza un modelo de **Machine Learning** para estimar el costo de un seguro en función de la edad del usuario.

## 🚀 Características
- Interfaz web amigable con HTML y CSS.
- Backend con Flask y Python 3.12.
- Modelo entrenado previamente con `scikit-learn`.
- Escalado de variables de entrada y salida (`StandardScaler`).
- Predicción del precio en tiempo real.

## 📂 Estructura del proyecto
```
trabajo-final/
├─ app.py                # Aplicación Flask
├─ requirements.txt      # Dependencias
├─ model/
│  ├─ insurance-ml.pkl   # Modelo entrenado
│  ├─ scaler_x.pkl       # Escalador de entrada
│  └─ scaler_y.pkl       # Escalador de salida
└─ templates/
   └─ index.html         # Plantilla HTML
```

## 🛠 Requisitos
- Python 3.12 (recomendado)
- pip
- Entorno virtual (opcional pero recomendado)

## 📥 Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/jNrER/Modulo8-Flask.git
   cd Modulo8-Flask
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   # En Windows (cmd o PowerShell)
   venv\Scripts\activate
   # En Git Bash
   source venv/Scripts/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador**
   ```
   http://127.0.0.1:5000
   ```

## 📸 Vista previa
![Interfaz de la app](https://via.placeholder.com/800x400.png?text=Vista+previa+de+la+aplicaci%C3%B3n)

## 📄 Licencia
Este proyecto es de uso educativo.
