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
service = Service('C:\webdriver\chromedriver.exe')
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# driver.implicitly_wait(10)
driver.get("http://erp.sta.co.kr/iWorks")

# alert 창 노출 대기
if EC.alert_is_present():
    result = driver.switch_to.alert
    result.accept()

print("아이디 입력중")
id = driver.find_element(By.NAME,"logid")
id.send_keys("IDDDDDDDDDDDDDDDDDDD") # <============================ 아이디를 입력해주세요.

print("비밀번호 입력중")
pw = driver.find_element(By.NAME, "pwd")
pw.send_keys("PWWWWWWWWWWW") # <============================ 비밀번호를 입력해주세요.

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


