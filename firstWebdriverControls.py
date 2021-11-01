from selenium.webdriver import Chrome
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.amazon.com/")
driver.maximize_window()

#Amazon
driver.find_element_by_id("twotabsearchtextbox").send_keys("Apple iphone")
driver.find_element_by_css_selector("[type='submit']").click()

#testingworld
