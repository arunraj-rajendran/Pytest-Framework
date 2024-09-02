import time
import os

from Pages import HomePage
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Config.config import TestData
from datetime import datetime


from Tests import conftest

saveGraphName = None
class GraphView(BasePage):

    global saveGraphName,userGraphName

    #By Locators
    canvasElement = (By.XPATH,"//canvas")
    infIconInGraph = (By.XPATH,"//span[contains(@class,'question-circle')]")
    searchInGraph = (By.XPATH,"//span[contains(@class,'search')]")
    graphImageExport = (By.XPATH,"//span[contains(@class,'image')]//parent::button")
    graphPDFExport = (By.XPATH,"//span[contains(@class,'pdf')]//parent::button")
    graphAnalystsNotebookExport = (By.XPATH,"//span[contains(@class,'sitemap')]//parent::button")
    graphTableView = (By.XPATH,"//span[contains(@class,'table')]//parent::div/parent::div")
    tableViewNodesTab = (By.XPATH,"//span[@class='p-tabview-title' and text()='Nodes']")
    tableViewEdgesTab = (By.XPATH,"//span[@class='p-tabview-title' and text()='Edges']")
    toolBar = (By.XPATH,"//div[contains(@class,'p-toolbar-group')]//child::button[1]")
    highlightedNodes = (By.XPATH,"//label[text()='Focus nodes']//preceding::div[@id='multiForNodes']")
    MultiSeclectCheckbox = (By.XPATH,"//div[contains(@class,'multiselect-panel')]//child::div[@role='checkbox']")
    checkDeselectOfAllHighlighttedNodes = (By.XPATH,"//div[contains(@class,'p-multiselect-items-wrapper')]//child::li[@aria-selected='true']")
    filterHighlightedNodes = (By.XPATH,"//div[contains(@class,'p-multiselect-items-wrapper')]")
    highlightNodesMultiSeclectTextbox = (By.XPATH,"//input[contains(@class,'p-multiselect-filter')]")
    highlightedEdges = (By.XPATH,"//label[text()='Focus edges']//preceding::div[@id='multiForEdges']//div[contains(@class,'trigger')]")
    visualprofile = (By.XPATH,"//div[contains(@class,'visual-profil-select')]")
    visualprofiledefault = (By.XPATH,"//li[@aria-label='Default']")
    visualprofiledtalied = (By.XPATH,"//li[@aria-label='Detailed']")
    visualprofileedgecentric = (By.XPATH,"//li[@aria-label='Edge centric']")
    visualprofilenodecentric = (By.XPATH,"//li[@aria-label='Node centric']")
    visualprofiletext = (By.XPATH,"(//div[contains(@class,'visual-profil-select')]//span)[2]")
    smartsidebar = (By.XPATH,"//div[@class='p-panel-content']")
    smartsidebarpanel = (By.XPATH,"//div[@class='p-sidebar-content']")
    smartsidebartitle1 = (By.XPATH,"(//span[@class='p-panel-title'])[1]")
    smartsidebartitle2 = (By.XPATH,"(//span[@class='p-panel-title'])[2]") 
    smartsidebartitle3 = (By.XPATH,"(//div[@class='header-content'])[1]")
    smartsidebartitle4 = (By.XPATH,"(//div[@class='header-content'])[2]")
    smartsidebardelete = (By.XPATH,"//button[contains(@class,' p-panel-toggler')]//span[contains(@class,'pi pi-trash')]")
    smartsidebarminimize = (By.XPATH,"(//button[contains(@class,' p-panel-toggler')]//span[contains(@class,'pi pi-minus')])[1]")
    smartsidebarmaximize = (By.XPATH,"//button[contains(@class,' p-panel-toggler')]//span[contains(@class,'pi pi-plus')]")
    smartsidebardeleteall = (By.XPATH,"//button[contains(@class,'p-sidebar-icon p-link')]//span[contains(@class,'trash')]")
    smartsidebarclose = (By.XPATH,"//button[@data-pc-section='closebutton']")  
    occupationproperty = (By.XPATH,"//div[contains(text(),'Occupation')]")  
    transactionCount = (By.XPATH,"//div[contains(@class,'sidebar-right')]//td[contains(text(),'Transaction count')]//following-sibling::td")
    dateAndTimeOfTransaction = (By.XPATH,"//td[text()='Date and time of transaction' or text()='Date et heure de la transaction' or text()='Fecha y hora de la transacción' or text()='Datum en tijd van de transactie']//following-sibling::td")
    dateOfBirthOfPerson = (By.XPATH,"//div[text()='Birth date' or text()='Fecha de nacimiento' or text()='Date de naissance' or text()='Geboortedatum']/..//following-sibling::td")
    dateOfBirthPropertyLabel = (By.XPATH,"//div[text()='Birth date' or text()='Fecha de nacimiento' or text()='Date de naissance' or text()='Geboortedatum']")
    transactionDegreeProperty = (By.XPATH,"//div[text()='Degree']")
    personPrefixProperty = (By.XPATH,"//div[text()='Prefix']")
    vaildFromPropertyDialog = (By.XPATH,"//div[contains(@class,'dialog')]//tbody//td[2]")
    propertytab =  (By.XPATH,"//div[contains(@class,'p-dialog-content')]") 
    propertytabrow =  (By.XPATH,"(//table[contains(@class,'p-datatable-table')])[2]//tr")
    closepropertytab = (By.XPATH,"//div[@class='p-dialog-header-icons']")
    showreportidtextbox = (By.XPATH,"//input[@id='reportId']")
    showbutton = (By.XPATH,"//span[text()='Show']")
    nodatarow = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tr//td")
    searchbox = (By.XPATH,"//input[@placeholder='Search']")
    table = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tr")
    tabledatedata1 = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tr[1]//td[3]")
    tabledatedata2 = (By.XPATH,"//table[contains(@class,'p-datatable-table')]//tr[2]//td[3]")
    sortdatefrom = (By.XPATH,"(//span[@data-pc-section='sort'])[2]")
    sortdatefromascending = (By.XPATH,"//span[@class='p-sortable-column-icon pi pi-fw pi-sort-amount-up-alt']")
    selectallcheckbox = (By.XPATH,"(//div[@role='checkbox'])[1]")
    unselectallcheckbox = (By.XPATH,"(//div[@class='p-checkbox p-component p-highlight'])[1]")
    xlsfiledownlodbutton = (By.XPATH,"//span[@class='p-button-icon p-c pi pi-file-excel']")
    csvfiledownlodbutton = (By.XPATH,"//span[@class='p-button-icon p-c pi pi-file']")
    pdffiledownlodbutton = (By.XPATH,"//span[@class='p-button-icon p-c pi pi-file-pdf']")
    selectcheckbox1 = (By.XPATH,"(//div[@class='p-checkbox p-component'])[2]")
    selectcheckbox2 = (By.XPATH,"(//div[@class='p-checkbox p-component'])[5]")
    selectcheckbox3 = (By.XPATH,"(//div[@class='p-checkbox p-component'])[7]")
    showongraph = (By.XPATH,"//button[text()='Show on graph']")
    selectjohnpurchaser = (By.XPATH,"//td[text()='Purchaser']//parent::tr//div[@class='p-checkbox p-component']")
    selectjohnpurchaserarrow = (By.XPATH,"//td[text()='Purchaser']//parent::tr//span[@class='p-button-icon p-c pi pi-arrow-right']")
    selectMaartje = (By.XPATH,"//td[text()='Maartje']//parent::tr//div[@class='p-checkbox p-component']")
    selectMaartjearrow = (By.XPATH,"//td[text()='Maartje']//parent::tr//span[@class='p-button-icon p-c pi pi-arrow-right']")
    selectjohnpeterpersonA = (By.XPATH,"//td[text()='John Peter']//parent::tr//div[@class='p-checkbox p-component']")
    selectjohnpeterpersonAarrow = (By.XPATH,"//td[text()='John Peter']//parent::tr//span[@class='p-button-icon p-c pi pi-arrow-right']")
    custombutton = (By.XPATH,"//button[text()='Customs']")
    
    applyFilter = (By.XPATH,"//button[@aria-label='Apply']")
    clearFilter = (By.XPATH,"//button[@aria-label='Clear']")
    closeFilterDropDown = (By.XPATH,"//button[contains(@data-pc-section,'closebutton')]")
    filterDate = (By.XPATH,"//span[text()='Submission date and time' or text()='Date and time of transaction' or text()='Birth date' or text()='Issue date']//..//child::button[contains(@class,'filter')]")
    expandFiterDropDown = (By.XPATH,"//div[contains(@class,'filter')]//div[contains(@class,'-trigger')]")
    dateBetweenFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Date Between']")
    yearIsFilterCategory = (By.XPATH,"//li[contains(@class,'dropdown-item') and @aria-label='Year Is']")
    dateFromFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[1]")
    dateToFilterValue = (By.XPATH,"(//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input)[2]")
    yearIsValue = (By.XPATH,"//div[contains(@class,'filter')]//span[contains(@class,'calendar')]/input")
    noOfRecords = (By.XPATH,"//tbody[contains(@class,'datatable')]/tr")
    noRecordsFound = (By.XPATH,"//*[contains(text(),'No data found')]")
    reportTab = (By.XPATH,"//span[text()='Report']//parent::button")
    personTab = (By.XPATH,"//li//*[contains(@class,'person')]/..")
    transactionTab = (By.XPATH,"//li//*[contains(@class,'transaction')]/..")
    identificationTab = (By.XPATH,"//span[text()='Identification']//parent::button")
    selectCalendarDate = (By.XPATH,"//table[contains(@class,'datepicker-calendar')]//span[contains(@class,'highlight')]")
    propertyDescription = (By.XPATH,"//div[text()='Description']//parent::td//following-sibling::td//div")
    readingModeModal = (By.XPATH,"//div[contains(@class,'descDialog')]")
    closeModal = (By.XPATH,"//div[contains(@class,'descDialog')]//button[contains(@class,'close')]")
    tableViewTabsList = (By.XPATH,"//div[@class='p-tabview-panels']//ul[@role='tablist' and @class='p-tabview-nav']/li[@role='presentation']")
    tableColumnHeaders = (By.XPATH,"//*[@role='table']//th")
    tableColumnHeadersText = (By.XPATH,"//*[@role='table']//th/div/span[text()]")
    tableColumnsWithSort = (By.XPATH,"//*[@role='table']//th//span[contains(@data-pc-section,'sort')]")
    tableColumnsWihtFilter = (By.XPATH,"//*[@role='table']//th//div[contains(@class,'filter')]")
    virtualNodesPlus = (By.XPATH,"//table[@role='table']//td/button[@aria-expanded='false']")
    virtualNodesMinus = (By.XPATH,"//table[@role='table']//td/button[@aria-expanded='true']")
    dateOfBirthTableView = (By.XPATH,"//div[contains(@class,'tabview')]//tbody//td[5]")
    dateAndTimeTableView = (By.XPATH,"//div[contains(@class,'tabview')]//tbody//td[5]")

    zoomReset = (By.XPATH,"//div[@class='zoomButtons']/button[@id='zoom-reset']")
    selectedNodeZoom = (By.XPATH,"//div[@class='zoomButtons']/button[@id='selectednodebtn']")
    search = (By.XPATH,"//div[@class='zoomButtons']/button[@id='search']")
    searchtxtField = (By.XPATH,"//div[@class='zoomButtons']//input[@id='search']")
    fitToScreen = (By.XPATH,"//div[@class='zoomButtons']/button[@id='fittoscreen']")
    zoomIn = (By.XPATH,"//div[@class='zoomButtons']/button[@id='zoom-in']")
    zoomOut= (By.XPATH,"//div[@class='zoomButtons']/button[@id='zoom-out']")
    unhighlightAll= (By.XPATH,"//div[@class='zoomButtons']/button[contains(@class,'unhighlight')]")
    deselectAll= (By.XPATH,"//div[@class='zoomButtons']//span[contains(@class,'deselect-all')]//parent::button")
    areaSelect= (By.XPATH,"//div[@class='zoomButtons']//span[contains(@class,'area-select')]")
    areaHighlight= (By.XPATH,"//div[@class='zoomButtons']//span[contains(@class,'area-highlight')]")
    propertyList = (By.XPATH,"//div[contains(@class,'sidebarPannel')]//tr/td[1]")
    propertyBold = (By.XPATH,"//div[contains(@class,'sidebarPannel')]//tr//b")
    tooltipText = (By.XPATH,"//div[contains(@class,'tooltip-text')]")
    #tableview
    virtualNode_personTab = (By.XPATH,"//div[contains(@class,'tabview')]//tbody/tr/td[9]")
    indicatorFilter_ReportTab = (By.XPATH,"//div[contains(@class,'tabview')]//th[3]//button[@aria-label='Show Filter Menu']")
    firstNameFilter_personTab = (By.XPATH,"//div[contains(@class,'tabview')]//thead/tr/th[4]//button[@aria-label='Show Filter Menu']")
    filterTextValue =(By.XPATH,"//div[contains(@class,'filter')]//input[@placeholder]")

    saveGraph = (By.XPATH,"//span[contains(@class,'save')]//..")
    disabledSaveButton = (By.XPATH,"//span[contains(@class,'save')]//parent::button[@disabled]")
    graphName = (By.XPATH,"//input[@placeholder='Graph name']")
    cancelSaveGraph = (By.XPATH,"//button[@aria-label='Cancel']")
    confirmSaveGraph = (By.XPATH,"//button[@aria-label='Confirm']")
    sameGraphNameError = (By.XPATH,"//span[text()='This graph name is already used.']")
    confirmDiscardChanges = (By.XPATH,"//div[text()='Confirm discard changes']")
    pendingUpdates= (By.XPATH,"//div[text()='Pending updates']")
    messageDiscardChanges = (By.XPATH,"//div[@role='dialog']//div[contains(@class,'content')]//span[contains(@class,'message')]")
    noDiscardChanges = (By.XPATH,"//div[@role='dialog']//div[contains(@class,'footer')]//button[contains(@aria-label,'No')]")
    yesDiscardChanges = (By.XPATH,"//div[@role='dialog']//div[contains(@class,'footer')]//button[contains(@aria-label,'Yes')]")
    okPendingUpdates = (By.XPATH,"//div[@role='dialog']//div[contains(@class,'footer')]//button[contains(@aria-label,'Ok')]")
    toasMessage = (By.XPATH,"//div[contains(@class,'p-toast-message-text')]/span")

    #construct of the page class
    def __init__(self,driver):
        super().__init__(driver)

    def do_check_GraphLoaded(self):
        visible = False
        print("Verify Graph is loaded or not")
        time.sleep(1)
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                visible = True
                break
            else:
                visible = False
            
        return visible

    def do_download_graph_image(self):
        downloaded = False
        print("Download Graph in image format")
        self.do_click(self.graphImageExport)
        time.sleep(2)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.png') or ('.png' in fname and fname.endswith('.png.crdownload')):
                print("Deletet the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False              
        return downloaded    
    
    def do_download_graph_pdf(self):
        downloaded = False
        print("Download Graph in pdf format")
        self.do_click(self.graphPDFExport)
        time.sleep(3)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.pdf') or ('.pdf' in fname and fname.endswith('.pdf.crdownload')):
                print("Deletet the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
                
        return downloaded    
    
    def do_download_graph_AnalyticsNotebook(self):
        downloaded = False
        print("Download Graph - AnalyticsNotebook")
        self.do_click(self.graphAnalystsNotebookExport)
        time.sleep(2)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.xlsx') or ('.xlsx' in fname and fname.endswith('.xlsx.crdownload')):
                print("Delete the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
                
        return downloaded   
    
    def do_Load_TableView(self):
        print("Open Graph table view")
        self.do_click(self.graphTableView)
        return self.is_ElementExist(self.tableViewNodesTab) and self.is_ElementExist(self.tableViewEdgesTab)
    
    def do_Verify_TableViewTabs(self):
        print("Verify Tabs Displayed in table view")
        tabsExists = False
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                if(self.is_ElementExist((By.XPATH,"//span[@class='p-tabview-title' and text()='"+node["label"].capitalize()+"']//parent::button"))):
                    print(node["label"].capitalize() + "Tab avaiable in the table view")
                    tabsExists = True                    
                else:
                    print(node["label"].capitalize() + "Tab not avaiable in the table view")
                    tabsExists = False
                    break
        return tabsExists
    
    def do_Verify_TableContents(self):
        print("Verify Contents in the table view")
        tableContent = {}
        valuesPopulated = True
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if valuesPopulated == False:
                break
            if not "isHide" in node:
                tabName = node["label"]
                properties = node["properties"]
                for property in properties:
                    if valuesPopulated == False:
                        break
                    propertyValues = node["properties"][property]
                    columnNames = []
                    if "valueLabel" in propertyValues:
                        tableContent[propertyValues["keyLabel"]]=propertyValues["valueLabel"]
                    else:
                        tableContent[propertyValues["keyLabel"]]=propertyValues["value"]
                    self.do_click((By.XPATH,"//span[text()='"+tabName.capitalize()+"']//parent::button"))
                    tableViewColumnHeader = (By.XPATH,"//table[@data-pc-section='table']/thead/tr/th")
                    columnCount = self.get_Element_count(tableViewColumnHeader)
                    for i in range(1,columnCount,1):
                        tableViewColumnName = (By.XPATH,"//table[@data-pc-section='table']/thead/tr/th["+str(i)+"]/div/span")
                        columnNames.append(self.get_Text_Value(tableViewColumnName))
                    
                    columNo = 0
                    for columnName in columnNames:
                        columNo = columNo+1
                        if columnName == propertyValues["keyLabel"]:
                            break
                    val = str(tableContent.get(columnName))
                    tableViewRow = (By.XPATH,"//table[@data-pc-section='table']/tbody/tr")
                    rowCount = self.get_Element_count(tableViewRow)
                    for j in range(1,rowCount,1):
                        if val is not None:
                            tableViewCell = (By.XPATH,"//table[@data-pc-section='table']/tbody/tr["+str(j)+"]/td["+str(columNo)+"]")
                            columnval = str(self.get_Text_Value(tableViewCell))
                            if val==columnval or columnval in val:
                                break
                            elif j==rowCount :
                                valuesPopulated = False
                                break
        return valuesPopulated

    def check_toolbar_enables_and_disables(self):
        print("Verify Quick traversal tool bar enabels and disables on clicking the node")
        toolbarClassEnabled = ""
        toolbarClassDisabled = ""
        action = ActionChains(self.driver)
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                action = ActionChains(self.driver)
                canvasXCoordinate = self.get_Element_X_Coordinate(self.canvasElement)
                canvasYCoordinate = self.get_Element_Y_Coordinate(self.canvasElement)+7 #Adding 7 to peform the clik on the center of the node
                newXcoordinate = node["x"]
                newYcoordinate = node["y"]
                searchElementYCoordinate = self.get_Element_Y_Coordinate(self.searchInGraph)
                infoIconYCoordinate = self.get_Element_Y_Coordinate(self.infIconInGraph)
                print("node "+ str(canvasYCoordinate+newYcoordinate) +" info: "+str(infoIconYCoordinate))
                if(canvasYCoordinate+newYcoordinate > searchElementYCoordinate+50 or canvasYCoordinate+newYcoordinate < infoIconYCoordinate-50):
                    if(canvasYCoordinate+newYcoordinate > searchElementYCoordinate+50):
                        scrollingLength = canvasYCoordinate+newYcoordinate - searchElementYCoordinate
                    elif(canvasYCoordinate+newYcoordinate < infoIconYCoordinate-5):         
                        scrollingLength = canvasYCoordinate+newYcoordinate - infoIconYCoordinate

                    action = ActionChains(self.driver)
                    action.move_by_offset(50,0).click_and_hold().move_by_offset(0,-scrollingLength).release().perform()
                    time.sleep(1)
                    action.move_by_offset(-50,0).perform()
                    time.sleep(1)
                    action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).double_click().perform()
                    action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()
                    time.sleep(1)
                    toolbarClassEnabled = toolbarClassEnabled + self.get_Attribute_Value(self.toolBar,"class")
                    action.move_by_offset(0,0).click().perform()
                    time.sleep(1)
                    toolbarClassDisabled = toolbarClassDisabled + self.get_Attribute_Value(self.toolBar,"class")
                    time.sleep(1)
                    action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).double_click().perform()
                    action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()
                    time.sleep(1)
                    action.move_by_offset(50,0).click_and_hold().move_by_offset(0,scrollingLength).release().perform()
                    time.sleep(1)
                    action.move_by_offset(-50,0).perform()
                    
                else:
                    action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).double_click().perform()
                    action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()
                    time.sleep(1)
                    toolbarClassEnabled = toolbarClassEnabled + self.get_Attribute_Value(self.toolBar,"class")
                    action.move_by_offset(0,0).click().perform()
                    time.sleep(1)
                    toolbarClassDisabled = toolbarClassDisabled + self.get_Attribute_Value(self.toolBar,"class")

        return "disabled" not in toolbarClassEnabled and "enabled" not in toolbarClassDisabled
    
    def check_clicking_highlighted_nodes_dropdown(self):
        print("Click Focus Nodes drop down")
        self.do_click(self.highlightedNodes)

    def check_deselect_multiselect_checkbox(self):
        time.sleep(2)
        print("Deselect multiselect checkbox")
        self.do_click(self.MultiSeclectCheckbox)
        count = self.get_Element_count(self.checkDeselectOfAllHighlighttedNodes)
        if count == 0:
            return True
        else:
            return False

    def check_filter_highlighted_nodes(self):
        print("Filtering nodes and egdes")
        self.do_Enter_Text(self.highlightNodesMultiSeclectTextbox, "Address")
        ele_Count = self.get_Element_count(self.filterHighlightedNodes)
        self.do_click(self.filterHighlightedNodes)
        self.do_Load_TableView()
        self.check_clicking_highlighted_nodes_dropdown()
        self.do_Load_TableView()
        self.check_clicking_highlighted_nodes_dropdown()
        selected_ele_count = self.get_Element_count(self.checkDeselectOfAllHighlighttedNodes)
        self.do_Enter_Text(self.highlightNodesMultiSeclectTextbox, "Transaction")   
        ele_Count1 = self.get_Element_count(self.filterHighlightedNodes)
        self.do_click(self.filterHighlightedNodes)
        self.do_click(self.highlightNodesMultiSeclectTextbox)
        action = ActionChains(self.driver)
        action.key_down(self.get_ctrl_key()).send_keys('a').key_up(self.get_ctrl_key())
        action.send_keys(Keys.BACKSPACE)
        action.perform()
        selected_ele_count1 = self.get_Element_count(self.checkDeselectOfAllHighlighttedNodes)
        if selected_ele_count1 == 2 and ele_Count1 == 1 and selected_ele_count == 1 and ele_Count==1:
            result = True
        else:
            result = False
        return result
    
    def check_filter_highlighted_Edges(self):
        print("Filtering nodes and egdes")
        self.do_Enter_Text(self.highlightNodesMultiSeclectTextbox, "Address")
        ele_Count = self.get_Element_count(self.filterHighlightedNodes)
        self.do_click(self.filterHighlightedNodes)
        self.do_Load_TableView()
        self.check_clicking_highlighted_edges_dropdown()
        self.do_Load_TableView()
        self.check_clicking_highlighted_edges_dropdown()
        selected_ele_count = self.get_Element_count(self.checkDeselectOfAllHighlighttedNodes)
        self.do_Enter_Text(self.highlightNodesMultiSeclectTextbox, "Transaction")   
        ele_Count1 = self.get_Element_count(self.filterHighlightedNodes)
        self.do_click(self.filterHighlightedNodes)
        self.do_click(self.highlightNodesMultiSeclectTextbox)
        action = ActionChains(self.driver)
        action.key_down(self.get_ctrl_key()).send_keys('a').key_up(self.get_ctrl_key())
        action.send_keys(Keys.BACKSPACE)
        action.perform()
        selected_ele_count1 = self.get_Element_count(self.checkDeselectOfAllHighlighttedNodes)
        if selected_ele_count1 == 2 and ele_Count1 == 1 and selected_ele_count == 1 and ele_Count==1:
            result = True
        else:
            result = False
        return result
    
    def check_clicking_highlighted_edges_dropdown(self):
        print("Click Highlighted Edges drop down")
        self.do_click(self.highlightedEdges)

    def check_selecting_detailed_visual_profile_dropdown(self):
        print("Click Visual Profile drop down")
        self.do_click(self.visualprofile)
        print("Select Detailed option in visual profile")
        self.do_click(self.visualprofiledtalied)
        selectedValue = self.get_Element_Text(self.visualprofiletext)
        print(selectedValue)
        if selectedValue == "Detailed":
            return True
        else:
            return False
        
    def check_selecting_edge_centric_visual_profile_dropdown(self):
        print("Click Visual Profile drop down")
        self.do_click(self.visualprofile)
        print("Select Edge centric option in visual profile")
        self.do_click(self.visualprofileedgecentric)
        selectedValue = self.get_Element_Text(self.visualprofiletext)
        print(selectedValue)
        if selectedValue == "Edge centric":
            return True
        else:
            return False
        
    def check_selecting_node_centric_visual_profile_dropdown(self):
        print("Click Visual Profile drop down")
        self.do_click(self.visualprofile)
        print("Select Node centric option in visual profile")
        self.do_click(self.visualprofilenodecentric)
        selectedValue = self.get_Element_Text(self.visualprofiletext)
        print(selectedValue)
        if selectedValue == "Node centric":
            return True
        else:
            return False
        
    def check_selecting_default_visual_profile_dropdown(self):
        print("Click Visual Profile drop down")
        self.do_click(self.visualprofile)
        print("Select Default option in visual profile")
        self.do_click(self.visualprofiledefault)
        selectedValue = self.get_Element_Text(self.visualprofiletext)
        print(selectedValue)
        if selectedValue == "Default":
            return True
        else:
            return False

    def check_smart_sidebar(self):
        print("Verify Smart Side bar")
        homepage = HomePage.HomePage(self.driver)
        jsonObject = self.get_chartData()
        i=0
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                if i<2:
                    i=i+1
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    node_position = {
                        'x': float(node.get('x')),
                        'y': float(node.get('y'))
                    }
                    
                    coordinate_modifier = {
                    'x': 1,
                    'y': 1
                    }

                    offset = {
                    'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                    'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            offset.get('x')+offset_modifier_circle_counter,
                            offset.get('y')- offset_modifier_circle_counter
                            ).double_click().perform()
                    time.sleep(3)
                else:
                    break
                if i==1:
                    smartSidebarCount = self.get_Element_count(self.smartsidebar)
                    assert smartSidebarCount == 1
        smartSidebarCount = self.get_Element_count(self.smartsidebar)
        return smartSidebarCount
    
    def check_smart_sidebar_minimize_button(self):
        print("Verify smart side bar minimize button")
        self.do_click(self.smartsidebarminimize)
        time.sleep(2)
        smartSidebarCount = self.get_Element_count(self.smartsidebar)
        self.do_click(self.smartsidebarmaximize)
        time.sleep(2)
        smartSidebarCount1 = self.get_Element_count(self.smartsidebar)
        if smartSidebarCount==1 and smartSidebarCount1==2:
            return True
        else:
            return False
        
    def check_smart_sidebar_delete_button(self):
        print("Verify smart sider bar delete button")
        self.do_click(self.smartsidebardelete)
        smartSidebarCount = self.get_Element_count(self.smartsidebar)
        return smartSidebarCount
    
    def check_smart_sidebar_deleteall_button(self):
        print("Verify smart side bar delete all button")
        self.do_click(self.smartsidebardeleteall)
        smartSidebarCount = self.get_Element_count(self.smartsidebar)
        return smartSidebarCount
    
    def check_smart_sidebar_panel_close(self):
        print("Verify smart side bar close button")
        smartSidebarPanelCount = self.get_Element_count(self.smartsidebarpanel)
        self.do_click(self.smartsidebarclose)
        smartSidebarPanelCount1 = self.get_Element_count(self.smartsidebar)
        if smartSidebarPanelCount==1 and smartSidebarPanelCount1==0:
            return True
        else:
            return False
        
    def check_property_value_history_tab(self):
        print("Open history tab and verify property value")
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        for node in nodes:
            if not "isHide" in node:
                if "John Purchaser" in str(node["labelValue"]):
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    node_position = {
                        'x': float(node.get('x')),
                        'y': float(node.get('y'))
                    }
                    
                    coordinate_modifier = {
                    'x': 1,
                    'y': 1
                    }

                    offset = {
                    'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                    'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            offset.get('x')+offset_modifier_circle_counter,
                            offset.get('y')- offset_modifier_circle_counter
                            ).double_click().perform()
                    time.sleep(3)
                    break
        self.do_click(self.occupationproperty)
        propertytabcount = self.get_Element_count(self.propertytab)
        propertytabrowcount = self.get_Element_count(self.propertytabrow)
        self.do_click(self.closepropertytab)
        if propertytabcount == 1 and propertytabrowcount>1:
            return True
        else:
            return False
        
    def get_date_and_time_of_transaction(self):
        print("Get date and time of the treansaction from sidebar")
        dateAndTime = self.get_Element_Text(self.dateAndTimeOfTransaction)
        self.do_click(self.smartsidebarclose)
        return dateAndTime
    
    def get_date_and_time_tableView(self):
        print("Get date and time of the treansaction from table view")
        dateAndTime = self.get_Element_Text(self.dateAndTimeTableView)
        return dateAndTime
    
    def get_date_of_birth_of_person(self):
        print("Get date of birth of the person from sidebar")
        dateOfBirth = self.get_Element_Text(self.dateOfBirthOfPerson)
        self.do_click(self.smartsidebarclose)
        return dateOfBirth

    def get_date_of_birth_of_person_tableView(self):
        print("Get date of birth of the person from table view")
        dateOfBirth = self.get_Element_Text(self.dateOfBirthTableView)
        return dateOfBirth
    
    def check_show_report(self):
        print("Verify show Report")
        self.do_Enter_Text(self.showreportidtextbox,"Bet_game_of_chance")
        self.do_click(self.showbutton)

    def check_search_box(self):
        print("Verify Report search box")
        tablerowcount = self.get_Element_count(self.table)
        self.do_Enter_Text(self.searchbox,TestData.reportName)
        tablerowcountafterfilter = self.get_Element_count(self.table)
        time.sleep(3)
        self.do_click(self.searchbox)
        self.do_Enter_Text(self.searchbox," ")
        self.do_Enter_Text(self.searchbox,"abcdef")
        nodatarowtext = self.get_Text_Value(self.nodatarow)
        time.sleep(5)
        self.do_click(self.searchbox)
        self.do_Enter_Text(self.searchbox," ")
        self.do_Enter_Text(self.searchbox," ")
        if tablerowcount>2 and tablerowcountafterfilter==2 and nodatarowtext=="No data found":
            return True
        else:
            return False
        
    def check_sort_button(self):
        print("Verify Latest Report sort functionality based on submissionn date and time")
        self.do_click(self.sortdatefrom)
        datedata1 = self.get_Element_Text(self.tabledatedata1)
        datedata2 = self.get_Element_Text(self.tabledatedata2)
        date_format = "%b %d, %Y %I:%M:%S %p"
        date1 = datetime.strptime(datedata1, date_format)
        date2 = datetime.strptime(datedata2, date_format)
        if date1<=date2:
            asscending = True
        else:
            asscending = False
        #self.do_click(self.sortdatefromascending)
        self.do_click(self.sortdatefrom)
        datedata1 = self.get_Element_Text(self.tabledatedata1)
        datedata2 = self.get_Element_Text(self.tabledatedata2)
        date1 = datetime.strptime(datedata1, date_format)
        date2 = datetime.strptime(datedata2, date_format)
        if date1>=date2 and asscending==True:
            return True
        else:
            return False
        
    def check_report_xls_download(self):
        self.do_click(self.selectallcheckbox)
        downloaded = False
        print("Download Graph - AnalyticsNotebook")
        self.do_click(self.xlsfiledownlodbutton)
        time.sleep(4)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.xlsx') or ('.xlsx' in fname and fname.endswith('.xlsx.crdownload')):
                print("Deletet the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
        self.do_click(self.unselectallcheckbox) 
        time.sleep(2)       
        return downloaded
    
    def check_report_csv_download(self):
        self.do_click(self.selectallcheckbox)
        downloaded = False
        print("Download Graph - AnalyticsNotebook")
        self.do_click(self.csvfiledownlodbutton)
        time.sleep(4)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.csv') or ('.csv' in fname and fname.endswith('.csv.crdownload')):
                print("Deletet the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
        self.do_click(self.unselectallcheckbox) 
        time.sleep(2)      
        return downloaded
    
    def check_report_pdf_download(self):
        self.do_click(self.selectallcheckbox)
        downloaded = False
        print("Download Graph - AnalyticsNotebook")
        self.do_click(self.pdffiledownlodbutton)
        time.sleep(4)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.pdf') or ('.pdf' in fname and fname.endswith('.pdf.crdownload')):
                print("Deletet the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
        self.do_click(self.unselectallcheckbox) 
        time.sleep(2)       
        return downloaded
    
    def check_action_button_show_on_graph(self):
        print("Select Multiple reports and show on graph")
        self.do_click(self.selectcheckbox1)
        self.do_click(self.selectcheckbox2)
        self.do_click(self.selectcheckbox3)
        self.do_click(self.showongraph)

    def Validate_police_and_Last_Name_Filter(self):
        print("Verify Police and Last name filter")
        self.do_click(self.selectjohnpurchaser)
        self.do_click(self.selectjohnpurchaserarrow)
        jsonObject = self.get_chartData()
        nodechecker = False
        for node in jsonObject["nodes"]:
            if "John Purchaser" in str(node["labelValue"]):
                nodechecker = True
                if nodechecker == True:
                    return nodechecker
        
        return nodechecker

    def Validate_custom(self):
        print("Verify Custom Action")
        self.do_click(self.selectjohnpurchaser)
        self.do_click(self.custombutton)
        downloaded = False
        print("Download Graph - AnalyticsNotebook")
        time.sleep(2)
        for fname in os.listdir(os.path.join(conftest.BASE_DIR,'ReportDownloads')):
            print("File downloaded :"+os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
            if fname.endswith('.xlsx') or ('.xlsx' in fname and fname.endswith('.xlsx.crdownload')):
                print("Delete the downloaded file")
                os.remove(os.path.join(conftest.BASE_DIR,'ReportDownloads',fname))
                downloaded = True
                break
            else:
                downloaded = False
                time.sleep(2)       
        return downloaded
    
    def Validate_search_person_firstname_graph(self):
        print("Search report by first name and show graph")
        self.do_click(self.selectMaartje)
        self.do_click(self.selectMaartjearrow)
        time.sleep(2)
        jsonObject = self.get_chartData()
        nodechecker = False
        for node in jsonObject["nodes"]:
            if "Maartje Meester" in str(node["labelValue"]):
                nodechecker = True
                if nodechecker == True:
                    return nodechecker
        
        return nodechecker
    
    def Validate_first_and_Last_Name_Filter(self):
        print("Search report by first and last name and show graph")
        self.do_click(self.selectjohnpeterpersonA)
        self.do_click(self.selectjohnpeterpersonAarrow)
        jsonObject = self.get_chartData()
        nodechecker = False
        for node in jsonObject["nodes"]:
            if "John Peter PERSON A" in str(node["labelValue"]):
                nodechecker = True
                if nodechecker == True:
                    return nodechecker

    def goto_Report_Tab(self):
        print("Go to Report tab in table view")
        self.do_click(self.reportTab)

    def goto_Person_Tab(self):
        print("Go to Person tab in table view")
        self.do_click(self.personTab)

    def goto_Transaction_Tab(self):
        print("Go to Transaction tab in table view")
        self.do_click(self.transactionTab)

    def goto_Identification_Tab(self):
        print("Go to Identification tab in table view")
        self.do_click(self.identificationTab)

    def do_click_filterdate(self):
        print("Click Filter icon for the date field")
        self.do_click(self.filterDate)

    def do_Clear_Filter(self):
        print("Clear applied filter")
        self.do_click(self.clearFilter)

    def do_Filter_Based_On_DateBetween(self):
        print("Choose Date Betweeen filter category")
        self.do_click_filterdate()
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.dateBetweenFilterCategory)

    def do_Enter_DateTimeFrom_And_DateTimeTo_Values(self,submissionDateFrom,submissionDateTo):
        print("Enter Date From and Date To values")
        self.do_select_calendar_date(self.dateFromFilterValue,submissionDateFrom,self.selectCalendarDate)
        if self.is_ElementExist(self.tableViewNodesTab):
            self.do_click(self.tableViewNodesTab)
            self.do_Filter_Based_On_DateBetween()
        self.do_select_calendar_date(self.dateToFilterValue,submissionDateTo,self.selectCalendarDate)
        time.sleep(1)
        self.do_click(self.tableViewNodesTab)
        time.sleep(1)
        self.do_click(self.filterDate)

    def do_Enter_DateFrom_And_DateTo_Values(self,submissionDateFrom,submissionDateTo):
        print("Enter Date From and Date To values")
        self.do_select_calendar_date(self.dateFromFilterValue,submissionDateFrom,self.selectCalendarDate)
        self.do_select_calendar_date(self.dateToFilterValue,submissionDateTo,self.selectCalendarDate)
        
    def do_filter_Based_on_YearIs(self):
        print("Choose Year Is filter category")
        self.do_click(self.filterDate)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.yearIsFilterCategory)
    
    def do_Enter_YearIs_Value(self,yearIs):
        print("Enter year value")
        self.do_Enter_Text(self.yearIsValue,yearIs)
        self.do_click(self.yearIsValue)
        self.do_select_Year(yearIs)
        
    def do_Apply_Filter(self):
        print("Click Apply filter")
        self.do_click(self.applyFilter)

    def get_No_Of_Records_Filtered(self):
        print("Verify Number of Records filtered")
        self.wait_until_page_loads()
        time.sleep(1)
        return self.get_Element_count(self.noOfRecords) - self.get_Element_count(self.noRecordsFound)

    def do_Select_Node(self):
        print("select first non hidden node from json")
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        for node in nodes:
            if not "isHide" in node:
                canvas_start = {
                    'x': self.get_Element_X_Coordinate(self.canvasElement),
                    'y': self.get_Element_Y_Coordinate(self.canvasElement)
                }

                node_position = {
                    'x': float(node.get('x')),
                    'y': float(node.get('y'))
                }
                
                coordinate_modifier = {
                'x': 1,
                'y': 1
                }

                offset = {
                'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                }

                offset_modifier_circle_counter = 0

                ac = ActionChains(self.driver)
                ac.move_to_element_with_offset(
                    self.get_Element(homepage.collaspseLeftPane),
                    -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                    -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                        offset.get('x')+offset_modifier_circle_counter,
                        offset.get('y')- offset_modifier_circle_counter
                        ).click().perform()
                time.sleep(2)
                ac.move_by_offset(0,0).click().perform()
                break

    def do_click_Node_when_left_pane_is_collapsed(self):
        print("Click first non hidden node from json when the left navigation pane is collapsed")
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        for node in nodes:
            if not "isHide" in node:
                canvas_start = {
                    'x': self.get_Element_X_Coordinate(self.canvasElement),
                    'y': self.get_Element_Y_Coordinate(self.canvasElement)
                }

                node_position = {
                    'x': float(node.get('x')),
                    'y': float(node.get('y'))
                }
                
                coordinate_modifier = {
                'x': 1,
                'y': 1
                }

                offset = {
                'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                }

                offset_modifier_circle_counter = 0

                ac = ActionChains(self.driver)
                ac.move_to_element_with_offset(
                    self.get_Element(homepage.expandLeftPane),
                    -self.get_Element_X_Coordinate(homepage.expandLeftPane)-18,
                    -self.get_Element_Y_Coordinate(homepage.expandLeftPane)-18).move_by_offset(
                        offset.get('x')+offset_modifier_circle_counter,
                        offset.get('y')- offset_modifier_circle_counter
                        ).click().perform()
                time.sleep(2)
                break

    def do_Verify_QuickAccessToolBar_Enabled(self):
        print("Verify Quick access tool bar is enabled")
        time.sleep(1)
        tooldBarStatus = self.get_Attribute_Value(self.toolBar,"class")
        return "disabled" not in tooldBarStatus
    
    def do_Verify_QuickAccessToolBar_Disabled(self):
        time.sleep(1)
        print("Verify Quick access tool bar is diabled")
        tooldBarStatus = self.get_Attribute_Value(self.toolBar,"class")
        return "disabled" in tooldBarStatus
        
    def do_select_node_given(self, nodetype, nodelabel):
        print("Click the node node type :"+nodetype +" and node label :"+str(nodelabel))
        homepage = HomePage.HomePage(self.driver)
        homepage.do_get_mouse_to_screen_homeposition()
        self.do_click_node(nodetype, nodelabel)
        
    def verify_Description_Property_Text(self):
        print("Click value field for Description property in smart side bar")
        propertyValue = self.get_Text_Value(self.propertyDescription)
        if("..." in propertyValue):
            return True
        else:
            return False
        
    def verify_full_screen_readingmode(self):
        print("Verify Full screen reading modal is displayed")
        self.do_click(self.propertyDescription)
        return self.is_ElementExist(self.readingModeModal)
    
    def do_close_modal(self):
        print("Close Full screen reading modal")
        self.do_click(self.closeModal)

    def verify_sort_and_filter_nodesTab(self):
        print("Verify Sort and filter option is availabel in table view nodes tab")
        status = True
        elements = self.get_Elements(self.tableViewTabsList)
        for j in elements:
            j.click()
            sort = self.get_Element_count(self.tableColumnHeaders)-self.get_Element_count(self.tableColumnsWithSort)==1
            filter = self.get_Element_count(self.tableColumnHeaders)-self.get_Element_count(self.tableColumnsWihtFilter)==1
            if(sort==False or filter==False):
                status = False
                break
        return status
    
    def verify_sort_and_filter_EdgesTab(self):
        print("Verify Sort and filter option is availabel in table view edges tab")
        status = True
        self.do_click(self.tableViewEdgesTab)
        elements = self.get_Elements(self.tableViewTabsList)
        for j in elements:
            j.click()
            sort = self.get_Element_count(self.tableColumnHeaders)-self.get_Element_count(self.tableColumnsWithSort)==1
            filter = self.get_Element_count(self.tableColumnHeaders)-self.get_Element_count(self.tableColumnsWihtFilter)==1
            if(sort==False or filter==False):
                status = False
                break
        return status

    def verify_virtual_nodes_exists(self):
        print("Verify Virtual Node exists")
        status = False
        elements = self.get_Elements(self.tableViewTabsList)
        for j in elements:
            j.click()
            if(self.get_Element_count(self.virtualNodesPlus)>0):
                status = True
                break
        return status    
        
    def verify_virtual_node_expand_and_collapse(self):
        print("Verify Virtual Node Expand and Collapse Funtionality is working")
        noOfColumnsWithSort = self.get_Element_count(self.tableColumnsWithSort)
        noOfRowsBeforeExpanding = self.get_Element_count(self.noOfRecords)
        elements = self.get_Elements(self.virtualNodesPlus)
        for ele in elements:
            ele.click()
            noOfRowsAfterExpanding = self.get_Element_count(self.noOfRecords)
            noOfExpandedVirtualNode = self.get_Element_count(self.virtualNodesMinus)
            noOfColumnsWithSortAfterExpand = self.get_Element_count(self.tableColumnsWithSort)
            if(noOfRowsAfterExpanding>noOfRowsBeforeExpanding and noOfColumnsWithSortAfterExpand == noOfColumnsWithSort*2 and noOfExpandedVirtualNode==1):
                expanded = True
            else:
                expanded = False
                break
            self.do_click(self.virtualNodesMinus)
            noOfRowsAfterCollapsing = self.get_Element_count(self.noOfRecords)
            noOfExpandedVirtualNode = self.get_Element_count(self.virtualNodesMinus)
            noOfColumnsWithSortAfterCollapse = self.get_Element_count(self.tableColumnsWithSort)
            if(noOfRowsAfterCollapsing==noOfRowsBeforeExpanding and noOfColumnsWithSortAfterCollapse == noOfColumnsWithSort and noOfExpandedVirtualNode==0):
                collapsed = True
            else:
                collapsed = False
                break
        return expanded and collapsed
    
    def verify_zoom_reset_exists(self):
        print("Verify Zoom reset button exists")
        return self.is_ElementExist(self.zoomReset)
    
    def verify_zoom_selected_node_exists(self):
        print("Verify Zoom selected node button exists")
        return self.is_ElementExist(self.selectedNodeZoom)
    
    def verify_zoom_fit_to_Screen_exists(self):
        print("Verify Zoom fit to screen button exists")
        return self.is_ElementExist(self.fitToScreen)
    
    def do_click_fit_to_screen(self):
        print("Click Zoom fit to screen button")
        self.do_click(self.fitToScreen)

    def verify_search_exists(self):
        print("Verify graph view search exists")
        return self.is_ElementExist(self.search)
    
    def verify_zoom_in_exists(self):
        print("Verify Zoom in button exists")
        return self.is_ElementExist(self.zoomIn)
    
    def click_zoom_in(self):
        print("Click Zoom in button")
        self.do_click(self.zoomIn)

    def verify_zoom_out_exists(self):
        print("Verify Zoom out button exists")
        return self.is_ElementExist(self.zoomOut)

    def verify_unhighlight_all_exists(self):
        print("Verify unhighlight all button exists")
        return self.is_ElementExist(self.unhighlightAll)
    
    def verify_unhighlight_all_disables(self):
        print("Verify unhighlight all button is disabled")
        self.do_click(self.unhighlightAll)
        classValue = self.get_Attribute_Value(self.unhighlightAll,"class")
        if "disabled" in classValue:
            return True
        else:
            return False
    
    def verify_deselect_all_exists(self):
        print("Verify deselect all button exists")
        return self.is_ElementExist(self.deselectAll)
    
    def verify_deselect_all_Enables(self):
        print("Verify deselect all button is enabled on clicking node")
        self.do_select_GivenNode("","","Click")
        classValue = self.get_Attribute_Value(self.deselectAll,"class")
        print (classValue)
        if "disabled" in classValue:
            return False
        else:
            return True
        
    def verify_deselect_all_Disables(self):
        print("Verify deselect all button exists")
        self.do_click(self.deselectAll)
        classValue = self.get_Attribute_Value(self.deselectAll,"class")
        if "disabled" in classValue:
            return True
        else:
            return False
        
    def verify_area_select_exists(self):
        print("Verify area select button exists")
        return self.is_ElementExist(self.areaSelect)
    
    def verify_area_highlight_exists(self):
        print("Verify area highlight button exists")
        return self.is_ElementExist(self.areaHighlight)

    def verify_info_icon(self):
        print("Verify info icon exists")
        self.do_click(self.infIconInGraph)
        
    def get_first_virtualnode_label(self):
        print("Get First virtual node label from json")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        labelValue = None
        for n in nodes:
            if "showCollapse" in n:
                labelValue = n["labelValue"]
                break
        return labelValue
    
    def get_first_non_virtualnode_label(self):
        print("Get First non virtual node label from json")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        labelValue = None
        for n in nodes:
            if not "showCollapse" in n:
                labelValue = n["labelValue"]
                break
        return labelValue
    
    def get_first_node_label_with_counter(self):
        print("Get First node label which has counter from json")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        labelValue = None
        for n in nodes:
            if (not "isHide" in n or str(n["isHide"]).lower()=="false") and (n["counterValue"])>0:
                labelValue = n["labelValue"]
                break
        return labelValue
    
    def check_node_is_highlighted(self,nodeType,nodeLable):
        print("Verify node - Node type :"+nodeType+" and node label :"+str(nodeLable)+" - is highlighted")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        for n in nodes:
            if (not "isHide" in n or str(n["isHide"]).lower()=="false") and (nodeType == "" or str(n["label"]).lower() == nodeType) and (nodeLable == "" or ''.join(filter(str.isdigit, ''.join(n["labelValue"])))==nodeLable or str(n["labelValue"][0]).lower()==str(nodeLable).lower()):
                if str(n["isNodeHighlight"]).lower() == "true":
                    return True
        return False
    
    def check_edge_is_highlighted(self,nodeType,nodeLable):
        print("Verify node - Node type :"+nodeType+" and node label :"+str(nodeLable)+" - is highlighted")
        chart_data = self.get_chartData()
        nodes = chart_data.get('edges')
        for n in nodes:
            if (not "isHide" in n or str(n["isHide"]).lower()=="false") and (nodeType == "" or str(n["label"]).lower() == nodeType.lower()) and (nodeLable == "" or ''.join(filter(str.isdigit, ''.join(n["labelValue"])))==nodeLable or str(n["labelValue"][0]).lower()==str(nodeLable).lower()):
                if str(n["isEdgeHighlight"]).lower() == "true":
                    return True
        return False

    def verify_given_virtual_node_is_expanded(self,nodeLabel):  
        print("Verify virtual node - node label :"+str(nodeLabel)+" is expanded")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')

        for n in nodes:
            if str(nodeLabel) in str(n["labelValue"]) and "isCollapse" in n and str(n["isCollapse"]).lower() == "true":
                return False
          
        return True
    
    def get_node_count(self):
        print("Get node count from the graph")
        chart_data = self.get_chartData()
        return len(chart_data['nodes'])

    def verify_click_counter_icon_expands_newNodes(self):
        print("Verify on clicking icon new nodes are populated")
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        nodeCountBefore = len(chart_data['nodes'])
        # get the reporting entity node
        node = next((n for n in nodes if n["labelValue"] == ["NL Sample 14"]), None)

        canvas_start = {
            'x': self.get_Element_X_Coordinate(self.canvasElement),
            'y': self.get_Element_Y_Coordinate(self.canvasElement)
        }

        node_position = {
            'x': float(node.get('x')),
            'y': float(node.get('y'))
        }
        
        coordinate_modifier = {
        'x': 1,
        'y': 1
        }

        offset = {
        'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
        'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
        }

        offset_modifier_circle_counter = -14

        ac = ActionChains(self.driver)
        ac.move_to_element_with_offset(
            self.get_Element(homepage.collaspseLeftPane),
            -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
            -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                offset.get('x')+offset_modifier_circle_counter,
                offset.get('y')- offset_modifier_circle_counter
                ).click().perform()

        time.sleep(2)
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        nodeCountAfter = len(chart_data['nodes'])
        if nodeCountBefore<nodeCountAfter:
            return True
        else:
            return False

    def do_click_node(self,nodeType,nodeLabel):
        print("Click node - Node type :"+nodeType+" and node label :"+str(nodeLabel))
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        for node in nodes:
            if not "isHide" in node:
                if ((str(nodeLabel) in str(node["labelValue"]) or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(node["labelValue"])))==str(nodeLabel)) and (nodeType.lower() in str(node["label"]).lower() or nodeType=="")):
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    node_position = {
                        'x': float(node.get('x')),
                        'y': float(node.get('y'))
                    }
                    
                    coordinate_modifier = {
                    'x': 1,
                    'y': 1
                    }

                    offset = {
                    'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                    'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            offset.get('x')+offset_modifier_circle_counter,
                            offset.get('y')- offset_modifier_circle_counter
                            ).click().perform()
                    time.sleep(2)

    def do_double_click_node(self,nodeType,nodeLabel):
        print("Double click node - Node type :"+nodeType+" and node label :"+str(nodeLabel))
        homepage = HomePage.HomePage(self.driver)
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        for node in nodes:
            homepage.do_get_mouse_to_screen_homeposition()
            if not "isHide" in node:
                if ((nodeLabel.lower() in str(node["labelValue"]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(node["labelValue"])))==nodeLabel) and (nodeType.lower() in str(node["label"]).lower() or nodeType=="")):
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    node_position = {
                        'x': float(node.get('x')),
                        'y': float(node.get('y'))
                    }
                    
                    coordinate_modifier = {
                    'x': 1,
                    'y': 1
                    }

                    offset = {
                    'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
                    'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            offset.get('x')+offset_modifier_circle_counter,
                            offset.get('y')- offset_modifier_circle_counter
                            ).double_click().perform()
                    time.sleep(1)

    def do_double_click_edge(self,nodeType,nodeLabel):
        print("Double click edge - edge type :"+nodeType+" and edge label :"+str(nodeLabel))
        homepage = HomePage.HomePage(self.driver)
        chart_data = self.get_chartData()
        edges = chart_data.get('edges')
        for edge in edges:
            homepage.do_get_mouse_to_screen_homeposition()
            if not "isHide" in edge or edge["isHide"]==False:
                if ((nodeLabel.lower() == str(edge["labelValue"][0]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(edge["labelValue"])))==nodeLabel) and (nodeType.lower() in str(edge["label"]).lower() or nodeType=="")):
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    source_node_position = {
                        'x': float(edge.get('source').get('x'))+canvas_start.get('x'),
                        'y': float(edge.get('source').get('y'))+canvas_start.get('y')
                    }
                    
                    target_node_position = {
                        'x': float(edge.get('target').get('x'))+canvas_start.get('x'),
                        'y': float(edge.get('target').get('y'))+canvas_start.get('y')
                    }

                    edge_position = {
                        'x' : source_node_position.get('x')-(source_node_position.get('x')-target_node_position.get('x'))/2,
                        'y' : source_node_position.get('y')-(source_node_position.get('y')-target_node_position.get('y'))/2
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            edge_position.get('x')+offset_modifier_circle_counter,
                            edge_position.get('y')- offset_modifier_circle_counter
                            ).double_click().perform()
                    time.sleep(1)
                    break

    def do_click_edge(self,nodeType,nodeLabel):
        print("Click edge - edge type :"+nodeType+" and edge label :"+str(nodeLabel))
        homepage = HomePage.HomePage(self.driver)
        chart_data = self.get_chartData()
        edges = chart_data.get('edges')
        for edge in edges:
            homepage.do_get_mouse_to_screen_homeposition()
            if not "isHide" in edge:
                if ((nodeLabel.lower() == str(edge["labelValue"][0]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(edge["labelValue"])))==nodeLabel) and (nodeType.lower() in str(edge["label"]).lower() or nodeType=="")):
                    canvas_start = {
                        'x': self.get_Element_X_Coordinate(self.canvasElement),
                        'y': self.get_Element_Y_Coordinate(self.canvasElement)
                    }

                    source_node_position = {
                        'x': float(edge.get('source').get('x'))+canvas_start.get('x'),
                        'y': float(edge.get('source').get('y'))+canvas_start.get('y')
                    }
                    
                    target_node_position = {
                        'x': float(edge.get('target').get('x'))+canvas_start.get('x'),
                        'y': float(edge.get('target').get('y'))+canvas_start.get('y')
                    }

                    edge_position = {
                        'x' : source_node_position.get('x')-(source_node_position.get('x')-target_node_position.get('x'))/2,
                        'y' : source_node_position.get('y')-(source_node_position.get('y')-target_node_position.get('y'))/2
                    }

                    offset_modifier_circle_counter = 0

                    ac = ActionChains(self.driver)
                    ac.move_to_element_with_offset(
                        self.get_Element(homepage.collaspseLeftPane),
                        -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
                        -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                            edge_position.get('x')+offset_modifier_circle_counter,
                            edge_position.get('y')- offset_modifier_circle_counter
                            ).click().perform()
                    time.sleep(1)
                    break

    def verify_click_counter_icon_expands_newNodes_given_label(self,nodeLabel):
        print("Verify clicking counter icon for the node - node label :"+str(nodeLabel)+" populates new node")
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        nodeCountBefore = len(chart_data['nodes'])
        node = next((n for n in nodes if ((nodeLabel.lower() in str(n["labelValue"][0]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(n["labelValue"])))==nodeLabel)) and not "isHide" in n), None)
        canvas_start = {
            'x': self.get_Element_X_Coordinate(self.canvasElement),
            'y': self.get_Element_Y_Coordinate(self.canvasElement)
        }

        node_position = {
            'x': float(node.get('x')),
            'y': float(node.get('y'))
        }
        
        coordinate_modifier = {
        'x': 1,
        'y': 1
        }

        offset = {
        'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
        'y': (node_position.get('y') + canvas_start.get('y'))*coordinate_modifier.get('y')
        }

        offset_modifier_circle_counter = -14

        ac = ActionChains(self.driver)
        ac.move_to_element_with_offset(
            self.get_Element(homepage.collaspseLeftPane),
            -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
            -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                offset.get('x')+offset_modifier_circle_counter,
                offset.get('y')+ offset_modifier_circle_counter
                ).click().perform()
        
        time.sleep(2)
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        nodeCountAfter = len(chart_data['nodes'])
        if nodeCountBefore<nodeCountAfter:
            return True
        else:
            return False
        
        """ time.sleep(8)
        chart_data = self.get_chartData()

        nodes = chart_data.get('nodes')
        nodeCountBefore = len(chart_data['nodes'])
        # get the reporting entity node
        node = next((n for n in nodes if n["labelValue"] == nodeLabel and not "isHide" in n), None)

        # get the canvas
        elem = self.driver.find_element(By.TAG_NAME, "canvas")

        # get the center point of the canvas
        canvas_center = {
            'x': int(elem.get_attribute('width'))/2,
            'y': int(elem.get_attribute('height'))/2
        }

        node_position = {
            'x': float(node.get('x')),
            'y': float(node.get('y'))
        }

        # move_to_element moves to the center of the element
        # x, y of chart_data is given from the top, left corner
        # so we need to calculate the offset of movement relative to the center of the canvas
        offset = {
        'x': node_position.get('x') - canvas_center.get('x'),
        'y': node_position.get('y') - canvas_center.get('y')
        }

        # offset modifier for counter icon for a circle node
        # this means the the counter icon is located 14px up and left from the center point of a circle node
        offset_modifier_circle_counter = -15

        # clicking on counter icon
        ac = ActionChains(self.driver)
        ac.move_to_element(elem).move_by_offset(
            offset.get('x') + offset_modifier_circle_counter,
            offset.get('y') + offset_modifier_circle_counter
        ).click().perform()

        time.sleep(5)
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')
        nodeCountAfter = len(chart_data['nodes'])
        if nodeCountBefore<nodeCountAfter:
            return True
        else:
            return False
        """

    def do_expand_collaps_virtual_node(self,nodeLabel):
        print("Expand/collapse Virtual node - node label :"+str(nodeLabel))
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        node = next((n for n in nodes if n["labelValue"] == nodeLabel and not "isHide" in n), None)

        canvas_start = {
            'x': self.get_Element_X_Coordinate(self.canvasElement),
            'y': self.get_Element_Y_Coordinate(self.canvasElement)
        }

        node_position = {
            'x': float(node.get('x')),
            'y': float(node.get('y'))
        }
        
        coordinate_modifier = {
        'x': 1,
        'y': 1
        }

        offset = {
        'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
        'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
        }

        offset_modifier_circle_counter = -14

        ac = ActionChains(self.driver)
        ac.move_to_element_with_offset(
            self.get_Element(homepage.collaspseLeftPane),
            -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
            -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                offset.get('x')+offset_modifier_circle_counter,
                offset.get('y')- offset_modifier_circle_counter
                ).click().perform()
        time.sleep(2)

    def do_unhighlight_given_node(self,nodeLabel):
        print("Unhighlightnode - node label :"+str(nodeLabel))
        chart_data = self.get_chartData()
        homepage = HomePage.HomePage(self.driver)
        nodes = chart_data.get('nodes')
        node = next((n for n in nodes if n["labelValue"] == nodeLabel and not "isHide" in n), None)

        canvas_start = {
            'x': self.get_Element_X_Coordinate(self.canvasElement),
            'y': self.get_Element_Y_Coordinate(self.canvasElement)
        }

        node_position = {
            'x': float(node.get('x')),
            'y': float(node.get('y'))
        }
        
        coordinate_modifier = {
        'x': 1,
        'y': 1
        }

        offset = {
        'x': (node_position.get('x') + canvas_start.get('x'))*coordinate_modifier.get('x'),
        'y': (node_position.get('y') + canvas_start.get('y')-7)*coordinate_modifier.get('y')
        }

        offset_modifier_circle_counter = 0

        ac = ActionChains(self.driver)
        ac.move_to_element_with_offset(
            self.get_Element(homepage.collaspseLeftPane),
            -self.get_Element_X_Coordinate(homepage.collaspseLeftPane)-18,
            -self.get_Element_Y_Coordinate(homepage.collaspseLeftPane)-18).move_by_offset(
                offset.get('x')+offset_modifier_circle_counter,
                offset.get('y')- offset_modifier_circle_counter
                ).click().perform()

        time.sleep(2)

    def verify_given_node_is_unhighlighted(self,nodeLabel):
        print("Verify node - node label :"+str(nodeLabel)+" is unhighlighted")
        chart_data = self.get_chartData()
        nodes = chart_data.get('nodes')

        for node in nodes:
            if node["labelValue"] == nodeLabel and str(node["isNodeHighlight"]).lower() == "false" and (not "isHide" in node or str(node["isHide"]).lower()=="false") :
                config = node["config"]
                size = config["size"]
                if size != "small":
                    return True
          
        return False

    def do_click_unhighlightAll(self):
        print("Click unhighight all button")
        classValue = self.get_Attribute_Value(self.unhighlightAll,"class")
        if not "disabled" in classValue:
            self.do_click(self.unhighlightAll)
        
    def do_click_search(self):
        print("Click graph view search")
        self.do_click(self.search)

    def do_enter_search_input(self,inputText):
        print("Enter search text "+inputText)
        self.do_Enter_Text(self.searchtxtField,inputText)
        self.do_Enter_Text(self.searchtxtField,Keys.ENTER)

    def verify_node_highlighted_for_search(self):
        print("Verify node highlighted for graph view search")
        jsonObject = self.get_chartData()
        status = False
        for node in jsonObject["nodes"]:
            if not "isHide" in node and "searchSelected" in node: 
                if (str(node["searchSelected"]) =="True"):
                    if (str(node["label"]) =="report" or str(node["label"]) =="transaction"):
                        status = True
                    else:
                        status = False
                        break
        return status
    
    def verify_edge_highlighted_for_search(self):
        print("Verify edge highlighted for graph view search")
        jsonObject = self.get_chartData()
        for edge in jsonObject["edges"]:
            if not "isHide" in edge and "searchSelected" in edge:
                if (str(edge["searchSelected"]) =="True"):
                    if ("report" in str(edge["label"]).lower() or "report" in str(edge["labelValue"]).lower()):
                        status = True
                    else:
                        status = False
                        break
        return status
    
    def verify_transactionCount_property_sidebar(self):
        print("Get transaction count from property side bar" )
        return self.get_Text_Value(self.transactionCount)

    def do_clear_smartsidebar(self):
        print("Click delete all and close button in the property side bar")
        self.do_click(self.smartsidebardeleteall)
        self.do_click(self.smartsidebarclose)

    def do_click_DOB_property(self):
        print("Click date of birth property in side bar")
        self.do_click(self.dateOfBirthPropertyLabel)

    def get_valid_from_value(self):
        print("Get Valid From the dialog")
        validFrom = self.get_Element_Text(self.vaildFromPropertyDialog)
        self.do_click(self.closepropertytab)
        self.do_click(self.smartsidebarclose)
        return validFrom
        
    def verify_degree_property_not_exist(self):
        print("Verify degree property(hidden) not exists in the property side bar")
        if self.is_ElementExist(self.transactionDegreeProperty):
            return False
        else:
            return True
    
    def verify_person_prefix_exist(self):
        print("Verify person prefix property exists in the property side bar")
        return self.is_ElementExist(self.personPrefixProperty)
        
    def verify_transaction_property_order(self):
        print("Verify transaction node properties order in the property side bar")
        eles = self.get_Elements(self.propertyList)
        i=0
        for ele in eles :
            if ele.text == TestData.transactionProperties[i]:
                order = True
            else:
                order = False
                break
            i =i+1
        self.do_clear_smartsidebar()
        return order
    
    def verify_person_property_order(self):
        print("Verify person node properties order in the property side bar")
        eles = self.get_Elements(self.propertyList)
        i=0
        for ele in eles :
            if ele.text == TestData.personProperties[i]:
                order = True
            else:
                order = False
                break
            i =i+1
        self.do_clear_smartsidebar()
        return order
    
    def verify_virtual_node_values_displayed(self):
        print("Verify values are available in the filter for virtual node column")
        for ele in self.get_Elements(self.virtualNode_personTab):
            if(ele.text == "Yes" or ele.text == "Unspecified" or ele.text == "No"):
                status = True
            else:
                status = False
                break
        return status
    
    def get_tooltip_text(self):
        print("Get tool tip text")
        return self.get_Element_Text(self.tooltipText)

    def verify_tooltip_displayed_toolbar_image(self):
        print("Mouse hover on graph image export button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.graphImageExport)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_toolbar_pdf(self):
        print("Mouse hover on pdf export button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.graphPDFExport)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_toolbar_analysts_notebook(self):
        print("Mouse hover on analysts notebook export button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.graphAnalystsNotebookExport)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_toolbar_tableView(self):
        print("Mouse hover on graph table view button")
        self.take_mouse_to_origin()
        ActionChains(self.driver).move_to_element(self.get_Element(self.graphTableView)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_zoomReset(self):
        print("Mouse hover on zoom reset button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.zoomReset)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_fit_selection_to_screen(self):
        print("Mouse hover on zoom fit selection to screen button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.selectedNodeZoom)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_fit_to_screen(self):
        print("Mouse hover on zoom - fit to screen button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.fitToScreen)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_search(self):
        print("Mouse hover on graph view search button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.searchInGraph)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_zoom_in(self):
        print("Mouse hover on zoom in button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.zoomIn)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_zoom_out(self):
        print("Mouse hover on zoom out button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.zoomOut)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_unhighlight_all(self):
        print("Mouse hover on unhighlight all button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.unhighlightAll)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_deselect_all(self):
        print("Mouse hover on deselect all button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.deselectAll)).perform()
        return self.get_tooltip_text()

    def verify_tooltip_displayed_area_select(self):
        print("Mouse hover on area select button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.areaSelect)).perform()
        return self.get_tooltip_text()
    
    def verify_tooltip_displayed_area_highlight(self):
        print("Mouse hover on area highlight button")
        ActionChains(self.driver).move_to_element(self.get_Element(self.areaHighlight)).perform()
        return self.get_tooltip_text()
    
    def verify_enumeration_filter_works(self):
        print("Verify filter works for Enumeration values")
        self.do_click(self.indicatorFilter_ReportTab)
        self.do_click(self.expandFiterDropDown)
        self.do_click(self.selectallcheckbox)
        if self.is_element_clickable(self.closeFilterDropDown):
            self.do_click(self.closeFilterDropDown)
        self.do_click(self.applyFilter)
        return self.get_No_Of_Records_Filtered()
    
    def filter_first_name_person_tab(self,filterValue):
        print("Filter first name column "+filterValue)
        self.do_click(self.firstNameFilter_personTab)
        self.do_Enter_Text(self.filterTextValue,filterValue)
        self.do_click(self.applyFilter)
        time.sleep(2)

    def verify_columns_order_nodes_table_view(self):
        print("Verify column order for the nodes in the table view")
        tabsList = self.get_Elements(self.tableViewTabsList)
        for tab in tabsList:
            if tab.text!="" :
                headers=[]
                self.do_click_element(tab)
                columnHeaders = self.get_Elements(self.tableColumnHeadersText)
                for header in columnHeaders:
                    headers.append(header.text)
                if tab.text != "Person" and tab.text != "Transaction":
                    for i in range(len(headers) - 1):
                        if headers[i] > headers[i + 1]:
                            return False
                else:
                    if headers != TestData.persontabColumnOrder and headers != TestData.transactiontabColumnOrder:
                        return False
        return True
    
    def verify_columns_order_edges_table_view(self):
        print("Verify column order for the edges in the table view")
        self.do_click(self.tableViewEdgesTab)
        tabsList = self.get_Elements(self.tableViewTabsList)
        for tab in tabsList:
            headers=[]
            self.do_click_element(tab)
            columnHeaders = self.get_Elements(self.tableColumnHeadersText)
            for header in columnHeaders:
                headers.append(header.text)
            for i in range(len(headers) - 1):
                if headers[i] > headers[i + 1]:
                    return False
        return True

    def click_save_graph(self):
        print("Click save graph")
        self.do_click(self.saveGraph)
        time.sleep(2)

    def verify_save_graph_is_enabled(self):
        print("Verify Save graph button is enabled or not")
        if self.is_ElementExist(self.disabledSaveButton):
            return False
        return True

    def enter_graph_name(self,graphName):
        print("Enter graph name "+graphName)
        self.do_Enter_Text(self.graphName,graphName)

    def verify_graph_save_modal_exists(self):
        print("Verify save graph modal exists")
        return self.is_ElementExist(self.confirmSaveGraph)

    def click_cancel_save_graph(self):
        print("Click cancel in the save graph modal")
        self.do_click(self.cancelSaveGraph)
        time.sleep(2)

    def click_confirm_save_graph(self):
        print("Click confirm in the save graph modal")
        self.do_click(self.confirmSaveGraph)

    def verify_error_message_displayed_for_Same_graph_name(self):
        print("Verify error message displayed when we enter the same graph name")
        return self.is_ElementExist(self.sameGraphNameError)

    def do_save_graph(self):
        global saveGraphName
        saveGraphName = None #"AutomationTest-06_11_2024_18_13_29"
        today_date = datetime.now()
        month = today_date.strftime("%m")
        day = today_date.strftime("%d")
        year = today_date.strftime("%Y")
        hour = today_date.strftime("%H")
        minute = today_date.strftime("%M")
        seconds = today_date.strftime("%S")
        saveGraphName = "WorkSpaceTest-"+month+"_"+day+"_"+year+"_"+hour+"_"+minute+"_"+seconds
        self.do_click(self.saveGraph)
        self.do_Enter_Text(self.graphName,saveGraphName)
        self.do_click(self.confirmSaveGraph)
        print("Save graph with name "+saveGraphName)
        time.sleep(2)

    def do_save_another_graph(self):
        global mergedGraphName
        mergedGraphName = None #"AutomationTest-06_11_2024_18_13_29"
        today_date = datetime.now()
        month = today_date.strftime("%m")
        day = today_date.strftime("%d")
        year = today_date.strftime("%Y")
        hour = today_date.strftime("%H")
        minute = today_date.strftime("%M")
        seconds = today_date.strftime("%S")
        mergedGraphName = "Merged Nodes Test-"+month+"_"+day+"_"+year+"_"+hour+"_"+minute+"_"+seconds
        self.do_click(self.saveGraph)
        self.do_Enter_Text(self.graphName,mergedGraphName)
        self.do_click(self.confirmSaveGraph)
        print("Save graph with name "+mergedGraphName)
        time.sleep(2)

    def do_save_graph_new_user(self):
        global userGraphName
        userGraphName = None #"AutomationTest-06_05_2024_16_56_00"
        today_date = datetime.now()
        month = today_date.strftime("%m")
        day = today_date.strftime("%d")
        year = today_date.strftime("%Y")
        hour = today_date.strftime("%H")
        minute = today_date.strftime("%M")
        seconds = today_date.strftime("%S")
        userGraphName = "User-"+month+"_"+day+"_"+year+"_"+hour+"_"+minute+"_"+seconds
        self.do_click(self.saveGraph)
        self.do_Enter_Text(self.graphName,userGraphName)
        self.do_click(self.confirmSaveGraph)
        print("Save graph with name "+userGraphName)
        time.sleep(2)

    def verify_discard_changes_modal_displayed(self):
        print("Verify discard saved changes modal displayed")
        return self.is_ElementExist(self.confirmDiscardChanges)
    
    def verify_pending_updates_displayed(self):
        print("Verify pending updates modal displayed")
        return self.is_ElementExist(self.pendingUpdates)

    def verify_modal_message(self,message):
        print("Verify modal message is "+message)
        if self.get_Text_Value(self.messageDiscardChanges) == message:
            return True
        return False
    
    def click_no_discard_changes(self):
        print("Click No on discard changes modal")
        self.do_click(self.noDiscardChanges)
        
    def click_yes_discard_changes(self):
        print("Click Yes on discard changes modal")
        self.do_click(self.yesDiscardChanges)
        time.sleep(2)

    def click_ok_pending_updates(self):
        print("Click Ok on pending updates modal")
        self.do_click(self.okPendingUpdates)

    def verify_the_property_is_in_bold(self,propertyName):
        print("Verify the property :"+propertyName+" is bold in the side bar")
        ele = self.get_Elements(self.propertyBold)
        for e in ele:
            if e.text == propertyName:
                return True
        return False

    def get_Toast_Message_Text(self):
        print("Get the toast message")
        self.wait_until_page_loads()
        return self.get_Element_Text(self.toasMessage)
    
    def verify_toast_message_displayed(self):
        print("Verify toast message is displayed or not")
        return self.is_ElementExist(self.toasMessage)