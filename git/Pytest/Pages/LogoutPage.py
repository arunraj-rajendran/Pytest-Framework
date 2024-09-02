import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LogOutPage(BasePage):

    #By Locators
    btn_logout = (By.XPATH,"//input[@id='kc-logout']")

    #construnct of the page class
    def __init__(self,driver):
        super().__init__(driver)
    
    #Logout from the application
    def do_Logout(self):
        print("Confirm Logout from Log out page")
        self.do_click(self.btn_logout)
        time.sleep(2)
        #return LoginPage.LoginPage(self.driver)

