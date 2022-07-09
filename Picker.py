import pyautogui
import keyboard

pyautogui.PAUSE = 0.01 #Set low delay between clicks
screenWidth, screenHeight = pyautogui.size() #get main screen just for fun 

print(f'Your screem size is {screenWidth}x{screenHeight}') 

print("Put your mouse on character box and press S for save")
keyboard.wait('ctrl') #wait the Ctrl key be pressed
characterPosX, characterPosY = pyautogui.position() #get current mouse position
print(f'Position of character is {characterPosX}x{characterPosY}')

print("Put your mouse on confirm button and press S for save")
keyboard.wait('ctrl')
comfirmPosX, comfirmPosY = pyautogui.position()
print(f'Position of confirm button is {characterPosX}x{characterPosY}')

keyboard.wait('alt+s')
print("Clicking! Press <p> to pause or <Esc> to close")
while True:
    pyautogui.click(characterPosX,characterPosY) #send click into specified position
    pyautogui.click()
    #print("click")
    pyautogui.click(comfirmPosX,comfirmPosY)
    #print("click")
    
    if  keyboard.is_pressed('p'):
        print("Paused! Press <alt+s> to continue  or esc to close")
        while True:
            #event = keyboard.read_event()
            if  keyboard.is_pressed('alt+s'):
                break
            if  keyboard.is_pressed('esc'):
                exit()
    if  keyboard.is_pressed('esc'):
        exit()


