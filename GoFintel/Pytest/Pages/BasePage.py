from datetime import datetime
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from gremlin_python.driver.aiohttp.transport import AiohttpTransport
from gremlin_python.process.graph_traversal import __
import uuid

# common imports listed on
# https://tinkerpop.apache.org/docs/3.7.0/reference/#gremlin-python-imports
from gremlin_python import statics
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import CardinalityValue
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import TextP
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.traversal import WithOptions

from janusgraph_python.driver.serializer import JanusGraphSONSerializersV3d0
from janusgraph_python.process.traversal import Text

from Tests import conftest

#This calss is the parent of all pages
#it contains all the generic methods and utilities for all the pages

class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.os = platform.system()

    def do_click(self, by_locator):
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(by_locator)).click()
        self.wait_until_page_loads()

    def is_element_clickable(self, by_locator):
        try:
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(by_locator))
            return True
        except:
            return False


    def do_click_element(self, by_element):
        WebDriverWait(self.driver,5).until(EC.visibility_of(by_element))
        by_element.click()
        self.wait_until_page_loads()

    def do_clear(self, by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))  
        ele.clear()
        ele.click()

    def do_Enter_Text(self, by_locator, text):
        ele = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(by_locator))
        ele.clear()
        ele.send_keys(text)

    def do_select_value(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()
        self.wait_until_page_loads()

    def get_Element_Text(self, by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return ele.text
    
    def get_Attribute_Value(self, by_locator, from_attribute):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return ele.get_attribute(from_attribute)
    
    def get_Text_Value(self, by_locator):
        try:
            ele = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(by_locator))
            return ele.text
        except:
            return ""
    
    def wait_until_page_loads(self):
        loaderImage = (By.XPATH,"//div[@class='loader']/div[@class='p-progress-spinner']")
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loaderImage))

    def get_Element(self, by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return ele
    
    def get_Elements(self, by_locator):
        eles = self.driver.find_elements(*by_locator)
        return eles
    
    def is_ElementExist(self, by_locator):
        try:
            ele = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def get_Element_count(self, by_locator):
        try:
            WebDriverWait(self.driver,1).until(EC.visibility_of_element_located(by_locator))
            eles = self.driver.find_elements(*by_locator)
            ele_count = len(eles)
            return ele_count
        except:
            ele_count = 0
            return ele_count
    
    def get_Title(self, title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))   
        return self.driver.title
    
    def get_Element_X_Coordinate(self,by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        location = ele.location
        return location.get('x')
    
    def get_Element_Y_Coordinate(self,by_locator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        location = ele.location
        return location.get('y')
    
    def get_chartData(self):
        chart_data = self.driver.execute_script('return window.chartData')
        jsonFormat= json.dumps(chart_data)
        jsonObject = json.loads(jsonFormat)
        return jsonObject
    
    def do_select_GivenNode(self, nodeType, nodeLabel, actionType):
        action = ActionChains(self.driver)
        jsonObject = self.get_chartData()
        infIconInGraph = (By.XPATH,"//span[contains(@class,'question-circle')]")
        searchInGraph = (By.XPATH,"//span[contains(@class,'search')]")
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                if ((nodeLabel.lower() in str(node["labelValue"]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(node["labelValue"])))==nodeLabel) and (nodeType.lower() in str(node["label"]).lower() or nodeType=="")):
                    canvasXCoordinate = self.get_Element_X_Coordinate(self.canvasElement)
                    canvasYCoordinate = self.get_Element_Y_Coordinate(self.canvasElement)+7 #Adding 7 to peform the clik on the center of the node
                    newXcoordinate = node["x"]
                    newYcoordinate = node["y"]
                    searchElementYCoordinate = self.get_Element_Y_Coordinate(searchInGraph)
                    infoIconYCoordinate = self.get_Element_Y_Coordinate(infIconInGraph)
                    if(canvasYCoordinate+newYcoordinate > searchElementYCoordinate+50 or canvasYCoordinate+newYcoordinate < infoIconYCoordinate-50):
                        if(canvasYCoordinate+newYcoordinate > searchElementYCoordinate+50):
                            scrollingLength = canvasYCoordinate+newYcoordinate - searchElementYCoordinate
                        elif(canvasYCoordinate+newYcoordinate < infoIconYCoordinate-5):         
                            scrollingLength = canvasYCoordinate+newYcoordinate - infoIconYCoordinate
                        action.move_by_offset(50,0).click_and_hold().move_by_offset(0,-scrollingLength).release().perform()
                        time.sleep(1)
                        action.move_by_offset(-50,0).perform()
                        time.sleep(1)
                        if(actionType=="doubleClick"):
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).double_click().perform()
                            time.sleep(1)
                            #action.move_by_offset(0,0).double_click().perform()
                        elif(actionType=="Click"):
                            time.sleep(15)
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                            time.sleep(2)
                        else:
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                            time.sleep(1)
                            action.move_by_offset(0,0).click().perform()

                        action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()
                        
                    else:
                        if(actionType=="doubleClick"):
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                            time.sleep(1)
                            action.move_by_offset(0,0).double_click().perform()
                        elif(actionType=="Click"):
                            time.sleep(3)
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                            time.sleep(2)
                        else:
                            action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                            time.sleep(1)
                            action.move_by_offset(0,0).click().perform()  

                        action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()
                    break

    def do_click_GivenNode(self, nodeType, nodeLabel, actionType):
        action = ActionChains(self.driver)
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                if ((nodeLabel.lower() in str(node["labelValue"]).lower() or nodeLabel=="" or ''.join(filter(str.isdigit, ''.join(node["labelValue"])))==nodeLabel) and (nodeType.lower() in str(node["label"]).lower() or nodeType=="")):
                    canvasXCoordinate = self.get_Element_X_Coordinate(self.canvasElement)
                    canvasYCoordinate = self.get_Element_Y_Coordinate(self.canvasElement)-20 #Adding -20 to peform the clik on the center of the node
                    newXcoordinate = node["x"]
                    newYcoordinate = node["y"]

                    if(actionType=="doubleClick"):
                        action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).double_click().perform()
                        time.sleep(1)
                        #action.move_by_offset(0,0).double_click().perform()
                    elif(actionType=="Click"):
                        time.sleep(3)
                        action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                        time.sleep(2)
                    else:
                        action.move_by_offset(canvasXCoordinate+newXcoordinate,canvasYCoordinate+newYcoordinate).click().perform()
                        time.sleep(1)
                        action.move_by_offset(0,0).click().perform()  

                    action.move_by_offset(-(canvasXCoordinate+newXcoordinate),-(canvasYCoordinate+newYcoordinate)).perform()

    def getFirstNodeLabel(self):
        jsonObject = self.get_chartData()
        for node in jsonObject["nodes"]:
            if not "isHide" in node:
                return str(node["labelValue"])
                
    def do_select_calendar_date(self,by_locator,input,by_highlightedDate):
        calendarYear = (By.XPATH,"//button[@data-pc-section='yeartitle']")
        counter = 0
        while True:
            eleCount = len(self.get_Elements(by_highlightedDate))
            self.do_click(by_locator)
            ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
            ele.send_keys(input)
            time.sleep(1)
            counter += 1
            if counter >= 10 or len(self.get_Elements(by_highlightedDate)) == eleCount+1:
                break
            else:
                ele.clear()
                time.sleep(1)
        ele = self.get_Elements(by_highlightedDate)
        self.do_click_element(ele[len(ele)-1])
        time.sleep(1)
        ele = self.get_Elements(by_highlightedDate)
        self.do_click_element(ele[len(ele)-1])
        time.sleep(1)

    def extract_year(date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")
        return date_obj.year

    def do_select_Year(self,givenValue):
        firstValueInPicker = (By.XPATH,"//span[contains(@class,'yearpicker')][1]")
        lastValueInPicker = (By.XPATH,"//span[contains(@class,'yearpicker')][10]")
        yearInPast = (By.XPATH,"//button[contains(@class,'datepicker-prev')]")
        yearInFuture = (By.XPATH,"//button[contains(@class,'datepicker-next')]")
        yearPicker = (By.XPATH,"//div[contains(@class,'yearpicker')]/span[text()='"+givenValue+"']")
        for i in range(10):
            startValue = self.get_Element_Text(firstValueInPicker)
            endValue = self.get_Element_Text(lastValueInPicker)
            if(int(startValue)>int(givenValue)):
                self.do_click(yearInPast)
            elif(int(givenValue)>int(endValue)):
                self.do_click(yearInFuture)
            else:
                self.do_click(yearPicker)
                break
    
    def get_ctrl_key(self):
        if self.os == 'Darwin':
            return Keys.COMMAND
        else:
            return Keys.CONTROL
        
    def get_action_class(self):
        action = ActionChains(self.driver)
        return action
    
    def get_open_tabs_count(self):
        tabCount = len(self.driver.window_handles)
        return tabCount
    
    def verify_date_format(self, date_string, date_format):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            print("Expected Date format :"+date_format+" Actual Date format :"+date_string)
            return False
    
    def take_mouse_to_origin(self):
        homelink = (By.XPATH,"//li[contains(@class,'breadcrumb')]//span[contains(@class,'home')]")
        actions = self.get_action_class()
        actions.move_to_element(self.get_Element(homelink)).perform()
        actions.move_by_offset(-262,-77).perform()

    def do_browser_back_navigation(self):
        self.driver.back()

    def execute_gremlin_query(self,Query):        
        g = traversal().withRemote(
                DriverRemoteConnection(
                    conftest.graphHost,
                    'gp_traversal',
                    username='jg_user',
                    password='jg_password',
                    pool_size=1,
                    message_serializer=JanusGraphSONSerializersV3d0(),
                    transport_factory=lambda:AiohttpTransport(call_from_event_loop=True)
                )
            )
        result = eval(Query)
        print("Query result:", result)


    def addNode(self):        
        g = traversal().withRemote(
                DriverRemoteConnection(
                    conftest.graphHost,
                    'gp_traversal',
                    username='jg_user',
                    password='jg_password',
                    pool_size=1,
                    message_serializer=JanusGraphSONSerializersV3d0(),
                    transport_factory=lambda:AiohttpTransport(call_from_event_loop=True)
                )
            )
        
        """ new_node = g.addV('person').property('lab','person')\
            .property('firstName', 'Testing')\
            .property('lastName', 'Node')\
            .property('entityId', uuid.uuid4())\
            .property('sources', 'workspace testing')\
            .property('birthDate','1992-06-18')\
            .toList() """
        
        new_node = g.addV('account').property('lab','account')\
            .property('account', 'NL00BANK123456789')\
            .property('entityId', uuid.uuid4())\
            .property('sources', 'workspace testing')\
            .property('swift','BANK01')\
            .property('institutionName','BANK')\
            .toList()

        involvedEdge = g.V().has('account', 'NL00BANK123456789').has('sources', 'workspace testing').as_('a')\
            .V().has('lab','transaction').has('sources', Text.text_contains('withdrawal')).as_('b')\
                .addE('INVOLVED')\
                    .property('lab', 'INVOLVED')\
                    .property('timestamp', '2026-06-18T12:33:44')\
                    .property('role', 'B')\
                    .property('fundsCode', 'BCR')\
                    .property('source', 'workspace testing')\
                    .property('entityId', uuid.uuid4())\
                    .from_('b').to('a').toList()
        
        """ signatoryEdge = g.V().has('account', 'NL00BANK123456789').has('sources', 'workspace testing').as_('a')\
            .V().has('lab','person').has('firstName','JAN').has('lastName','Persoon A').has('sources','	person_merging').as_('b')\
                .addE('SIGNATORY')\
                    .property('lab', 'SIGNATORY')\
                    .property('timestamp', '2026-06-18T12:33:44')\
                    .property('role', '1')\
                    .property('isPrimary', 'true')\
                    .property('source', 'workspace testing')\
                    .property('entityId', uuid.uuid4())\
                    .property('distanceType', 'levenshtein')\
                    .property('distance', 3)\
                    .property('edgeType','link')\
                    .from_('a').to('b').toList() """
        
