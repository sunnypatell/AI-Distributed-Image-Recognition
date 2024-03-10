# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    # Placeholder function for model prediction
    # You can replace this with your actual model prediction logic
    data = request.json
    image_path = data["image_path"]
    # Perform model prediction here
    prediction = {"class": "dog", "confidence": 0.85}  # Example prediction
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
