from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)

# Enable CORS for frontend connection
CORS(app)

# Load trained model and vectorizer
model = pickle.load(open("ml_model/model.pkl", "rb"))
vectorizer = pickle.load(open("ml_model/vectorizer.pkl", "rb"))


@app.route("/")
def home():
    return "Dark Web Threat Intelligence System Running"


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        text = data["text"]

        # Convert text to vector
        text_vector = vectorizer.transform([text])

        # Predict threat level
        prediction = model.predict(text_vector)[0]

        # Risk score logic
        if prediction == "High":
            risk_score = 9
        elif prediction == "Medium":
            risk_score = 6
        else:
            risk_score = 2

        return jsonify({
            "input": text,
            "threat_level": prediction,
            "risk_score": risk_score
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)