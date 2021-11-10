from selenium.webdriver import Chrome
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.set_page_load_timeout(300)
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element_by_link_text("Create New Account").click()
#driver.sleep(20) #fixed wait
driver.find_element_by_name("firstname").send_keys("Python")
#driver.close()
