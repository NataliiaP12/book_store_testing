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

read_more = driver.find_element_by_css_selector(".post-181 .button")
read_more.click()

book_title = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary > h1"), "HTML5 Forms")
)

driver.quit()