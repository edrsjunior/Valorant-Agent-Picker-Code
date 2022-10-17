from concurrent.futures import thread
from multiprocessing.connection import wait
from time import sleep
from multiprocessing.connection import wait
from time import sleep
import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY,btnX,btnY):
    pyautogui.click(characterPosX,characterPosY) #send click into specified position
    pyautogui.click(btnX,btnY) #send click into specified position
            
def showMenu():
    #-------------------------MENU-----------------------------
    print("MENU \n")
    print("1 - Para definir a posição do botao confirmar (Necessário apenas a primeira vez)")
    print("2 - Para definir a posição do personagem (Necessário apenas a primeira vez)")
    print("3 - Para escolher um persongem pré-definido")
    print("0 - Exit")
    #----------------------------------------------------------
