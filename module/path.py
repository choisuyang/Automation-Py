import time
import os


class PathModule():

    def xPathClick(self,By, driver, xpath):
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)

    def idClick(self):
        print('hihi')
        # driver.find_element(By.ID, id).click()
        # time.sleep(2)