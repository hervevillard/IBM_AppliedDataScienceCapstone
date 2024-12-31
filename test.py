import win32api, win32con
from datetime import datetime
import sys, os
from time import sleep
from random import  randint
from screeninfo import get_monitors


# get screen extens
extents = [(m.width -400, m.height - 400) for m in get_monitors()]
exent = extents[0]
print(exent)

def click(x,y): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
duration = 0
for i in range(1000000):
    x, y = randint(10, exent[0]), randint(10, exent[1])
    print(x,y)
    click(x,y)
    print(i, ' task count')
    rand = randint(1, 70)
    print('Current duration: ', rand) 
    sleep(rand)
    duration += rand
    print('Total duration: ',duration)
    
