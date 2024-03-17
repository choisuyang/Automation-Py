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

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()

with open('info.json') as file:
    datas = json.load(file)

    ID  = datas['ID']
    PW = datas['PW']


class AutoPayment() :

    def autoFunc() : 
        setUrl = "3435277941"
        productTitleCheck = "프로모션용 테스트123"
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
        # driver.find_element(By.CLASS_NAME, "select-item_option").click()
        # time.sleep(2)

        # 첫번재 옵션 클릭
        # driver.find_element(By.XPATH, "//*[@id='optOrderSel_0']/ul/li[1]/a").click()
        # time.sleep(2)

        # horizontal = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcValue1']")
        # horizontal.send_keys("10")

        # vertical = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcValue2']")
        # vertical.send_keys("10")

        # totalPrice = driver.find_element(By.XPATH,"//*[@id='optOrderTxtCalcPrice']")
        # totalPrice.send_keys("10000")

        # driver.find_element(By.ID, "optOrderTxtCalcBtn").click()

        # WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.CLASS_NAME, 'button__add-item') )).click()

        # WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.XPATH, "//*[@id='layer__add-item']/div[1]/div/div/div/button"))).click()

        # driver.find_element(By.XPATH, "//*[@id='layer__add-item']/div[1]/div/div/div/ul/li[1]/a").click()

        # driver.find_element(By.ID, "plusOptionApplyBtn").click()

        WebDriverWait(driver, 2 ).until( EC.element_to_be_clickable( (By.ID, "coreInsOrderBtn"))).click()

        # time.sleep(6)

        # 주소 변경버튼
        WebDriverWait(driver, 5).until( EC.element_to_be_clickable( (By.ID, 'xo_id_add_new_address') )).click()
        # driver.find_element(By.ID, "xo_id_open_address_book").click()
        time.sleep(5)

        # 배송지 변경
        # driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/button').click()
        # time.sleep(10)

        #배송지 추가
        driver.find_element(By.XPATH, "//*[@id='content']/div[1]/div[1]/div[1]/div[2]/div").click()
        deliveryName = driver.find_element(By.ID, "reciverName")
        deliveryName.send_keys("테스트")
        time.sleep(2)
        # driver.find_element(By.ID, "reciverName").send_keys("홍길동")
        # time.sleep(2)
        # driver.find_element(By.ID, "hpNo").send_keys("01011112222")
        # time.sleep(2)
        # driver.find_element(By.ID, "zipCodeSearchButton").click()
        # time.sleep(2)

        # driver.find_element(By.XPATH, "//*[@ id='container']/div/div/div[1]/div[1]/div[1]/form/input").send_keys("강남")


        # 종료
        print("종료중")
        driver.quit()

AutoPayment.autoFunc()