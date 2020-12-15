import time

import telebot
import visa
from selenium import webdriver
import sys

bot = telebot.TeleBot(sys.argv[2])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)


def create_user(driver):
    try:
        driver.find_element_by_xpath("//div[@class='clsDivDatetimeSlot']/..").click()

        user = {'passport': '11106422',
                'passport_expired': '22/09/2028',
                'name': 'Jajwalish',
                'surname': 'Raios',
                'email': 'agafinovaguzel@gmail.com',
                'cellphone': 'rega11rega11@mail.ru',
                'nationality': 'Nepal',
                'create_pass': 'Abcd123456!'}
        visa.create_user(driver, user['passport'], user['passport_expired'], user['name'], user['surname'],
                         user['email'],
                         user['cellphone'], user['nationality'], user['create_pass'])

        bot.send_photo(chat_id=int(sys.argv[3]), photo=driver.get_screenshot_as_png())
        time.sleep(10)
        bot.send_photo(chat_id=int(sys.argv[3]), photo=driver.get_screenshot_as_png())
    except Exception as e:
        bot.send_message(chat_id=int(sys.argv[3]), text=str(e))
        bot.send_photo(chat_id=int(sys.argv[3]), photo=driver.get_screenshot_as_png())


time.sleep(int(sys.argv[1]))
times, screenshot = visa.get_times(driver)
if times:
    bot.send_message(chat_id=int(sys.argv[3]), text=str(times))
    bot.send_photo(chat_id=int(sys.argv[3]), photo=screenshot)
    create_user(driver)
else:
    import datetime
    bot.send_message(chat_id=int(sys.argv[3]), text=f'{sys.argv[1]} : {datetime.datetime.now()}')

driver.quit()
