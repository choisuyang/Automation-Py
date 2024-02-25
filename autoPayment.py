# -*- coding: utf-8 -*-
# 스크립트 실행 관련 참조 모
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()
class AutoPayment() :

    def autoFunc() : 
        driver= webdriver.Chrome()
        driver.maximize_window()

        # driver.implicitly_wait(10)
        driver.get("https://www.gmarket.co.kr/")


        # 종료
        print("종료중")
        driver.quit()

