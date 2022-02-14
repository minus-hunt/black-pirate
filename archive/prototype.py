import random
from selenium import webdriver
from time import sleep
from data_test import test_proxy_list, mobile_user_agents_list
from readed_data import mails, passwords

ZIPCODE = '84538'
REF_LINK_wellhello = 'https://www.instagram.com/linkshim/?u=https://trackwin.net/go/bbac11f74605426ba0eee42428aa9b3e36' \
                     '5b64d1eb0a0b0b&e=AT2W4yR8n43hteLbIqfVGwbjWbiF7zmYB0ivNtNCMvZqUOSPwZ7LxY0IsNkE62K790NbhCryJ9jcnwN' \
                     'voEDzYkFrJAjD8RjW7jlZ#'




def test_function_wellhello(useragent):
    options = webdriver.ChromeOptions()

    # Добавление опций
    options.add_argument(f"user-agent={useragent}")
    options.add_argument(f"--proxy-server={test_proxy_list[1]}")

    # Инициализация браузера
    driver = webdriver.Chrome(
        executable_path='../chromedriver/chromedriver.exe',
        options=options
    )

    try:
        driver.get(REF_LINK_wellhello)
        sleep(3)

        # ...вы покидаете инстаграм.....
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div/p[2]/button').click()
        sleep(random.randrange(3, 5))

        # ...looking woman or man
        driver.find_element_by_xpath('/html/body/div[1]/form/div[1]/div[1]/p').click()
        sleep(random.randrange(3, 5))

        # choose age of partner
        # first roll
        driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/select[1]').click()
        sleep(2)
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[2]/div/select[1]/option[{random.randrange(1, 3)}]').click()
        sleep(2)

        # second roll
        driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/select[2]').click()
        sleep(2)
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[2]/div/select[2]/option[{random.randrange(3, 6)}]').click()
        sleep(2)

        # next
        driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/button').click()
        sleep(random.randrange(3, 4))

        # are a man or a woman
        driver.find_element_by_xpath('/html/body/div[1]/form/div[3]/div[1]/p')
        sleep(random.randrange(3, 4))

        # what is your age
        driver.find_element_by_xpath('/html/body/div[1]/form/div[4]/div/select').click()
        sleep(1)
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[4]/div/select/option[{random.randrange(8, 24)}]').click()
        sleep(random.randrange(3, 4))

        # enter zipcode
        zipcode_input = driver.find_element_by_id('zipcode')
        zipcode_input.clear()
        for i in ZIPCODE:
            zipcode_input.send_keys(i)
            sleep(random.random())
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/form/div[5]/div[1]/button').click() # next_button
        sleep(random.randrange(3, 4))

        # are u in relationship
        relationship = [
            '/html/body/div[1]/form/div[6]/div/button[1]',
            '/html/body/div[1]/form/div[6]/div/button[6]'
        ]
        driver.find_element_by_xpath(random.choice(relationship)).click()
        sleep(random.randrange(3, 4))

        # eye color
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[7]/div/button[{random.randrange(1, 7)}]').click()
        sleep(random.randrange(3, 4))

        # wich hair
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[8]/div/button[{random.randrange(1,6)}]').click()
        sleep(random.randrange(3, 4))

        # your color skin
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[9]/div/button[{random.randrange(3,9)}]').click()
        sleep(random.randrange(2, 4))

        # what is your posture
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[10]/div/button[{random.randrange(1, 4)}]').click()
        sleep(random.randrange(4, 6))

        # how tall are you
        driver.find_element_by_xpath('/html/body/div[1]/form/div[11]/div/select').click() # roll
        sleep(2)
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[11]/div/select/option[{random.randrange(8, 18)}]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/form/div[11]/div/button').click()
        sleep(random.randrange(4, 6))

        # pubic hair
        driver.find_element_by_xpath(f'/html/body/div[1]/form/div[12]/div/button[{random.randrange(1, 3)}]').click()
        sleep(random.randrange(2, 3))

        # ENTER PASSWORD
        password = random.choice(passwords)

        password_input = driver.find_element_by_id('password')
        password_input.clear()
        for i in password:
            password_input.send_keys(i)
            sleep(random.random())
        sleep(1)

        driver.find_element_by_xpath('/html/body/div[1]/form/div[13]/div[1]/button').click()
        sleep(random.randrange(2, 3))

        # EMAIL
        email = random.choice(mails)
        if email in email_black_list:
            email = random.choice(mails)
            return email
        else:
            email_black_list.append(email)

        email_input = driver.find_element_by_id('email')
        email_input.clear()
        for i in email:
            email_input.send_keys(i)
            sleep(random.random())
        sleep(2)

        driver.find_element_by_xpath('/html/body/div[1]/form/div[14]/div[1]/div/button').click()
        sleep(random.randrange(2, 3))

        # done to continue!
        driver.find_element_by_xpath('/html/body/div[1]/section/div/a/div').click()
        sleep(5)

    except Exception as ex:
        with open('log_file', 'a') as file:
    finally:
        driver.quit()
        driver.close()

