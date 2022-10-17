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

funcs.showMenu()

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
        funcs.showMenu()
        print("Choose an option: ")
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
            funcs.showMenu()
            print("Choose an option: ")
    elif keyboard.is_pressed("3"):
        # for a loop in agents keys
        cont = 0
        tableOfAgents = PrettyTable(['Indice','Nome'])
        for agent in data:
            if agent != "confirmBtn":
                tableOfAgents.add_row([cont,agent])
                cont += 1

        print(tableOfAgents)
        # wait for the user press a number and save the value in a variable
        print("Choose an agent: ")
        agentChoosed = int(input())
        agentChoosed += 1
        # get the agent name from the index
        agentName = list(data.keys())[agentChoosed]
        print(f'You choosed: {agentName}')
        try:
            #get the agent position
            characterPosX = data[agentName]['x']
            characterPosY = data[agentName]['y']
            confirmBtnX = data['confirmBtn']['x']
            confirmBtnY = data['confirmBtn']['y']
            print(f'X={characterPosX} e Y:{characterPosY}')
            print('-'*30)
            print("COMMANDS")
            print("Press Alt+S to Start")
            print("Press Q to Stop")
            keyboard.wait("Alt+s")
            print('-'*30)

            out = False
            while not out:
                funcs.clickChampion(characterPosX,characterPosY,confirmBtnX,confirmBtnY)
                if keyboard.is_pressed("q"):
                    print("\nStoping...")
                    print("Press Alt+s to continue or Alt+q to exit to menu \n")
                    # wait keyboard press Alt+s or 0
                    sleep(0.5)
                    while True:
                        if(keyboard.is_pressed("Alt+s")):
                            print("Continuing...")
                            break
                        if(keyboard.is_pressed("Alt+q")):
                            print("Exiting...")
                            funcs.showMenu()
                            print("Choose an option: ")
                            out = True
                            break
        except KeyError:
            print("\n\n!!!!!!Agente ou botão não cadastrado, tente novamente!!!!!!!!\n\n\n")
    elif keyboard.is_pressed("0"):
        print("Exiting...")
        sleep(5)
        break
        
print("Closing....")
    
        
    


    
    



