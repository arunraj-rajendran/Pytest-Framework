import pytest
from Config.config import TestData
from Pages import GraphView, Reports
from Pages import AirFlow
from Pages.LoginPage import LoginPage
from Pages.WorkSpace import workspace
from Tests.test_base import BaseTest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Test_Workspace(BaseTest):
    @pytest.mark.regression
    def test_saved_graph_in_workspace_from_search_person(self):
        global saveGraphName
        global homePage, workSpace, graphView,loginPage
        graphView = GraphView.GraphView(self.driver)
        workSpace = workspace(self.driver)
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_Login(TestData.userName,TestData.password)
        searchperson = homePage.goto_Search_Person()
        assert searchperson.check_Search_By_First_Name_and_Last_Name_Field()
        assert graphView.Validate_first_and_Last_Name_Filter()
        assert graphView.do_check_GraphLoaded()
        graphView.click_zoom_in()
        graphView.do_save_graph()
        homePage.goto_my_graphs()
        print ("Saved Graph Name from search person:"+GraphView.saveGraphName)
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        homePage.goto_all_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        workSpace.clear_graph_name_filter()

    @pytest.mark.regression
    def test_saved_graph_in_workspace_from_latest_reports(self):
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[2])
        graphView = self.reports.goto_report_graph()
        graphView.do_save_graph()
        homePage.goto_my_graphs()
        print ("Saved Graph Name from latest reports:"+GraphView.saveGraphName)
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        homePage.goto_all_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)

    @pytest.mark.regression
    def test_saved_graph_is_user_specific_in_mygraphs(self):
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName1,TestData.password1)
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName) == False
        workSpace.click_All_Graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName,TestData.password)

    @pytest.mark.regression
    def test_mark_graph_as_favourite(self):
        homePage.goto_LatestReports()
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.mark_first_graph_favourite_or_unfavourite()
        if workSpace.check_graph_marked_as_favourite() == False:
            workSpace.mark_first_graph_favourite_or_unfavourite()
        workSpace.clear_graph_name_filter()
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)

    @pytest.mark.regression
    def test_Rename_graph(self):
        workSpace.click_edit_row()
        workSpace.click_cancel_edit()
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        workSpace.click_edit_row()
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        assert workSpace.verify_save_edit_exists() == False
        workSpace.click_edit_row()
        workSpace.enter_graph_rename("renaming graph")
        workSpace.click_save_edit()
        assert workSpace.verify_filtered_graph_name("renaming graph")
        workSpace.click_edit_second_graph()
        workSpace.enter_graph_rename_second_graph("renaming graph")
        workSpace.click_save_edit_second_graph()
        workSpace.verify_error_message_displayed_for_Same_graph_name()
        workSpace.click_cancel_edit_second_graph()
        workSpace.click_edit_row()
        workSpace.enter_graph_rename(GraphView.saveGraphName)
        workSpace.click_save_edit()
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)

    @pytest.mark.regression
    def test_error_displays_on_same_name(self):
        graphName = workSpace.get_filtered_graph_name()
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportName[1])
        graphView = self.reports.goto_report_graph()
        graphView.click_save_graph()
        graphView.enter_graph_name(graphName)
        graphView.click_confirm_save_graph()
        graphView.verify_error_message_displayed_for_Same_graph_name()
        graphView.click_cancel_save_graph()
        homePage.goto_my_graphs()

    @pytest.mark.regression
    def test_save_graph_from_mygraphs(self):
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        firstVirtualNode = graphView.get_first_virtualnode_label()
        graphView.do_expand_collaps_virtual_node(firstVirtualNode)
        graphView.click_save_graph()
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.verify_given_virtual_node_is_expanded(firstVirtualNode)
        graphView.do_expand_collaps_virtual_node(firstVirtualNode)
        graphView.click_save_graph()

    @pytest.mark.regression
    def test_save_graph_discardChanges(self):
        homePage.goto_LatestReports()
        homePage.goto_all_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        firstNonVirtualNode = graphView.get_first_non_virtualnode_label()
        graphView.do_select_node_given("",firstNonVirtualNode)
        homePage.click_link_in_breadcrumb("Results")
        assert graphView.verify_discard_changes_modal_displayed()
        assert graphView.verify_modal_message(TestData.messageDiscardChanges)
        graphView.click_no_discard_changes()
        homePage.click_link_in_breadcrumb("Results")
        assert graphView.verify_discard_changes_modal_displayed()
        graphView.click_yes_discard_changes()
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.verify_given_node_is_unhighlighted(firstNonVirtualNode)==False  

    @pytest.mark.regression
    def test_save_graph_from_allgraphs(self):
        homePage.goto_all_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        firstVirtualNode = graphView.get_first_virtualnode_label()
        graphView.do_unhighlight_given_node(firstVirtualNode)
        graphView.click_save_graph()
        homePage.click_link_in_breadcrumb("Results")
        assert graphView.verify_discard_changes_modal_displayed() == False
        workSpace.click_show_on_graph()
        assert graphView.do_check_GraphLoaded()
        assert graphView.verify_given_node_is_unhighlighted(firstVirtualNode) 

    @pytest.mark.regression
    def test_save_graph_from_another_user(self):
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName1,TestData.password1)
        workSpace.click_All_Graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        nodeLabel = graphView.get_first_node_label_with_counter()
        assert graphView.verify_click_counter_icon_expands_newNodes_given_label(str(nodeLabel[0]))
        graphView.do_save_graph_new_user()
        if graphView.verify_discard_changes_modal_displayed() == True:
            graphView.click_yes_discard_changes()
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.userGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.userGraphName)
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName,TestData.password)
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.userGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.userGraphName)==False
        workSpace.clear_graph_name_filter()
        
    @pytest.mark.regression
    def test_pending_updates_modal(self):
        homePage.goto_LatestReports()
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        graphView.do_click_unhighlightAll()
        graphView.click_save_graph()
        homePage.click_link_in_breadcrumb("Results")
        workSpace.execute_query(TestData.addPropertyToReportNode)
        workSpace.click_show_on_graph()
        graphView.do_click_fit_to_screen()
        graphView.click_save_graph()
        assert graphView.verify_pending_updates_displayed()
        assert graphView.verify_modal_message(TestData.pendingUpdates)
        graphView.click_ok_pending_updates()
        homePage.click_link_in_breadcrumb("Results")
        graphView.click_yes_discard_changes()

    @pytest.mark.regression
    def test_graph_updates_add_property_node(self):  
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 1 changes, 0 nodes deleted and 0 edges deleted"
        assert graphView.check_node_is_highlighted("report","UTR (EUR)")
        graphView.do_double_click_node("report","UTR (EUR)")
        assert graphView.verify_the_property_is_in_bold("FIU reference number")
        graphView.do_select_node_given("report","UTR (EUR)")
        assert graphView.verify_the_property_is_in_bold("FIU reference number") == False
        assert graphView.get_Toast_Message_Text() == "There are 0 changes, 0 nodes deleted and 0 edges deleted"
        graphView.click_save_graph()
        workSpace.execute_query(TestData.dropPropertyFromReportNode)
        homePage.click_link_in_breadcrumb(GraphView.saveGraphName)
        assert graphView.get_Toast_Message_Text() == "There are 1 changes, 0 nodes deleted and 0 edges deleted"
        assert graphView.check_node_is_highlighted("report","UTR (EUR)")
        graphView.do_double_click_node("report","UTR (EUR)")
        assert graphView.verify_the_property_is_in_bold("FIU reference number") == False

    @pytest.mark.regression
    def test_graph_properties_changes_edge(self):  
        homePage.goto_my_graphs()
        graphView.click_yes_discard_changes()
        workSpace.execute_query(TestData.addPropertyToEdge)
        workSpace.execute_query(TestData.modifyPropertyInEdge)
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 3 changes, 0 nodes deleted and 0 edges deleted"
        assert graphView.check_edge_is_highlighted("From","From")
        graphView.do_double_click_edge("From","From")
        assert graphView.verify_the_property_is_in_bold("Funds code")
        assert graphView.verify_the_property_is_in_bold("Output spent total")
        graphView.do_click_edge("From","From")
        assert graphView.verify_the_property_is_in_bold("Funds code") == False
        assert graphView.verify_the_property_is_in_bold("Output spent total") == False
        assert graphView.get_Toast_Message_Text() == "There are 1 changes, 0 nodes deleted and 0 edges deleted"
        graphView.do_select_node_given("report","UTR (EUR)")
        assert graphView.get_Toast_Message_Text() == "There are 0 changes, 0 nodes deleted and 0 edges deleted"
        graphView.click_save_graph()
        workSpace.execute_query(TestData.modifyPropertyBackToState)
        homePage.click_link_in_breadcrumb(GraphView.saveGraphName)
        assert graphView.get_Toast_Message_Text() == "There are 1 changes, 0 nodes deleted and 0 edges deleted"
        graphView.do_double_click_edge("From","From")
        assert graphView.verify_the_property_is_in_bold("Funds code")
        assert graphView.verify_the_property_is_in_bold("Output spent total") == False
        homePage.click_link_in_breadcrumb("Results")
        graphView.click_yes_discard_changes()
        workSpace.execute_query(TestData.dropPropertyFromEdge)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 2 changes, 0 nodes deleted and 0 edges deleted"
        graphView.do_double_click_edge("From","From")
        assert graphView.verify_the_property_is_in_bold("Funds code")
        graphView.do_click_edge("From","From")
        assert graphView.verify_the_property_is_in_bold("Funds code") == False
        assert graphView.get_Toast_Message_Text() == "There are 0 changes, 0 nodes deleted and 0 edges deleted"
        graphView.click_save_graph()

    @pytest.mark.regression
    def test_graph_updates_add_and_drop_node_and_edge(self):
        homePage.goto_my_graphs()
        workSpace.execute_query(TestData.addNodeLinking)
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 3 changes, 0 nodes deleted and 0 edges deleted"
        homePage.click_link_in_breadcrumb("Results")
        workSpace.execute_query(TestData.dropCloseSimilarityEdges)
        workSpace.click_show_on_graph()
        assert graphView.verify_toast_message_displayed() == False or graphView.get_Toast_Message_Text() == "There are 1 changes, 0 nodes deleted and 0 edges deleted"
        self.reports = homePage.goto_LatestReports()
        self.reports.goto_Report(TestData.reportNameForMergedNodes)
        self.reports.goto_report_graph()
        graphView.verify_click_counter_icon_expands_newNodes_given_label("2,000")
        graphView.do_save_another_graph()
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.mergedGraphName)
        workSpace.click_show_on_graph()
        homePage.click_link_in_breadcrumb("Results")
        workSpace.execute_query(TestData.deleteMergedNodes)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 5 changes, 0 nodes deleted and 2 edges deleted"
        homePage.click_link_in_breadcrumb("Results")
        workSpace.execute_query(TestData.addBackTheMergedEdge1)
        workSpace.execute_query(TestData.addBackTheMergedEdge2)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 2 changes, 0 nodes deleted and 2 edges deleted"
        homePage.click_link_in_breadcrumb("Results")
        workSpace.execute_query(TestData.deleteNode)
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 6 changes, 1 nodes deleted and 4 edges deleted" or graphView.get_Toast_Message_Text() == "There are 3 changes, 1 nodes deleted and 3 edges deleted"
        homePage.click_link_in_breadcrumb("Results")
        workSpace.addNode()
        workSpace.click_show_on_graph()
        assert graphView.get_Toast_Message_Text() == "There are 5 changes, 1 nodes deleted and 4 edges deleted" or graphView.get_Toast_Message_Text() == "There are 2 changes, 1 nodes deleted and 3 edges deleted"

    @pytest.mark.regression
    def test_update_flag(self):
        airFlow = AirFlow.airflow(self.driver)
        airFlow.run_dag("update_flag")
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.mergedGraphName)
        assert workSpace.verify_filtered_graph_updatesFlag("Yes")
        workSpace.clear_graph_name_filter()
        homePage.goto_all_graphs()
        workSpace.apply_graph_name_filter(GraphView.mergedGraphName)
        assert workSpace.verify_filtered_graph_updatesFlag("Yes")
        workSpace.click_show_on_graph()
        graphView.do_click_unhighlightAll()
        graphView.click_save_graph()
        homePage.click_link_in_breadcrumb("Results")
        assert workSpace.verify_filtered_graph_updatesFlag("No")
        workSpace.clear_graph_name_filter()

    @pytest.mark.regression
    def test_assigned_graphs(self):
        workSpace.click_My_Graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_edit_row()
        workSpace.assign_graph_to_user(TestData.userName)
        workSpace.click_save_edit()
        workSpace.click_Assigned_Graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        workSpace.click_edit_row()
        assert workSpace.verify_rename_graph_enabled()== False
        workSpace.assign_graph_to_user(TestData.userName1)
        workSpace.click_save_edit()
        assert workSpace.verify_filtered_graph_name("")
        workSpace.clear_graph_name_filter()
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName1,TestData.password1)
        homePage.goto_assigned_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        workSpace.click_show_on_graph()
        graphView.verify_save_graph_is_enabled()==True
        graphView.do_click_unhighlightAll()
        graphView.click_save_graph()
        graphView.verify_graph_save_modal_exists()
        graphView.click_cancel_save_graph()
        homePage.goto_my_graphs()
        graphView.click_yes_discard_changes()
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName,TestData.password)

    @pytest.mark.regression
    def test_status_change(self):
        homePage.goto_my_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        workSpace.click_edit_row()
        workSpace.modify_status_of_graph("Under review")
        workSpace.assign_graph_to_user(TestData.userName)
        workSpace.click_save_edit()
        workSpace.click_Assigned_Graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        assert workSpace.get_graph_status() == "Under review"
        workSpace.click_edit_row()
        workSpace.modify_status_of_graph("Sent for approval")
        workSpace.assign_graph_to_user(TestData.userName1)
        workSpace.click_save_edit()
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName1,TestData.password1)
        homePage.goto_assigned_graphs()
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        assert workSpace.get_graph_status() == "Sent for approval"
        assert workSpace.get_assigned_to_name() == TestData.userName1
        homePage.do_Logout()
        loginPage.do_Login(TestData.userName,TestData.password)

    @pytest.mark.regression
    def test_table_view_search(self):
        homePage.goto_my_graphs()
        workSpace.table_view_search("Sent for approval")
        workSpace.apply_graph_name_filter(GraphView.saveGraphName)
        assert workSpace.verify_filtered_graph_name(GraphView.saveGraphName)
        workSpace.click_edit_row()
        workSpace.modify_status_of_graph("Approved")
        workSpace.click_save_edit()
        workSpace.clear_graph_name_filter()

    
    """def test_set_env_back(self):
        airFlow = AirFlow.airflow(self.driver)  
        airFlow.run_dag("init_env")"""
    
"""     def test_addNode(self):
        workSpace = workspace(self.driver)
        workSpace.add_Node()  """