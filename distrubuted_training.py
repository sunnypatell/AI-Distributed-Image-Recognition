# distributed_training.py

import tensorflow as tf
from tensorflow.keras.applications import ResNet50
import prepare_dataset  # Import the dataset preparation module


def main():
    # Load the image dataset
    images, labels = prepare_dataset.load_images_from_directory("dataset")

    # Define model architecture
    strategy = (
        tf.distribute.MirroredStrategy()
    )  # Utilize all available GPUs for training
    with strategy.scope():
        model = ResNet50(
            weights=None, input_shape=(224, 224, 3), classes=len(np.unique(labels))
        )
        model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )

    # Train the model
    model.fit(images, labels, epochs=10, batch_size=32)
    print("Training completed.")


if __name__ == "__main__":
    main()
