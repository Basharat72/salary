from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_salary = None
    if request.method == "POST":
        exp = float(request.form["experience"])
        predicted_salary = model.predict(np.array([[exp]]))[0]
    return render_template("index.html", prediction=predicted_salary)

if __name__ == "__main__":
    app.run(debug=True)
