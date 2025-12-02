from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()

time.sleep(3)

# Login
driver.find_element(By.ID, "email").send_keys("gmail.com")
driver.find_element(By.ID, "pass").send_keys("12456378@")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@data-testid='royal-login-button']").click()

time.sleep(5)


post_box = driver.find_element(By.XPATH, "//div[@aria-label='Create a post']")
post_box.click()

time.sleep(3)

# Type message
textbox = driver.find_element(By.XPATH, "//div[@role='textbox']")
textbox.send_keys("This is an automated post using Selenium!")

time.sleep(2)

# Click Post button
post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
post_button.click()

time.sleep(5)
