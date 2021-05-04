import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
import logging
import inspect


@pytest.mark.usefixtures("setUp")
class BaseClass:   # we can use Case Class to define utilities that can be used in our test and just call them when needed

#### Utilities to be used in Tests where is needed
 def verifyLinkPrsence(self,text): # we are passing text to verify on test execution no longer hardcoded
    wait = WebDriverWait(self.driver, 9)

    wait.until(expected_conditions.presence_of_element_located(
        (By.LINK_TEXT, text)))  # text tobe verified

 def getGender(self,text):
     dropdown = Select(self.driver.find_element_by_id(
         "exampleFormControlSelect1"))  # create objcet dropdown and using select function give locator as argument

     dropdown.select_by_visible_text(text)  # by using object select the option you want


 ####### logging - we define logging code into BaseClasse to be used where is needed into test cases by calling getLogger method######

 def getLogger(self):
     loggerName = inspect.stack()[1][3]  # to get test name from each script
     logger = logging.getLogger(loggerName)  # pass it over to get logger

     fileHandler = logging.FileHandler("logfile.log")
     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
     fileHandler.setFormatter(formatter)
     logger.addHandler(fileHandler)

     logger.setLevel(logging.DEBUG)
     return logger


