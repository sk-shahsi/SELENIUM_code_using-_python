from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("iphone")
driver.find_element(By.ID, "nav-search-submit-button").click()
time.sleep(4)

products = driver.find_elements(
    By.XPATH,
    "//div[contains(@class,'s-result-item') and @data-component-type='s-search-result']"
)

print("Total products found:", len(products))

for i, p in enumerate(products, start=1):

#TITLE
    title = "No title"
    try:
        title = p.find_element(By.XPATH, ".//span[not(@class)]").text
    except:
        pass

#PRICE
    try:
        price = p.find_element(By.CSS_SELECTOR, ".a-price-whole").text
    except:
        price = "No price"

    print(f"\nProduct #{i}")
    print("Title:", title)
    print("Price:", price)
