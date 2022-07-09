from ast import If
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

characterPosX = input("Character column?")
characterPosY = input("Character line?")

keyboard.wait('alt+s')
while True:
    pyautogui.click(characterPosX,characterPosY,2,100)
    pyautogui.click(characterPosX,characterPosY,2,100)
    keyboard.wait('p')
    keyboard.wait('alt+s')


