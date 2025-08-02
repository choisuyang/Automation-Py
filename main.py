# # -*- coding: utf-8 -*-
# # 스크립트 실행 관련 참조 모
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# # service = Service('C:\webdriver\chromedriver.exe')
# # driver = webdriver.Chrome(service=service)

# class main() :

#     def autoInput() : 
#         # driver = webdriver.Chrome(service=service, options=chrome_options)
#         driver= webdriver.Chrome()
#         driver.maximize_window()

#         # driver.implicitly_wait(10)
#         driver.get("https://display.cjonstyle.com/p/item/2027083954?channelCode=30002002&k=%EB%B3%BC%ED%8E%9C&shop_id=2002112507")


#         # 종료
#         print("종료중")
#         driver.quit()




# main.autoInput()
# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pyautogui
# import os
# from image_search import ImageSearch 

# # 크롬 옵션 설정
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)  # 브라우저 자동 종료 방지
# chrome_options.add_argument("--start-maximized")  # 창 최대화
# chrome_options.add_argument("--disable-notifications")  # 알림 비활성화

# class Main:
    

#     @staticmethod
#     def auto_input():
#         # WebDriverManager로 크롬 드라이버 자동 설치 및 실행
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#         # 웹 페이지 이동
#         driver.get("https://display.cjonstyle.com/p/item/2027083954?channelCode=30002002&k=%EB%B3%BC%ED%8E%9C&shop_id=2002112507")

#         # 대기 (필요한 경우)
#         time.sleep(3)
        
#         driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div[2]/div[2]/div[4]/a").click()
#         time.sleep(40)
        
#         driver.find_element(By.XPATH,"//*[@id='bottomOrderButtonSection']/button").click()
#         time.sleep(3)
        
#         main_window = driver.current_window_handle  # 현재 창 핸들

#         # 새로 열린 창으로 전환
#         WebDriverWait(driver, 10).until(EC.new_window_is_opened)
#         new_window_handle = [handle for handle in driver.window_handles if handle != main_window][0]
        
#         # 새 창으로 전환
#         driver.switch_to.window(new_window_handle)

#         # 새 창에서 작업하기
#         print("새 윈도우로 전환 후 작업 시작")
#         time.sleep(3)
        
#         text = driver.find_element(By.XPATH, "//*[@id='txt1']").text  # 예시로 버튼 클릭 (적절한 XPATH로 변경)
#         print("======>" , text)
#         time.sleep(2)
        
#         img_path_keypad = os.path.dirname(__file__)+ '\\img\\'

#         searchImage = ImageSearch()

#         searchImage.autoMouse(img_path_keypad + '1.png')
#         time.sleep(2)

#         # 종료
#         print("종료 중")
#         driver.quit()

# if __name__ == "__main__":
#     Main.auto_input()


# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os

import sys

# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # 브라우저 자동 종료 방지
chrome_options.add_argument("--start-maximized")  # 창 최대화
chrome_options.add_argument("--disable-notifications")  # 알림 비활성화
# chrome_options.add_argument("--user-data-dir=/Users/choesuyang/Documents/chrome_profile")
# chrome_options.add_argument("--profile-directory=Default")  # 기본 프로필 설정 (필요시 사용)
# chrome_options.add_argument("--remote-debugging-port=9222")

sys.path.append(os.path.join(os.path.dirname(__file__), 'tests'))
from image_search import ImageSearch  # ImageSearch 모듈 임포트

class Main:
    
    def auto_input(self):  # 인스턴스 메서드로 변경
        # WebDriverManager로 크롬 드라이버 자동 설치 및 실행
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # 웹 페이지 이동
        driver.get("https://display.cjonstyle.com/p/item/2027083954?channelCode=30002002&k=%EB%B3%BC%ED%8E%9C&shop_id=2002112507")

        # 대기 (필요한 경우)
        time.sleep(3)
        
        driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div[2]/div[2]/div[4]/a").click()
        time.sleep(40)
        
        driver.find_element(By.XPATH,"//*[@id='bottomOrderButtonSection']/button").click()
        time.sleep(3)
        
        main_window = driver.current_window_handle  # 현재 창 핸들

        # 새로 열린 창으로 전환
        WebDriverWait(driver, 10).until(EC.new_window_is_opened)
        new_window_handle = [handle for handle in driver.window_handles if handle != main_window][0]
        
        # 새 창으로 전환
        driver.switch_to.window(new_window_handle)
        
        # 새 창에서 작업하기
        print("새 윈도우로 전환 후 작업 시작")
        time.sleep(3)
        
        text = driver.find_element(By.XPATH, "//*[@id='txt1']").text  # 예시로 버튼 클릭 (적절한 XPATH로 변경)
        print("======>" , text)
        time.sleep(2)
        
        imgtext = driver.find_element(By.XPATH, "//*[@id='nppfs-keypad-cop_pwd']/div/div/img[4]")  # 예시로 버튼 클릭 (적절한 XPATH로 변경)
        # imgtext.click()
        time.sleep(2)
        print("abc------>",imgtext)
        # driver.maximize_window()
        
        # 이미지 찾고 클릭
        searchImage = ImageSearch()
        searchImage.autoMouse(3)
        searchImage.autoMouse(6)
        searchImage.autoMouse(9)
        searchImage.autoMouse(7)
        time.sleep(2)

        # 종료
        print("종료 중")
        driver.quit()

if __name__ == "__main__":
    main_instance = Main()  # 인스턴스 생성
    main_instance.auto_input()  # 메서드 호출