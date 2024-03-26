import configparser
# Built in Python module for parsing configuration files

class DataReader:
    config = configparser.ConfigParser()
    # Creating an instance of the ConfigParser class
    config.read('./resources/TestData/env.properties') # Path to properties file
    # The read method of the ConfigParser class used to read and parse the contents of a configuration file
    
    
    @staticmethod
    def get_property(key):
        return DataReader.config.get('DEFAULT', key)
        # Returning the instance (config) of the ConfigParser class which is calling the get method,
        # used to retrieve a the value associated with a specific key
        
# Reads the env.properties file, currently located in ./resources/TestData/env.properties, 
# looking for the provided key and returning the value