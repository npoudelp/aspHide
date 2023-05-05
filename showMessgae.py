import time
import os
from datetime import datetime

from intro import showBrand
import selectImage as si
from PIL import Image

escSeq = "001000000101101101000101010011100100010001011101"

fileExp = ""


def writeTextToFile(text):
    global imgName, fileExp
    fileName = f"{os.path.expanduser('~')}/{datetime.now()}.txt"
    fileExp = fileName
    openFile = open(fileName, 'w')
    openFile.write(text)


def hold(text):
    checkToExit = input("\nEnter 'q!' to exit without saving and 'w!' to save and exit: ")
    if checkToExit == 'q!':
        pass
    elif checkToExit == 'w!':
        writeTextToFile(text)
        si.clear()
        print(f"Your message is saved in {fileExp}")
        holding = input("Enter to continue...")
    else:
        hold(text)


def display(text):
    return text


def show(imageName):
    global escSeq
    global imgName
    imgName = imageName
    si.clear()

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
    time.sleep(2)
    si.clear()
    os.chdir(f"{os.path.dirname(__file__)}")
    showBrand()
    print("\nYour message ends with [END]\n")
    print(display(decodedMessage))
    hold(decodedMessage)


message = ""
imgName = ""
