import pyautogui
import keyboard
from threading import Thread

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY):
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(960, 815)

def startClicks(characterPosX,characterPosY):
    print("Waiting... Press Alt+S to start script")
    keyboard.wait('alt+s')
    tClick = Thread(target = clickChampion(characterPosX,characterPosY))
    tClick.start()
    print("Running... Press Q to stop")
    keyboard.wait('q')
    tClick.join()
