from selenium.webdriver import Chrome
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
print(driver.set_page_load_timeout)
print(driver.find_element_by_name("login").text)
print(driver.find_element_by_name("login").get_attribute("type"))
driver.close()