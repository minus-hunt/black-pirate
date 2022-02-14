from selenium import webdriver
import time
# from data_test import  desktop_user_agents_list
import random

proxy = ''
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

link = 'https://google.com'
# link = 'https://2ip.ru'


def get_page(link, useragent=None, proxy=None):
    options = webdriver.ChromeOptions()

    # Уникальность нового пользователя
    # Условие проверяет если в функцию передан параметр, то применяется опция
    if useragent != None:
        options.add_argument(f"user-agent={useragent}")

    if proxy != None:
        options.add_argument(f"--proxy-server={proxy}")

    # Сокрытие факта использования Selenium
    options.add_argument('--disable-blink-features=AutomationControlled')  # Отключение видимости вебдрайвера
    options.add_argument('--lang=en')  # Использование только английского языка

    options.add_experimental_option("excludeSwitches", ['enable-automation'])  # Устранение уведомления, что браузером управляет автоматизир. по.
    # options.add_argument('headless')  # Перевод работы браузера в фоновый режим

    # Инициализация работы браузера
    # Так же должен быть указан путь до драйвера по стандартам линукса
    browser = webdriver.Chrome(
        executable_path='../chromedriver/chromedriver.exe',  # Добавить сюда путь до драйвера!!!
        options=options
    )

    browser.get(link)


if __name__ == "__main__":
    get_page(link, useragent)
    time.sleep(5)
