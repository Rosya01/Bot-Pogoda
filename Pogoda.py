import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('e702392fd0cb42d4a467dfc4f0953369', config_dict)
mgr = owm.weather_manager()

place = input("Где ты находишься?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура где-то " + str(temp) + " градусов")

if temp < 10 :
    print("На улице холодно, оденься нормально")
elif temp < 0 :
    print("На улице либо зима , либо это север. Оденься потеплее)")
elif temp < 20 :
    print("Там прохладно, но можно жить")
elif temp < 30 :
    print("В футболке норм будет")
else:
    print("ЕЕЕЕЕ ЛЕТО!!!!!")