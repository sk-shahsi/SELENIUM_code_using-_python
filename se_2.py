from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

driver.maximize_window()
time.sleep(5)

select = driver.find_element(By.PARTIAL_LINK_TEXT, "Today's Deals")

time.sleep(5)
select.click()
time.sleep(5)
select_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "All Deals")
time.sleep(5)
select_1.click()
time.sleep(5)




time.sleep(50)


