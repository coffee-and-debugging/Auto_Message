# Auto Message

import pyautogui

import time

time.sleep(4)

count = 0

while count < 20:

    pyautogui.typewrite("Hey buddy!, how you doing?")

    pyautogui.press("enter")

    count = count + 1
