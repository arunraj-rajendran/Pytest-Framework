class TestData:
    #Log in
    URL = "http://qa.gofintel.local:3000/"
    userName = "test@gmail.com"
    password = "12password34changeMe"
    logInPage_title = "Sign in to goFintel"

    userName1 = "test01@gofintel.local"
    password1 = "vienna2023"
   
    #AirFlow URL
    airFlowURL = "http://qa.gofintel.local:8081/home"
    airflowUserName = "airflow"
    airFlowPassword = "12password34changeMe"

    #Reports
    reportName = ["DOS-EW-18337_trs3", "DOS-EW-14222_trs1","DOS-EW-14222_trs3"]
    reportName1 = "Wire_transfer-1"
    reportNameForTransactionCount = ["DOS-TW-01081_trs2en3","DOS-EW-14222_trs1"]
    reportNameForVirtualNodes = ["DOS-EW-14222_trs3","DOS-EW-18337_trs3"]
    reportNameForEnumerationFilter = "Money_transfer"
    reportNameForMergedNodes = "Cash_withdrawal"
    submissionDateTimeFrom = "12/15/2023 08:36:06 PM"
    submissionDateTimeTo = "12/16/2023 08:36:07 PM"
    yearIs = "2023"

    #Report Table View
    reportSubmissionDateTimeFrom = "12/15/2023 08:36:06 PM"
    reportSubmissionDateTimeTo = "12/16/2023 08:36:07 PM"
    negativeReportSubmissionDateTimeTo = "12/16/2023 08:36:05 PM"
    reportYearIs = "2023"
    negativeReportYearIs = "2022"
    DateAndTimeOfTransactionFrom = "12/14/2021 08:36:07 PM"
    DateAndTimeOfTransactionTo = "12/18/2021 08:36:07 PM"
    negativeDateAndTimeOfTransactionTo = "12/16/2021 08:36:07 PM"
    transactionYearIs = "2021" 
    personBirthDateFrom = "05/23/1996"
    personBirthDateTo = "06/23/1997"
    negativePersonBirthDateTo = "10/23/1996"
    personBirthYearIs = "1997"

    #Search Person
    country = "Netherlands"
    birthDateFrom = "01/01/1970"
    birthDateTo = "01/01/1980"
    birthYearIs ="1977"

    #Search Report
    indicatorfilter1 = "A funds transfer amounting to € 15,000 or more (casino)."
    indicatorfilter2 = "A transaction amounting to € 15,000 or more"
    indicatorfilter3 = "A transaction by which one or more items of property are brought under the control of a pawn shop, and the amount made available by the pawn shop is € 20,000 or more."
    autocompletename1 = "NL Sample 12345"
    autocompletename2 = "NL Sample 11912"
    autocompletename3 = "NL Sample 29991"
    breadCrumbTest = "NL Sample 123"

    firstname = "John"
    firstname1 = "Maartje"
    firstname2 = "John Peter"
    firstname3 = "asp"
    Lastname = "Purchaser"
    Lastname1 = "PERSON A"
    Lastname3 = "art"
    submissionDateFrom = "01/01/2022"
    yearIsRecordCount = 16 


    #Latest Report table submission date and time format for different locales
    EnglishDateTimeFormat = "%b %d, %Y %I:%M:%S %p"
    SpanishDateTimeFormat = "%d %B %Y %H:%M:%S" #"%d de %b. de %Y %H:%M:%S"
    FrenchDateTimeFormat = "%d %B %Y %H:%M:%S" #"%d %b. %Y %H:%M:%S"
    DutchDatTimeFormat = "%d %B %Y %H:%M:%S" #"%d %b. %Y %H:%M:%S"

    EnglishDateFormat = "%b %d, %Y"
    OtherDateFormat = "%d %B %Y"

    #Property Order
    transactionProperties=['Tr. number','Value of transaction', 'Description', 'Date and time of transaction', 'Suspicious', 'Label', 'Late deposit indicator', 'Sources']
    personProperties=['Last name','Prefix', 'First name', 'Birth date', 'Label', 'Middle name', 'Sources', 'Transaction count', 'Virtual node']

    #ToolTipText
    imageExport = "PNG"
    pdfExport = "PDF"
    analystsNotebook = "Analyst's Notebook"
    showTableView = "Show table view of graph"
    hideTableView = "Hide table view of graph"
    zoomReset = "Actual Size"
    fitSelectionToScreen = "Fit selection to screen"
    fitToScreen = "Fit to screen"
    search = "Search"
    zoomIN = "Zoom In"
    zoomOut = "Zoom Out"
    unhighlightAll = "Unhighlight all"
    deselectAll = "Deselect all"
    areaSelectTool = "Area select tool"
    areaUnhighlightTool = "Area unhighlight tool"


    #TableView
    persontabColumnOrder=["Last name","Prefix","First name","Birth date","Sources","Transaction count","Virtual node"]
    transactiontabColumnOrder = ['Tr. number', 'Value of transaction', 'Description', 'Date and time of transaction', 'Suspicious', 'Internal ref. nb.', 'Late deposit indicator', 'Sources']

    #breadCrumb
    latestReportsNav = ["Reports","Latest reports","Results"]
    latestReportsGraphNav = ["Reports","Latest reports","Results","Details"]
    searchReportNav = ["Reports","Search report","Input"]
    searchReportTableNav = ["Reports","Search report","Input","Results"]
    searchReportGraphNav = ["Reports","Search report","Input","Results","Details"]
    showReportNav = ["Reports","Show report","Input"]
    showReportGraphNav = ["Reports","Show report", "Input","Details"]
    searchReportTestNav = ["Reports","Search report (testing)","Input"]
    searchReportTestTableNav = ["Reports","Search report (testing)","Input","Results"]
    searchContactPersonTableNav = ["Reporting Entities","Search contact person","Input","Results"]
    searchPersonsNav = ["Pesons","Search person","Input"]
    searchPersonsTableNav = ["Pesons","Search person","Input","Results","Details"]

    #SearhReport
    reportingEntityName = "NL Sample 123"
    typeOfReport = "Suspicious Transaction Report"
    submissionDateFrom = "07/22/2018"
    submissionDateTo = "04/05/2024"
    submissionDateAndTimeFrom = "07/22/2018 09:15:10 AM"
    submissionDateAndTimeTo = "04/05/2024 11:10:35 PM"

    #SaveGraphDiscardChangesMessage
    messageDiscardChanges =  "Are you sure you want to discard all changes done on the current graph?"
    pendingUpdates = "There are pending updates on the graph. Please process all updates first and then try saving the graph again."


    #SaveGraphName
    graphNames = ["Automation Test", "Regression Test", "WorkspaceTest"]

    #Queries
    addPropertyToTransactionNode = "g.V().has('transactionNumber', '123456789').has('entityId','ddc18108-2105-4513-bae4-cded5b3127a5').property('transmodeComment', 'Electronic','startTime', '2024-03-18T15:52:22','sourceType', 'manual','source', 'workspace testing').toList()"
    dropPropertyFromTransactionNode = "g.V().has('transactionNumber', '123456789').has('entityId','ddc18108-2105-4513-bae4-cded5b3127a5').properties('transmodeComment').hasValue('Electronic').property('endTime', '2024-03-18T16:52:22').toList()"
    addPropertyToReportNode = "g.V().has('reportId', 'DOS-EW-14222_trs3').property('fiuRefNumber', 'test number', 'startTime', '2024-03-18T15:52:22', 'sourceType', 'manual', 'source', 'workspace testing').toList()"
    dropPropertyFromReportNode = "g.V().has('reportId', 'DOS-EW-14222_trs3').properties('fiuRefNumber').hasValue('test number').property('endTime', '2024-03-18T16:52:22').toList()"

    addPropertyToEdge = "g.V().has('reportId', 'DOS-EW-14222_trs3').out('TRANSACTION').inE('FROM').property('outputSpentTotal', 1000).toList()"
    modifyPropertyInEdge = "g.V().has('reportId', 'DOS-EW-14222_trs3').out('TRANSACTION').inE('FROM').property('fundsCode', 'MTR').toList()"
    modifyPropertyBackToState = "g.V().has('reportId', 'DOS-EW-14222_trs3').out('TRANSACTION').inE('FROM').property('fundsCode', 'GIO').toList()"
    dropPropertyFromEdge = "g.V().has('reportId', 'DOS-EW-14222_trs3').out('TRANSACTION').inE('FROM').properties('outputSpentTotal').drop().toList()"

    dropCloseSimilarityEdges = "g.V().has('firstName', 'kasper').has('lastName', 'Starter').outE('CLOSE_SIMILARITY').drop().toList()"
    addNodeLinking = "g.V().has('firstName', 'kasper').has('lastName', 'Starter').as_('a').V().has('firstName', 'Wouter').as_('b').addE('CLOSE_SIMILARITY').property('lab', 'CLOSE_SIMILARITY').property('entityId', uuid.uuid4()).property('timestamp', '2026-03-18T12:33:44').property('source', 'workspace testing').property('distanceType', 'levenshtein').property('distance', 3).property('edgeType','link').from_('a').to('b').toList()"

    deleteMergedNodes = "g.V().has('firstName', 'JAN').has('sources', Text.text_contains_prefix('Cash')).outE('MERGED').drop().toList()"
    addBackTheMergedEdge1 = "g.V().has('firstName', 'JAN').has('sources', Text.text_contains_prefix('Cash')).where(__.out('ADDRESS').has('address', 'Weg 1')).as_('a').V().has('firstName', 'JAN').has('lastName', 'Persoon A').has('virtual').as_('b').addE('MERGED').property('lab', 'MERGED').property('entityId', uuid.uuid4()).property('timestamp', '2026-06-18T12:33:44').property('source', 'workspace testing').from_('a').to('b').toList()"
    addBackTheMergedEdge2 = "g.V().has('firstName', 'JAN').has('sources', Text.text_contains_prefix('Cash')).where(__.out('ADDRESS').has('address', 'Laan 7')).as_('a').V().has('firstName', 'JAN').has('lastName', 'Persoon A').has('virtual').as_('b').addE('MERGED').property('lab', 'MERGED').property('entityId', uuid.uuid4()).property('timestamp', '2026-06-18T12:33:44').property('source', 'workspace testing').from_('a').to('b').toList()"
    deleteNode = "g.V().has('reportId', 'Cash_withdrawal').out('TRANSACTION').out('INVOLVED').has('lab', 'account').drop().toList()"


    deleteNodeCreated = "g.V().has('lab','person').has('firstName','Testing').drop().toList()"