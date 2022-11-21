from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_link_text("Shop")
shop.click()

html5_webapp_development = driver.find_element_by_css_selector(".post-182 .button")
html5_webapp_development.click()
time.sleep(3)

basket_items = driver.find_element_by_css_selector("#wpmenucartli .cartcontents")
basket_items_get_text = basket_items.text
assert basket_items_get_text == "1 Item"

basket_price = driver.find_element_by_css_selector("#wpmenucartli .amount")
basket_price_get_text = basket_price.text
assert basket_price_get_text == "₹180.00"

basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()

subtotal_price = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-subtotal span"))
)

total_price = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".order-total span"))
)

driver.quit()