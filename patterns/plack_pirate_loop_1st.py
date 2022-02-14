from selenium import webdriver
from fake_useragent import UserAgent
import datetime
import csv

# Вводим данные
type_proxy = input('Enter type of proxy (socks5 - s or http(s) - h): >>')
proxy = input('Enter the ip of proxy server: >>')
#useragent = UserAgent().random
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
link = input('Enter the referral link: >>')
today = datetime.datetime.now()

# Запись данных в таблицу
with open('statistic.csv', 'a') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([type_proxy, proxy, useragent, link, today])

# Добавляем опции
options = webdriver.ChromeOptions()

# Условная конструкция проверяет и подключает прокси в зависимости от протокола
if type_proxy == 'h':
    options.add_argument(f'--proxy-server=socks5://{proxy}')
elif type_proxy == 's':
    options.add_argument(f'--proxy-server=socks5://{proxy}')
else:
    print('[!] Вы ввели неизвестный тип протокола!')

options.add_argument(f'user-agent={useragent}')
options.add_argument('--lang=en')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# Инициализируем работу браузера
browser = webdriver.Chrome(
    executable_path='../chromedriver/chromedriver.exe',  # для ubuntu "chromedriver/chromedriver"
    options=options
)

# Запускаем браузер по указанной ссылке
browser.get(link)