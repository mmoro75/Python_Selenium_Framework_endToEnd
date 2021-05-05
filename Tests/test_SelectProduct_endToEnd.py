# Test case is developed using Page object design meaning each page for our webiste correspond to a Class
# such Page Objects Class contains all the element as object that can be recalled during test scrips

from utilities.BaseClass import BaseClass  #import BaseClass to inherit setup fixture for your test
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckOutPage

class TestOne(BaseClass):  # using BaseClass inheritance the script will have the knowledge of sutup browser defined in the BaseClass
  def test_SelectProduct(self):

       homepage = HomePage(self.driver) # I am now creating an object for homepage class
       homepage.shopItems().click() # now I can access the methods in HomePage class using the object
       chekout = CheckOutPage(self.driver)
       products = chekout.getProducts()

        # now grab all the products ( we are now using Xpath to get the entire product elements including text and add button

       for product in products: # loop into products
        # now in the loop let's move to child to extract the text = "//div[@class='card h-100']/div/h4/a"
            productName = self.driver.find_element_by_xpath("//div[@class='card h-100']/div/h4/a").text
           # productName = chekout.productName.text
            if productName == "Blackberry":
              # only when product is Blackbuarrys add to card
                # now move locator to add in the product list = "//div[@class='card h-100']/div[2]/button
                chekout.product().click() # add in the list

       self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click() # now click on checkout
       self.driver.find_element_by_css_selector("button[class='btn btn-success']").click() # to land to final page

       self.driver.find_element_by_id("country").send_keys("it") # search for country

       self.verifyLinkPrsence("Italy") # I can use the method in BaseClass as the Class is already inherited in this test and I am passing the text
      # wait = WebDriverWait(self.driver,9) # with implicti wait stop 7 second to wait forthe options to be displayed
      # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"Italy")))  # wait until the element is pesent in thelist

       self.driver.find_element_by_link_text("Italy").click() # select italy option

       self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click() # acceptterm and conditions

       self.driver.find_element_by_css_selector("[type='submit']").click() # submit

       mess = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text

       assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in mess

