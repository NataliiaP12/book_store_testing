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
js_data_structures_and_algorithm = driver.find_element_by_css_selector(".post-180 .button")
js_data_structures_and_algorithm.click()

basket = driver.find_element_by_class_name("wpmenucart-contents")
basket.click()

time.sleep(3)
delete_html5_webapp_development = driver.find_element_by_css_selector("tbody .cart_item:nth-child(1) .remove")
delete_html5_webapp_development.click()
undo = driver.find_element_by_link_text("Undo?")
undo.click()

quantiti_js_data_structures_and_algorithm = driver.find_element_by_css_selector("tbody .cart_item:nth-child(1) .input-text")
quantiti_js_data_structures_and_algorithm.clear()
quantiti_js_data_structures_and_algorithm.send_keys("3")

update_basket = driver.find_element_by_name("update_cart")
update_basket.click()

# 9: ???
# quantiti_js_data_structures_and_algorithm = driver.find_element_by_css_selector("tbody .cart_item:nth-child(1) .input-text")
# quantiti_js_data_structures_and_algorithm_get_text = quantiti_js_data_structures_and_algorithm.text
# assert quantiti_js_data_structures_and_algorithm_get_text == "3"

time.sleep(3)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()

error = driver.find_element_by_class_name("woocommerce-error")
error_get_text = error.text
assert "Please enter a coupon code." in error_get_text

driver.quit()