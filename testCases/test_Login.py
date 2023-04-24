import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox import webdriver

import time

from selenium import webdriver

from pageObjects.LoginPage import LoginClass

from utilites.readproperties import ReadConfig

from utilites.CustomLogger import LogGenerator

#@pytest.mark.usefixtures("setup")
class TestLogin:
    baseUrl =  ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_pagetitle_001 (self,setup):
        self.logger.info("started test_pagetitle_001")
        self.logger.info("Verifying page tile")
        self.driver = setup
        self.driver.get(self.baseUrl)
        exp_title = "Administator Login"
        actul_title = self.driver.title

        if exp_title == actul_title:
            self.logger.info("test_pagetitle_001 is passed")
            assert True
            self.driver.save_screenshot("D:\\Credence Python Projects by Tushar Sir\\PhpTravels\\Screenshots\\test_pagetitle--pass.png")
        else:
            self.logger.info("test_pagetitle_001 is failed")
            exp_title!= actul_title
            self.driver.save_screenshot("..\\Screenshots\\test_pagetitle--fail.png")
            assert False
        self.driver.close()
        self.logger.info("test_pagetitle_001 is completed")

    @pytest.mark.sanity
    def test_login_002 (self,setup):
        self.logger.info("started test_login_002")
        self.logger.info("verifying test_login_002")
        self.driver = setup
        self.driver.get(self.baseUrl)
        # self.driver = setup
        # print(self.driver.title)
        self.lg = LoginClass(self.driver)
        time.sleep(3)
        self.lg.SetEmail(self.username)
        self.logger.info("Enter username")
        self.lg.SetPassword(self.password)
        self.logger.info("Enter password")
        self.lg.ClickLogin()
        self.logger.info("click on login password")
        stauts = self.lg.CheckLogin()
        print(stauts)
        if stauts == True:
            assert True
            self.lg.ClickOptions()
            self.logger.info("test_login_002 is passed")
            self.logger.info("click on Options")
            self.lg.ClickLogout()
            self.logger.info("click on Logout")
            self.driver.close()
            self.logger.info("test_login_002 is completed")
        elif stauts != True:
            assert False
            self.logger.info("test_login_002 is Failed")
            self.logger.info("click on Logout")
            self.driver.close()
            self.logger.info("test_login_002 is completed")

    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_sample_001(self):
        print("this is sample test04")
        assert True

    @pytest.mark.skip
    def test_sample_002(self):
        print("this is sample test05")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_sample_003(self):
        print("this is sample test06")
        assert True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_sample_004(self):
        print("this is sample test07")
        assert False