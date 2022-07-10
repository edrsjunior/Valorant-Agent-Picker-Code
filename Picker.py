from threading import Thread
import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between clicks

def  clickChampion():
    
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(comfirmPosX,comfirmPosY)
        global keepRunning 
        if  keepRunning:
            break
       



screenWidth, screenHeight = pyautogui.size() #get main screen just for fun 

print(f'Your screem size is {screenWidth}x{screenHeight}') 

print("Put your mouse on character box and press Ctrl for save")
keyboard.wait('ctrl') #wait the Ctrl key be pressed
characterPosX, characterPosY = pyautogui.position() #get current mouse position
print(f'Position of character is {characterPosX}x{characterPosY}')

print("Put your mouse on confirm button and press S for save")
keyboard.wait('ctrl')
comfirmPosX, comfirmPosY = pyautogui.position()
print(f'Position of confirm button is {characterPosX}x{characterPosY}')

while True:
    keyboard.wait('alt+s')
    keepRunning = False
    tClick = Thread(target = clickChampion)
    tClick.start()
    keyboard.wait('q')
    keepRunning = True
    tClick.join()
    
    


    
    



