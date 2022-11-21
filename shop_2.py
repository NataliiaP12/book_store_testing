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

html = driver.find_element_by_link_text("HTML")
html.click()

products_count = driver.find_elements_by_css_selector(".products > li")
if len(products_count) == 3:
    print("На странице отображаются 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(products_count)))

driver.quit()