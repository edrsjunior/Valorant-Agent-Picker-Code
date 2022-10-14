from concurrent.futures import thread
from multiprocessing.connection import wait
from time import sleep
import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY,btnX,btnY):
    out = False
    while not out:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(btnX,btnY)
        if keyboard.is_pressed("q"):
            print("\n\nStoping...\n")
            print("Press y to continue or 0 to exit\n")
            # wait keyboard press y or 0
            while True:
                if(keyboard.is_pressed("y")):
                    print("Continuing...")
                    break
                if(keyboard.is_pressed("0")):
                    print("Exiting...")
                    out = True
                    break
            
            
