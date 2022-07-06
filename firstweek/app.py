from flask import request, render_template
from flask import Flask
import joblib
model = joblib.load("decision tree")
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form['rates'])
        result = model.predict([[rates]])
        print(result)
        return render_template("index.html", result=result[0])
    else:
        return render_template("index.html", result="waitting")


if __name__ == "__main__":
    app.run(port=9999)
