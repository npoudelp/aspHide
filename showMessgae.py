import time

import intro
import selectImage as si
from PIL import Image

escSeq = "001000000101101101000101010011100100010001011101"


def hold():
    checkToExit = input("\nEnter '!q' to exit: ")
    if checkToExit == '!q':
        pass
    else:
        hold()


def display(text):
    return text


def show(imageName):
    global escSeq
    si.clear()
    intro.showBrand()

    print(f"Selecting image {imageName}\n")
    binText = ""
    img = Image.open(imageName)

    for y in range(img.size[1]):
        if len(binText) >= 48:
            if binText[-48:] == escSeq:
                break
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            binR = f"{r:08b}"
            binText = binText + binR[6:]
            if len(binText) >= 48:
                if binText[-48:] == escSeq:
                    break

    startText = 0
    endText = startText + 8
    decodedMessage = ""

    loopBinText = len(binText) / 8
    loopCount = 0
    while loopCount < loopBinText:
        slicedBits = binText[startText: endText]
        startText = startText + 8
        endText = startText + 8
        desSlicedBits = int(str(slicedBits), 2)
        decodedMessage = decodedMessage + chr(desSlicedBits)
        loopCount = loopCount + 1

    print("Message extracted successfully...")
    time.sleep(0.5)
    si.clear()
    intro.showBrand()
    print("\n\tYour message ends with [END]\n")
    print(display(decodedMessage))
    hold()
