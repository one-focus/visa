import telebot
import visa

bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")

dates, screenshot = visa.get_dates()
if dates:
    bot.send_message(chat_id=262438, text=dates)
    bot.send_photo(chat_id=262438, photo=screenshot)
