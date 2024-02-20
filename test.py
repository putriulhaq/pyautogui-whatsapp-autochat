import pyautogui
from time import sleep
import sys
import webbrowser as wb

print(pyautogui.position())

#contact list
loop = int(input('how many loops do you want: '))
name = input('type your contact: ')
message = input('type your message: ')
contacts = [name]

def click_search_name(name):
    x1, y1 = [209,123]
    pyautogui.moveTo(x1, y1)
    pyautogui.click()
    pyautogui.typewrite(name, interval=0.2)
    pyautogui.sleep(1)
    # pyautogui.moveTo([211,181])
    pyautogui.moveTo([223,245])
    # print(pyautogui.position())
    pyautogui.click()
    # pyautogui.press('enter')

# =# method to find and send message
def click_send_message(msg): 
    x3, y3 = [950,750] 
    pyautogui.moveTo(x3, y3) 
    pyautogui.click() 
    # pyautogui.sleep() 
    pyautogui.typewrite(msg) 
    pyautogui.press('enter')

for index, name in enumerate(contacts):
    try:
        click_search_name(name)
    except:
        print("Unable to locate search bar or name")

    # try:
    #     for i in range(loop):
    #         # click_send_message(message)
    # except:
    #     print("Unable to locate message bar")

# pyautogui.scroll(10)
# pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"
# pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click