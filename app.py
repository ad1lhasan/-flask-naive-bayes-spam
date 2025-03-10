from flask import Flask, render_template, request
import pickle

# Load Model & Vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        message = request.form["message"]
        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template("index.html", prediction=result, message=message)

if __name__ == "__main__":
    app.run(debug=True)

