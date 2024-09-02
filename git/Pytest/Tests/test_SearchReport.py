import datetime
import pytest
from datetime import datetime
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_SearchReports(BaseTest):
    
    @pytest.mark.regression
    def test_Search_Report_Using_SubmisionDateFrom(self):
        global homePage
        global searchReports
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_Login(TestData.userName,TestData.password)
        searchReports = homePage.goto_Search_Report()
        self.reportsPage = searchReports.from_date_text_box()
        firstRowSubmissionDate = self.reportsPage.do_sortBasedonSubmissionDate()
        input_date_format = "%b %d, %Y %I:%M:%S %p"
        sortedDate = datetime.strptime(str(firstRowSubmissionDate), input_date_format)
        formatted_sortedDate = sortedDate.strftime("%m/%d/%Y")
        givenDate = datetime.strptime(TestData.submissionDateFrom, '%m/%d/%Y')
        formatted_givenDate = givenDate.strftime("%m/%d/%Y")
        assert formatted_sortedDate>=formatted_givenDate

    @pytest.mark.regression
    def test_Search_Report_Using_Indicators(self):
        homePage.goto_Search_Report()
        assert searchReports.check_search_report_indicator_field()

    @pytest.mark.regression
    def test_Auto_Complete(self):
        homePage.goto_Search_Report()
        assert searchReports.check_auto_complete_name_field()

    @pytest.mark.regression
    def test_Multiple_auto_Complete_name_field(self):
        homePage.goto_Search_Report()
        assert searchReports.check_multiple_auto_complete_name_field()

    @pytest.mark.regression
    def test_transaction_value_increment_and_decrement(self):
        homePage.goto_Search_Report_testing()
        assert searchReports.check_value_of_transaction_field()

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_fileterCategory_DateBetween(self):
        reports = homePage.goto_LatestReports()
        reports.do_Filter_Based_On_DateBetween()
        reports.do_Enter_DateFrom_And_DateTo_Values(TestData.submissionDateTimeFrom,TestData.submissionDateTimeTo)
        reports.do_Apply_Filter()
        recordCount = reports.get_No_Of_Records_Filtered()
        assert recordCount==1

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_fileterCategory_YearIs(self): 
        reports = homePage.goto_LatestReports()
        reports.do_filter_Based_on_YearIs()
        reports.do_Enter_YearIs_Value(TestData.yearIs)
        reports.do_Apply_Filter()
        recordCount = reports.get_No_Of_Records_Filtered()
        assert recordCount==TestData.yearIsRecordCount

    #586 - Table view can't have filter enabled only on specific columns
    @pytest.mark.regression
    @pytest.mark.bug
    def test_filter_only_in_one_column(self):
        searchReportsTesting = homePage.goto_Search_Report_testing()
        searchReportsTesting.do_Click_Show_Button()
        assert searchReportsTesting.get_No_of_filter_buttons()==1

    @pytest.mark.regression
    def test_Search_Report_bradcrumb(self):
        searchReports = homePage.goto_Search_Report()
        assert homePage.verify_bread_crumb(TestData.searchReportNav)
        searchReports.enter_reporting_entity_name(TestData.reportingEntityName)
        searchReports.select_Type_of_report(TestData.typeOfReport)
        searchReports.enter_submission_date_from(TestData.submissionDateFrom)
        searchReports.enter_submission_date_to(TestData.submissionDateTo)
        searchReports.do_Click_Show_Button()
        assert searchReports.get_No_Of_Records_Filtered()==1
        assert homePage.verify_bread_crumb(TestData.searchReportTableNav)
        homePage.click_link_in_breadcrumb("Input")
        assert homePage.verify_bread_crumb(TestData.searchReportNav)
        assert searchReports.get_report_entity_value()==TestData.reportingEntityName
        assert searchReports.get_type_of_report_value()==TestData.typeOfReport
        homePage.click_link_in_breadcrumb("Search report")
        assert searchReports.get_report_entity_value()==""
        assert searchReports.get_type_of_report_value()==""
        assert homePage.verify_bread_crumb(TestData.searchReportNav)
        searchReports.driver.back()
        homePage.click_link_in_breadcrumb("Input")
        assert homePage.verify_bread_crumb(TestData.searchReportNav)
        assert searchReports.get_report_entity_value()==TestData.reportingEntityName
        assert searchReports.get_type_of_report_value()==TestData.typeOfReport
    
    @pytest.mark.regression
    def test_Search_ReportTesting_bradcrumb_navigation(self):
        searchReports = homePage.goto_Search_Report_testing()
        assert homePage.verify_bread_crumb(TestData.searchReportTestNav)
        searchReports.enter_reporting_entity_name(TestData.reportingEntityName)
        searchReports.enter_submission_date_from(TestData.submissionDateAndTimeFrom)
        searchReports.enter_submission_date_to(TestData.submissionDateAndTimeTo)
        searchReports.enter_value_of_transaction("10")
        searchReports.do_Click_Show_Button()
        assert searchReports.get_No_Of_Records_Filtered()==6
        assert homePage.verify_bread_crumb(TestData.searchReportTestTableNav)
        homePage.click_link_in_breadcrumb("Input")
        assert homePage.verify_bread_crumb(TestData.searchReportTestNav)
        assert searchReports.get_report_entity_text_value()==TestData.reportingEntityName
        assert searchReports.get_transaction_value()=="10"
        homePage.click_link_in_breadcrumb("Search report (testing)")
        assert searchReports.get_report_entity_text_value()==""
        assert searchReports.get_transaction_value()=="0"
        assert homePage.verify_bread_crumb(TestData.searchReportTestNav)
        searchReports.driver.back()
        assert homePage.verify_bread_crumb(TestData.searchReportTestNav)
        assert searchReports.get_report_entity_text_value()==TestData.reportingEntityName
        
        


        




    