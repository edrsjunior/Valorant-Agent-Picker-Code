import pyautogui
import keyboard


screenWidth, screenHeight = pyautogui.size()


print(f'Your screem size is {screenWidth}x{screenHeight}')
if screenWidth > 1920:
    screenWidth = 1920
    print("Screen width setted to Full HD")
if screenHeight > 1080:
    screenHeight = 1080
    print("Screen heith setted to Full HD")

print("Put your mouse on character box and press S for save")
keyboard.wait('s')
characterPosX, characterPosY = pyautogui.position()
print(f'Position of character is {characterPosX}x{characterPosY}')

print("Put your mouse on comfirm button and press S for save")
keyboard.wait('s')
comfirmPosX, comfirmPosY = pyautogui.position()
print(f'Position of character is {characterPosX}x{characterPosY}')

keyboard.wait('alt+s')
print("pass")
while True:
    pyautogui.click(characterPosX,characterPosY,2)
    pyautogui.click()
    print("click")
    pyautogui.click(comfirmPosX,comfirmPosY,2)
    print("click")
    if  keyboard.is_pressed('p'):
        keyboard.wait('alt+s')
    if  keyboard.is_pressed('esc'):
        exit()


