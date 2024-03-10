# prepare_dataset.py

import os
import cv2
import numpy as np


def load_images_from_directory(directory):
    images = []
    labels = []
    for label in os.listdir(directory):
        label_dir = os.path.join(directory, label)
        for image_file in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_file)
            image = cv2.imread(image_path)
            image = cv2.resize(image, (224, 224))  # Resize images to a common size
            images.append(image)
            labels.append(label)
    return np.array(images), np.array(labels)


def main():
    dataset_directory = "dataset"
    images, labels = load_images_from_directory(dataset_directory)
    print(f"Loaded {len(images)} images with {len(np.unique(labels))} classes.")


if __name__ == "__main__":
    main()
