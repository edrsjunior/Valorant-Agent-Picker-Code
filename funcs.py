from concurrent.futures import thread
import pyautogui
import keyboard
from threading import Thread

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY):
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(960, 815)

        if keyboard.is_pressed("q"):
            print("Stop Click")
            break   
    
