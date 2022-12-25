import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller , Button
from time import sleep

mouse = Controller()

class Whatsapp:

    def __init__(self,speed=.5,click_speed =.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message  = ""
        self.last_message = ""

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen("punto_verde.png",confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0,duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        
        except Exception as e:
            print("Exception (nav_green_dot): ", e)

wha_bot = Whatsapp(speed=.5,click_speed=.4)
        
sleep(3)        
wha_bot.nav_green_dot()