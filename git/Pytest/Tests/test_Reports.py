import time
import pytest
from Config.config import TestData
from Pages import GraphView, Reports
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Test_Reports(BaseTest):

    @pytest.mark.regression
    def test_GraphLoadsOrNot(self):
        global homePage
        global graphView
        global searchperson
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_Login(TestData.userName,TestData.password)
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        assert graphView.do_check_GraphLoaded()
    
    @pytest.mark.regression
    def test_QuickHighlightToolbar(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.check_clicking_highlighted_nodes_dropdown()  
        assert graphView.check_deselect_multiselect_checkbox()
        assert graphView.check_filter_highlighted_nodes()
        graphView.check_clicking_highlighted_edges_dropdown()
        assert graphView.check_deselect_multiselect_checkbox()
        assert graphView.check_filter_highlighted_Edges()
    
    @pytest.mark.regression
    def test_Visual_Profile(self):
        assert graphView.check_selecting_detailed_visual_profile_dropdown()
        assert graphView.check_selecting_edge_centric_visual_profile_dropdown()
        assert graphView.check_selecting_node_centric_visual_profile_dropdown()
        assert graphView.check_selecting_default_visual_profile_dropdown() 

    @pytest.mark.regression
    def test_Smart_Sidebar(self):
        assert graphView.check_smart_sidebar()==2
        assert graphView.check_smart_sidebar_minimize_button()
        assert graphView.check_smart_sidebar_delete_button()==1
        assert graphView.check_smart_sidebar_deleteall_button()==0
        assert graphView.check_smart_sidebar_panel_close()

    @pytest.mark.regression
    def test_GraphExport_Image(self):
        assert graphView.do_download_graph_image()

    @pytest.mark.regression
    def test_GraphExport_Pdf(self):
        assert graphView.do_download_graph_pdf()

    @pytest.mark.regression
    def test_GraphExport_AnalyticsNotebook(self):
        assert graphView.do_download_graph_AnalyticsNotebook()
     
    @pytest.mark.regression
    def test_Graph_TableView(self):
        assert graphView.do_Load_TableView()
        assert graphView.do_Verify_TableViewTabs()
        assert graphView.do_Verify_TableContents()
    
    @pytest.mark.regression
    def test_History_tab(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName1)
        graphView = self.reports.goto_report_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.check_property_value_history_tab()

    @pytest.mark.regression
    def test_Show_Report(self):
        showReport = homePage.goto_Show_Report()
        graphView = showReport.check_show_report(TestData.reportName[1])
        assert graphView.do_check_GraphLoaded()
 
    @pytest.mark.regression
    def test_Search_Box(self):
        homePage.goto_LatestReports()
        assert graphView.check_search_box()

    @pytest.mark.regression
    def test_Sort_Button(self):
        homePage.goto_LatestReports()
        assert graphView.check_sort_button()

    @pytest.mark.regression
    def test_ReportExport_Xls(self):
        homePage.goto_LatestReports()
        assert graphView.check_report_xls_download()

    @pytest.mark.regression
    def test_ReportExport_Csv(self):
        assert graphView.check_report_csv_download()

    @pytest.mark.regression
    def test_ReportExport_pdf(self):
        assert graphView.check_report_pdf_download() 
    
    @pytest.mark.regression
    def test_Action_Button_Show_On_Graph(self):
        homePage.goto_LatestReports()
        graphView.check_action_button_show_on_graph()
        assert graphView.do_check_GraphLoaded()
    
    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_DateBetween_Filter_TableView_ReportTab(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.do_Load_TableView()
        graphView.goto_Report_Tab()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateTimeFrom_And_DateTimeTo_Values(TestData.reportSubmissionDateTimeFrom,TestData.reportSubmissionDateTimeTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateTimeFrom_And_DateTimeTo_Values(TestData.reportSubmissionDateTimeFrom,TestData.negativeReportSubmissionDateTimeTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0
    
    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_YearIs_Filter_TableView_ReportTab(self): 
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.reportYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.negativeReportYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0
    
    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_DateBetween_Filter_TableView_TransactionTab(self):
        graphView.goto_Transaction_Tab()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateTimeFrom_And_DateTimeTo_Values(TestData.DateAndTimeOfTransactionFrom,TestData.DateAndTimeOfTransactionTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateTimeFrom_And_DateTimeTo_Values(TestData.DateAndTimeOfTransactionFrom,TestData.negativeDateAndTimeOfTransactionTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_YearIs_Filter_TableView_TransactionTab(self):
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.transactionYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.negativeReportYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0

    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_DateBetween_Filter_TableView_PersonTab(self):
        graphView.goto_Person_Tab()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateFrom_And_DateTo_Values(TestData.personBirthDateFrom,TestData.personBirthDateTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_Filter_Based_On_DateBetween()
        graphView.do_Enter_DateFrom_And_DateTo_Values(TestData.personBirthDateFrom,TestData.negativePersonBirthDateTo)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0 
    
    #250 - "Date between" and "Year" as date operators - NL-8
    @pytest.mark.regression
    def test_YearIs_Filter_TableView_PersonTab(self):
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.personBirthYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 1
        graphView.do_click_filterdate()
        graphView.do_Clear_Filter()
        graphView.do_filter_Based_on_YearIs()
        graphView.do_Enter_YearIs_Value(TestData.negativeReportYearIs)
        graphView.do_Apply_Filter()
        assert graphView.get_No_Of_Records_Filtered() == 0
    
    #261 - Node deselection with ESC (single and multi)
    @pytest.mark.regression
    def test_ESC_Key_To_Desect_Node(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_Select_Node()
        assert graphView.do_Verify_QuickAccessToolBar_Enabled()
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        assert graphView.do_Verify_QuickAccessToolBar_Disabled()
   
    #331 - Node selection not working when menu is collapsed
    @pytest.mark.regression
    def test_Node_selection_when_menu_is_collapsed(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_Select_Node()
        graphView.do_click_node("","")
        homePage.do_Collapse_LeftPane()
        graphView.do_click_Node_when_left_pane_is_collapsed()
        assert graphView.do_Verify_QuickAccessToolBar_Enabled()
        homePage.do_Expand_LeftPane()

    #347 - i-Button to display properties - NL-14
    @pytest.mark.regression
    def test_full_screen_reading_mode(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        assert graphView.do_check_GraphLoaded()
        graphView.do_double_click_node("Transaction","")
        assert graphView.verify_Description_Property_Text()
        assert graphView.verify_full_screen_readingmode()
        graphView.do_close_modal()
     
    #348 - Filter/sort option for table view of graph - NL-19
    @pytest.mark.regression
    def test_filter_and_sort_available_inTabeView(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.do_Load_TableView()
        assert graphView.verify_sort_and_filter_nodesTab()
        assert graphView.verify_sort_and_filter_EdgesTab()
    
    #349 - Expand/collapse virtual nodes - NL-21
    @pytest.mark.regression
    def test_expand_and_collapse_virtual_nodes(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.do_Load_TableView()
        assert graphView.verify_virtual_nodes_exists()
        assert graphView.verify_virtual_node_expand_and_collapse()
   
    #351 - Plus and Minus zoom buttons - NL-16
    @pytest.mark.regression
    def test_zoom_toolbar_icons(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        assert graphView.verify_zoom_reset_exists()
        assert graphView.verify_zoom_selected_node_exists()
        assert graphView.verify_search_exists()
        assert graphView.verify_zoom_fit_to_Screen_exists()
        assert graphView.verify_zoom_in_exists()
        assert graphView.verify_zoom_out_exists()
        assert graphView.verify_unhighlight_all_exists()
        assert graphView.verify_deselect_all_exists()
        assert graphView.verify_area_highlight_exists()
        assert graphView.verify_area_select_exists()
        assert graphView.verify_unhighlight_all_disables()
        assert graphView.verify_deselect_all_Enables()
        assert graphView.verify_deselect_all_Disables()
    
    @pytest.mark.regression
    def test_counterIcon_nodes(self):    
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        assert graphView.verify_click_counter_icon_expands_newNodes_given_label(str("Jasmijn Beentjes "))
    
    @pytest.mark.regression
    @pytest.mark.bug
    def test_gaphView_search(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.do_click_unhighlightAll()
        graphView.do_click_search()
        graphView.do_enter_search_input("Report")
        assert graphView.verify_node_highlighted_for_search()
        assert graphView.verify_edge_highlighted_for_search()
        graphView.do_enter_search_input("Dec 17")
        assert graphView.verify_node_highlighted_for_search()
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName1)
        graphView = self.reports.goto_report_graph()
        assert graphView.verify_node_highlighted_for_search()== False

    @pytest.mark.regression
    def test_transactioncount_property_sidebar(self): 
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("person","")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 2
        graphView.do_clear_smartsidebar()
        graphView.do_double_click_node("account","")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 1
        graphView.do_clear_smartsidebar()
        graphView.do_double_click_node("entity","")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 1
        graphView.do_clear_smartsidebar()

        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForTransactionCount[0])
        graphView = self.reports.goto_report_graph()
        #graphView.do_click_fit_to_screen()
        graphView.do_double_click_node("person","JAN DE WAARD")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 3
        graphView.do_clear_smartsidebar()
        graphView.do_double_click_node("account","NL77BNKX5454541110")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 3
        graphView.do_clear_smartsidebar()
        graphView.do_double_click_node("account","XX54565673564375")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 3
        graphView.do_clear_smartsidebar()
        graphView.do_double_click_node("entity","ZZZ BV")
        assert int(graphView.verify_transactionCount_property_sidebar()) == 3
        graphView.do_clear_smartsidebar()
    
    @pytest.mark.regression
    def test_locale_date_and_time(self): 
        self.reports = homePage.goto_LatestReports()
        dtValue = self.reports.get_submission_date()
        assert self.reports.verify_date_format_is_english(dtValue,TestData.EnglishDateTimeFormat)
        homePage.changeLanguage_To_French()
        dtValue = self.reports.get_submission_date()
        assert self.reports.verify_date_format_is_french(dtValue,TestData.FrenchDateTimeFormat)
        homePage.changeLanguage_To_Spanish()
        dtValue = self.reports.get_submission_date()
        assert self.reports.verify_date_format_is_spanish(dtValue,TestData.SpanishDateTimeFormat)
        homePage.changeLanguage_To_Nederlands()
        dtValue = self.reports.get_submission_date()
        assert self.reports.verify_date_format_is_nederlands(dtValue,TestData.DutchDatTimeFormat)
        
        homePage.changeLanguage_To_English()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        dateTime = graphView.get_date_and_time_of_transaction()
        assert self.reports.verify_date_format_is_english(dateTime,TestData.EnglishDateTimeFormat)
        graphView.do_double_click_node("person","")
        dateOfBirth = graphView.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_english(dateOfBirth,TestData.EnglishDateFormat)
        graphView.do_double_click_node("person","")
        graphView.do_click_DOB_property()
        validFrom = graphView.get_valid_from_value()
        assert self.reports.verify_date_format_is_english(validFrom,TestData.EnglishDateTimeFormat)
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        dateOfBirthTableView = graphView.get_date_of_birth_of_person_tableView()
        assert self.reports.verify_date_format_is_english(dateOfBirthTableView,TestData.EnglishDateFormat)
        graphView.goto_Transaction_Tab()
        dateTimeTableView = graphView.get_date_and_time_tableView()
        assert self.reports.verify_date_format_is_english(dateTimeTableView,TestData.EnglishDateTimeFormat)

        self.reports = homePage.goto_LatestReports()
        homePage.changeLanguage_To_French()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        dateTime = graphView.get_date_and_time_of_transaction()
        assert self.reports.verify_date_format_is_french(dateTime,TestData.FrenchDateTimeFormat)
        graphView.do_double_click_node("person","")
        dateOfBirth = graphView.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_french(dateOfBirth,TestData.OtherDateFormat)
        graphView.do_double_click_node("person","")
        graphView.do_click_DOB_property()
        validFrom = graphView.get_valid_from_value()
        assert self.reports.verify_date_format_is_french(validFrom,TestData.FrenchDateTimeFormat)
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        dateOfBirthTableView = graphView.get_date_of_birth_of_person_tableView()
        assert self.reports.verify_date_format_is_french(dateOfBirthTableView,TestData.OtherDateFormat)
        graphView.goto_Transaction_Tab()
        dateTimeTableView = graphView.get_date_and_time_tableView()
        assert self.reports.verify_date_format_is_french(dateTimeTableView,TestData.FrenchDateTimeFormat)

        self.reports = homePage.goto_LatestReports()
        homePage.changeLanguage_To_Spanish()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        dateTime = graphView.get_date_and_time_of_transaction()
        assert self.reports.verify_date_format_is_spanish(dateTime,TestData.SpanishDateTimeFormat)
        graphView.do_double_click_node("person","")
        dateOfBirth = graphView.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_spanish(dateOfBirth,TestData.OtherDateFormat)
        graphView.do_double_click_node("person","")
        graphView.do_click_DOB_property()
        validFrom = graphView.get_valid_from_value()
        assert self.reports.verify_date_format_is_spanish(validFrom,TestData.SpanishDateTimeFormat)
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        dateOfBirthTableView = graphView.get_date_of_birth_of_person_tableView()
        assert self.reports.verify_date_format_is_spanish(dateOfBirthTableView,TestData.OtherDateFormat)
        graphView.goto_Transaction_Tab()
        dateTimeTableView = graphView.get_date_and_time_tableView()
        assert self.reports.verify_date_format_is_spanish(dateTimeTableView,TestData.SpanishDateTimeFormat)

        self.reports = homePage.goto_LatestReports()
        homePage.changeLanguage_To_Nederlands()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        dateTime = graphView.get_date_and_time_of_transaction()
        assert self.reports.verify_date_format_is_nederlands(dateTime,TestData.DutchDatTimeFormat)
        graphView.do_double_click_node("person","")
        dateOfBirth = graphView.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_nederlands(dateOfBirth,TestData.OtherDateFormat)
        graphView.do_double_click_node("person","")
        graphView.do_click_DOB_property()
        validFrom = graphView.get_valid_from_value()
        assert self.reports.verify_date_format_is_nederlands(validFrom,TestData.DutchDatTimeFormat)
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        dateOfBirthTableView = graphView.get_date_of_birth_of_person_tableView()
        assert self.reports.verify_date_format_is_nederlands(dateOfBirthTableView,TestData.OtherDateFormat)
        graphView.goto_Transaction_Tab()
        dateTimeTableView = graphView.get_date_and_time_tableView()
        assert self.reports.verify_date_format_is_nederlands(dateTimeTableView,TestData.DutchDatTimeFormat)

        searchPerson = homePage.goto_Search_Person()
        searchPerson.do_Click_Show_Button()
        dateOfBirth = searchPerson.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_english(dateOfBirth,TestData.EnglishDateFormat)
        homePage.changeLanguage_To_French()
        dateOfBirth = searchPerson.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_french(dateOfBirth,TestData.OtherDateFormat)
        homePage.changeLanguage_To_Spanish()
        dateOfBirth = searchPerson.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_spanish(dateOfBirth,TestData.OtherDateFormat)
        homePage.changeLanguage_To_Nederlands()
        dateOfBirth = searchPerson.get_date_of_birth_of_person()
        assert self.reports.verify_date_format_is_nederlands(dateOfBirth,TestData.OtherDateFormat)

        searchReport = homePage.goto_Search_Report()
        searchReport.do_Click_Show_Button()
        submissionDate = searchReport.get_submission_date_and_time()
        assert self.reports.verify_date_format_is_english(submissionDate,TestData.EnglishDateTimeFormat)
        homePage.changeLanguage_To_French()
        submissionDate = searchReport.get_submission_date_and_time()
        assert self.reports.verify_date_format_is_french(submissionDate,TestData.FrenchDateTimeFormat)
        homePage.changeLanguage_To_Spanish()
        submissionDate = searchReport.get_submission_date_and_time()
        assert self.reports.verify_date_format_is_spanish(submissionDate,TestData.SpanishDateTimeFormat)
        homePage.changeLanguage_To_Nederlands()
        submissionDate = searchReport.get_submission_date_and_time()
        assert self.reports.verify_date_format_is_nederlands(submissionDate,TestData.DutchDatTimeFormat)
    
    @pytest.mark.regression
    def test_hidden_And_Empty_property(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        assert graphView.verify_degree_property_not_exist()
        graphView.do_double_click_node("person","")
        assert graphView.verify_person_prefix_exist()

    @pytest.mark.regression
    def test_property_order_sidebar(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.do_double_click_node("transaction","")
        assert graphView.verify_transaction_property_order()
        graphView.do_double_click_node("person","")
        assert graphView.verify_person_property_order()
    
    #474 - Virtual node filter is not working 
    @pytest.mark.regression
    @pytest.mark.bug
    def test_virtual_node_values_tableview(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForVirtualNodes[1])
        graphView = self.reports.goto_report_graph()
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        assert graphView.verify_virtual_node_values_displayed()
    
    #537 - Tooltip missing for table view of graph
    @pytest.mark.regression
    @pytest.mark.bug
    def test_tooltip_displayed_toolbar(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        assert graphView.verify_tooltip_displayed_toolbar_image() == TestData.imageExport 
        assert graphView.verify_tooltip_displayed_toolbar_pdf() == TestData.pdfExport
        assert graphView.verify_tooltip_displayed_toolbar_analysts_notebook() == TestData.analystsNotebook
        assert graphView.verify_tooltip_displayed_toolbar_tableView() == TestData.showTableView
        graphView.do_Load_TableView()
        assert graphView.verify_tooltip_displayed_toolbar_tableView() == TestData.hideTableView

    #533 - Tooltip missing for Graph View Search
    @pytest.mark.regression
    @pytest.mark.bug
    def test_tooltip_displayed_graph_toolbar(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        assert graphView.verify_tooltip_displayed_zoomReset() == TestData.zoomReset
        assert graphView.verify_tooltip_displayed_fit_selection_to_screen() == TestData.fitSelectionToScreen
        assert graphView.verify_tooltip_displayed_fit_to_screen() == TestData.fitToScreen
        assert graphView.verify_tooltip_displayed_search()== TestData.search
        assert graphView.verify_tooltip_displayed_zoom_in()== TestData.zoomIN
        assert graphView.verify_tooltip_displayed_zoom_out()== TestData.zoomOut
        assert graphView.verify_tooltip_displayed_unhighlight_all()== TestData.unhighlightAll
        assert graphView.verify_tooltip_displayed_deselect_all()== TestData.deselectAll
        assert graphView.verify_tooltip_displayed_area_select()== TestData.areaSelectTool
        assert graphView.verify_tooltip_displayed_area_highlight()== TestData.areaUnhighlightTool
    
    #543 - White screen on enumeration filter in table view of graph
    @pytest.mark.regression
    @pytest.mark.bug
    def test_enumeration_filter_dropdown(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForEnumerationFilter)
        graphView = self.reports.goto_report_graph()
        graphView.do_Load_TableView()
        graphView.goto_Report_Tab()
        assert graphView.verify_enumeration_filter_works() >=1

    #595 - Table view of graph, birth date is current date in case no date specified
    @pytest.mark.regression
    @pytest.mark.bug
    def test_date_value_when_it_is_null(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForEnumerationFilter)
        graphView = self.reports.goto_report_graph()
        graphView.do_Load_TableView()
        graphView.goto_Person_Tab()
        graphView.filter_first_name_person_tab("Sandra")
        assert graphView.get_date_of_birth_of_person_tableView()==""

    #595 - Table view of graph, birth date is current date in case no date specified
    @pytest.mark.regression
    @pytest.mark.bug
    def test_table_view_column_order(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForEnumerationFilter)
        graphView = self.reports.goto_report_graph()
        graphView.do_Load_TableView()
        assert graphView.verify_columns_order_nodes_table_view()
        assert graphView.verify_columns_order_edges_table_view()
    
    #602 - Nodes get unselected when counter icon is clicked
    #638 - Node gets unselected when the table view is clicked 
    @pytest.mark.regression
    @pytest.mark.bug
    def test_node_still_selected_counterIcon_tableView(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.do_Select_Node()
        assert graphView.verify_click_counter_icon_expands_newNodes_given_label(str("Jasmijn Beentjes "))
        assert graphView.do_Verify_QuickAccessToolBar_Enabled()
        graphView.do_Load_TableView()
        assert graphView.do_Verify_QuickAccessToolBar_Enabled()

    @pytest.mark.regression
    #@pytest.mark.ExecuteNow
    def test_Show_Report_bradcrumb_navigation(self):
        showReport = homePage.goto_Show_Report()
        assert homePage.verify_bread_crumb(TestData.showReportNav)
        showReport.check_show_report(TestData.reportName[0])
        assert homePage.verify_bread_crumb(TestData.showReportGraphNav)
        """ homePage.click_link_in_breadcrumb("Details")
        assert graphView.do_check_GraphLoaded() """
        homePage.click_link_in_breadcrumb("Input")
        assert showReport.get_reportid_value() == TestData.reportName[0]
        homePage.click_link_in_breadcrumb("Show report")
        assert showReport.get_reportid_value() == ""
        showReport.driver.back()
        assert showReport.get_reportid_value() == TestData.reportName[0]
        showReport.driver.back()
        #assert homePage.verify_bread_crumb(TestData.showReportGraphNav)
        assert graphView.do_check_GraphLoaded() 

    @pytest.mark.regression
    def test_save_modal(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[0])
        graphView = self.reports.goto_report_graph()
        graphView.click_save_graph()
        assert graphView.verify_graph_save_modal_exists() == True
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        time.sleep(2)
        assert graphView.verify_graph_save_modal_exists() == False
        graphView.click_save_graph()
        graphView.click_cancel_save_graph()
        assert graphView.verify_graph_save_modal_exists() == False

    """def test_gremlin(self):
        self.reportPage = Reports.Reports(self.driver)
        self.reportPage.verify_gremlin_results(TestData.deleteNode) """