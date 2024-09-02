## Running the tests 

For running the tests follow the below steps:

1. make sure you have at least python 3.9 installed
2. install Google Chrome and check its version
3. download ChromeDriver based on your OS from here: https://sites.google.com/chromium.org/driver/downloads (make sure that the major version of the driver is the same as the major version of the installed Google Chrome)
4. create a python virtual environment:
   1. on Windows: `python -m venv .venv`
   2. on Linux/Mac: `python -m venv .venv`
5. activate the virtual environment:
   1. on Windows: `.venv\Scripts\activate`
   2. on Linux/Mac: `source .venv/bin/activate`
6. install the packages: `pip install -r requirements.txt`


You can run the tests with the following command
`pytest Tests -v -s  --url=http://10.208.75.11:3000/realms/goFintel --chrome_driver_path=C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe --headless=No --graph_host=ws://10.208.75.11:8182/gremlin --airflow_url=http://qa.gofintel.local:8081/home --airflow_user=airflow --airflow_password=12password34changeMe`

To run in headeless mode  `pytest Tests -v -s  --url=http://10.208.75.11:3000/realms/goFintel --chrome_driver_path=C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe --headless=Yes --graph_host=ws://10.208.75.11:8182/gremlin --airflow_url=http://qa.gofintel.local:8081/home --airflow_user=airflow --airflow_password=12password34changeMe`

Or you can run only a specific unit test with:
`python3 -m pytest Tests/test_HomePage.py -v --chrome_driver_path=C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe --headless=No --graph_host=ws://10.208.75.11:8182/gremlin --airflow_url=http://qa.gofintel.local:8081/home --airflow_user=airflow --airflow_password=12password34changeMe`
`pytest Tests/test_Reports.py -v -s --url=http://qa.gofintel.local:3000 --chrome_driver_path=C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe --headless=No --graph_host=ws://10.208.75.11:8182/gremlin --airflow_url=http://qa.gofintel.local:8081/home --airflow_user=airflow --airflow_password=12password34changeMe`

To run in headless mode  `pytest Tests -v -s --url=http://qa.gofintel.local:3000 --chrome_driver_path=C:\\GoFintelAutomationSuite\\chromedriver-win64\\chromedriver.exe --headless=Yes --graph_host=ws://10.208.75.11:8182/gremlin --airflow_url=http://qa.gofintel.local:8081/home --airflow_user=airflow --airflow_password=12password34changeMe` 

Following arguments are mandatory while executing the tests.
1. --chrome_driver_path (Chome driver path, which was downloaded in step 3)
2. --graph_host (The graph server, this is to update the nodes and edges during the test)
3. --airflow_url,--airflow_user,--airflow_password(Airflow url and credentails of an environment for which the test going to be executed, this is to run the dag's)

Other arguments 
1. --url (If not given, test will be executed in QA env by default)
2. --headless (If not given, it will be considered as "No" by default)