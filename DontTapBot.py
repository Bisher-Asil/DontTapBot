from pyautogui import *
import pyautogui 
import time
import keyboard
import random
import win32api, win32con

## This code is written to win on http://www.donttap.com/, it was written in an hour cuz I was bored, yes the numbers below are manually aquired (wont work on different screens)
#1 : 717,356
#2: 896, 336
#3: 1018 336
#4: 1180 336
#5 719 493
#6 876 486
#7 1019 485
#8 1188 482
#9 727 640
#10 879 646
#11 1026 651
#12 1185 650
#13 729 813
#14 880 801
#15 1025 801
#16 1191 801

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
try:
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(717,356)[0] == 0:
            click(717,356)
        if pyautogui.pixel(896,356)[0] == 0:
            click(896,356)
        if pyautogui.pixel(1018,356)[0] == 0:
            click(1018,356)
        if pyautogui.pixel(1180,356)[0] == 0:
            click(1180,356)
        if pyautogui.pixel(717,490)[0] == 0:
            click(717,490)
        if pyautogui.pixel(896,490)[0] == 0:
            click(896,490)
        if pyautogui.pixel(1018,490)[0] == 0:
            click(1018,490)
        if pyautogui.pixel(1180,490)[0] == 0:
            click(1180,490)

        if pyautogui.pixel(717,640)[0] == 0:
            click(717,640)
        if pyautogui.pixel(896,640)[0] == 0:
            click(896,640)
        if pyautogui.pixel(1018,640)[0] == 0:
            click(1018,640)
        if pyautogui.pixel(1180,640)[0] == 0:
            click(1180,640)

        if pyautogui.pixel(717,801)[0] == 0:
            click(717,801)
        if pyautogui.pixel(896,801)[0] == 0:
            click(896,801)
        if pyautogui.pixel(1018,801)[0] == 0:
            click(1018,801)
        if pyautogui.pixel(1180,801)[0] == 0:
            click(1180,801)
    
except :
    pass