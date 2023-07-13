import os

import selectImage as si
import time
import intro
import about
import hideMessage as hm
import showMessgae as sm


def checkPython():
    check = os.system('python --version')
    if check != 0:
        print("Err:: This program needs python to run. Please install it and try again...")
        quit()


def showErr():
    global error
    return error
    error = ""


def main(ack):
    os.chdir(f"{os.path.dirname(__file__)}")
    global error
    si.clear()
    intro.showBrand()

    if ack == "hidden":
        print(f"\nYour message is hidden in {os.path.expanduser('~')}")
    if ack == "about":
        print(f"\nWould you like to give suggestion? https://nirojpoudel.com.np/pages/contact.php")

    if len(error) > 1:
        print(f'\nError::: {showErr()}\n')

    print("\nMain menu of aspHide\n")
    print("++[0]\tExit")
    print("++[1]\tHide message in image")
    print("++[2]\tRead message from image")
    print("++[3]\tAbout the application")
    print("\n")

    try:
        selectedNumber = int(input(f"Select your option (0-{optionRange}): "))
        if selectedNumber == 0:
            si.clear()
            print(open("./txtFiles/smile.txt", "r").read())
            time.sleep(1)
            si.clear()
            quit()
        elif selectedNumber == 1:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(0.5)
            if si.getName() == "[EXIT]":
                main("")
            else:
                hm.hide(si.getName())
                main("hidden")
        elif selectedNumber == 2:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(0.5)
            if si.getName() == "[EXIT]":
                main("")
            else:
                sm.show(si.getName())
                main("shown")
        elif selectedNumber == 3:
            about.aboutApp()
            main("about")
        elif selectedNumber > 3 or selectedNumber < 0:
            error = "Number out of range"
            main("")
        else:
            error = "Unexpected error occurred..."
    except ValueError:
        error = "Only number accepted"
        main("")


os.chdir(f"{os.path.dirname(__file__)}")
error = ""
aspShowRun = False
optionRange = "3"
si.clear()
intro.showAsp()
time.sleep(0.01)
checkPython()
main("")
