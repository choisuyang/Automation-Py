import time
import os


class PathModule():

    def xPathClick(self,By, driver, xpath):
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(10)