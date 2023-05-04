import time
import selectImage as si
from PIL import Image

escSeq = "001000000101101101000101010011100100010001011101"


def show(imageName):
    global escSeq

    print(imageName)
    binText = ""
    img = Image.open(imageName)

    print(len(escSeq))

    for x in range(img.size[0]):
        if len(binText) >= 42:
            if binText[-42:] == escSeq:
                break
        for y in range(img.size[1]):
            r, g, b = img.getpixel((x, y))
            binR = f"{r:08b}"
            binText = binText + binR[6:]
            if len(binText) >= 48:
                if binText[-42:] == escSeq:
                    break
    print(binText)
    startText = 0
    endText = startText + 8

    decodedMessage = ""
    for bits in binText:
        slicedBits = binText[startText: endText]
        startText = startText + 8
        endText = startText + 8
        desSlicedBits = int(slicedBits, 2)
        print(slicedBits)
        print(desSlicedBits)

        input("Holding...")


# show("/home/asp/aaa.jpg")
