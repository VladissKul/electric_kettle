import multiprocessing
import os

import keyboard as keyboard
from threading import *

from exceptions import *
import time
import sys

try:
    amount_of_water = float(input("Налейте воду: "))
    if amount_of_water <= 0:
        raise LittleWater()
    if amount_of_water > 1.0:
        raise MuchWater()
except LittleWater:
    print('Вы не налили воду')
except MuchWater:
    print('Вы налили слишком много воды')


class Kettle:
    def __init__(self):
        self.boil_time = 10
        self.state = 'Выкл'


run = True

vitek = Kettle()

def water_temp1():
    water_temp = 20
    temp_delta = (100 - water_temp) / 10
    print('Чтобы выключить чайник нажмите q')
    while water_temp < 100:
        time.sleep(1)
        water_temp += temp_delta
        print(f'Температура воды {water_temp} °C')
    vitek.state = 'Вскипел'
    print(vitek.state)
    vitek.state = 'Выкл'
    print(vitek.state)
    run = False


thread = Thread(target=water_temp1, daemon=True)
thread.start()

while run:
    try:  # используется try чтобы при нажатии другой клавиши не выводилась ошибка
        if keyboard.is_pressed('q'):
            vitek.state = 'Выкл'
            print(vitek.state)
            break
    except:
        break