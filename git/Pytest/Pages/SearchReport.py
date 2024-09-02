import time
from Config.config import TestData
from Pages import Reports
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class SearchReports(BasePage):

    #By Locators
    datefrom = (By.XPATH,"//span[@id='submissionDateFrom']//input")
    highlighteddate = (By.XPATH,"//span[@class='p-highlight']")
    showbutton = (By.XPATH,"//span[text()='Show']")
    indicatorfilter = (By.XPATH,"(//div[@class='p-multiselect-label-container'])[2]")
    indicatorselectallcheckboxunchecked = (By.XPATH,"//div[@id='reportIndicators_selectall' and @aria-checked='false']")
    indicatorselectallcheckboxchecked = (By.XPATH,"//div[@id='reportIndicators_selectall' and @aria-checked='true']")  
    indicatorfileternotselected = (By.XPATH,"//li[@class='p-multiselect-item' and @aria-selected='false']")
    indicatorfileterselected = (By.XPATH,"//li[@class='p-multiselect-item p-highlight' and @aria-selected='true']")
    closeindicatorfilter = (By.XPATH,"//button[@type='button' and @data-pc-section='closebutton']")
    indicatorfiltertable = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tr")
    reportentitynametextfield = (By.XPATH,"//span[contains(@id,'reportingEntityName')]//input")
    reportentitynameAutoselectedfield = (By.XPATH,"//span[contains(@id,'reportingEntityName')]//li/span[1]")
    autocompletecount = (By.XPATH,"//li[@class='p-autocomplete-item']")
    valueoftransactiontextbox = (By.XPATH,"//input[@role='spinbutton']")
    valuedecreament = (By.XPATH,"//button[@data-pc-section='decrementbutton']")
    valueincreament = (By.XPATH,"//button[@data-pc-section='incrementbutton']")
    showbutton = (By.XPATH,"//span[text()='Show']")
    submissionDateAndTimeColumn = (By.XPATH,"//div[contains(@class,'tableReport')]//tbody//td[4]")
    filterButtonsInTable = (By.XPATH,"//th//button[@aria-label='Show Filter Menu']")
    typeOfReportDropDown = (By.XPATH,"//label[text()='Type of report']//preceding::div[contains(@class,'multiselect-trigger')]")
    typeOfReportValue = (By.XPATH,"//label[text()='Type of report']//preceding::div[contains(@class,'multiselect-label')]//span[contains(@class,'label')]")
    searchTypeOfReport = (By.XPATH,"//input[contains(@class,'multiselect-filter')]")
    submissionDateFrom = (By.XPATH,"//span[contains(@id,'submissionDateFrom')]/input")
    submissionDateTo = (By.XPATH,"//span[contains(@id,'submissionDateTo')]/input")
    selectCalendarDate = (By.XPATH,"//table[contains(@class,'datepicker')]//span[contains(@class,'highlight')]")
    noOfRecords = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr")
    noRecordsFound = (By.XPATH,"//*[contains(text(),'No available options')]")
    closeFilterDropDown = (By.XPATH,"//button[contains(@data-pc-section,'close')]")

    #construct of the page class
    def __init__(self,driver):
        super().__init__(driver)

    def from_date_text_box(self):
        print("Enter From Date")
        self.do_select_calendar_date(self.datefrom,TestData.submissionDateFrom,self.selectCalendarDate)
        time.sleep(1)
        self.do_click(self.showbutton)
        return Reports.Reports(self.driver)
    
    def check_search_report_indicator_field(self):
        print("Verify Search Report indicator field")
        self.do_click(self.indicatorfilter)
        self.do_click(self.indicatorselectallcheckboxunchecked)
        self.do_click(self.closeindicatorfilter)
        self.do_click(self.indicatorfilter)
        time.sleep(1)
        selectedoptions = self.get_Element_count(self.indicatorfileterselected)
        self.do_click(self.indicatorselectallcheckboxchecked)
        unselectedoptions = self.get_Element_count(self.indicatorfileternotselected)
        indicator1 = (By.XPATH,"//span[text()='"+TestData.indicatorfilter1+"']")
        indicator2 = (By.XPATH,"//span[text()='"+TestData.indicatorfilter2+"']")
        indicator3 = (By.XPATH,"//span[text()='"+TestData.indicatorfilter3+"']")
        self.do_click(indicator1)
        self.do_click(indicator2)
        self.do_click(indicator3)
        self.do_click(self.closeindicatorfilter)
        self.do_click(self.showbutton)
        personcount = self.get_Element_count(self.indicatorfiltertable)
        if selectedoptions>1 and unselectedoptions>1 and personcount>1:
            return True
        else:
            return False
        
    def check_auto_complete_name_field(self):
        print("Verify Name field Auto complete functionlity")
        self.do_Enter_Text(self.reportentitynametextfield,"NL")
        autocompleteoptioncount = self.get_Element_count(self.autocompletecount)
        self.do_Enter_Text(self.reportentitynametextfield," sample 3")
        time.sleep(2)
        autocompleteoptioncount1 = self.get_Element_count(self.autocompletecount)
        if autocompleteoptioncount>1 and autocompleteoptioncount1 < autocompleteoptioncount:
            return True
        else:
            return False
        
    def check_multiple_auto_complete_name_field(self):
        print("Verify Multipl Auto Complete")
        self.do_Enter_Text(self.reportentitynametextfield,"NL Sample 12")
        autocompletename = (By.XPATH,"//li[@class='p-autocomplete-item' and text()='"+TestData.autocompletename1+"']")
        self.do_click(autocompletename)
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        self.do_click(self.reportentitynametextfield)
        self.do_Enter_Text(self.reportentitynametextfield,"NL")
        autocompletename = (By.XPATH,"//li[@class='p-autocomplete-item' and (text()='"+TestData.autocompletename2+"' or text()='"+TestData.autocompletename3+"')]")
        self.do_click(autocompletename)
        return True
    
    def check_value_of_transaction_field(self):
        print("Verify Transaction field incremental and decremental icons")
        self.do_Enter_Text(self.valueoftransactiontextbox,"1000")
        self.do_click(self.valuedecreament)
        self.do_click(self.valuedecreament)
        valueafterdecreament = self.get_Attribute_Value(self.valueoftransactiontextbox,"value")
        self.do_click(self.valueincreament)
        self.do_click(self.valueincreament)
        self.do_click(self.valueincreament)
        self.do_click(self.valueincreament)
        valueafterincreament = self.get_Attribute_Value(self.valueoftransactiontextbox,"value")
        if valueafterincreament=="1,002" and valueafterdecreament=="998":
            return True
        else:
            return False

    def enter_value_of_transaction(self,value):
        print("Enter transaction value as "+value)
        self.do_Enter_Text(self.valueoftransactiontextbox,value)

    def do_Click_Show_Button(self):
        print("Click Show Button")
        self.do_click(self.showbutton)
        self.wait_until_page_loads()
        time.sleep(1)

    def get_submission_date_and_time(self):
        print("Get submission date and time")
        submissionDateAndTime = self.get_Element_Text(self.submissionDateAndTimeColumn)
        return submissionDateAndTime

    def get_No_of_filter_buttons(self):
        print("Get number of filter buttons available in the table")
        return self.get_Element_count(self.filterButtonsInTable)
    
    def enter_reporting_entity_name(self,entityName):
        print("Enter reporting entitiy name "+entityName)
        self.do_Enter_Text(self.reportentitynametextfield,entityName)
        autoSelect = (By.XPATH,"//ul[contains(@class,'autocomplete')]//li[text()='"+entityName+"']")
        if self.is_ElementExist(autoSelect):
            self.do_click(autoSelect)

    def select_Type_of_report(self,typeOfReport):
        print("Select type of report as "+typeOfReport)
        self.do_click(self.typeOfReportDropDown)
        self.do_Enter_Text(self.searchTypeOfReport,typeOfReport)
        element = (By.XPATH,"//span[text()='Suspicious Transaction Report']")
        self.do_click(element)
        self.do_click(self.closeFilterDropDown)
        time.sleep(1)

    def enter_submission_date_from(self,dateFrom):
        print("Enter value for submission date from "+dateFrom)
        self.do_select_calendar_date(self.submissionDateFrom,dateFrom,self.selectCalendarDate)

    def enter_submission_date_to(self,dateTo):
        print("Enter value for submission date to "+dateTo)
        self.do_select_calendar_date(self.submissionDateTo,dateTo,self.selectCalendarDate)
        

    def get_No_Of_Records_Filtered(self):
        print("Verify Number of records filtered")
        time.sleep(2)
        return self.get_Element_count(self.noOfRecords) - self.get_Element_count(self.noRecordsFound)    
    
    def get_report_entity_value(self):
        print("Get report entity value from the field")
        return self.get_Attribute_Value(self.reportentitynametextfield,"value")
    
    def get_report_entity_text_value(self):
        print("Get report entity text value from the field")
        return self.get_Text_Value(self.reportentitynameAutoselectedfield)

    def get_type_of_report_value(self):
        print("Get type of report from the field")
        return self.get_Text_Value(self.typeOfReportValue)
    
    def get_transaction_value(self):
        print("Get transaction value from the field")
        return self.get_Attribute_Value(self.valueoftransactiontextbox,"value")
    