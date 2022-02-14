from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from authentication import username, password
import time
import random
from selenium.common.exceptions import NoSuchFrameException
import requests
import os


class InstagramBot(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('../chromedriver/chromedriver.exe')

    def close_browser(self):
        """ФУНКЦИЯ ЗАКРЫТИЯ БРАУЗЕРА"""
        self.browser.close()
        self.browser.quit()

    def login(self):
        """ВХОД В ПРОФИЛЬ"""
        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))

        # browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        # time.sleep(2)

        username_input = browser.find_element_by_name('username')
        username_input.clear()

        for i in username:
            username_input.send_keys(i)
            time.sleep(round(random.random(), 1))

        time.sleep(2)

        password_input = browser.find_element_by_name('password')
        password_input.clear()
        for i in password:
            password_input.send_keys(i)
            time.sleep(round(random.random(), 1))

        password_input.send_keys(Keys.ENTER)

    def like_photo_by_hashtag(self, hashtag):
        """ПОСТАНОВКА ЛАЙКА ПО ХЕШТЕГУ"""
        browser = self.browser

        browser.get(f"https://www.instagram.com/explore/tags/{hashtag}")
        time.sleep(5)

        # for i in range(1, 4):  # диапазон который задан тут задает количество скролов на одну страницу
        #     # ниже приведен блок с применением java script
        #     browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        #     time.sleep(random.randrange(3, 5))

        # Сбор ВСЕХ ссылок со страницы
        hrefs = browser.find_element_by_tag_name('a')

        # Собираем ссылки на ПОСТЫ со страницы с помощью list comprehension
        posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

        # for url in posts_urls:
        #     try:
        #         browser.get(url)
        #         time.sleep(3)
        #         like_button = browser.find_element_by_xpath(
        #             '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
        #     except Exception as ex:
        #         print(ex)
        #         self.close_browser()

        with open(f"{hashtag}.txt", "a") as file:
            for pu in posts_urls:
                file.write(pu + '\n')

    # проверка по xpath существует ли элемент на странице
    def xpath_exists(self, url):
        """ПРОВЕКА, ЕСТЬ ЛИ ИСКОМЫЙ ЭЛЕМЕНТ НА СТРАНИЦЕ"""
        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchFrameException:
            exist = False
        return exist

    # метод который ставит лайки по прямой ссылке на пост
    def put_exactly_like(self, userpost):
        """ПОСТАНОВКА ЛАЙКА ПО ПРЯМОЙ ССЫЛКЕ НА ПОСТ"""
        browser = self.browser
        browser.get(userpost)
        time.sleep(2)

        wrong_userpage = 'здесь должен быть xpath до тега с несущесвующей страницей'
        if self.xpath_exists(wrong_userpage):
            print('[!] Такого поста не существует или профиль закрыт.')
            self.close_browser()
        else:
            print('Пост успешно найден.')
            time.sleep(3)

            like_button = '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div/span/svg'
            browser.find_element_by_xpath(like_button).click()

            print(f'Лайк на пост {userpost} успешно поставлен!')
            self.close_browser()

    # метод который собирает ссылки на все посты пользователя
    def get_all_posts_urls(self, userpage):
        """МЕТОД СОБИРАЕТ ССЫЛКИ НА ВСЕ ПОСТЫ ПОЛЬЗОВАТЕЛЯ"""
        browser = self.browser
        browser.get(userpage)
        time.sleep(3)

        wrong_userpage = '//*[@id="react-root"]/section/main/div/div/h2'  # здесь размещается xpath с несуществующей страницы
        if self.xpath_exists(wrong_userpage):
            print('[!] Такого пользоваеля не существует или профиль закрыт.')
            self.close_browser()
        else:
            print('Профиль успешно найден')
            time.sleep(3)

            # инстаграм при первой загрузке выдает по 24 поста, а при последующей прокрутке по 12
            # строка ниже возвращает число постов со страницы пользователя в целочисленном типе
            posts_count = int(browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/ul/li[1]/span/span').text)
            loops_count = posts_count / 12
            print(loops_count)

            posts_url = []

            for i in range(0, loops_count):
                hrefs = browser.find_element_by_tag_name('a')
                hrefs = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

                for href in hrefs:
                    posts_url.append(href)

                browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(random.randrange(3, 5))
                print(f"Итерация #{i} ")

            # создание файла для полученных ссылок на публикации со страницы
            file_name = userpage.split('/')[-2]  # для названия файла

            # запись неупорядоченных ссылок
            with open(f"{file_name}.txt", "a") as file:
                for pu in posts_url:
                    file.write(pu + '\n')

            # упорядовачине ссылок и удаление дубликатов
            set_posts_urls = set(posts_url)
            set_posts_urls = list(set_posts_urls)

            # запись упорядоченных ссылок
            with open(f"{file_name}_set.txt", 'a') as file:
                for post_url in set_posts_urls:
                    file.write(post_url + "\n")


    # поставка лайков по ссылке на аккаунт пользователя
    def put_many_likes(self, userpage):
        """ПРОСТАНОВКА ЛАЙКОВ НА ВСЕ ПОСТЫ ПОЛЬЗОВАТЕЛЯ"""
        browser = self.browser
        self.get_all_posts_urls(userpage)
        file_name = userpage.split('/')[-2]
        time.sleep(4)
        browser.get(userpage)
        time.sleep(3)

        # открытие файла с ссылками на чтение и простановка лайков
        with open(f"{file_name}_set.txt") as file:
            url_lists = file.readlines()

            for post_url in url_lists:
                try:
                    browser.get(post_url)
                    time.sleep(2)

                    like_button = 'пусто' # xpath до кнопки нажатия лайка
                    browser.find_element_by_xpath(like_button).click()
                    #time.sleep(random.randrange(88, 100))
                    time.sleep(3)

                    print(f"Лайк на пост: {post_url} успешно поставлен!")
                except Exception as ex:
                    print(ex)
                    self.close_browser()

            self.close_browser()

    def download_usserpage_content(self, userpage):
        """МЕТОД КОТОРЫЙ СКАЧИВАЕТ КОНТЕНТ СО СТРАНИЦЫ ПОЛЬЗОВАТЕЛЯ"""
        browser = self.browser
        self.get_all_posts_urls(userpage)
        file_name = userpage.split('/')[-2]
        time.sleep(4)
        browser.get(userpage)
        time.sleep(3)

        # создаем папку с именем пользователя
        if os.path.exists(f"{file_name}"):
            print("Папка уже существует!")
        else:
            os.mkdir(file_name)

        img_and_video_src_urls = []

        # открытие файла с ссылками на чтение и простановка лайков
        with open(f"{file_name}_set.txt") as file:
            url_lists = file.readlines()

            for post_url in url_lists: # задать диапазон до определенного кол-ва постов: url_videos[0:10]
                try:
                    browser.get(post_url)
                    time.sleep(4)

                    img_src = '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/img'
                    video_src = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div/div[1]/div/div/video'
                    post_id = post_url.split('/')[-2]

                    if self.xpath_exists(img_src):
                        img_src_url = browser.find_element_by_xpath(img_src).get_attribute('src')
                        img_and_video_src_urls.append(img_src_url)

                        # сохранение изображения
                        get_img = requests.get(img_src_url)
                        with open(f"{file_name}/{file_name}_{post_id}_img.jpg", "wb") as img_file:
                            img_file.write(get_img.content)

                    elif self.xpath_exists(video_src):
                        video_src_url = browser.find_element_by_xpath(video_src).get_attribute('src')
                        img_and_video_src_urls.append(video_src_url)

                        # сохранение видео
                        get_video = requests.get(img_src_url, stream=True)
                        with open(f"{file_name}/{file_name}_{post_id}_video.mp4", "wb") as video_file:
                            for chunk in get_video.iter_content(chunk_size=1024 * 1024):
                                if chunk:
                                    video_file.write(chunk)

                    else:
                        print("[!] Упс. Что то пошло не так!")
                        img_and_video_src_urls.append(f"{post_url}, нет ссылки!!!")

                    print(f"Контент из поста {post_url} успешно скачан!")

                except Exception as ex:
                    print(ex)
                    self.close_browser()

            self.close_browser()

        with open(f"{file_name}/{file_name}_img_and_video_src_urls.txt", "a") as file:
            for i in img_and_video_src_urls:
                file.write(i + "\n")



if __name__ == '__main__':
    my_bot = InstagramBot(username, password)
    my_bot.login()
    time.sleep(6)
    my_bot.close_browser()
