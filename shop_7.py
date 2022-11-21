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

driver.execute_script("window.scrollBy(0, 300);")

html5_webapp_development = driver.find_element_by_css_selector(".post-182 .button")
html5_webapp_development.click()
time.sleep(3)

basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()

proceed_to_checkout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
)
proceed_to_checkout.click()

all_inputs = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".woocommerce-billing-fields .input-text"))
)

first_name = driver.find_element_by_css_selector("#billing_first_name_field .input-text")
first_name.send_keys("Ann")

last_name = driver.find_element_by_css_selector("#billing_last_name_field .input-text")
last_name.send_keys("Brown")

email_adress = driver.find_element_by_css_selector("#billing_email_field .input-text")
email_adress.send_keys("1TEST2TEST3TEST@mail.ru")

phone = driver.find_element_by_css_selector("#billing_phone_field .input-text")
phone.send_keys("1234567890")

country = driver.find_element_by_id("billing_country_field")
country.click()

#country_select = driver.find_element_by_css_selector("#select2-drop .select2-search .select2-input")
#country_select.send_keys("United Kingdom (UK)")

#country_UK = driver.find_element_by_id("select2-chosen-1")
#country_UK.click()

adress = driver.find_element_by_css_selector("#billing_address_1_field .input-text")
adress.send_keys("Baker-street, 221B")

town = driver.find_element_by_css_selector("#billing_city_field .input-text")
town.send_keys("London")

postcode = driver.find_element_by_css_selector("#billing_postcode_field .input-text")
postcode.send_keys("NW1")

driver.execute_script("window.scrollBy(0, 600);")

check_payments = driver.find_element_by_css_selector(".payment_method_cheque .input-radio")
check_payments.click()

place_order = driver.find_element_by_id("place_order")
place_order.click()

place_order_text = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)

payment_method_text = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3)"), "Check Payments")
)

driver.quit()