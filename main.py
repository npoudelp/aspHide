import selectImage as si
import time
import intro
import about
import hideMessage as hm
import showMessgae as sm


def showErr():
    global error
    return error
    error = ""


def main(ack):
    global error
    si.clear()
    intro.showBrand()

    if ack == "hidden":
        print(f"\nYour message is hidden in {si.getName()}")
    if ack == "about":
        print(f"\nWould you like to give suggestion? nirojpoudel.com.np")

    if (len(error) > 1):
        print(f'\nError::: {showErr()}\n')

    print("\nThis is the main menu of aspHide")
    print("1>\tHide message in image")
    print("2>\tRead message from image")
    print("3>\tAbout the application")
    print("\n")

    try:
        selectedNumber = int(input(f"Select your option (1-{optionRange}): "))
        if selectedNumber == 1:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(2)
            hm.hide()
            main("hidden")
        elif selectedNumber == 2:
            si.start()
            print(f"Full path of your image is {si.getName()}")
            time.sleep(2)
            sm.show()
            main("shown")
        elif selectedNumber == 3:
            about.aboutApp()
            main("about")
        else:
            error = "Number out of range"
    except ValueError:
        error = "Only number accepted"
        main()


error = ""
aspShowRun = False
optionRange = "3"
si.clear()
intro.showAsp()
time.sleep(0.5)
main("")
