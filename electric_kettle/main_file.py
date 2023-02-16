import logging, keyboard, time
from threading import Thread
from electric_kettle.exceptions import *
from electric_kettle.classes import Kettle

logging.basicConfig(filename="../mylog.log", encoding='utf-8', level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")

def water_heating():
    water_temp = vitek.default_water_temp
    temp_delta = (vitek.shutdown_temp - water_temp) / 10
    print('Чтобы выключить чайник нажмите q')
    vitek.state = 'Вкл'
    print(vitek.state)
    while water_temp < vitek.shutdown_temp:
        time.sleep(1)
        water_temp += temp_delta
        print(f'Температура воды {water_temp} °C')
    vitek.state = 'Вскипел'
    print(vitek.state)
    vitek.state = 'Выкл'
    print(vitek.state)
    logging.info("the program worked well")


if __name__ == "__main__":

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
    except ValueError:
        print('Неверно указаны входные данные, укажите количество воды которое хотите налить')
        quit()

    thread = Thread(target=water_heating, daemon=True)
    thread.start()  # создание и запуск потока для реализации функционала прерывания работы чайника

    while True:
        try:  # используется конструкция try чтобы при нажатии другой клавиши не выводилась ошибка
            if keyboard.is_pressed('q'):
                vitek.state = 'Остановлен'
                print(vitek.state)
                logging.info("the program worked well, the kettle was turned off manually")
                break
        except:
            break