import configparser
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class configFileHandler():

    def configFileParser(configParam):
        try:
            config = configparser.ConfigParser()
            config.sections()
            config.read('/Users/tml/Desktop/Automation_Projects/Python_Project/PythonSelFramework/Config/config.ini')
            return config.get('SectionOne',configParam)

        except Exception as ex:
            logging.error("Error while reading value from Config")
            logging.error(ex)

