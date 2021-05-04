# Test case is developed using Page object design meaning each page for our webiste correspond to a Class
# such Page Objects Class contains all the element as object that can be recalled during test scrips
import logging

import pytest
import openpyxl
import selenium
from selenium import webdriver  # import webdriver from selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass  #import BaseClass to inherit setup fixture for your test
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage

class TestSubmitForm(BaseClass):  # using BaseClass inheritance the script will have the knowledge of sutup browser defined in the BaseClass

   def test_submitForm(self,getData): # getting data defined in homepage for parametrized data

       log = self.getLogger() ## to call logging from inherited BaseClass
       homepage = HomePage(self.driver)

       log.info(f"setting up name as:  {getData[0]}")
       homepage.getName().send_keys(getData[0])  # getting data index for the values defined in homepage getData
       log.info(f"setting up email as: {getData[1]}")
       homepage.getEmail().send_keys(getData[1])
       log.info(f"setting up password as: {getData[2]}")
       homepage.getPassword().send_keys(getData[2])
       log.info(f"setting up gender as: {getData[3]}")
       self.getGender(getData[3])
       self.driver.find_element_by_xpath("//input[@type='submit']").click()
       # homepage.submit().click()
       # alertMes = homepage.alert().text
       alertMes = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
       log.info("test from application is: " +alertMes)
       assert ("Success!" in alertMes)
       self.driver.refresh()

   ## for parametrized test to use multiple data we can use pytest fixturs and put the code where multiple data is needed
   ## not good practice to put it in configtest as not all the tests require multiple data

   @pytest.fixture(params=[("Marco", "marco.moro1@gmail", "1234", "Male"),
                           ("Gino", "Gino@gmail.com", "1234", "Female")])  # define data set
   def getData(self, request):
       return request.param  # return params


'''
#### sing data from spreadsheet - as method is static it can be executed as follow
@pytest.fixture(params=HomePage.getTestDataExl("Testcase1"))
def getData(request):
    return request.param  # return params

'''
        


