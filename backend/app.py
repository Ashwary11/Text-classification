from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Allow frontend to access the API

# Load Model & Vectorizer
model = joblib.load(r"C:\Users\ashwa\text-classification\model\text_classifier.pkl")
vectorizer = joblib.load(r"C:\Users\ashwa\text-classification\model\vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]

    return jsonify({"prediction": "positive" if prediction == 1 else "negative"})

if __name__ == "__main__":
    app.run(debug=True)
