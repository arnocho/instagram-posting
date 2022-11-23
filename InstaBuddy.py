from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from py_console import console
import json, os, random

with open('quotes.txt') as f:
    quotes = [line.rstrip() for line in f]

with open('config.json', 'r') as f:
    config = json.load(f)
    username = config["instagram"]["USERNAME"]
    passord = config["instagram"]["PASSWORD"]
    chrome_p = config["general"]["chrome_path"]
    headless = config["general"]["headless"]
    time_after_url_change = config["times"]["time_after_url_change"]
    time_send_key_sleep  = config["times"]["time_send_key_sleep"]
    time_after_click  = config["times"]["time_after_click"]
    time_after_post = config["times"]["time_after_post"]
    description_hashtags = config["description"]["hashtags"]
    folder_root = config["description"]["folder_root"]


class InstaBuddy:
    def __init__(self):
        self.username = username
        self.password = passord
        self.time_after_url_change = time_after_url_change
        self.time_after_click = time_after_click
        self.time_send_key_sleep = time_send_key_sleep
        self.time_after_post = time_after_post
        self.description_hashtags = description_hashtags
        self.folder_root = folder_root
        chrome_path = chrome_p
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.headless = headless
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(executable_path=chrome_path, options=self.options)
        params = {
            "latitude": 48.8534,
            "longitude": 2.3488,
            "accuracy": 100
        }
        self.driver.execute_cdp_cmd("Page.setGeolocationOverride", params)
                   

    def post_data_init(self):
        self.image_to_upload = self.get_random_image()
        self.description = self.build_description(self.image_to_upload[1])
    
    def clean_post_data(self):
        os.remove(self.image_to_upload[0])

    def get_random_quote(self):
        return random.choice(quotes)

    def build_description(self, credit : str):
        description = self.get_random_quote() + f"\n\nCredits: @{credit}\n\n.\n.\n.\n.\n.\n.\n.\n.\n\n" + description_hashtags
        return description

    def get_random_image(self):
        dirs = os.listdir(folder_root)
        random_folder = random.choice(dirs)
        dir_path = folder_root + random_folder + "/"
        images = os.listdir(dir_path)
        random_image = random.choice(images)
        final_image = dir_path + random_image
        return [final_image, random_folder]

    def clean_close_driver(self):
        self.driver.close()
        self.driver.quit()

    def go_to_page(self, url):
        self.driver.get(url)
        sleep(self.time_after_url_change)

    def create_folder(self):
        if(os.path.isdir(self.username) == False):
            os.mkdir(self.username)

    def click_on_xpath(self, xpath) -> bool:
        try:
            element = self.driver.find_element("xpath", xpath)
            element.click()
            sleep(self.time_after_click)
            return True
        except:
            return False

    def write_text_on_xpath(self, xpath, text, finish_enter=False) -> bool:
        try:
            element = self.driver.find_element("xpath", xpath)
            element.send_keys(text)
            sleep(self.time_send_key_sleep)
            if finish_enter:
                element.send_keys(Keys.RETURN)
            return True
        except:
            return False

    def write_text_on_name(self, name, text, finish_enter=False) -> bool:
        try:
            element = self.driver.find_element("name", name)
            element.send_keys(text)
            sleep(self.time_send_key_sleep)
            if finish_enter:
                element.send_keys(Keys.RETURN)
            return True
        except:
            return False

    def is_suspected(self):
        try:
            sleep(time_after_url_change)
            self.driver.find_element("name","eiCW-")
            return True
        except Exception:
            return False

