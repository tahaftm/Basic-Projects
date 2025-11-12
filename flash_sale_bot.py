import pyautogui
import time
import pyperclip

# while True:
#     print(pyautogui.position())

pyautogui.click(998,755)
time.sleep(2)
#Gologin process

while True:
    # Step 1: Move to start position and drag to end position
 
 
    # Double-click to select the text
    pyautogui.doubleClick(558, 330, button='left')
    time.sleep(1)  # short pause to make sure selection happens

    # Copy the select text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # wait for clipboard to update

    # Step 2: Copy selected text (Ctrl+C) 

    text = pyperclip.paste()
    actual_value = float(text)-10.00
    pyperclip.copy(str(actual_value))
    pyautogui.click(670,350)
    time.sleep(1)
    pyautogui.hotkey("ctrl","v")
    time.sleep(1)
    # to scroll down  
    pyautogui.scroll(-107)
    time.sleep(1)   
