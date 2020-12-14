import time

import telebot
import visa
from selenium import webdriver
import sys

bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")

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
    bot.send_message(chat_id=262438, text=str(times))
    bot.send_photo(chat_id=262438, photo=screenshot)

driver.quit()