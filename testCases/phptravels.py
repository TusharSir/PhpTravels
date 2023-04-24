import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

# service_obj = Service()

#
# class test_OrangeHRM:
#     def test_Login(self):

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://phptravels.net/admin")
print(driver.title)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("admin@phptravels.com")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("demoadmin1")
driver.find_element(By.XPATH, "//span[normalize-space()='Login']").click()

#try except block
# try:
#     l = driver.find_element(By.XPATH, "//h1[@class='display-4 mb-0']")
#     s= l.text
#     print("Element exist -" + s)
#     #NoSuchElementException thrown if not present
# except NoSuchElementException:
#     print("Element does not exist")

time.sleep(5)

#driver.find_element(By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']").click()

try:
    l = driver.find_element(By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']")
    s = l.text
    print("Element exist -" + s)
    # NoSuchElementException thrown if not present
except NoSuchElementException:
    print("Element does not exist")
#
# wait = WebDriverWait(driver, 20)
#
# w= wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[id='dropdownMenuProfile'] i[class='material-icons']")))
# print(w)
# driver.find_element(By.CSS_SELECTOR,"button[id='dropdownMenuProfile'] i[class='material-icons']").click()
# #time.sleep(5)
#
# driver.find_element(By.XPATH, "//div[normalize-space()='Logout']").click()
driver.close()
