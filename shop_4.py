from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

username = driver.find_element_by_id("username")
username.send_keys("1TEST2TEST3TEST@mail.ru")

login_password = driver.find_element_by_id("password")
login_password.send_keys("G5F2E4D1C3B6A")

login_btn = driver.find_element_by_name("login")
login_btn.click()

shop = driver.find_element_by_link_text("Shop")
shop.click()

read_more = driver.find_element_by_css_selector(".post-169 .button")
read_more.click()

old_price = driver.find_element_by_css_selector(".price del")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"

new_price = driver.find_element_by_css_selector(".price ins")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"

img_book = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a"))
)
img_book.click()

img_close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
)
img_close.click()

driver.quit()