from concurrent.futures import thread
import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between click

def  clickChampion(characterPosX,characterPosY,btnX,btnY):
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(btnX,btnY)
        if keyboard.is_pressed("q"):
            print("Stoping...")
            print("Press y to continue or 0 to exit")
            op = input("Insira a opção desejada!")	
            if op == "0":
                break   
            
