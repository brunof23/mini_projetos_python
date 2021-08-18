import pyautogui
import time


time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

for x in range(1, 100, 1):

    time.sleep(60)

    pyautogui.write(str(x))
    pyautogui.press('space')
    pyautogui.write('minutos')
    pyautogui.press('enter')




