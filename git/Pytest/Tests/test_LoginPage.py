from venv import logger
import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    @pytest.mark.regression
    def test_Login_Page_Load(self):
        self.loginPage = LoginPage(self.driver)
        pageLoadStatus = self.loginPage.is_UserName_visible()
        print("Verify Page loaded: " + str(pageLoadStatus))
        assert pageLoadStatus

    @pytest.mark.regression
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_Login_Page_title(TestData.logInPage_title)
        print("Verify Page title: " + title)
        assert title == TestData.logInPage_title

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password",
                            [("User","12password34changeMe"),
                            ("test@gmail.com","TestWrongPassword")
                            ]
                            )
    def test_Login_InvalidCredentials(self, username,password):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_Login(username,password)
        print("Verify Invalid Credentials error Exist: " + str(self.loginPage.is_Error_Exist()))
        assert self.loginPage.is_Error_Exist()

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password",
                             [("test@gmail.com","12password34changeMe")]
                             )
    def test_Login_ValidCredentials(self, username,password):
        global homePage
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_Login(username,password)
        homePage.do_click_homeButton()
        print("Verify Log in Successful: " + str(homePage.is_WelcomeText_visible()))
        assert homePage.is_WelcomeText_visible()
        print("Logging out for next test")
        homePage.do_Logout()
        assert self.loginPage.is_UserName_visible()

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password",
                             [("test@gmail.com","12password34changeMe")]
                             )
    def test_login_validCredentials_French(self,username,password):  
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_changeLanguage_to_french()
        self.loginPage.do_Login(username,password)
        print("Verify Log in Successful: " + str(homePage.is_WelcomeText_visible()))
        assert homePage.is_WelcomeText_visible()
        print("Logging out for next test")
        homePage.do_Logout()
        assert self.loginPage.is_UserName_visible() 
