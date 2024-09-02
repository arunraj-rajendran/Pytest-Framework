import locale
import time
from Config.config import TestData
from Pages import GraphView
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Reports(BasePage):

    #By Locators
    filterReports = (By.XPATH,"//div[@class='content tableReport']//th[2]//button")
    filterDropDown = (By.XPATH,"//div[@class='p-column-filter-constraints']//span[1]")
    dropDownValue = (By.XPATH,"//li//span[text()='Equals' or text()='Es igual' or text()='Équivaut à' or text()='Is gelijk aan']")
    searchField = (By.XPATH,"//div[@class='p-column-filter-constraint']//input[@placeholder]")
    applyFilter = (By.XPATH,"//div[@class='p-column-filter-buttonbar']//button[2]")
    firstReportGraph = (By.XPATH,"//div[@class='content tableReport']//child::tr[1]/td/button")
    firstRow = (By.XPATH,"//div[@class='content tableReport']//tbody//child::tr[1]")
    sortBasedonSubmissionDate = (By.XPATH,"//span[text()='Submission date and time']//..//child::span[contains(@data-pc-section,'sort')]")
    homelink = (By.XPATH,"//li[contains(@class,'breadcrumb')]//span[contains(@class,'home')]")
    search = (By.XPATH,"//input[@placeholder='Search']")
    filterSubmissionDate = (By.XPATH,"//span[text()='Submission date and time']//..//child::button[contains(@class,'filter')]")
    expandFiterDropDown = (By.XPATH,"//div[contains(@class,'filter')]//div[contains(@class,'dropdown-trigger')]")
    dateBetweenFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Date Between']")
    yearIsFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Year Is']")
    dateFromFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[1]")
    dateToFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[2]")
    yearIsValue = (By.XPATH,"//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input")
    yearPicker = (By.XPATH,"//div[contains(@class,'yearpicker')]/span[text()='"+TestData.yearIs+"']")
    noOfRecords = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr")
    noRecordsFound = (By.XPATH,"//*[contains(text(),'No available options')]")
    submissionDateValue = (By.XPATH,"//tbody[@class='p-datatable-tbody']/tr/td[3]")
    submissionDateValueSearchReports = (By.XPATH,"//tbody[@class='p-datatable-tbody']/tr/td[4]")
    firstRowcheckbox = (By.XPATH,"//div[contains(@class,'content tableReport')]//tbody/tr[1]//div[@role]")
    showOnGraph = (By.XPATH,"//button[text()='Show on graph']")
    selectCalendarDate = (By.XPATH,"//table[contains(@class,'datepicker')]//span[contains(@class,'highlight')]")

    #construct of the page class
    def __init__(self,driver):
        super().__init__(driver)

    def goto_Report(self,reportName):
        print("Filter and show Report "+reportName)
        self.do_click(self.filterReports)
        time.sleep(1)
        self.do_click(self.filterDropDown)
        self.do_click(self.dropDownValue)
        self.do_Enter_Text(self.searchField,reportName)
        self.do_click(self.applyFilter)

    def goto_report_graph(self):
        print("Click on show graph for the first report")
        time.sleep(1)
        element_to_hover_over = self.get_Element(self.firstRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.firstReportGraph)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()
        self.wait_until_page_loads()
        time.sleep(1)
        return GraphView.GraphView(self.driver)
        
    def get_submission_date(self):
        print("Get submission date")
        return str(self.get_Element_Text(self.submissionDateValue))
    
    def do_sortBasedonSubmissionDate(self):
        print("Sort the table based on Subission date column")
        time.sleep(1)
        self.do_click(self.sortBasedonSubmissionDate)
        return str(self.get_Element_Text(self.submissionDateValueSearchReports))
    
    def do_Filter_Based_On_DateBetween(self):
        print("Filter submission date and choose filter catgory as Date Between")
        self.do_click(self.filterSubmissionDate)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.dateBetweenFilterCategory)

    def do_Enter_DateFrom_And_DateTo_Values(self,submissionDateFrom,submissionDateTo):
        print("Enter Date from and Date to values")
        self.do_select_calendar_date(self.dateFromFilterValue,submissionDateFrom,self.selectCalendarDate)
        self.do_select_calendar_date(self.dateToFilterValue,submissionDateTo,self.selectCalendarDate)
        self.do_click(self.search)
        time.sleep(1)
        self.do_click(self.filterSubmissionDate)

    def do_filter_Based_on_YearIs(self):
        print("Filter submission date and choose filter catgory as Year Is")
        self.do_click(self.filterSubmissionDate)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.yearIsFilterCategory)
    
    def do_Enter_YearIs_Value(self,yearIs):
        print("Enter Year Value")
        self.do_Enter_Text(self.yearIsValue,yearIs)
        self.do_click(self.yearIsValue)
        self.do_select_Year(yearIs)
        
    def do_Apply_Filter(self):
        print("Click Apply Filter")
        self.do_click(self.applyFilter)

    def do_click_on_show_graph(self):
        print("Click on show graph")
        self.do_click(self.showOnGraph)
        return GraphView.GraphView(self.driver)

    def do_select_firstrow(self):
        print("Select first row of the table")
        self.do_click(self.firstRowcheckbox)

    def get_No_Of_Records_Filtered(self):
        print("Verify Number of records filtered")
        self.wait_until_page_loads()
        time.sleep(1)
        return self.get_Element_count(self.noOfRecords) - self.get_Element_count(self.noRecordsFound)

    def verify_date_format_is_english(self,dtValue,EnglishFormat):
        print("Verify date format is in english")
        return self.verify_date_format(dtValue, EnglishFormat)
    
    def verify_date_format_is_spanish(self,dtValue,SpanishFormat):
        print("Verify date format is in spanish")
         # Define French month abbreviations
        spanish_month_abbreviations = {
            'de ene. de': 'January',
            'de feb. de': 'February',
            'de mar. de': 'March',
            'de abr. de': 'April',
            'de may. de': 'May',
            'de jun. de': 'June',
            'de jul. de': 'July',
            'de ago. de': 'August',
            'de sep. de': 'September',
            'de oct. de': 'October',
            'de nov. de': 'November',
            'de dic. de': 'December'
        }
        for spanish_month, english_month in spanish_month_abbreviations.items():
            dtValue = dtValue.replace(spanish_month, english_month)
        return self.verify_date_format(dtValue, SpanishFormat)
    
    def verify_date_format_is_french(self,dtValue,FrenchFormat):
        print("Verify date format is in french")
        # Define French month abbreviations
        french_month_abbreviations = {
            'janv.': 'january',
            'févr.': 'february',
            'mars': 'march',
            'avr.': 'april',
            'mai': 'may',
            'juin': 'june',
            'juil.': 'july',
            'août': 'august',
            'sept.': 'september',
            'oct.': 'october',
            'nov.': 'november',
            'déc.': 'december'
        }
        
        for french_month, english_month in french_month_abbreviations.items():
            dtValue = dtValue.replace(french_month, english_month)
        return self.verify_date_format(dtValue, FrenchFormat)
    
    def verify_date_format_is_nederlands(self,dtValue,DutchFormat):
        print("Verify date format is in dutch format")
        dutch_month_abbreviations = {
            'jan.': 'January',
            'feb.': 'February',
            'mrt.': 'March',
            'apr.': 'April',
            'mei.': 'May',
            'jun.': 'June',
            'jul.': 'July',
            'aug.': 'August',
            'sep.': 'September',
            'okt.': 'October',
            'nov.': 'November',
            'dec.': 'December',
            'jan': 'January',
            'feb': 'February',
            'mrt': 'March',
            'apr': 'April',
            'mei': 'May',
            'jun': 'June',
            'jul': 'July',
            'aug': 'August',
            'sep': 'September',
            'okt': 'October',
            'nov': 'November',
            'dec': 'December'
        }
        for dutch_month, english_month in dutch_month_abbreviations.items():
            dtValue = dtValue.replace(dutch_month, english_month)
        return self.verify_date_format(dtValue, DutchFormat)
    
    def verify_gremlin_results(self,Query):
        self.execute_gremlin_query(Query)