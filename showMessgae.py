import time

from PIL import Image

escSeq = "001000000101101101000101010011100100010001011101"


def show(imageName):
    global escSeq

    print(imageName)
    binText = ""
    img = Image.open(imageName)

    # print(len(escSeq))

    for y in range(img.size[1]):
        if len(binText) >= 42:
            if binText[-42:] == escSeq:
                break
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            binR = f"{r:08b}"
            binText = binText + binR[6:]
            # print(binText)
            print(binR)
            if len(binText) >= 48:
                if binText[-48:] == escSeq:
                    break

            input("Holding...")

    print(binText)
    input("Holding...")

show("/aaa.jpeg")
