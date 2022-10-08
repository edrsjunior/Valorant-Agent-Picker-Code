from concurrent.futures import thread
from multiprocessing.connection import wait
import time
import pyautogui
import keyboard
from threading import Thread

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY,btnX,btnY):
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(btnX,btnY)
        if keyboard.is_pressed("q"):
            break
