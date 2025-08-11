from flask import Flask, request, render_template
import joblib
import numpy as np

# Carga de modelo y escaladores
model = joblib.load('./model/insurance-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    age = ""

    if request.method == 'POST':
        age = (request.form.get('age') or "").strip()
        try:
            age_val = int(age)
            if age_val <= 0 or age_val > 120:
                raise ValueError("Edad fuera de rango razonable.")

            # Escala, predice e inversa
            X = np.array([[age_val]])
            Xs = sc_x.transform(X)
            yhat = model.predict(Xs)
            yhat_inv = sc_y.inverse_transform(yhat)

            result = round(float(yhat_inv[0][0]), 2)

        except Exception as e:
            error = f"Ocurrió un problema con el dato ingresado: {e}"

    return render_template('index.html', result=result, error=error, age=age)

if __name__ == '__main__':
    app.run(debug=True)
