#                               References: 
# https://www.pythontutorial.net/advanced-python/python-threading/
# https://www.w3schools.com/python/python_variables_global.asp
# https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/



from ast import While
import pyautogui
import keyboard
import funcs
import json
from threading import Thread

global stopClick
screenWidth, screenHeight = pyautogui.size() #get main screen just for fun 
print(f'Your screem size is {screenWidth}x{screenHeight}') 

op = -1
while op != 0:
    #-------------------------MENU-----------------------------
    print("MENU \n")
    print("1 - Para definir a posição do botao confirmar (Necessário apenas a primeira vez)")
    print("2 - Para definir a posição do personagem (Necessário apenas a primeira vez)")
    print("3 - Para escolher um persongem pré-definido")
    print("0 - Exit")
    op = int(input("Insira a opção desejada!  "))
    #----------------------------------------------------------

    #leitura de arquivo
    print("\nReading Agent Position File")
    data = None
    with open('agents.json','r',encoding="utf-8") as f:
        data = json.load(f)

    if op == 1:
        print("Put your mouse on confirm button and press Ctrl for save")
        keyboard.wait('ctrl') #wait the Ctrl key be pressed
        confirmBtnX,confirmBtnY = pyautogui.position() #get current mouse position
        data["ConfirmBtn"] = {
                "x" : confirmBtnX,
                "y" : confirmBtnY
            }
    if op == 2:
        print("Put your mouse on character box and press Ctrl for save")
        keyboard.wait('ctrl') #wait the Ctrl key be pressed
        characterPosX, characterPosY = pyautogui.position() #get current mouse position
        agentName = input("Insert Agent Name: ")
        op = 'y'
        if agentName in data:
            op = str(input("The agent is alredy saved, are you sure that want replace the position? Yes or No! "))

        if op.lower() in ['y','yes']:
            print('Recording Position...')
            data[agentName] = {
                "x" : characterPosX,
                "y" : characterPosY
            }
            
            with open('agents.json','w',encoding="utf-8") as f:
                f.write(json.dumps(data))
            print(f'Position of character is {characterPosX}x{characterPosY} Recorded')
            
    elif op == 3:
        agentName = input("Insert Agent Name: ")
        characterPosX = data[agentName]['x']
        characterPosY = data[agentName]['y']
        print(f'X={characterPosX} e Y:{characterPosY}')
        # print("COMMANDS")
        # print("Press Alt+S to Start")
        # print("Press Q to Stop")
        keyboard.wait("Alt+s")
        funcs.clickChampion(characterPosX,characterPosY,confirmBtnX,confirmBtnY)
print("Closing....")
    
        
    


    
    



