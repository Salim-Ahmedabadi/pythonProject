from configparser import ConfigParser
config=ConfigParser()
config.read("D:\\Selenium_Python\\TestData\\myconfig.cfg"))
print(config.get("BrowserInformation","browser_name"))
print(config.get("BrowserInformation","application_url"))
print(config.get("PersonalInfo", "firstname"))
