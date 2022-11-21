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

default_sorting = driver.find_element_by_css_selector(".orderby > [value='menu_order']")
selected_default = WebDriverWait(driver, 20).until(
    EC.element_to_be_selected(default_sorting)
)

select = driver.find_element_by_class_name("orderby")
select.click()
high_to_low = driver.find_element_by_css_selector(".orderby > [value='price-desc']")
high_to_low.click()

high_to_low = driver.find_element_by_css_selector(".orderby > [value='price-desc']")
selected_high = WebDriverWait(driver, 20).until(
    EC.element_to_be_selected(high_to_low)
)

driver.quit()