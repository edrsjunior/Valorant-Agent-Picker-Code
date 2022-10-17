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
            print("\nStoping...")
            print("Press Alt+s to continue or q to exit to menu \n")
            # wait keyboard press Alt+s or 0
            sleep(0.5)
            while True:
                if(keyboard.is_pressed("Alt+s")):
                    print("Continuing...")
                    break
                if(keyboard.is_pressed("Alt+q")):
                    print("Exiting...")
                    out = True
                    break
            
            
