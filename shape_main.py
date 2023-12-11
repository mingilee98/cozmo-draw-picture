from PIL import Image, ImageOps
import base64
from io import BytesIO
import sys
import os
import detection
import cozmo
import cozmo_movement


def main():
    # get the image from the input
    encoded_string = sys.argv[1]

    save_image(encoded_string)
    shape = detection.find_shape("images/shape_image.png")

    cozmo_function = None
    if shape == "Triangle":
        cozmo_function = cozmo_movement.move_triangle
    elif shape == "Rectangle":
        cozmo_function = cozmo_movement.move_rectangle
    elif shape == "Pentagon":
        cozmo_function = cozmo_movement.move_pentagon
    elif shape == "Hexagon":
        cozmo_function = cozmo_movement.move_hexagon
    elif shape == "Circle":
        cozmo_function = cozmo_movement.move_circle

    cozmo.run_program(cozmo_function, use_viewer=False, force_viewer_on_top=False)


def save_image(encoded_string):
    # save img
    image_bytes = base64.b64decode(encoded_string)
    img = Image.open(BytesIO(image_bytes))

    # new image with a white background
    new_image = Image.new("RGB", img.size, (255, 255, 255))
    new_image.paste(img, (0, 0), img)

    resized_image = new_image.resize((256, 256))

    path = os.getcwd() + "/images"
    resized_image.save(path + "/shape_image.png")


if __name__ == "__main__":
    main()
