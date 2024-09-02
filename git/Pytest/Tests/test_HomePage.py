import pytest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_HomePage(BaseTest):

    @pytest.mark.regression
    def test_Homepage_English_to_French_Language(self):
        global homePage
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_Login(TestData.userName,TestData.password)
        homePage.changeLanguage_To_French()
        print("Verify Derniers Rapports in French Exist: " + str(homePage.is_DerniersRapports_Exist()))
        assert homePage.is_DerniersRapports_Exist()
        homePage.changeLanguage_To_English()

    @pytest.mark.regression
    def test_Homepage_French_to_English_Language(self):
        homePage.changeLanguage_To_English()
        print("Verify Latest Report in English Exist: " + str(homePage.is_LatestReports_Exist()))
        assert homePage.is_LatestReports_Exist() 

    #342 - Multiple tabs NL-1
    @pytest.mark.regression
    def test_Open_Links_in_newTab(self):
        print("Verify links are opened in new tab")
        homePage.do_Open_In_New_tab_latestReports()
        assert homePage.do_verify_new_tab_is_opened()
        homePage.do_Open_In_New_tab_searchContactPerson()
        assert homePage.do_verify_new_tab_is_opened()
        homePage.do_Open_In_New_tab_searchPerson()
        assert homePage.do_verify_new_tab_is_opened()
        homePage.do_Open_In_New_tab_searchReport()
        assert homePage.do_verify_new_tab_is_opened()
        homePage.do_Open_In_New_tab_showReport()
        assert homePage.do_verify_new_tab_is_opened()
        homePage.do_Open_In_New_tab_searchReportTesting()
        assert homePage.do_verify_new_tab_is_opened()

    @pytest.mark.regression
    def test_App_Version_screen(self):
        print("Verify UI and Backend Versions are displayed")
        appVersion = homePage.do_click_appversion()
        assert appVersion.is_ui_version_visible()
        assert appVersion.is_backend_version_visible()

    @pytest.mark.regression
    def test_Latest_reports_bradcrumb_navigation(self):
        self.reports = homePage.goto_LatestReports()
        assert homePage.verify_bread_crumb(TestData.latestReportsNav)
        self.reports.goto_Report(TestData.reportName[0])
        self.reports.goto_report_graph()
        assert homePage.verify_bread_crumb(TestData.latestReportsGraphNav)
        homePage.click_link_in_breadcrumb("Results")
        assert self.reports.get_No_Of_Records_Filtered()==1
        homePage.click_link_in_breadcrumb("Latest reports")
        assert self.reports.get_No_Of_Records_Filtered()>1

    