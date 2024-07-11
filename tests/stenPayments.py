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
import os
from SearchImage import SearchImage

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()
class AutoPayment() :

    def autoStenFunc() : 
        driver= webdriver.Chrome()
        driver.maximize_window()

        # driver.implicitly_wait(10)
        driver.get("https://www.sten.or.kr/index.php")

        #유효성 체크
        for i in range (0, 2):
            title = driver.title
            if (title == "STEN") :
                print('STEN 접속 확인')
                break;
            else:
                print("Title 을 확인해주세요")
        print("pass")

        id = driver.find_element(By.ID,"mb_id")
        id.send_keys("aaaaaaaaaa")
        print("아이디입력")
        
        pw = driver.find_element(By.ID, "mb_password")
        pw.send_keys("llllllllll")
        time.sleep(2)
        print("비밀번호 입력")

        driver.find_element(By.CLASS_NAME,"login-button").click()
        time.sleep(2)
        print("로그인 버튼 클릭")


        driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/dl[1]/dd[1]/div[2]/div/div[3]/ul/li[3]/a").click()
        print('ISTQB 선택')

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/a").click()
        print("ISTQB 시험신청 클릭")
        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr[1]/td[3]/table/tbody/tr/td/table/tbody/tr[6]/td/table[1]/tbody/tr[5]/td[4]/input").click()
        time.sleep(2)

        driver.find_element(By.ID, "pay_type0").click()
        time.sleep(2)

        driver.find_element(By.ID, "check_agree").click()
        print("동의함 클릭")
        time.sleep(2)

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr[1]/td[3]/table[2]/tbody/tr[2]/td[2]/form/table[2]/tbody/tr/td/img").click()
        print("시험 신청하기 클릭")
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/center/table/tbody/tr/td[2]/form/table/tbody/tr/td[1]/a/img").click()
        print("Home 으로 이동")
        time.sleep(2)
        
        driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/div/dl[2]/dd[1]/div/dl[2]/dd/map/area[2]").click()
        print("나의 신청내역 접속")
        time.sleep(10)      
        
        # # 종료
        print("종료중")
        driver.quit()

AutoPayment.autoStenFunc()