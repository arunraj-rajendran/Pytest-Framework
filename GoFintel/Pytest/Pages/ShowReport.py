from Pages import GraphView
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class Showreport(BasePage):
    showreportidtextbox = (By.XPATH,"//label[@for='reportId']//preceding-sibling::input")
    showbutton = (By.XPATH,"//span[text()='Show']")

    def check_show_report(self, reportid):
        print("Verify show Report")
        self.do_Enter_Text(self.showreportidtextbox,reportid)
        self.do_click(self.showbutton)
        return GraphView.GraphView(self.driver)

    def get_reportid_value(self):
        print("Get report id value from the field")
        return self.get_Attribute_Value(self.showreportidtextbox,"value")