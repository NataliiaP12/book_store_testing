from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

read_more = driver.find_element_by_css_selector(".post-163 .button")
read_more.click()

reviews = driver.find_element_by_css_selector(".reviews_tab a")
reviews.click()

your_rating = driver.find_element_by_class_name("star-5")
your_rating.click()

your_review = driver.find_element_by_id("comment")
your_review.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Ann")

email = driver.find_element_by_id("email")
email.send_keys("12345@mail.ru")

submit = driver.find_element_by_id("submit")
submit.click()

driver.quit()