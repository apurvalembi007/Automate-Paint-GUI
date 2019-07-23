import pyautogui
import time,sys
# print(pyautogui.size())
# print(pyautogui.position())
# pyautogui.moveTo(100, 150,duration=10)
# pyautogui.click()
# pyautogui.moveRel(None,10,duration=20)
# pyautogui.doubleClick()

print('Press Ctrl-C to quit.')


time.sleep(20)
pyautogui.click()

distance = 800
while distance > 0:
    try:
        pyautogui.dragRel(distance, 0, duration=0.5)  # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up
        time.sleep(40)
    except KeyboardInterrupt:
        sys.exit()

