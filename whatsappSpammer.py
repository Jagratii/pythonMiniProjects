import pyautogui
import webbrowser
import time

webbrowser.open("web.whatsapp.com")
time.sleep(30)

for i in range(100):
    pyautogui.press("k")
    pyautogui.press("y")
    pyautogui.press("a")
    pyautogui.press("enter")
    pyautogui.press("k")
    pyautogui.press("a")
    pyautogui.press("r")
    pyautogui.press("enter")
    pyautogui.press("r")
    pyautogui.press("h")
    pyautogui.press("i")
    pyautogui.press("enter")
    pyautogui.press("h")
    pyautogui.press("o")
    pyautogui.press("enter")

