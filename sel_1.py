
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome()

driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium python")

time.sleep(5)  # wait 5 seconds
search.submit()

time.sleep(10)

driver.back()
time.sleep(5)
driver.forward()
time.sleep(50)


