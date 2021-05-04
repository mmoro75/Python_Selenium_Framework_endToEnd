# home page class containing all the objects for our website home to be used in test script
from selenium.webdriver.common.by import By

class CheckOutPage:

    def __init__(self, driver):   # the constructor method will be initialized at object creation and diver will be called from test script
        self.driver = driver

    products = (By.XPATH,"//div[@class='card h-100']") # shop object created by using objcet syntax tuple containing locator and element
    productName = (By.XPATH,"//div[@class='card h-100']/div/h4/a")
    product = (By.XPATH,"//div[@class='card h-100']/div/button")
    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)  # to deconstruct tuple passed as class variable use * at beginning
        #### the above step it would represent the self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    def productName(self):
        return self.driver.find_element(*CheckOutPage.productName)
        # the above step it would represent product.find_element_by_xpath("div/h4/a")
    def getProduct(self):
        return self.driver.find_element(*CheckOutPage.product)