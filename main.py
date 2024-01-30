import pyautogui, cv2, sys, keyboard, time, threading
from PIL import Image

photos = [Image.open("cactus-three-small.png"), Image.open("cactus-big.png"), Image.open("cactus-small.png"),
          Image.open("cactus-small-2.png")]


def start():
    print("start")
    pyautogui.moveTo(190, 490, 0.5)
    pyautogui.click()
    pyautogui.press('space')

def checkColour():
    return pyautogui.pixel(*pyautogui.position())

def quit():
    global exitProgram
    exitProgram = False

keyboard.add_hotkey('q', lambda: quit())

def  play2():
    global exitProgram
    exitProgram = True
    start()
    while exitProgram:
        if checkColour() != (247, 247, 247):
            pyautogui.press('space')
    sys.exit()

play2()

'''def play():
    flag = True
    while flag:
        for photo in photos:
            for cactus in pyautogui.locateAllOnScreen(photo, confidence=0.88):
                if cactus:
                    if cactus[0] < 350:
                        pyautogui.press('space')
                        print("jumped at", cactus[0])
        continue
play()'''

'''
def mend():
    print("enter the function")
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 20, y)
    print("exit")
'''

'''
def play2():
    global exitProgram, startTime
    exitProgram = True
    startTime = time.time()
    start()
    while exitProgram:
        if checkColour() != (247, 247, 247):
            pyautogui.press('space')
        if((time.time() - startTime) == 20):
            startTime = time.time()
            mend()
    sys.exit()
'''