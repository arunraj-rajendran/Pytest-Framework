import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage

class LoginPage(BasePage):

    #By Locators
    txt_username = (By.ID,"username")
    txt_password = (By.ID,"password")
    btn_logIn = (By.XPATH,"//*[@id='kc-login']")
    ele_ErroText = (By.ID,"input-error")
    changeLanguage = (By.ID,"kc-current-locale-link")
    frenchLanguage = (By.XPATH,"//a[text()='Français']")
    englishLanguage = (By.XPATH,"//a[text()='English']")
    spanishLanguage = (By.XPATH,"//a[text()='Español']")
    dutchLanguage = (By.XPATH,"//a[text()='Nederlands']")

    #construnct of the page class
    def __init__(self,driver):
        super().__init__(driver)

    #Page Actions
    def get_Login_Page_title(self, title):
        print("Get Log in Page title")
        return self.get_Title(title)
    
    #check username is visible
    def is_UserName_visible(self):
        print("Get Log in Page title")
        return self.is_ElementExist(self.txt_username)
    
    #Log in to the application
    def do_Login(self, username, password):
        print("Log in to the application - Username: "+ username +" Password: "+ password)
        homePage = HomePage(self.driver)
        self.do_Enter_Text(self.txt_username, username)
        self.do_Enter_Text(self.txt_password, password)
        self.do_click(self.btn_logIn)
        time.sleep(2)
        if self.get_Element_count(homePage.selectedLanguage) > 0:
            homePage = HomePage(self.driver)
            homePage.changeLanguage_To_English()
        return HomePage(self.driver)

    #check invalid credential error is visible
    def is_Error_Exist(self):
        print("Verify Error Message Exists")
        return self.is_ElementExist(self.ele_ErroText)
    
    def do_changeLanguage_to_french(self):
        print("Change Language to French")
        self.do_click(self.changeLanguage)
        self.do_click(self.frenchLanguage)

    def do_changeLanguage_to_spanish(self):
        print("Change Language to spanish")
        self.do_click(self.changeLanguage)
        self.do_click(self.frenchLanguage)

    def do_changeLanguage_to_dutch(self):
        print("Change Language to dutch")
        self.do_click(self.changeLanguage)
        self.do_click(self.frenchLanguage)

    
