from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()


driver = webdriver.Chrome()
driver.get("https://www.google.com")



search = driver.find_element(By.NAME, "q")
search.send_keys("selenium python")
time.sleep(3)
search.submit()
time.sleep(50)


# button = driver.find_element(By.NAME, "btnK")
# button.click()
