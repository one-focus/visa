import telebot
import visa
from selenium import webdriver

bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")

<<<<<<< HEAD
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)

times, screenshot = visa.get_times(driver)
if not times:
    driver.quit()
else:
    bot.send_message(chat_id=262438, text=times)
=======
dates, screenshot = visa.get_dates()
if dates:
    bot.send_message(chat_id=262438, text=dates)
>>>>>>> 0feea4d07424dd59db011e8cee6c43fa8f1f68f4
    bot.send_photo(chat_id=262438, photo=screenshot)
