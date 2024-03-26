from behave import given, when, then
from pages.EcommercePracticeHomePage import EcommercePracticeHomePage
from utilities.Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.DataReader import DataReader


class SearchSteps:
    

    @given('I am on the Home page')
    def step_impl(context):
        context.home_page = EcommercePracticeHomePage()
        context.driver = Driver.get_driver()
        context.driver.get(DataReader.get_property('website'))

    @when('I enter "{search_term}" in the search field')
    def step_impl(context, search_term):
       context.home_page.searchField.send_keys(search_term)

    @when('click on the search button')
    def step_impl(context):
        context.home_page.searchBTN.click()
        
    @then('I should see a list of results')
    def step_impl(context):
        assert context.home_page.searchTab.is_displayed(), 'Failed'
        assert context.home_page.iPhoneProduct.is_displayed(), 'Failed'