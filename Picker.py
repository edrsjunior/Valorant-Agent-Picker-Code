#                               References: 
# https://www.pythontutorial.net/advanced-python/python-threading/
# https://www.w3schools.com/python/python_variables_global.asp
# https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/



from threading import Thread
import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between clicks

def  clickChampion():
    global keepRunning 
    while True:
        pyautogui.click(characterPosX,characterPosY) #send click into specified position
        pyautogui.click(comfirmPosX,comfirmPosY)
        if  keepRunning:
            break
       
screenWidth, screenHeight = pyautogui.size() #get main screen just for fun 

print(f'Your screem size is {screenWidth}x{screenHeight}') 

print("Put your mouse on character box and press Ctrl for save")
keyboard.wait('ctrl') #wait the Ctrl key be pressed
characterPosX, characterPosY = pyautogui.position() #get current mouse position
print(f'Position of character is {characterPosX}x{characterPosY}')

print("Put your mouse on confirm button and press Ctrl for save")
keyboard.wait('ctrl')
confirmPosX, confirmPosY = pyautogui.position()
print(f'Position of confirm button is {confirmPosX}x{confirmPosY}')

while True:
    print("Waiting... Press <alt+s> to start")
    keyboard.wait('alt+s')
    keepRunning = False
    tClick = Thread(target = clickChampion)
    tClick.start()
    print("Running... Press <q> to stop")
    keyboard.wait('q')
    keepRunning = True
    tClick.join()
    
    


    
    



