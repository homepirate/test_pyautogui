import pyautogui

pyautogui.PAUSE = 1
pyautogui.sleep(3)

print(pyautogui.confirm(text='How are you?', buttons=['Happy', 'Okey', 'Angry']))