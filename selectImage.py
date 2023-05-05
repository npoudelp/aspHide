import os


def clear():
    os.system('clear')


def showErr():
    global error
    return error
    error = ""


def start():
    global admin, userDir, error
    if len(error) > 0:
        print(f'\nError::: {showErr()}\n')

    userDir = input("Directory you want to begin with (/): ")
    if userDir != "" and os.path.exists(userDir):
        select()
    elif userDir == "":
        print("\nSelecting root (/) directory as default directory\n")
        userDir = "/"
        select()
    elif not os.path.exists(userDir):
        error = "Given directory is not valid"
        start()
    else:
        print(f"\nError on selection: Please report to {admin}\n")


def getLenOfDir():
    global userDir
    return len(os.listdir(userDir))


def select():
    global userDir, error, imageName, admin

    clear()

    if len(error) > 0:
        print(f'\nError::: {showErr()}\n')

    print(f"You are on {userDir}")
    for count, file in enumerate(os.listdir(userDir)):
        print(f"{count + 1}>\t{file}")

    try:
        fileNumber = int(input(f"Select file number (1-{getLenOfDir()}): "))
        if getLenOfDir() >= fileNumber >= 1:
            selectedFile = os.listdir(userDir)[fileNumber - 1]
            newUserDir = f"{userDir}/{selectedFile}"
            if os.path.isdir(newUserDir) and '.' not in selectedFile:
                os.chdir(newUserDir)
                userDir = newUserDir
                select()
            else:
                if selectedFile.endswith('.png') or selectedFile.endswith('.jpg') or selectedFile.endswith('.jpeg'):
                    imageName = f'{userDir}/{selectedFile}'
                else:
                    error = "Only .jpeg and .jpg file format are supported for now"
                    select()

        elif fileNumber == 0:
            end()

        else:
            error = "Number out of range"
            select()
    except ValueError:
        error = "Only numbers accepted"
        select()


def getName():
    global imageName
    return imageName


def end():
    global imageName
    imageName = "[EXIT]"


admin = "nirojpoudel.com.np"
error = ""
imageName = None
userDir = None
