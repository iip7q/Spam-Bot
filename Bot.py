import time
from colorama import *
import pyautogui as pygui
import keyboard
import threading
init(autoreset=True)


print(Fore.LIGHTBLUE_EX + '''
|>>>>>>>>>>>>>>>>>>>>>>>>|
|< Spam Bot By A Frogr  >|
|< date: 2021-09-08     >|
|>>>>>>>>>>>>>>>>>>>>>>>>|
''')
time.sleep(1)

text = input('Text To Spam: ')
print(Fore.RED + 'Press Enter then go to the input bar')
time.sleep(1)
btn = input('Press Enter to continue: ')
time.sleep(1)
  
def spam():
    while True:
        pygui.typewrite(text)
        pygui.press('enter')
        pygui.PAUSE = False
spam = threading.Thread(target=spam())
spam.start()
