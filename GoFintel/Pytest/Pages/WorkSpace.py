import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from Pages import GraphView
from selenium.webdriver.common.action_chains import ActionChains

class workspace(BasePage):

    #By Locators
    myGraphsTab = (By.XPATH,"//div[contains(@class,'tabview-nav')]//span[text()='My graphs']/..")
    allGraphsTab = (By.XPATH,"//div[contains(@class,'tabview-nav')]//span[text()='All graphs']/..")
    assignedGraphsTab = (By.XPATH,"//div[contains(@class,'tabview-nav')]//span[text()='Assigned graphs']/..")
    exportToFile = (By.XPATH,"(//span[contains(@class,'file')]//parent::button)[1]")
    exportToExcel = (By.XPATH,"//span[contains(@class,'excel')]//parent::button")
    exportToPdf = (By.XPATH,"//span[contains(@class,'pdf')]//parent::button")
    tableViewSearch = (By.XPATH,"//input[@placeholder='Search']")
    selectAllGraphs = (By.XPATH,"//th[contains(@role,'columnheader')]//div[contains(@class,'checkbox')]")
    selectFirstGraph = (By.XPATH, "//td//div[contains(@class,'checkbox')]")
    firstFavouriteIcon = (By.XPATH, "//td//input[contains(@class,'togglebutton')]//parent::div")
    graphNameFilter = (By.XPATH,"//span[text()='Graph']//following-sibling::div[contains(@class,'filter')]")
    filterDropDown = (By.XPATH,"//div[@class='p-column-filter-constraints']//span[1]")
    dropDownValue = (By.XPATH,"//li/span[text()='Equals' or text()='Es igual' or text()='Équivaut à' or text()='Is gelijk aan']")
    searchField = (By.XPATH,"//div[@class='p-column-filter-constraint']//input[@placeholder]")
    applyFilter = (By.XPATH,"//div[@class='p-column-filter-buttonbar']//button[2]")
    createdOnFilter = (By.XPATH,"//span[text()='Created on']//following-sibling::div[contains(@class,'filter')]")
    lastSavedOnFilter = (By.XPATH,"//span[text()='Last saved on']//following-sibling::div[contains(@class,'filter')]")
    updatesFilter = (By.XPATH,"//span[text()='Updates']//following-sibling::div[contains(@class,'filter')]")
    expandFiterDropDown = (By.XPATH,"//div[contains(@class,'filter')]//div[contains(@class,'-trigger')]")
    dateBetweenFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Date Between']")
    dateFromFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[1]")
    dateToFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[2]")
    updatesYes = (By.XPATH,"//li[span='Yes']//preceding-sibling::div[contains(@class,'checkbox')]")
    updatesNo = (By.XPATH,"//li[span='No']//preceding-sibling::div[contains(@class,'checkbox')]")
    multiselectClose = (By.XPATH,"//button[contains(@class,'close')]")
    filteredGraphName = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[3]")
    filteredGraphNameInAllGraphs = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[2]")
    filteredGraphUpdatesFlag = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[8]")
    clearFilter = (By.XPATH,"//button[@aria-label='Clear']")
    firstRow = (By.XPATH,"//div[@class='content tableReport']//tbody//child::tr[1]")
    secondRow = (By.XPATH,"//div[@class='content tableReport']//tbody//child::tr[2]")
    edit = (By.XPATH,"//button[@name='row-edit']")
    saveEdit = (By.XPATH,"//button[@name='row-save']")
    cancelEdit = (By.XPATH,"//button[@name='row-cancel']")
    openGraph = (By.XPATH,"(//div[@class='content tableReport']//child::tr[1]/td/button)[1]")
    renameGraph = (By.XPATH,"//div[@class='content tableReport']//child::tr[1]/td/input")
    homelink = (By.XPATH,"//li[contains(@class,'breadcrumb')]//span[contains(@class,'home')]")
    editSecondRow = (By.XPATH,"//div[@class='content tableReport']//child::tr[2]//button[@name='row-edit']")
    saveRenameSecondRow = (By.XPATH,"//div[@class='content tableReport']//child::tr[2]//button[@name='row-save']")
    cancelRenameSecondRow = (By.XPATH,"//div[@class='content tableReport']//child::tr[2]//button[@name='row-cancel']")
    openGraphSecondRow = (By.XPATH,"(//div[@class='content tableReport']//child::tr[2]/td/button)[1]")
    renameGraphSecondRow = (By.XPATH,"//div[@class='content tableReport']//child::tr[2]/td/input")
    sameGraphNameError = (By.XPATH,"//span[text()='This graph name is already used.']")
   
    assignedToDropDown = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[7]//div[@role='button']")
    assignedToColumn = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[7]//span")
    statusDropDown = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[6]//div[@role='button']")
    statusColumn = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr[1]/td[6]//span")
    dropdownSearch = (By.XPATH,"//div[contains(@class,'dropdown-filter')]/input")
    selectFromDropDownlist = (By.XPATH,"//div[contains(@class,'dropdown-items')]//li")

    def click_My_Graphs(self):
        print("Click My graphs tab")
        self.do_click(self.myGraphsTab)

    def click_All_Graphs(self):
        print("Click All graphs tab")
        self.do_click(self.allGraphsTab)

    def click_Assigned_Graphs(self):
        print("Click Assigned graphs tab")
        self.do_click(self.assignedGraphsTab)

    def click_exportToFile(self):
        print("Click export to file")
        self.do_click(self.exportToFile)

    def verify_export_options_diabled(self):
        print("Verify export options are disabled")
        if "disabled" in self.get_Attribute_Value(self.click_exportToFile,"class") and "disabled" in self.get_Attribute_Value(self.exportToExcel,"class") and "disabled" in self.get_Attribute_Value(self.exportToPdf):
            return True
        return False
    
    def verify_export_options_enabled(self):
        print("Verify export options are enabled")
        if "disabled" not in self.get_Attribute_Value(self.click_exportToFile,"class") and "disabled" not in self.get_Attribute_Value(self.exportToExcel,"class") and "disabled" not in self.get_Attribute_Value(self.exportToPdf):
            return True
        return False

    def click_exportToExcel(self):
        print("Click export to excel")
        self.do_click(self.exportToExcel)

    def click_exportToPDF(self):
        print("Click export to pdf")
        self.do_click(self.exportToPdf)

    def table_view_search(self,searchText):
        print("Enter text in the table view search :"+searchText)
        self.do_Enter_Text(self.tableViewSearch,searchText)

    def select_all_graph(self):
        print("Click select all graph")
        self.do_click(self.selectAllGraphs)

    def select_first_graph(self):
        print("Click select first graph")
        self.do_click(self.select_first_graph)

    def mark_first_graph_favourite_or_unfavourite(self):
        print("Mark first graph as favorite")
        self.do_click(self.firstFavouriteIcon)
        time.sleep(2)

    def check_graph_marked_as_favourite(self):
        print("Verify graph is marked as favorite")
        favaourite = self.get_Attribute_Value(self.firstFavouriteIcon,"class")
        if "highlight" in favaourite:
            return True
        return False
    
    def check_graph_marked_as_nonfavourite(self):
        print("Verify graph is marked as non favorite")
        favaourite = self.get_Attribute_Value(self.firstFavouriteIcon,"class")
        if "highlight" not in favaourite:
            return True
        return False
    
    def apply_graph_name_filter(self,graphName):
        print("Apply filter on graph name column :"+graphName)
        self.do_click(self.graphNameFilter)
        time.sleep(1)
        self.do_click(self.filterDropDown)
        self.do_click(self.dropDownValue)
        self.do_Enter_Text(self.searchField,graphName)
        self.do_click(self.applyFilter)
        time.sleep(2)

    def apply_created_on_filter(self):
        print("Apply filter on created on column from yeaterday to today")
        self.do_click(self.createdOnFilter)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.dateBetweenFilterCategory)
        today_date = datetime.now()
        formatted_today_date = today_date.strftime("%m/%d/%Y %H:%M:%S")
        yesterday_date = today_date - timedelta(days=1)
        formatted_yesterday_date = yesterday_date.strftime("%m/%d/%Y %H:%M:%S")
        self.do_Enter_Text(self.dateFromFilterValue,formatted_yesterday_date)
        self.do_Enter_Text(self.dateToFilterValue,formatted_today_date)
        time.sleep(1)
        self.do_click(self.tableViewSearch)
        time.sleep(1)
        self.do_click(self.createdOnFilter)
        self.do_click(self.applyFilter)

    def apply_last_saved_on_filter(self):
        print("Apply filter on last saved on column from yeaterday to today")
        self.do_click(self.lastSavedOnFilter)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.dateBetweenFilterCategory)
        today_date = datetime.now()
        formatted_today_date = today_date.strftime("%m/%d/%Y %H:%M:%S")
        yesterday_date = today_date - timedelta(days=1)
        formatted_yesterday_date = yesterday_date.strftime("%m/%d/%Y %H:%M:%S")
        self.do_Enter_Text(self.dateFromFilterValue,formatted_yesterday_date)
        self.do_Enter_Text(self.dateToFilterValue,formatted_today_date)
        time.sleep(1)
        self.do_click(self.tableViewSearch)
        time.sleep(1)
        self.do_click(self.lastSavedOnFilter)
        self.do_click(self.applyFilter)

    def apply_updates_yes_filter(self):
        print("Apply filter with value Yes on updates column")
        self.do_click(self.updatesFilter)
        self.do_click(self.filterDropDown)
        self.do_click(self.updatesYes)
        self.do_click(self.multiselectClose)
        self.do_click(self.applyFilter)

    def apply_updates_no_filter(self):
        print("Apply filter with value No on updates column")
        self.do_click(self.updatesFilter)
        self.do_click(self.filterDropDown)
        self.do_click(self.updatesNo)
        self.do_click(self.multiselectClose)
        self.do_click(self.applyFilter)

    def clear_graph_name_filter(self):
        print("Clear appied filter on graph name column")
        self.do_click(self.graphNameFilter)
        self.do_click(self.clearFilter)
        self.wait_until_page_loads()
        time.sleep(2)

    def clear_created_on_filter(self):
        print("Clear appied filter on created on column")
        self.do_click(self.createdOnFilter)
        self.do_click(self.clearFilter)

    def clear_last_saved_on_filter(self):
        print("Clear appied filter on last saved on column")
        self.do_click(self.lastSavedOnFilter)
        self.do_click(self.clearFilter)

    def clear_updates_filter(self):
        print("Clear appied filter on updates column")
        self.do_click(self.updatesFilter)
        self.do_click(self.clearFilter)

    def verify_filtered_graph_name(self,graphName):
        print("Verify filtered graph name is :"+graphName)
        filteredGraphMyGraphs = self.get_Text_Value(self.filteredGraphName)
        filteredGraphAllGraphs = self.get_Text_Value(self.filteredGraphNameInAllGraphs)
        if filteredGraphMyGraphs == graphName or filteredGraphAllGraphs==graphName:
            return True
        return False
    
    def verify_filtered_graph_updatesFlag(self,flag):
        print("Verify filtered graph Updates flag is :"+flag)
        filteredGraphMyGraphs = self.get_Text_Value(self.filteredGraphUpdatesFlag)
        if filteredGraphMyGraphs == flag:
            return True
        return False
    
    def click_edit_row(self):
        print("Click on row edit button in the first row")
        element_to_hover_over = self.get_Element(self.firstRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.edit)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()
    
    def click_edit_second_graph(self):
        print("Click on row editbutton in the second row")
        element_to_hover_over = self.get_Element(self.secondRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.editSecondRow)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def enter_graph_rename(self,newName):
        print("Enter graph name during rename in the first row :"+newName)
        self.do_Enter_Text(self.renameGraph,newName)

    def enter_graph_rename_second_graph(self,newName):
        print("Enter graph name during rename in the second row :"+newName)
        self.do_Enter_Text(self.renameGraphSecondRow,newName)

    def verify_rename_graph_enabled(self):
        if self.is_ElementExist(self.renameGraph):
            return True
        return False

    def click_save_edit(self):
        print("Click confirm row edit for first row")
        element_to_hover_over = self.get_Element(self.firstRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.saveEdit)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def click_save_edit_second_graph(self):
        print("Click confirm row edit for second row")
        element_to_hover_over = self.get_Element(self.secondRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.saveRenameSecondRow)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def click_cancel_edit(self):
        print("Click cancel row edit for first row")
        element_to_hover_over = self.get_Element(self.firstRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.cancelEdit)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def click_cancel_edit_second_graph(self):
        print("Click cancel row edit for second row")
        element_to_hover_over = self.get_Element(self.secondRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.cancelRenameSecondRow)
        actions.move_to_element(self.get_Element(self.homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def verify_save_edit_exists(self):
        print("Verify confirm row edit exists")
        return self.is_ElementExist(self.saveEdit)
    
    def verify_error_message_displayed_for_Same_graph_name(self):
        print("Verify error message displayed for entering the same name while renaming")
        return self.is_ElementExist(self.sameGraphNameError)

    def click_show_on_graph(self):
        print("Click show on graph from the first row")
        element_to_hover_over = self.get_Element(self.firstRow)
        actions = ActionChains(self.driver)
        actions.move_to_element(element_to_hover_over).perform()
        self.do_click(self.openGraph)
        self.take_mouse_to_origin()
        time.sleep(2)
        return GraphView.GraphView(self.driver)
           
    def get_filtered_graph_name(self):
        print("Get filtered graph name")
        return self.get_Text_Value(self.filteredGraphName)

    def assign_graph_to_user(self,userName):
        print("Assign graph to user "+userName)
        self.do_click(self.assignedToDropDown)
        self.do_Enter_Text(self.dropdownSearch,userName)
        self.do_click(self.selectFromDropDownlist)

    def modify_status_of_graph(self,status):
        print("Assign graph to user "+status)
        self.do_click(self.statusDropDown)
        self.do_Enter_Text(self.dropdownSearch,status)
        self.do_click(self.selectFromDropDownlist)

    def get_graph_status(self):
        print("Get graph status")
        return self.get_Text_Value(self.statusColumn)
    
    def get_assigned_to_name(self):
        print("Get agraph assigned to name")
        return self.get_Text_Value(self.assignedToColumn)

    def execute_query(self,Query):
        print("Execute gremlin query :"+Query)
        self.execute_gremlin_query(Query)
        time.sleep(2)

    def add_Node(self):
        self.addNode()
    