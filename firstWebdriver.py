from selenium.webdriver import Chrome
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.close()

