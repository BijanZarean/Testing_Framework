from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities.DataReader import DataReader
# Service classes for each browser are used to manage the respective driver executables.
# Options classes are for configuring browser-specific options.

# The Driver class provides a mechanism to manage WebDriver instances dynamically for different browsers.
# The get_driver method creates WebDriver instances based on the specified browser,
# The quit_driver method ensures proper cleanup by quitting the WebDriver instance when it's no longer needed.



class Driver:
    driver = None
    # Declaring a class variable driver and initializes it to None. 
    # This variable will hold the singleton WebDriver instance. 
    # Being a class variable, it is shared across all instances of the Driver class.
    
    @classmethod
    def get_driver(cls, browser_type=DataReader.get_property('browser')):
    # The first parameter, cls, refers to the class itself. 
    # get_driver takes an optional browser_type parameter, with a default value of 'chrome', 
    # allowing the caller to specify the browser type.
        
        if cls.driver is None:
        # Checks if the driver class variable is None, which would mean no WebDriver has been initialized yet. 
        # This is part of implementing a singleton pattern to ensure only one WebDriver instance is created.
        
            if browser_type == 'chrome':
                chrome_options = ChromeOptions()
                chrome_options.add_experimental_option("detach", True)
                cls.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
            # If the browser_type is set to 'chrome, 
            # creates an instance of ChromeOptions to configure browser-specific settings (like headless mode). 
            # It then initializes the Chrome WebDriver using ChromeService() and the options.
            
            elif browser_type == 'chrome-headless':
                chrome_options = ChromeOptions()
                chrome_options.add_argument('--headless')
                cls.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
            # For headless browsers, additional arguments are added to the options (e.g., --headless for Chrome and Firefox), 
            # configuring the browser to run without a GUI.
            
            elif browser_type == 'firefox':
                cls.driver = webdriver.Firefox(service=FirefoxService())
            elif browser_type == 'firefox-headless':
                firefox_options = FirefoxOptions()
                firefox_options.add_argument('--headless')
                cls.driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
            elif browser_type == 'safari':
                cls.driver = webdriver.Safari(service=SafariService())
            elif browser_type == 'edge':
                cls.driver = webdriver.Edge(service=EdgeService())
            else:
                # Default to headless Chrome if browser type is unknown.
                chrome_options = ChromeOptions()
                chrome_options.add_argument('--headless')
                cls.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        return cls.driver
        # Returns the initialized WebDriver instance.

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
    # Class method that quits the existing WebDriver instance (if any) by calling quit() on it and 
    # then resets the driver class variable to None. This ensures proper cleanup of the browser session.