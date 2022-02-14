import csv
import datetime
import time
import random

now = datetime.datetime.utcnow()

program_name = __file__.split('\\')[-1]
proxy = '192.168.1.1'
email =  f"{random.randrange(1000, 9999)}@gmail.com"
password = random.randrange(1000000, 9999999)
today = datetime.datetime.utcnow()
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

while True:
    with open('statistic.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([program_name, proxy, email, password, today, useragent])

    time.sleep(5)