import telebot
import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('e702392fd0cb42d4a467dfc4f0953369', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("5115647575:AAFHPEse1GAVb80-BBo-48oEDMYLiK9WHMg")

@bot.message_handler(content_types =['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']
	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура где-то " + str(temp) + " градусов" + "\n\n"
	if temp < 10:
		answer +="На улице холодно, оденься нормально"
	elif temp < 0:
		answer +="На улице либо зима , либо это север. Оденься потеплее)"
	elif temp < 20:
		answer +="Там прохладно, но можно жить"
	elif temp < 30:
		answer +="В футболке норм будет"
	else:
		answer +="ЕЕЕЕЕ ЛЕТО!!!!!"

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)