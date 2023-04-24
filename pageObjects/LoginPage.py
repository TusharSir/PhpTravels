import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginClass:
    Text_Email_XPATH = "//input[@type='text']"
    Text_Password_XPATH = "//input[@name='password']"
    Btn_Login_XPATH = "//span[normalize-space()='Login']"
    Click_Options_CSS = "button[id='dropdownMenuProfile'] i[class='material-icons']"
    Click_Logout_XPATH = "//div[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, Email):
        self.driver.find_element(By.XPATH, self.Text_Email_XPATH).clear()
        self.driver.find_element(By.XPATH, self.Text_Email_XPATH).send_keys(Email)

    def SetPassword(self, Password):
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).clear()
        self.driver.find_element(By.XPATH, self.Text_Password_XPATH).send_keys(Password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.Btn_Login_XPATH).click()

    def ClickOptions(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, self.Click_Options_CSS)))
        self.driver.find_element(By.CSS_SELECTOR, self.Click_Options_CSS).click()
        # wait = WebDriverWait(self.driver, 30)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.Click_Options_XPATH)))
        # self.driver.find_element(By.XPATH, self.Click_Options_XPATH).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH, self.Click_Logout_XPATH).click()

    def CheckLogin(self):
        try:
            time.sleep(4)
            l = self.driver.find_element(By.CSS_SELECTOR, self.Click_Options_CSS)
            # s = l.text
            # print("Element exist -" + s)
            return True
            # NoSuchElementException thrown if not present
        except NoSuchElementException:
            # print("Element does not exist")
            return False
