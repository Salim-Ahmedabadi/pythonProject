from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=""
driver=Chrome(executable_path=path)
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.find_element_by_id("email").send_keys(("salimkk780@gmail.com")
act=ActionChains(driver)
act.send_keys("salimkk780@gmail.com").perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.DELETE).perform()
act.key_down(Keys.SHIFT).send_keys("+").key_up(Keys.SHIFT).perform()
act.send_keys(Keys.TAB).perform()
act.send_keys("pass123").perform
driver.close()


