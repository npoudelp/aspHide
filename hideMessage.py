import time
import numpy as np
from PIL import Image
import sys
import codecs


def getText():
    text = input("Enter the message: \n")
    text = text + " [END]"

    encodedText = ""

    for char in text:
        acsiiOfChar = ord(char)
        binOfChar = f"{acsiiOfChar:08b}"
        encodedText = encodedText + binOfChar

    return encodedText


def hide(imageName):
    img = Image.open(imageName)
    for y in range(img.size[0]):
        for x in range(img.size[1]):
            r, g, b = img.getpixel((x, y))

    input("Holding...")
