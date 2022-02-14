from selenium import webdriver
import time
import random
from data_test import mobile_user_agents_list, test_proxy_list

url = 'https://2ip.ru'
url2 = 'https://whatmyuseragent.com/'
url3 = 'https://google.com'

EMAIL = 'superhentai@gmail.com'
PASSWORD = 'qwerty123'

for proxy in test_proxy_list:
    # ДОБАВЛЯЕМ ОПЦИИ
    options = webdriver.ChromeOptions()

    options.add_argument(  # здесь указывается user-agent в зависимости от того какой нужен для оффера моб или деск
        f"user-agent={random.choice(mobile_user_agents_list)}")

    options.add_argument(
        f"--proxy-server={proxy}")

    # ИНИЦИЛИЗИРУЕ ОБЪЕКТ БРАУЗЕРА
    driver = webdriver.Chrome(
        executable_path='../chromedriver/chromedriver.exe',
        options=options)

    # ВЫПОЛНЯЕМ ЗАДУМАННУЮ РАБОТУ
    try:
        driver.get(url=url)
        time.sleep(2)

        if driver.xpath_exists('/html/body/div[1]/div/p[3]/a[2]'):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/p[3]/a[2]').click()
            time.sleep(3)

        driver.get(url='https://wellhello.com/registration')
        time.sleep(2)
        continue_button = driver.find_element_by_xpath('//*[@id="consent-continue-button"]')
        continue_button.click()

        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="consent-continue-button"]').click()

        time.sleep(3)

        gender_space = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div[1]/div/div[1]')
        gender_space.click()

        time.sleep(2)

        # ВВОД МЫЛА
        email_input = driver.find_element_by_id('email')
        email_input.clear()
        for i in EMAIL:
            email_input.send_keys(i)
            time.sleep(round(random.random(), 1))

        # ВВОД ПАРОЛЯ
        password_input = driver.find_element_by_id('password')
        password_input.clear()
        for i in PASSWORD:
            password_input.send_keys(i)
            time.sleep(round(random.random(), 1))

        time.sleep(2)

        # ВВОД ВОЗРАСТА
        age_input = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div[5]/div/div')
        age_input.click()

        time.sleep(4)

        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/div[2]/div[5]/div/ul/li[3]').click()
        time.sleep(2)

        zip_code = driver.find_element_by_id('zip_code')
        zip_code.clear()
        for i in range(5):
            zip_code.send_keys(random.randint(0, 9))
            time.sleep(random.random())

        time.sleep(2)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
