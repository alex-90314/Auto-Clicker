import pyautogui

while True:
    #if "esc" in pyautogui.KEYBOARD_KEYS:
    #   break
    if "`" in pyautogui.KEYBOARD_KEYS:
        print(pyautogui.position())