# is used for explicit waits in Selenium.
from selenium.webdriver.support.ui import WebDriverWait
# provides commonly used expected conditions to wait for in Selenium.
from selenium.webdriver.support import expected_conditions as EC
# provides methods for locating elements by different strategies.
from selenium.webdriver.common.by import By
# managing WebDriver instances
from utilities.Driver import Driver


class EcommercePracticeHomePage:
    # Constructor of page class that creates instance variable and returns a WebDriver instance
    def __init__(self):
        self.driver = Driver.get_driver()

    # This method waits until the element located by the specified locator is visible on the web page.
    # It waits for a maximum of 10 seconds (specified by WebDriverWait), after which it raises a TimeoutException
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    

    # @property: This decorator allows defining properties with getter methods
    @property
    def searchField(self):
        return self.wait_for_element((By.NAME, "search"))
    
    @property
    def searchBTN(self):
        return self.wait_for_element((By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]"))
    
    @property
    def searchTab(self):
        return self.wait_for_element((By.XPATH, "//a[contains(text(),'Search')]"))
    
    @property
    def iPhoneProduct(self):
        return self.wait_for_element((By.XPATH, "//a[contains(text(),'iPhone')]"))