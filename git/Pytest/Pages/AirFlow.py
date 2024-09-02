import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from Tests import conftest

class airflow(BasePage):

    #By Locators
    userName = (By.XPATH,"//input[@id='username']")
    password = (By.XPATH,"//input[@id='password']")
    signIn  = (By.XPATH,"//input[@value='Sign In']")
    searchDag = (By.XPATH,"//input[@id='dag_query']")
    triggerDag = (By.XPATH,"//a[@aria-label='Trigger DAG']")
    triggerDagButton = (By.XPATH,"//button[text()='Trigger DAG']")

    def __init__(self,driver):
        super().__init__(driver) 
        
    def run_dag(self,dagName):
        print("Triggering "+dagName+" from airflow")
        searchDagDropDownOption = (By.XPATH,"//ul//strong[text()='"+dagName+"']//parent::a")
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(conftest.airflowURL)

        if self.is_ElementExist(self.userName):
            self.do_Enter_Text(self.userName,conftest.airflowUserName)
            self.do_Enter_Text(self.password,conftest.airflowPassword)
            self.do_click(self.signIn)
        self.do_Enter_Text(self.searchDag,dagName)
        if self.is_element_clickable(searchDagDropDownOption):
            self.do_click(searchDagDropDownOption)
        else:
            self.do_click(self.searchDag)
            action = self.get_action_class()
            action.send_keys(Keys.ENTER).perform()
        self.do_click(self.triggerDag)
        self.do_click(self.triggerDagButton)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)
