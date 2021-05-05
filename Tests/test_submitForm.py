# Test case is developed using Page object design meaning each page for our webiste correspond to a Class
# such Page Objects Class contains all the element as object that can be recalled during test scrips
import logging

import pytest
from utilities.BaseClass import BaseClass  #import BaseClass to inherit setup fixture for your test
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage

class TestSubmitForm(BaseClass):  # using BaseClass inheritance the script will have the knowledge of sutup browser defined in the BaseClass

   def test_submitForm(self,getData): # getting data defined in homepage for parametrized data

       log = self.getLogger() ## to call logging from inherited BaseClass
       homepage = HomePage(self.driver)

       log.info(f"setting up name as: {getData['firstname']}")
       homepage.getName().send_keys(getData['firstname'])  # getting data index for the values defined in homepage getData
       log.info(f"setting up email as: {getData['email']}")
       homepage.getEmail().send_keys(getData["email"])
       log.info(f"setting up password as: {getData['password']}")
       homepage.getPassword().send_keys(getData['password'])
       log.info(f"setting up gender as: {getData['gender']}")
       self.getGender(getData['gender'])
       self.driver.find_element_by_xpath("//input[@type='submit']").click()
       # homepage.submit().click()
       # alertMes = homepage.alert().text
       alertMes = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
       log.info("test from application is: " +alertMes)
       assert ("Success!" in alertMes)
       self.driver.refresh()

   ## for parametrized test to use multiple data we can use pytest fixturs and put the code where multiple data is needed
   ## not good practice to put it in configtest as not all the tests require multiple data

   @pytest.fixture(params=HomePage.SubmitFormData)  # using data set from HomePage
   def getData(self, request):
       return request.param  # return params



'''
#### sing data from spreadsheet - as method is static it can be executed as follow
@pytest.fixture(params=HomePage.getTestDataExl("Testcase1"))
def getData(request):
    return request.param  # return params
    
'''


        


