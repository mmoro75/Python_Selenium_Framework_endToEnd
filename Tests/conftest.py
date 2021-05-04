import pytest
import selenium
from _pytest.outcomes import xfail
from selenium import webdriver

driver = None  # initialize driver variable as none


# the below code is to set up options in command line to call specific browser by command when running tests( default is chrome)
# i.e py.test --browser_name firefox
############## see documentation at #################
#  https://docs.pytest.org/en/stable/example/simple.html#how-to-change-command-line-options-defaults
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome, firefox or IE"
    )


@pytest.fixture(scope="class")  # configuring browser invoke to be use in multiple tests
def setUp(request):
    global driver  # now driver is available for html screenshot code below
    browser_name = request.config.getoption("browser_name")  # get option from command py.test
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\geckodriver.exe")

    elif browser_name == "Ie":
        driver = webdriver.Ie(executable_path="C:\\Users\\u6017127\\Documents\\Eikon\\Project\\TestPython\\IE")
    #            print("internet explorer not available at the moment")
    driver.get("https://rahulshettyacademy.com/angularpractice")
    request.cls.driver = driver  # assign driver object to class level using request feature of pytest fixture ( now driver is a class variable so it has to be defined as slef.driver in tests)
    # setting up teardown as well by using keyword yield = code will be executed after test cases is completed
    yield
    driver.close()


#  to get HTML report install -pip install htmlreport and run the command py.test --html=report.html
    # to store report in a specific path just pass it ove form command like:
     # py.test - -html = c:\user\u6017127\reports\report.html


### the code below is to include screenshot into HTML report #######################


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



################################### For Jenkins integration to run yout test and get junit result ##################

# download jenkins at: https://www.jenkins.io/download/
   # to start jenkins java -jar jenkins.war http=8081
       # brose localhost/8081 to start jenkins
          # start new job

## py.test --browser_name "$Browser_name" --html =$WORKSPACE/reports/report.html -v --junitxml=result.xml  #

      # "$Browser_name" is the variable configured in jenkins as parametrized options
      # env variable $WORKSPACE is the one configured in jebkins ad mainpath
      # junit xml is to publish the result in main page with jenking in Post built actions -> junit report
