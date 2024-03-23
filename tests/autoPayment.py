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
import json
from selenium.webdriver.common.keys import Keys

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module.path import PathModule

xPath = PathModule()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()

with open('info.json') as file:
    datas = json.load(file)

    ID  = datas['ID']
    PW = datas['PW']



class AutoPayment() :

    def autoFunc() : 
        setUrl = "3638847117"
        productTitleCheck = "선택형+계산형+추가구성"
        driver= webdriver.Chrome()
        driver.maximize_window()

        # driver.implicitly_wait(10)
        driver.get("https://www.gmarket.co.kr/")

        #유효성 체크
        for i in range (0, 2):
            title = driver.title
            if (title == "G마켓 - 지금부터의 마켓") :
                break;
            else:
                print("Title 을 확인해주세요")
        print("타이틀 유효성 확인")

        print("로그인 중")
        driver.find_element(By.CLASS_NAME, "link__usermenu").click()
        time.sleep(2)

        id = driver.find_element(By.ID,"typeMemberInputId")
        id.send_keys(f"{ID}")
        
        pw = driver.find_element(By.ID, "typeMemberInputPassword")
        pw.send_keys(f"{PW}")
        time.sleep(2)

        driver.find_element(By.ID,"btn_memberLogin").click()
        time.sleep(2)

        driver.get(f"https://item.gmarket.co.kr/Item?goodscode={setUrl}")
        time.sleep(2)

        productTitle = driver.find_element(By.CLASS_NAME, "itemtit").text
        if productTitle.find(productTitleCheck) :
            print("타이틀 문자 확인됨")
        else :
            print("타이틀 문자 확인 불가")

        # 옵션 선택
        print("옵션 선택")
        driver.find_element(By.CLASS_NAME, "select-item_option").click()
        time.sleep(2)
        

        # 첫번재 옵션 클릭
        xPath.xPathClick(By, driver, "//*[@id='optOrderSel_0']/ul/li[2]/a")
        xPath.idClick()
        horizontal = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcValue1']")
        horizontal.send_keys("10")

        vertical = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcValue2']")
        vertical.send_keys("10")

        totalPrice = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcPrice']")
        totalPrice.send_keys("10000")

        driver.find_element(By.ID, "optOrderTxtCalcBtn").click()

        WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.CLASS_NAME, 'button__add-item') )).click()

        WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.XPATH, "//*[@id='layer__add-item']/div[1]/div/div/div/button"))).click()

        driver.find_element(By.XPATH, "//*[@id='layer__add-item']/div[1]/div/div/div/ul/li[1]/a").click()

        driver.find_element(By.ID, "plusOptionApplyBtn").click()

        print("구매하기 클릭")
        WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.ID, "coreInsOrderBtn"))).click()

        # 주소 변경버튼
        print("주소 입력중")
        WebDriverWait(driver, 5).until( EC.element_to_be_clickable( (By.ID, 'xo_id_add_new_address') )).click()
        # driver.find_element(By.ID, "xo_id_open_address_book").click()
        
        #frame 변경
        box2 = driver.find_element(By.CLASS_NAME,"box__iframe")
        driver.switch_to.frame(box2.find_element(By.TAG_NAME,"iframe"))
        #배송지 추가
        driver.find_element(By.ID,"deliveryName").send_keys("")
        driver.find_element(By.ID,"deliveryName").send_keys("강남 테스트")
        time.sleep(2)
        driver.find_element(By.ID, "reciverName").send_keys("홍길동")
        time.sleep(2)
        driver.find_element(By.ID, "hpNo").send_keys("01011112222")
        time.sleep(2)
        driver.find_element(By.ID, "zipCodeSearchButton").click()
        time.sleep(2)

        #frame 변경        
        driver.switch_to.frame("addr_search_frame")
        print("fraime")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/form/input").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,"input_search").send_keys("강남")
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div[6]/div[2]/ul/li[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div[4]/div[2]/a").click()
        time.sleep(2)
        driver.switch_to.default_content()

        box2 = driver.find_element(By.CLASS_NAME,"box__iframe")
        driver.switch_to.frame(box2.find_element(By.TAG_NAME,"iframe"))
        time.sleep(2)
        #상세정보
        driver.find_element(By.ID,"backAddress").send_keys("1번출구")
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[1]/div[2]/form/div/button[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[3]/div/div[2]/button[2]").click()
        time.sleep(4)
        
        driver.switch_to.default_content()
        # time.sleep(4)
        # 체크박스
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[3]").click()
        time.sleep(2)

        # 통관부호
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[5]/div/div").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[5]/div/div/div/input").clear()
        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div/div[5]/div/div/div/input").send_keys("P123123123123")
        time.sleep(2)
        

        #일반결제
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[1]/section/div/div/div[2]/div[2]/div/label").click()
        time.sleep(2)
        print("결제수단 선택")

        #무통장
        xPath.xPathClick(By, driver, "/html/body/div[2]/div[2]/div[2]/div/div[1]/section/div/div/div[2]/div[2]/div[2]/div/ul/li[3]")
        xPath.xPathClick(By, driver, "/html/body/div[2]/div[2]/div[2]/div/div[1]/section/div/div/div[2]/div[2]/div[2]/div/div/div/ul/li[2]/a")
        print("무통장 선택")

        #결제하기
        xPath.xPathClick(By, driver, "/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/button")        
        time.sleep(4)

        # 종료
        print("종료중")
        driver.quit()

AutoPayment.autoFunc()