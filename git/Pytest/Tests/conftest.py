import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.service import Service as ChromeService

def pytest_addoption(parser):
    parser.addoption(
        '--url', action='store', default="http://qa.gofintel.local:3000/", help='Application URL for test execution'
    )
    parser.addoption(
        '--chrome_driver_path', action='store', help='Chrome Driver path to invoke browser' #,default="C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe"
    )

    parser.addoption(
        '--headless', action='store', default='no', help='Invokes headless chrome browser'
    )

    parser.addoption(
        '--graph_host', action='store', help='Graph server to execute the gramlin queries'#, default="ws://10.208.75.11:8182/gremlin" 
    )

    parser.addoption(
        '--airflow_url', action='store', help='airflow url to executed the dag'#, default="http://qa.gofintel.local:8081/home" 
    )

    parser.addoption(
        '--airflow_user', action='store', help='airflow user name to login'#, default="airflow"
    )

    parser.addoption(
        '--airflow_password', action='store', help='airflow password to login'#, default="12password34changeMe"
    )


@pytest.fixture(params =["chrome"],scope='class',autouse=True)
def init_driver(request):
    import os
    global BASE_DIR
    global graphHost,airflowURL,airflowUserName,airflowPassword
    BASE_DIR = os.getcwd() #os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    global driver
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        print(BASE_DIR)
        p = {'download.default_directory': os.path.join(BASE_DIR,'ReportDownloads')}
        print(p)
        """ options.add_experimental_option("prefs", {
            "download.default_directory": os.path.join(BASE_DIR,'ReportDownloads'),  # Set your desired download directory
            "safebrowsing.enabled": False
        }) """
        options.add_experimental_option('prefs', p)  
        options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
        options.add_argument('--window-size=1920,1080')
        if(request.config.getoption('--headless').lower() == "yes"):
            options.add_argument('--headless')
        chrome_driver_path = request.config.getoption('--chrome_driver_path')
        #chrome_driver_path = "C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe"
        chrome_service = ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(options=options,service = chrome_service)     

    print(request.config.getoption('--url'))
    if request.param == "firefox":
        driver = webdriver.Firefox()

    graphHost = request.config.getoption("--graph_host")
    airflowURL = request.config.getoption("--airflow_url")
    airflowUserName = request.config.getoption("--airflow_user")
    airflowPassword = request.config.getoption("--airflow_password")

    if not graphHost or graphHost == "no":
        pytest.exit("Error: --graph_host argument is required to execute gremlin queries")

    if airflowURL == "no" or airflowUserName == "no" or airflowPassword == "no":
        pytest.exit("Error: --airflow_url,airflow_user and airflow_password arguments are required to to trigger the dag")

    if chrome_driver_path=="no":
        pytest.exit("Error: --chrome_driver_path is needed")
        
    driver.maximize_window()
    #driver.implicitly_wait(1)
    driver.set_page_load_timeout(10)
    driver.get(request.config.getoption('--url'))
    request.cls.driver = driver
    yield
    driver.close() 

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    import os
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        """ if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file) """

        if (report.skipped and xfail) or (report.failed and not xfail) or (report.passed):
            # add the screenshots to the html report
            file_name = report.nodeid.replace("::","_")+".png"
            file_name=file_name.replace("Tests/","")
            file_name=file_name.replace(".py","-")
            sceenshotPath = os.path.join(BASE_DIR,'Screenshots',file_name)
            _capture_screenshot(sceenshotPath)
            if sceenshotPath:
                html='<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '\
                     'onclick="window.open(this.src)" align="right"/></div>' % sceenshotPath 
            extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)