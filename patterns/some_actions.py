from selenium import webdriver
from time import sleep
import random

send = 'что делать дальше?'

driver = webdriver.Chrome('../chromedriver/chromedriver.exe')

# Navigate to url
driver.get("http://www.google.com")

# ----------------------------------------------------------------------------------------------------------------------
# Работа с полем ввода
zipcode_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
webdriver.ActionChains(driver).move_to_element(zipcode_input).click().perform()
zipcode_input.clear()
for i in send:
    zipcode_input.send_keys(i)
    sleep(random.random())
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Перемещение мыши к элементу и щелчек
gmailLink = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
webdriver.ActionChains(driver).move_to_element(gmailLink).click().perform()

# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------
# Head
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sleep(random.randrange(3, 12))


