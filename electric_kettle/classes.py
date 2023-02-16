import configparser

config = configparser.ConfigParser()  # создаём объект парсера
config.read("settings.ini", encoding="utf-8")


class Kettle:
    def __init__(self):
        self.boil_time = int(config["Vitek"]["boil_time"])
        self.state = config["Vitek"]["state"]
        self.shutdown_temp = int(config["Vitek"]["shutdown_temp"])
        self.water_volume = float(config["Vitek"]["water_volume"])
        self.default_water_temp = int(config["Vitek"]["default_water_temp"])

    def __str__(self):
        return f'Время закипания воды - {self.boil_time} секунд, ' \
               f'температура автоматического выключения - {self.shutdown_temp} °C, ' \
               f'количество воды - {self.water_volume}'
