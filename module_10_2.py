# Задача "За честь и отвагу!":

import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def fight(self, name, power, enemies=100):
        day = enemies // power
        while enemies:
            for i in range(1, (enemies // power) + 1):
                time.sleep(1)
                enemies -= power
                print(f'{name} сражается {i}..., осталось {enemies} воинов.')
        print(f'{name} одержал победу спустя {day} дней(дня)!')
    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight(self.name, self.power)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')