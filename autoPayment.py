# -*- coding: utf-8 -*-
# 스크립트 실행 관련 참조 모
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()
class AutoPayment() :

    def autoFunc() : 
        driver= webdriver.Chrome()
        driver.maximize_window()

        # driver.implicitly_wait(10)
        driver.get("https://www.gmarket.co.kr/")

        #유효성 체크
        for i in range (0, 2):
            title = driver.title
            print('1111')
            if (title == "G마켓 - 지금부터의 마켓") :
                print('222')
                break;
            else:
                print("Title 을 확인해주세요")
        print("pass")

        driver.find_element(By.CLASS_NAME, "link__usermenu").click()
        time.sleep(2)

        id = driver.find_element(By.ID,"typeMemberInputId")
        id.send_keys("chltndid72")
        
        pw = driver.find_element(By.ID, "typeMemberInputPassword")
        pw.send_keys("test1004")
        time.sleep(2)

        driver.find_element(By.ID,"btn_memberLogin").click()
        time.sleep(2)


        # # 종료
        # print("종료중")
        # driver.quit()

AutoPayment.autoFunc()