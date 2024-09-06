import pyautogui

pyautogui.PAUSE = 1
pyautogui.sleep(3)

pyautogui.press('enter', presses=5, interval=0.2)
pyautogui.press('tab', presses=3, interval=0.2)
pyautogui.hotkey('ctrl', 'a')

pyautogui.moveTo(x=700, y=600, duration=2)
pyautogui.leftClick()

for i in range(3):
    pyautogui.hotkey('shift', 'tab')

name = 'JACK'
pyautogui.typewrite("print(f'Hello, {name}!')")
