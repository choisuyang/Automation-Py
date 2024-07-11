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
<<<<<<< HEAD
import sys
import os
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

with open('info.json') as file:
    datas = json.load(file)

    ID  = datas['ID']
    PW = datas['PW']

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Chrome 드라이버 경로를 직접 지정
chrome_driver_path = 'C:\webdriver\chromedriver.exe'

# 아이디/비번 저장소
credentials_list = [
    ["id","pw"]
]

#  전체 코드 시작 / 회원별로 for 문 시작
for credential in credentials_list:
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    driver.get("http://erp.sta.co.kr/iWorks")
    print("공수페이지 진입")

    # 상단 알럿 노출시 클릭 
    if EC.alert_is_present():
        result = driver.switch_to.alert
        result.accept()

    # 아이디 입력
    id = driver.find_element(By.NAME, "logid")
    id.send_keys(credential[0])
    print("아이디 입력중")

    # 비밀번호 입력
    pw = driver.find_element(By.NAME, "pwd")
    pw.send_keys(credential[1])
    print("비밀번호 입력중")

    # 로그인 버튼 클릭
    logBtn = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[4]/td[3]/img")
    logBtn.click()
    print("로그인 버튼 클릭")

    # 화면 노출까지 대기
    time.sleep(3)

    # 공수관리 버튼 클릭
    element = driver.find_element(By.XPATH, '//*[@id="200"]')
    element.click()
    print("공수관리 버튼 클릭")

    # 작업공수실적등록 클릭
    sub_tree_xpath = '//*[@id="sub_tree"]/ul/li/div/span'
    try:
        element_sub_tree = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, sub_tree_xpath))
        )
        element_sub_tree.click()
        print("작업공수 실적등록 클릭")

    except Exception as e:
        print(f"Failed to click element: {e}")

    # 화면 노출까지 대기
    time.sleep(2)

    # iframe 변경
    driver.switch_to.frame("513")

    # 작업공수셀 몇개인지 카운트
    count = driver.find_element(By.ID, "grid2").get_attribute("childElementCount")
    time.sleep(2)
    totalCount = (int(count) + int(1))
    print("작업 공수 몇개인지 파악중")

    # totalCount 만큼 for 문 진행
    for i in range(1, totalCount):
        # 실적 부분 10 입력
        performance = driver.find_element(By.XPATH, f"//*[@id='grid2']/tr[{i}]/td[8]/span/span/input[1]")
        performance.send_keys('10')
        
        # 구분에서 드롭다운 버튼 클릭
        driver.find_element(By.XPATH, f"/html/body/div[6]/form/div[2]/table/tbody/tr[{i}]/td[9]/span").click()
        time.sleep(0.3)

        # 드롭다운에서 매출가동 선택
        # driver.find_element(By.XPATH, f"/html/body/div[{10 + (i*2)}]/div/div[2]/ul/li[2]").click()
        # 대기
        driver.find_element(By.XPATH, f"/html/body/div[{10 + (i*2)}]/div/div[2]/ul/li[4]").click()

    time.sleep(3)

    # 저장 버튼 클릭
    saveBtn = driver.find_element(By.ID, "btnSave")
    saveBtn.click()
    print("저장버튼 클릭")
    
    time.sleep(3)

    print("종료중....")
    driver.quit()
=======

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_version = chromedriver_autoinstaller.get_chrome_version()
# service = Service('C:\webdriver\chromedriver.exe')
# driver = webdriver.Chrome(service=service)

class main() :

    def autoInput() : 
        # driver = webdriver.Chrome(service=service, options=chrome_options)
        driver= webdriver.Chrome()
        driver.maximize_window()

        # driver.implicitly_wait(10)
        driver.get("http://erp.sta.co.kr/iWorks")

        # alert 창 노출 대기
        if EC.alert_is_present():
            result = driver.switch_to.alert
            result.accept()

        print("아이디 입력중")
        id = driver.find_element(By.NAME,"logid")
        id.send_keys("sychoi2") # <============================ 아이디를 입력해주세요.

        print("비밀번호 입력중")
        pw = driver.find_element(By.NAME, "pwd")
        pw.send_keys("test1004!!") # <============================ 비밀번호를 입력해주세요.

        print("로그인 버튼 클릭")
        logBtn = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[4]/td[3]/img")
        logBtn.click()

        time.sleep(3)



        # img_path_keypad = os.path.dirname(__file__)+ '\\img\\'

        # searchImage = SearchImage()

        # searchImage.autoMouse(img_path_keypad + '1.png')
        # time.sleep(2)

        # searchImage.autoMouse(img_path_keypad + '2.png')

        # print("공수관리 위치 찾는중")
        # while True:
        #     img_capture = pyautogui.locateOnScreen(img_path_keypad + "1.png")
        #     print(img_path_keypad+"1.png")
        #     if img_capture ==None:
        #         print('좌표위치1', img_capture)
                
        #     else:
        #         pyautogui.click(img_capture)
        #         time.sleep(2)
        #         break


        # while True:
        #     workload = pyautogui.locateOnScreen(img_path_keypad + "2.png")
        #     if workload ==None:
        #         print('좌표위치2', workload)
        #     else:
        #         pyautogui.click(workload)
        #         time.sleep(2)
        #         break

        element = driver.find_element(By.XPATH, '//*[@id="200"]')
        element.click()

        sub_tree_xpath = '//*[@id="sub_tree"]/ul/li/div/span'
        try:
            element_sub_tree = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, sub_tree_xpath))
            )
            element_sub_tree.click()

        except Exception as e:
            print(f"Failed to click element: {e}")

        print("iframe 이동중")
        time.sleep(2)
        driver.switch_to.frame("513")

        print("컬럼 갯수 확인중")
        count = driver.find_element(By.ID, "grid2").get_attribute("childElementCount")
        time.sleep(2)
        print(f"전체 갯수 : {count}")
        totalCount = (int(count) + int(1))

        print("공수입력중~~")
        for i in range(1,totalCount):
            # 공수 입력 "10"
            performance = driver.find_element(By.XPATH,f"//*[@id='grid2']/tr[{i}]/td[8]/span/span/input[1]").send_keys('10')
            
            # Drop down 클릭
            driver.find_element(By.XPATH,f"/html/body/div[6]/form/div[2]/table/tbody/tr[{i}]/td[9]/span").click()
            time.sleep(0.3)

            # 매출가동 선택
            driver.find_element(By.XPATH,f"/html/body/div[{10 + (i*2)}]/div/div[2]/ul/li[2]").click()

        time.sleep(3)


        # 저장버튼 클릭
        print("저장 버튼 클릭")
        saveBtn = driver.find_element(By.ID, "btnSave")
        saveBtn.click()
        time.sleep(3)

        # 종료
        print("종료중")
        driver.quit()


        # # Google Sheet API 
        # scope = [
        #     "https://spreadsheets.google.com/feeds",
        #     "https://www.googleapis.com/auth/drive",
        # ]

        # # Google Sheet API KEY JSON FILE
        # json_file_name = 'C:\probable-drive-390605-549417099dcf.json'
        # credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
        # gc = gspread.authorize(credentials)

        # # Google Sheet URL
        # spreadsheet_url ='https://docs.google.com/spreadsheets/d/12zxWn3JDNE06DFVFs7-7x775UBFQybBzSuw2OlSwEPc/edit#gid=0'

        # # 스프레스시트 문서 가져오기
        # doc = gc.open_by_url(spreadsheet_url)

        # # 시트 선택하기
        # worksheet = doc.worksheet('시트1')

        # # 사용예제
        # start_number = 14
        # Cell = str(start_number)
        # goods_Number = worksheet.acell('D'+Cell).value
        # print(goods_Number)
        # urlTextFile = open("c:\\webdriver\\item_number.txt", "w")
        # urlTextFile.write(goods_Number)
        # urlTextFile.close()

main.autoInput()
>>>>>>> 57456d68c3450a631688b3f9fdbb4f3033a1b89b
