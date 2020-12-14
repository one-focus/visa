import os
import time

import telebot
import visa
from selenium import webdriver
import sys

bot = telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN'))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)

time.sleep(int(sys.argv[1]))
times, screenshot = visa.get_times(driver)
if times:
    bot.send_message(chat_id=int(os.environ.get('TELEGRAM_TO')), text=str(times))
    bot.send_photo(chat_id=int(os.environ.get('TELEGRAM_TO')), photo=screenshot)

driver.quit()