# app.py

import os
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

app = Flask(__name__)

# Load the pre-trained ResNet50 model
model = tf.keras.applications.ResNet50(weights="imagenet")


# Function to preprocess the uploaded image
def preprocess_image(image):
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array


@app.route("/predict", methods=["POST"])
def predict():
    # Check if a file is uploaded
    if "image" not in request.files:
        return jsonify({"error": "No image provided"})

    # Get the uploaded image file
    image = request.files["image"]

    # Read the image file and preprocess it
    img = Image.open(image)
    img_array = preprocess_image(img)

    # Make prediction
    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=3)[0]

    # Format prediction results
    predictions = [
        {"label": label, "probability": float(prob)}
        for (_, label, prob) in decoded_preds
    ]

    return jsonify({"predictions": predictions})


if __name__ == "__main__":
    app.run(debug=True)
