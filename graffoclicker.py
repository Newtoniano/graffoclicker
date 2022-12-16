import random
import time

import pyautogui


# Use mouseposition.py to find the correct coordinates
def taskClicker():
    pyautogui.click(x=800, y=500)
    # Scroll until bottom of list
    pyautogui.moveTo(1218, 510, duration=round(random.random(), 1))
    pyautogui.scroll(-6000)
    # None apply checkbox position
    pyautogui.moveTo(965, 717, duration=round(random.random(), 1))
    pyautogui.click()
    # Top right menu click
    pyautogui.moveTo(1520, 264, duration=round(random.random(), 1))
    pyautogui.click()
    # Click N/A in top right menu
    pyautogui.moveTo(1520, 362, duration=round(random.random(), 1))
    pyautogui.click()
    # Click Submit task
    pyautogui.moveTo(1548, 513, duration=round(random.random(), 1))
    pyautogui.click()


startBot = pyautogui.confirm(
    "Do you want to start Graffoclicker? Please be on the task window when you start."
)
if startBot == "OK":
    # TODO: runtime stats overlay
    targetDuration = int(pyautogui.prompt("Insert desired duration in minutes")) * 60
    if targetDuration:
        # Make window active again after clicking on the prompt
        pyautogui.click()

        tasksDone = 0
        startTime = time.time()

        try:
            while True:
                currentTime = time.time()
                if currentTime - startTime > targetDuration:
                    break
                taskClicker()
                tasksDone += 1
                pyautogui.hotkey("alt", "tab")
                time.sleep(
                    random.randint(30, 180)
                )  # Random 30s-3m delay between each run
                pyautogui.hotkey("alt", "tab")

            print(
                f"Graffoclicker finished running at {time.localtime()} after {targetDuration} minutes. {tasksDone} tasks have been submitted."
            )
            pyautogui.alert(
                f"Graffoclicker finished running at {time.localtime()} after {targetDuration} minutes. {tasksDone} tasks have been submitted."
            )
        except KeyboardInterrupt:
            print(
                f"Graffoclicker stopped early. {tasksDone} tasks have been submitted."
            )
            pyautogui.alert(
                f"Graffoclicker stopped early. {tasksDone} tasks have been submitted."
            )
