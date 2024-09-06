import pyautogui

print(pyautogui.size())
pyautogui.sleep(3)

pyautogui.moveTo(1852, 666, duration=2)
pyautogui.dragTo(939, 448, duration=2, button='left')