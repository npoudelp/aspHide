import time
from os import system
from intro import showBrand
def aboutApp():
    system("clear")
    showBrand()
    print("\n")
    aboutFile = open("description.txt", "r")
    print(aboutFile.read())
    print("\n")
    userInput = input("Enter any to go to main menu: ")
    if userInput:
        print(userInput)
    else:
        aboutApp()
