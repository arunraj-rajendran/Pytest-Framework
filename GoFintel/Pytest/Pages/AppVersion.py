import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class AppVersion(BasePage):

    uiVersion = (By.XPATH,"//div[contains(@class,'layout-content relative')]//li[contains(text(),'UI Version')]")
    backendVersion = (By.XPATH,"//div[contains(@class,'layout-content relative')]//li[contains(text(),'Backend Version')]")

    def is_ui_version_visible(self):
        print("Verify UI Version Text is visible : "+ str(self.is_ElementExist(self.uiVersion)))
        return self.is_ElementExist(self.uiVersion)
    
    def is_backend_version_visible(self):
        print("Verify Backend Version Text is visible : "+ str(self.is_ElementExist(self.backendVersion)))
        return self.is_ElementExist(self.backendVersion)