from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text("My Account")
my_account.click()

email_adress = driver.find_element_by_id("reg_email")
email_adress.send_keys("1TEST2TEST3TEST@mail.ru")

password = driver.find_element_by_id("reg_password")
password.send_keys("G5F2E4D1C3B6A")

register_btn = driver.find_element_by_name("register")
register_btn.click()

driver.quit()