# model_deployment.py

import tensorflow as tf
from flask import Flask, request, jsonify


def load_model():
    # Load the trained model
    model = tf.keras.models.load_model("trained_model.h5")
    return model


def preprocess_image(image):
    # Preprocess the image (resize, normalize, etc.)
    # Placeholder function, implement based on your preprocessing requirements
    return image


app = Flask(__name__)
model = load_model()


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    image = preprocess_image(image)
    prediction = model.predict(image)
    return jsonify(prediction.tolist())


if __name__ == "__main__":
    app.run(debug=True)
