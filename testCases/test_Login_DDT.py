import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox import webdriver

import time

from selenium import webdriver

from pageObjects.LoginPage import LoginClass
from utilites import XLUtils

from utilites.readproperties import ReadConfig

from utilites.CustomLogger import LogGenerator


# @pytest.mark.usefixtures("setup")
class TestLogin_DDT:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGenerator.loggen()
    path = '.\\TestData\\Logindata.xlsx'

    @pytest.mark.regression
    def test_login_ddt_003(self, setup):
        self.logger.info("started test_login_ddt_003")
        self.logger.info("verifying test_login_ddt_003")
        self.driver = setup
        self.driver.get(self.baseUrl)
        # self.driver = setup
        # print(self.driver.title)
        self.lg = LoginClass(self.driver)
        time.sleep(3)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.userName = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lg.SetEmail(self.userName)
            self.logger.info("Enter username")
            self.lg.SetPassword(self.password)
            self.logger.info("Enter password")
            self.lg.ClickLogin()
            self.logger.info("click on login password")
            stauts = self.lg.CheckLogin()
            #print(stauts)
            if stauts == True:
                if self.exp == "Pass":
                    lst_status.append("Pass")
                    self.lg.ClickOptions()
                    self.logger.info("test_login_ddt_003 is passed")
                    self.logger.info("click on Options")
                    self.lg.ClickLogout()
                    self.logger.info("click on Logout")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Pass")

                elif self.exp == "Fail":
                    lst_status.append("Pass")
                    self.lg.ClickOptions()
                    self.logger.info("test_login_ddt_003 is passed")
                    self.logger.info("click on Options")
                    self.lg.ClickLogout()
                    self.logger.info("click on Logout")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")

                # self.driver.close()
            else:
                if self.exp == "Pass":
                    lst_status.append("Fail")
                    self.logger.info("test_login_ddt_003 is Failed")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                    self.logger.info("test_login_ddt_003 is completed")

                elif self.exp == "Fail":
                    lst_status.append("Pass")
                    self.logger.info("test_login_ddt_003 is Failed")
                    XLUtils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                self.logger.info("test_login_ddt_003 is completed")

        print(lst_status)

        if "Fail" in lst_status:
            assert False
        else:
            assert True
        self.driver.close()
