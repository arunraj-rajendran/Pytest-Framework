import pytest
from Config.config import TestData
from Pages import GraphView, SearchPersonPage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_SearchPersons(BaseTest):

    @pytest.mark.regression
    def test_SearchPerson_IsDirector_Filter(self):
        global homePage
        global searchPersonPage
        global searchperson
        global GraphView
        GraphView = GraphView.GraphView(self.driver)
        self.loginPage = LoginPage(self.driver)
        searchperson = SearchPersonPage.SearchPerson(self.driver)
        homePage = self.loginPage.do_Login(TestData.userName,TestData.password)
        searchPersonPage = homePage.goto_Search_Person()
        assert searchPersonPage.check_unspecified_search_person()
        homePage.goto_Search_Person()
        assert searchPersonPage.check_No_In_Isdirector_search_person()
        homePage.goto_Search_Person()
        assert searchPersonPage.check_Yes_In_Isdirector_search_person()
        homePage.goto_Search_Person()

    @pytest.mark.regression  
    def test_SearchPerson_Nationality_Filter(self):
        assert searchPersonPage.check_Nationality_DropDown_search_person()

    @pytest.mark.regression
    def test_Action_Button_Police(self):
        homePage.goto_Search_Person()
        assert searchperson.check_First_Name_Field()
        assert GraphView.Validate_police_and_Last_Name_Filter()
        assert GraphView.do_check_GraphLoaded()

    @pytest.mark.regression
    def test_Action_Button_Custom(self):
        homePage.goto_Search_Person()
        assert searchperson.check_First_Name_Field()
        assert GraphView.Validate_custom()

    @pytest.mark.regression
    def test_Search_By_First_Name(self):
        homePage.goto_Search_Person()
        assert searchperson.check_Search_By_First_Name_Field()
        assert GraphView.Validate_search_person_firstname_graph()
        assert GraphView.do_check_GraphLoaded()

    @pytest.mark.regression
    def test_Search_By_Last_Name(self):
        homePage.goto_Search_Person()
        assert searchperson.check_Search_By_Last_Name_Field()
        assert GraphView.Validate_police_and_Last_Name_Filter()
        assert GraphView.do_check_GraphLoaded()

    @pytest.mark.regression
    def test_Search_By_First_Name_And_Last_Name(self):
        homePage.goto_Search_Person()
        assert searchperson.check_Search_By_First_Name_and_Last_Name_Field()
        assert GraphView.Validate_first_and_Last_Name_Filter()
        assert GraphView.do_check_GraphLoaded()

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_fileterCategory_DateBetween(self):
        searchPerson = homePage.goto_Search_Person()
        searchPerson.do_Click_Show_Button()
        searchPerson.do_Filter_Based_On_DateBetween()
        searchPerson.do_Enter_DateFrom_And_DateTo_Values(TestData.birthDateFrom,TestData.birthDateTo)
        searchPerson.do_Apply_Filter()
        recordCount = searchPerson.get_No_Of_Records_Filtered()
        assert recordCount==7

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_fileterCategory_YearIs(self):
        searchPerson = homePage.goto_Search_Person()
        searchPerson.do_Click_Show_Button()
        searchPerson.do_filter_Based_on_YearIs()
        searchPerson.do_Enter_YearIs_Value(TestData.birthYearIs)
        searchPerson.do_Apply_Filter()
        recordCount = searchPerson.get_No_Of_Records_Filtered()
        assert recordCount==3

    #344 - "Show" Button should be fixed - NL-10
    @pytest.mark.regression
    def test_ShowButton_Position(self):
        searchPerson = homePage.goto_Search_Person()
        assert searchPerson.do_Verify_Show_Button_Position()

    @pytest.mark.regression
    def test_infoIcon_exists(self):
        searchPerson = homePage.goto_Search_Person()
        searchPerson.do_Click_Show_Button()
        searchPerson.verify_info_icon_exists()
    
    
    #474 - Virtual node filter is not working 
    @pytest.mark.regression
    @pytest.mark.bug
    def test_virtual_node_filter(self): 
        searchPerson = homePage.goto_Search_Person()
        searchPerson.do_Click_Show_Button()
        assert searchPerson.do_filter_virtual_node("No")==0
        assert searchPerson.do_filter_virtual_node("Yes")==21
        assert searchPerson.do_filter_virtual_node("Unspecified")==34
        searchPerson.do_clear_virtual_node_filter()
        assert searchPerson.get_No_Of_Records_Filtered()==55
