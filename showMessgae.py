import time
import os
from datetime import datetime

from intro import showBrand
import selectImage as si
from PIL import Image

escSeqForMessage = "001000000101101101000101010011100100010001011101"
escSeqForPassword = "01011011011110110101111001011101"
passwordFlag = 0
wrongCount = 0
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
        return
    elif checkToExit == 'w!':
        writeTextToFile(text)
        si.clear()
        print(f"Your message is saved in {fileExp}")
        holding = input("Enter to continue...")
    else:
        hold(text)


def display(text):
    return text


def checkPassword():
    global escSeqForPassword, imgName, passwordFlag, wrongCount
    if passwordFlag != 0:
        si.clear()
        print("Wrong password\n")
    password = input("Password (for main menu: [MAIN]): ")
    password = password + '[{^]'
    encodedPassword = ""
    if password == '[MAIN][{^]':
        return '[MAIN]'
    else:
        passwordFromImage = ""
        for char in password:
            acsiiOfChar = ord(char)
            binOfChar = f"{acsiiOfChar:08b}"
            encodedPassword = encodedPassword + binOfChar

        img = Image.open(imgName)
        for y in range(img.size[1]):
            if len(passwordFromImage) >= 32:
                if passwordFromImage[-32:] == escSeqForPassword:
                    break
            for x in range(img.size[0]):
                r, g, b = img.getpixel((x, y))
                binR = f'{r:08b}'
                passwordFromImage = passwordFromImage + binR[6:]
                if len(passwordFromImage) >= 32:
                    if passwordFromImage[-32:] == escSeqForPassword:
                        break

        if passwordFromImage == encodedPassword:
            return '[YES]'
        else:
            passwordFlag = 1
            wrongCount = wrongCount + 1
            if wrongCount >= 3:
                return '[NO]'
            checkPassword()


def show(imageName):
    global escSeqForMessage, passwordFlag, wrongCount, imgName
    imgName = imageName
    passwordFlag = 0
    wrongCount = 0
    si.clear()

    status = checkPassword()

    if status == '[YES]':
        print(f"Selecting image {imageName}\n")
        binText = ""
        img = Image.open(imageName)

        for y in range(img.size[1]):
            if len(binText) >= 48:
                if binText[-48:] == escSeqForMessage:
                    break
            for x in range(img.size[0]):
                r, g, b = img.getpixel((x, y))
                binR = f"{r:08b}"
                binText = binText + binR[6:]
                if len(binText) >= 48:
                    if binText[-48:] == escSeqForMessage:
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
        time.sleep(1)
        si.clear()
        os.chdir(f"{os.path.dirname(__file__)}")
        showBrand()
        print("\nYour message ends with [END]\n")
        print(display(decodedMessage))
        hold(decodedMessage)

    elif status == '[NO]':
        name = input("Hold: ")
        print(name)
    else:
        print("\nUnknown error occurred...")


message = ""
imgName = ""
