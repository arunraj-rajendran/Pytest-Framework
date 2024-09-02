import time
from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SearchPerson(BasePage):

    #By Locators
    highlighteddate = (By.XPATH,"//span[@class='p-highlight']")
    showbutton = (By.XPATH,"//span[text()='Show']")
    isdirectorunspecified = (By.XPATH,"//div[@aria-label='Unspecified']")
    isdirectorno = (By.XPATH,"//div[@aria-label='No']")
    isdirectoryes = (By.XPATH,"//div[@aria-label='Yes']")
    showpersontable = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tbody//tr")
    nationalityDropDown = (By.XPATH,"//div[@id='nationality']")
    nationalityInput = (By.XPATH,"//div[@class='p-dropdown-filter-container']/input")
    dropDownValue = (By.XPATH,"//div[@class='p-dropdown-items-wrapper']//li[@aria-label='"+TestData.country+"']")
    firstname = (By.XPATH,"//input[@id='firstName']")
    lasttname = (By.XPATH,"//input[@id='lastName']")
    closeFilterDropDown = (By.XPATH,"//button[contains(@data-pc-section,'close')]")
    applyFilter = (By.XPATH,"//button[@aria-label='Apply']")
    clearFilter = (By.XPATH,"//button[@aria-label='Clear']")
    search = (By.XPATH,"//input[@placeholder='Search']")
    filterBirthDate = (By.XPATH,"//span[text()='Birth date']//..//child::button[contains(@class,'filter')]")
    filterVirtualNode= (By.XPATH,"//span[text()='Virtual node']//..//child::button[contains(@class,'filter')]")
    expandFiterDropDown = (By.XPATH,"//div[contains(@class,'filter')]//div[contains(@class,'-trigger')]")
    virtualNodeFilter_No = (By.XPATH,"//div[contains(@class,'multiselect')]//li//span[text()='No']")
    virtualNodeFilter_Yes = (By.XPATH,"//div[contains(@class,'multiselect')]//li//span[text()='Yes']")
    virtualNodeFilter_Unspecified = (By.XPATH,"//div[contains(@class,'multiselect')]//li//span[text()='Unspecified']")
    selectAllCheckbox = (By.XPATH,"//div[contains(@class,'multiselect')]//div[contains(@class,'p-checkbox p-component')][1]")
    dateBetweenFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Date Between']")
    yearIsFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Year Is']")
    dateFromFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[1]")
    dateToFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[2]")
    yearIsValue = (By.XPATH,"//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input")
    yearPicker = (By.XPATH,"//div[contains(@class,'yearpicker')]/span[text()='"+TestData.yearIs+"']")
    noOfRecords = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr")
    noRecordsFound = (By.XPATH,"//*[contains(text(),'No available options') or contains(text(),'No data found')]")
    selectCalendarDate = (By.XPATH,"//table[contains(@class,'datepicker-calendar')]//span[contains(@class,'highlight')]")
    infoIcon = (By.XPATH,"//td[8]//button[contains(@class,'rounded') and contains(@class,'icon-only')]")
    inputBreadCrumb = (By.XPATH,"//span[contains(text(),'Input')]//parent::a")
    dateOfBirthColumn =(By.XPATH,"//div[contains(@class,'tableReport')]//tbody//td[5]")

    #construct of the page class
    def __init__(self,driver):
        super().__init__(driver)


    def check_unspecified_search_person(self):
        print("Verify Unspecified search person")
        selected=self.get_Attribute_Value(self.isdirectorunspecified,"aria-pressed")
        self.do_click(self.showbutton)
        time.sleep(3)
        personcount = self.get_Element_count(self.showpersontable)
        if selected == "true" and personcount>0:
            return True
        else:
            return False
        
    def check_No_In_Isdirector_search_person(self):
        print("Verify Is director = No")
        self.do_click(self.isdirectorno)
        selected=self.get_Attribute_Value(self.isdirectorno,"aria-pressed")
        self.do_click(self.showbutton)
        time.sleep(3)
        personcount = self.get_Element_count(self.showpersontable)
        if selected == "true" and personcount>0:
            return True
        else:
            return False
        
    def check_Yes_In_Isdirector_search_person(self):
        print("Verify Is director = Yes")
        self.do_click(self.isdirectoryes)
        selected=self.get_Attribute_Value(self.isdirectoryes,"aria-pressed")
        self.do_click(self.showbutton)
        time.sleep(3)
        personcount = self.get_Element_count(self.showpersontable)
        if selected == "true" and personcount>0:
            return True
        else:
            return False
        
    def check_Nationality_DropDown_search_person(self):
        print("Verify search person with nationality filter")
        self.do_click(self.nationalityDropDown)
        self.do_Enter_Text(self.nationalityInput,TestData.country)
        self.do_click(self.dropDownValue)
        self.do_click(self.showbutton)
        personcount = self.get_Element_count(self.showpersontable)
        if personcount>0:
            return True
        else:
            return False
        
    def check_First_Name_Field(self):
        print("Verify search person with First Name filter")
        self.do_Enter_Text(self.firstname,TestData.firstname)
        self.do_click(self.showbutton)
        personcount = self.get_Element_count(self.showpersontable)
        if personcount>0:
            return True
        else:
            return False
        
    def check_Search_By_First_Name_Field(self):
        print("Verify search person with First Name filter")
        self.do_Enter_Text(self.firstname,TestData.firstname3)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountContains = self.get_Element_count(self.showpersontable)
        self.do_click(self.inputBreadCrumb)
        self.do_Enter_Text(self.firstname,TestData.firstname1)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountStartsWith = self.get_Element_count(self.showpersontable)
        if personcountStartsWith>0 and personcountContains==3:
            return True
        else:
            return False
        
    def check_Search_By_Last_Name_Field(self):
        print("Verify search person with Last Name filter")
        self.do_Enter_Text(self.lasttname,TestData.Lastname3)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountContains = self.get_Element_count(self.showpersontable)
        self.do_click(self.inputBreadCrumb)
        self.do_Enter_Text(self.lasttname,TestData.Lastname)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountStartsWith = self.get_Element_count(self.showpersontable)
        if personcountStartsWith>0 and personcountContains==4:
            return True
        else:
            return False
        
    def check_Search_By_First_Name_and_Last_Name_Field(self):
        print("Verify search person with First Name and Last Name filter")
        self.do_Enter_Text(self.firstname,TestData.firstname3)
        self.do_Enter_Text(self.lasttname,TestData.Lastname3)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountContains = self.get_Element_count(self.showpersontable)
        self.do_click(self.inputBreadCrumb)
        self.do_Enter_Text(self.firstname,TestData.firstname2)
        self.do_Enter_Text(self.lasttname,TestData.Lastname1)
        self.do_click(self.showbutton)
        time.sleep(2)
        personcountStartsWith = self.get_Element_count(self.showpersontable)
        if personcountStartsWith>0 and personcountContains==3:
            return True
        else:
            return False
        
    def do_Click_Show_Button(self):
        print("Click Show Button")
        self.do_click(self.showbutton)
        self.wait_until_page_loads()
        time.sleep(2)
    
    def do_Filter_Based_On_DateBetween(self):
        print("Filter Birth date and choose category as Date Between")
        self.do_click(self.filterBirthDate)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.dateBetweenFilterCategory)

    def do_Enter_DateFrom_And_DateTo_Values(self,birthDateFrom,birthDateTo):
        print("Enter Date From and Date To Values")
        self.do_select_calendar_date(self.dateFromFilterValue,birthDateFrom,self.selectCalendarDate)
        time.sleep(2)
        self.do_select_calendar_date(self.dateToFilterValue,birthDateTo,self.selectCalendarDate)

    def do_filter_Based_on_YearIs(self):
        print("Filter Birth date and choose category as Year is")
        self.do_click(self.filterBirthDate)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.yearIsFilterCategory)
    
    def do_Enter_YearIs_Value(self,yearIs):
        print("Enter Year Value")
        self.do_Enter_Text(self.yearIsValue,yearIs)
        self.do_select_Year(yearIs)
        
    def do_Apply_Filter(self):
        print("Click apply filter")
        self.do_click(self.applyFilter)
        self.wait_until_page_loads()
        time.sleep(1)

    def do_clear_virtual_node_filter(self):
        print("Click clear filter")
        self.do_click(self.filterVirtualNode)
        self.do_click(self.clearFilter)

    def get_No_Of_Records_Filtered(self):
        print("Verify Number of Records filtered")
        time.sleep(2)
        return self.get_Element_count(self.noOfRecords) - self.get_Element_count(self.noRecordsFound)
    
    #344 - "Show" Button should be fixed - NL-10
    def do_Verify_Show_Button_Position(self):
        print("Verify Show button position is on the top")
        showButtonYCoordinate = self.get_Element_Y_Coordinate(self.showbutton)
        firstNameYCoordinate = self.get_Element_Y_Coordinate(self.firstname)
        if(showButtonYCoordinate<firstNameYCoordinate):
            return True
        else:
            return False
    
    def verify_info_icon_exists(self):
        print("Verify info icon is displayed")
        return self.is_ElementExist(self.infoIcon)
    
    def get_date_of_birth_of_person(self):
        print("Get date of birth from first row")
        ele = self.get_Elements(self.dateOfBirthColumn)
        for e in ele:
            if(e.text != ""):
                return e.text
        return ""
    
    def do_filter_virtual_node(self,filterValue):
        print("Verify virtual node filter is working for the category"+filterValue)
        filterCategory = (By.XPATH,"//div[contains(@class,'multiselect')]//li//span[text()='"+filterValue+"']")
        self.do_click(self.filterVirtualNode)
        self.do_click(self.expandFiterDropDown)
        time.sleep(1)
        if self.is_element_clickable(self.selectAllCheckbox)==False:
            self.do_click(self.expandFiterDropDown)
        self.do_click(self.selectAllCheckbox)
        time.sleep(1)
        self.do_click(self.selectAllCheckbox)
        time.sleep(1)
        self.do_click(filterCategory)
        time.sleep(1)
        self.do_click(self.closeFilterDropDown)
        self.do_click(self.applyFilter)
        return self.get_No_Of_Records_Filtered()
       
