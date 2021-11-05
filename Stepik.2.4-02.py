from selenium import webdriver
browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
import time
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
try:
    browser.get("http://suninjuly.github.io/cats.html")
    button = browser.find_element_by_id("button")



finally:
    time.sleep(3)
    browser.quit()