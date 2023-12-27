import cv2
import numpy as np
import random
import pandas as pd
import os


def draw_circle(image, center, radius):
    cv2.circle(image, center, radius, (0, 0, 0), 1)


def draw_triangle(image, vertices):
    cv2.polylines(image, [vertices], isClosed=True, color=(0, 0, 0), thickness=1)


def draw_rectangle(image, rect):
    cv2.rectangle(image, rect[0], rect[1], (0, 0, 0), 1)

def generate_image(shape_type):
    image_size = (256, 256, 3)
    image = np.ones(image_size, dtype=np.uint8) * 255

    if shape_type == "circle":
        center = (random.randint(50, 200), random.randint(50, 200))
        radius = random.randint(20, 50)
        draw_circle(image, center, radius)
    elif shape_type == "triangle":
        vertices = np.array(
            [
                [random.randint(50, 200), random.randint(50, 200)],
                [random.randint(50, 200), random.randint(50, 200)],
                [random.randint(50, 200), random.randint(50, 200)],
            ],
            np.int32,
        )
        draw_triangle(image, vertices)
    elif shape_type == "rectangle":
        rect = [
            (random.randint(50, 200), random.randint(50, 200)),
            (random.randint(50, 200), random.randint(50, 200)),
        ]
        draw_rectangle(image, rect)

    return image


def save_image(image, label, index):
    filename = f"{label}_{index}.png"
    print(filename)
    cv2.imwrite(filename, image)


# generate training data
for i in range(1000):
    for shape in ["circle", "triangle", "rectangle"]:
        img = generate_image(shape)
        save_image(img, shape, i)

# label training data and save as csv
training_data = os.getcwd() + "/training_data/"
training_df = pd.DataFrame(columns=["filename", "label"])

for filename in os.listdir(training_data):
    if filename.endswith(".png"):
        label = filename.split("_")[0]
        training_df = training_df.append(
            {"filename": filename, "label": label}, ignore_index=True
        )

training_df.to_csv("training_data.csv", index=False)
