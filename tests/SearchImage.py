import time
import pyautogui
import os


class SearchImage():

    def autoMouse(self,searchImage):
        
        img_path_keypad = os.path.dirname(__file__)+ '//img//'
        print("위치찾는중")
        while True:
            img_capture = pyautogui.locateOnScreen(searchImage)
            if img_capture ==None:
                print('좌표위치', img_capture)
                time.sleep(5)
            else:
                pyautogui.click(img_capture)
                break