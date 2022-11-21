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

logout_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
)

driver.quit()