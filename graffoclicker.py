import random
import time

import pyautogui
import pymsgbox


# Use mouseposition.py to find the correct coordinates
def taskClicker():
    # scrollbar position
    pyautogui.moveTo(100, 150, duration=round(random.random(), 1))
    # set scroll lenght
    pyautogui.scroll(-10)
    # None apply checkbox position
    pyautogui.moveTo(300, 450, duration=round(random.random(), 1))
    pyautogui.click()
    # Top right menu position
    pyautogui.moveTo(350, 600, duration=round(random.random(), 1))
    pyautogui.click()
    # Send task position
    pyautogui.moveTo(200, 180, duration=round(random.random(), 1))
    pyautogui.click()


tasksDone = 0
startBot = pymsgbox.confirm(
    "Do you want to start Graffoclicker? Please be on the task page when you start."
)
if startBot == "OK":
    # TODO: runtime stats overlay
    tasksDone = 0
    try:
        while True:
            taskClicker()
            tasksDone += 1
            pyautogui.hotkey("alt", "tab")
            time.sleep(random.randint(10, 180))  # Random 10s-3m delay between each run
    except KeyboardInterrupt:
        print(f"Graffoclicker stopped. {tasksDone} tasks submitted.")
        pymsgbox.alert(f"Graffoclicker stopped. {tasksDone} tasks submitted.")
