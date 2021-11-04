from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path=""
driver=Chrome(executable_path=path)
driver.get("https://output.jsbin.com/osebed/2")
obj=Select(driver.find_element_by_css_selector("[value='apple']"))
obj.select_by_value("banana")

obj=Select(driver.find_element_by_name("sex"))
obj.deselect_by_visible_text("Male")
obj.select_by_value("2")
obj.select_by_index(1)

driver.close()