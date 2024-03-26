# fixture and use_fixture functions are used to define and apply fixtures in Behave.
from behave import fixture, use_fixture
# is used to manage the WebDriver instance.
from utilities.Driver import Driver
# is used for explicit waits in Selenium.
from selenium.webdriver.support.ui import WebDriverWait
import os
from datetime import datetime
import allure


# Fixture for setup and teardown
@fixture
def browser_setup(context):
    # Setup
    #print("This is before hook")
    context.driver = Driver.get_driver()  # Get the WebDriver instance
    context.driver.maximize_window()
    # Maximize the browser window
    context.driver.implicitly_wait(5)  
    # Set implicit wait time

    # Pass the driver to the scenario context
    # The setup phase (before yield) includes actions to be performed before each scenario, 
    # such as initializing the WebDriver instance, maximizing the browser window, and setting implicit wait time.
    yield context.driver
    # The teardown phase (after yield) includes actions to be performed after each scenario, 
    # such as taking a screenshot if the scenario fails and quitting the WebDriver instance.

    # Teardown
    
    if context.failed:
         # Define directory and file name for screenshot
        screenshots_directory = "/Users/bijanzarean-work/Documents/Project/Testing_Framework/screenshots"
        if not os.path.exists(screenshots_directory):
            os.makedirs(screenshots_directory)
        filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        filepath = os.path.join(screenshots_directory, filename)
        
        # Take a screenshot and save to the defined filepath
        context.driver.save_screenshot(filepath)
        
        # Attach the screenshot to the Allure report
        allure.attach.file(filepath, name="Screenshot on Failure", attachment_type=allure.attachment_type.PNG)
   
    Driver.quit_driver()
    # Quit the driver, comment this out and the browser wont close after a run

def before_all(context):
    use_fixture(browser_setup, context)
    # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
    # Register the fixture
