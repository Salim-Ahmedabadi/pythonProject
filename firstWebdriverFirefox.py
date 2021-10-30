from selenium.webdriver import Firefox
path=""
driver=Firefox(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.close()
