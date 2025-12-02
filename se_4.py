from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

time.sleep(3)  # wait for page to load

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("iphone")

time.sleep(1)

driver.find_element(By.ID, "nav-search-submit-button").click()

time.sleep(5)
