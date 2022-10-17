#                               References: 
# https://www.pythontutorial.net/advanced-python/python-threading/
# https://www.w3schools.com/python/python_variables_global.asp
# https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/



from ast import Try, While
from time import sleep
import pyautogui
import keyboard
import funcs
import json
from prettytable import PrettyTable

global stopClick
screenWidth, screenHeight = pyautogui.size() #get main screen just for fun 
print(f'Your screem size is {screenWidth}x{screenHeight}') 


#-------------------------MENU-----------------------------
print("MENU \n")
print("1 - Para definir a posição do botao confirmar (Necessário apenas a primeira vez)")
print("2 - Para definir a posição do personagem (Necessário apenas a primeira vez)")
print("3 - Para escolher um persongem pré-definido")
print("0 - Exit")
#----------------------------------------------------------

#leitura de arquivo
print("\nReading Agent Position File")
data = None
with open('agents.json','r',encoding="utf-8") as f:
    data = json.load(f)

print("File Read Sucefully \n")


print("Choose an option: ")
while True:
    if keyboard.is_pressed("1"):
        print("Put your mouse on confirm button and press Ctrl for save")
        keyboard.wait('ctrl') #wait the Ctrl key be pressed
        confirmBtnX,confirmBtnY = pyautogui.position() #get current mouse position
        data["ConfirmBtn"] = {
                "x" : confirmBtnX,
                "y" : confirmBtnY
            }
    if keyboard.is_pressed("2"):
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
            
    elif keyboard.is_pressed("3"):
        # for a loop in agents keys
        cont = 0
        tableOfAgents = PrettyTable(['Indice','Nome'])
        for agent in data:
            tableOfAgents.add_row([cont,agent])
            cont += 1

        print(tableOfAgents)
        # wait for the user press a number and save the value in a variable
        sleep(0.5)
        while True:
            if keyboard.is_pressed("0"):
                agentChoosed = 0
                break
            elif keyboard.is_pressed("1"):
                agentChoosed = 1
                break
            elif keyboard.is_pressed("2"):
                agentChoosed = 2
                break
            elif keyboard.is_pressed("3"):
                agentChoosed = 3
                break
            elif keyboard.is_pressed("4"):
                agentChoosed = 4
                break
            elif keyboard.is_pressed("5"):
                agentChoosed = 5
                break
            elif keyboard.is_pressed("6"):
                agentChoosed = 6
                break
            elif keyboard.is_pressed("7"):
                agentChoosed = 7
                break
            elif keyboard.is_pressed("8"):
                agentChoosed = 8
                break
            elif keyboard.is_pressed("9"):
                agentChoosed = 9
                break
    
        #get the agent name by the number choosed
        agentName = list(data.keys())[agentChoosed]
        print(f'You choosed {agentName}')
        try:
            #get the agent position
            characterPosX = data[agentName]['x']
            characterPosY = data[agentName]['y']
            confirmBtnX = data['confirmBtn']['x']
            confirmBtnY = data['confirmBtn']['y']
            print(f'X={characterPosX} e Y:{characterPosY}')
            print("COMMANDS")
            print("Press Alt+S to Start")
            print("Press Q to Stop")
            keyboard.wait("Alt+s")
            funcs.clickChampion(characterPosX,characterPosY,confirmBtnX,confirmBtnY)
        except KeyError:
            print("\n\n!!!!!!Agente ou botão não cadastrado, tente novamente!!!!!!!!\n\n\n")
    
    elif keyboard.is_pressed("0"):
        print("Exiting...")
        break

print("Closing....")
    
        
    


    
    



