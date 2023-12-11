from PIL import Image, ImageOps
import base64
from io import BytesIO
import sys
import os
import cv2


def main():
    # get the image from the input
    if len(sys.argv) > 1:
        encoded_string = sys.argv[1]
    else:
        print("No input provided.")

    # save img
    image_bytes = base64.b64decode(encoded_string)
    img = Image.open(BytesIO(image_bytes))

    # new image with a white background
    new_image = Image.new("RGB", img.size, (255, 255, 255))
    new_image.paste(img, (0, 0), img)

    resized_image = new_image.resize((256, 256))

    path = os.getcwd() + "/images"
    resized_image.save(path + "/image.png")


if __name__ == "__main__":
    main()
