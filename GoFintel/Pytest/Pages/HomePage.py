import time
from Pages import AppVersion, LogoutPage, Reports, SearchPersonPage, SearchReport, ShowReport
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):

    #By Locators
    homeButton = (By.XPATH,"//a/span[contains(@class,'home')]")
    ele_welcomeText = (By.XPATH,"//div[contains(@class,'tabview-nav-content')]//*[text()='My graphs' or text()='Mes graphiques']")
    latestReports = (By.XPATH,"//div[@class='menu-wrapper']//following::*[text()='Latest reports']")
    derniersRapports = (By.XPATH,"//div[@class='menu-wrapper']//following::*[text()='Derniers rapports']")
    changeLanguage = (By.XPATH,"//div[@class='layout-topbar-actions-right']//div[@class = 'p-dropdown-trigger']")
    frenchLanguage = (By.XPATH,"//div[@class='p-dropdown-items-wrapper']//li[@aria-label= 'Français']")
    englishLanguage = (By.XPATH,"//div[@class='p-dropdown-items-wrapper']//li[@aria-label= 'English']")
    spanishLanguage = (By.XPATH,"//div[@class='p-dropdown-items-wrapper']//li[@aria-label= 'Español']")
    dutchLanguage = (By.XPATH,"//div[@class='p-dropdown-items-wrapper']//li[@aria-label= 'Nederlands']")
    
    userIcon = (By.XPATH,"//div[@class='layout-topbar-actions-right']//li[@class = 'layout-topbar-item']/button")
    logOut = (By.XPATH,"//div[@class='layout-topbar-actions-right']//child::ul//span[text()='Log Out' or text()='Se déconnecter']//parent::button")
    showreport = (By.XPATH,"//a[text()='Show report']")
    searchperson = (By.XPATH,"//a[text()='Search person']")
    searchreport = (By.XPATH,"//a[text()='Search report']")
    searchreporttesting = (By.XPATH,"//a[text()='Search report (testing)']")
    myGraphs = (By.XPATH,"//a[text()='My graphs']")
    allGraphs = (By.XPATH,"//a[text()='All graphs']")
    assignedGraphs = (By.XPATH,"//a[text()='Assigned graphs']")
    leftPane = (By.XPATH,"//div[contains(@class,'layout-menu-active')]")
    expandLeftPane = (By.XPATH,"//div[contains(@class,'layout-wrapper  layout-menu-light layout-topbar-blue layout-menu-static p-input-filled')]//button[2]")
    collaspseLeftPane = (By.XPATH, "//div[contains(@class,'layout-wrapper  layout-menu-light layout-topbar-blue layout-menu-static layout-menu-active p-input-filled')]//button[2]")
    selectedLanguage = (By.XPATH,"//div[contains(@class,'layout-topbar-actions-right')]//span[contains(@class,'inputtext')]")
    reportsTabMegaMenu = (By.XPATH,"//span[text()='Reports']//parent::a")
    reportingEntitiesTabMegaMenu = (By.XPATH,"//span[text()='Reporting entities']//parent::a")
    personsTabMegaMenu = (By.XPATH,"//span[text()='Persons']//parent::a")
    latestReportsMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Latest reports']//parent::a")
    searchReportMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Search report']//parent::a")
    showReportMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Show report']//parent::a")
    searchReportTestingMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Search report (testing)']//parent::a")
    searchContactPersonMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Search contact person']//parent::a")
    searchPersonMegaMenu = (By.XPATH,"//div[contains(@class,'megamenu')]//span[text()='Search person']//parent::a")
    appVersion = (By.XPATH,"//div[@class='menu-wrapper']//following::*[text()='App Version']")
    breadCrumbList = (By.XPATH,"//div[contains(@class,'breadcrumb')]//li")

    #construct of the page class
    def __init__(self,driver):
        super().__init__(driver) 

    def is_WelcomeText_visible(self):
        print("Verify Welcome Text is visible : "+ str(self.is_ElementExist(self.ele_welcomeText)))
        return self.is_ElementExist(self.ele_welcomeText)
    
    def changeLanguage_To_French(self):
        if self.get_Text_Value(self.selectedLanguage) != "Français":
            print("Change Language from english to french")
            self.do_click(self.changeLanguage)
            self.do_click(self.frenchLanguage)
            self.wait_until_page_loads()
            time.sleep(1)

    def is_DerniersRapports_Exist(self):
        print("Verify Latest Report Exists in french")
        return self.is_ElementExist(self.derniersRapports)
    
    def changeLanguage_To_English(self):
        if self.get_Text_Value(self.selectedLanguage) != "English":
            print("Change Language to english")
            self.do_click(self.changeLanguage)
            self.do_click(self.englishLanguage)
            self.wait_until_page_loads()
            time.sleep(1)

    def is_LatestReports_Exist(self):
        print("Verify Latest Report Exists")
        return self.is_ElementExist(self.latestReports)
    
    def changeLanguage_To_Spanish(self):
        if self.get_Text_Value(self.selectedLanguage) != "Español":
            print("Change Language to Español")
            self.do_click(self.changeLanguage)
            self.do_click(self.spanishLanguage)
            self.wait_until_page_loads()
            time.sleep(1)

    def changeLanguage_To_Nederlands(self):
        if self.get_Text_Value(self.selectedLanguage) != "Nederlands":
            print("Change Language to Nederlands")
            self.do_click(self.changeLanguage)
            self.do_click(self.dutchLanguage)
            self.wait_until_page_loads()
            time.sleep(1)

    def do_Logout(self):
        print("Logout from Home page")
        self.do_click(self.userIcon)
        self.do_click(self.logOut)
        return LogoutPage.LogOutPage(self.driver)
        
    def goto_LatestReports(self):
        self.changeLanguage_To_English()
        print("Go to Latest Reports")
        self.do_click(self.latestReports)
        self.do_get_mouse_to_screen_homeposition()
        return Reports.Reports(self.driver)
    
    def goto_Show_Report(self):
        print("Goto Show Report")
        self.do_click(self.showreport)
        return ShowReport.Showreport(self.driver)
    
    def goto_Search_Person(self):
        print("Goto Search Person")
        self.changeLanguage_To_English()
        self.do_click(self.searchperson)
        return SearchPersonPage.SearchPerson(self.driver)

    def goto_Search_Report(self):
        print("Go to search Report")
        self.changeLanguage_To_English()
        self.do_click(self.searchreport)
        return SearchReport.SearchReports(self.driver)
    
    def goto_Search_Report_testing(self):
        print("Go to search report testing")
        self.changeLanguage_To_English()
        self.do_click(self.searchreporttesting)
        return SearchReport.SearchReports(self.driver)
    
    def goto_my_graphs(self):
        print("Go to Work space - My graphs")
        self.do_click(self.myGraphs)
        self.do_get_mouse_to_screen_homeposition()

    def goto_all_graphs(self):
        print("Go to Work space - All graphs")
        self.do_click(self.allGraphs)
        self.do_get_mouse_to_screen_homeposition()

    def goto_assigned_graphs(self):
        print("Go to Work space - Assigned graphs")
        self.do_click(self.assignedGraphs)
        self.do_get_mouse_to_screen_homeposition()

    def do_Expand_LeftPane(self):
        print("Expand or collapse Left Pane")
        self.do_click(self.expandLeftPane)

    def do_Collapse_LeftPane(self):
        print("Expand or collapse Left Pane")
        self.do_click(self.collaspseLeftPane)
        time.sleep(3)

    def do_get_mouse_to_screen_homeposition(self):
        action = ActionChains(self.driver)
        if (self.get_Element_count(self.leftPane)<1):
            action.move_to_element_with_offset(self.get_Element(self.expandLeftPane),-self.get_Element_X_Coordinate(self.expandLeftPane)-18,-self.get_Element_Y_Coordinate(self.expandLeftPane)-18).perform()
        else :
            action.move_to_element_with_offset(self.get_Element(self.collaspseLeftPane),-self.get_Element_X_Coordinate(self.collaspseLeftPane)-18,-self.get_Element_Y_Coordinate(self.collaspseLeftPane)-18).perform()

    def do_click_homeButton(self):
        print("Click home button in the bread crumb")
        self.do_click(self.homeButton)
 
    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_latestReports(self):
        print("Open Latest Reports from mega menu in new tab")
        self.do_click(self.reportsTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.latestReportsMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_searchReport(self):
        print("Open Search Report from mega menu in new tab")
        self.do_click(self.reportsTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.searchReportMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_showReport(self):
        print("Open Show Report from mega menu in new tab")
        self.do_click(self.reportsTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.showReportMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_searchReportTesting(self):
        print("Open Search Reoprt (Testing) from mega menu in new tab")
        self.do_click(self.reportsTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.searchReportTestingMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_searchContactPerson(self):
        print("Open Search Contact Person from mega menu in new tab")
        self.do_click(self.reportingEntitiesTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.searchContactPersonMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_Open_In_New_tab_searchPerson(self):
        print("Open Search Person from mega menu in new tab")
        self.do_click(self.personsTabMegaMenu)
        action = self.get_action_class()
        self.get_ctrl_key()
        action.key_down(self.get_ctrl_key()).perform()
        self.do_click(self.searchPersonMegaMenu)
        action.key_up(self.get_ctrl_key()).perform()

    #342 - Multiple tabs NL-1
    def do_verify_new_tab_is_opened(self):
        
        print("Verify New tab is opened")
        if(self.get_open_tabs_count()>1):
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            assert self.is_ElementExist(self.homeButton)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return True
        else:
            return False
        
    def do_click_appversion(self):
        print("Click App version link in the left navgation")
        self.do_click(self.appVersion)
        return AppVersion.AppVersion(self.driver)
    
    def verify_bread_crumb(self,latestReportsnav):
        print("Verify bread crumb is "+str(latestReportsnav))
        i =1
        breadCrumNav = []
        ele = self.get_Elements(self.breadCrumbList)
        for e in ele:
            if i>2 and i%2 !=0:
                breadCrumNav.append(e.text)
            i=i+1
        if breadCrumNav == latestReportsnav:
            return True
        else:
            return False
        
    def click_link_in_breadcrumb(self,linkToClik):
        print("Click  "+linkToClik+"in the bread crumb")
        ele = self.get_Elements(self.breadCrumbList)
        for e in ele:
            if e.text == linkToClik:
                self.do_click_element(e)
                break
        time.sleep(1)
