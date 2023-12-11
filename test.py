import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd


model = tf.keras.models.load_model("shape_detection_model.keras")

# load and preprocess the PNG image
img_path = "images/image.png"
# img_path = "training_data/rectangle_6.png"
img = image.load_img(img_path, target_size=(256, 256))
img_array = image.img_to_array(img)

# turn gray area into black
gray_areas = img_array <= 250
img_array[gray_areas] = 0
plt.imshow(img_array)
plt.show()
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0


# make predictions
predictions = model.predict(img_array)

class_labels = ["circle", "rectangle", "triangle"]
predicted_class = class_labels[np.argmax(predictions)]

print(f"The predicted class is: {predicted_class}")
