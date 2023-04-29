import time

def showAsp():
    with open('asp.txt', 'r') as brand:
        lines = [line.rstrip('\n') for line in brand.readlines()]
        for line in lines:
            print(line)
            time.sleep(1 / 50)


def showBrand():
    with open('brand.txt', 'r') as brand:
        lines = [line.rstrip('\n') for line in brand.readlines()]
        for line in lines:
            print(line)
            time.sleep(1 / 10)