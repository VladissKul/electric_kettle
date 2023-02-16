import logging
import keyboard
from threading import Thread
from exceptions import *
import time
import configparser

logging.basicConfig(filename="mylog.log", encoding='utf-8', level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini", encoding="utf-8")
class Kettle:
    def __init__(self):
        self.boil_time = int(config["Vitek"]["boil_time"])
        self.state = config["Vitek"]["state"]
        self.shutdown_temp = int(config["Vitek"]["shutdown_temp"])
        self.water_volume = float(config["Vitek"]["water_volume"])


vitek = Kettle()

try:
    amount_of_water = float(input("Налейте воду: "))
    if amount_of_water <= 0:
        raise LittleWater()
    if amount_of_water > vitek.water_volume:
        raise MuchWater()
except LittleWater:
    print('Вы не налили воду')
    quit()
except MuchWater:
    print('Вы налили слишком много воды')
    quit()





run = True

# print(type(vitek.boil_time))
# print(vitek.state)
# print(vitek.shutdown_temp)


def water_temp1():
    water_temp = 20
    temp_delta = (vitek.shutdown_temp - water_temp) / 10
    print('Чтобы выключить чайник нажмите q')
    while water_temp < vitek.shutdown_temp:
        time.sleep(1)
        water_temp += temp_delta
        print(f'Температура воды {water_temp} °C')
    vitek.state = 'Вскипел'
    print(vitek.state)
    vitek.state = 'Выкл'
    print(vitek.state)
    logging.info("the program worked well")
    run = False


thread = Thread(target=water_temp1, daemon=True)
thread.start()

while run:
    try:  # используется try чтобы при нажатии другой клавиши не выводилась ошибка
        if keyboard.is_pressed('q'):
            vitek.state = 'Выкл'
            print(vitek.state)
            logging.info("the program worked well, the kettle was turned off manually")
            break
    except:
        break