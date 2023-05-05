import time
from datetime import datetime
import os
from PIL import Image


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
    text = getText()
    pixelToHide = len(text) / 2
    img = Image.open(imageName)
    loadImg = img.load()
    pixelCount = 0
    textStart = 0
    textEnd = textStart + 2
    for y in range(img.size[1]):
        if pixelCount == pixelToHide:
            break
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            binR = f"{r:08b}"
            textSection = text[textStart: textEnd]
            textStart = textStart + 2
            textEnd = textStart + 2
            encodedBinR = binR[:6] + textSection
            encodedDecR = int(encodedBinR, 2)
            loadImg[x, y] = (encodedDecR, g, b)
            pixelCount = pixelCount + 1

            if pixelCount == pixelToHide:
                break

    img.save(f"{os.path.expanduser('~')}/encoded-{datetime.now()}.{'png'}", format="png")
    img.close()
    print("\nMessage hidden successfully...")
    hold = input("\nPress enter to continue...")
    time.sleep(1)


