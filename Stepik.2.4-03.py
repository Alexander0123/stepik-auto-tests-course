from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
import time
import math
browser.implicitly_wait(5)
def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет нужно кликабельной
    element1 = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button1 = browser.find_element_by_id('book').click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button2 = browser.find_element_by_id('solve').click()
    print(browser.switch_to.alert.text)



finally:
    time.sleep(4)
    browser.quit()