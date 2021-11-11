from time import sleep
from random import randint
from sys import exit


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self, test):
        i = randint(0, 2)
        while i != 3:
            for x in range(3):
                """Если сигнал соответсвует проверочному значению, то сигнал загорается"""
                if TrafficLight.__color[i] == test[x]:
                    print(TrafficLight.__color[i])
                    if i == 0:
                        sleep(7)
                    elif i == 1:
                        sleep(2)
                    elif i == 2:
                        sleep(randint(1, 10))
                    i += 1
                    """Если сигнал НЕ соответствует проверочному значению, скрипт прерывается"""
                else:
                    print('Error\n'
                          'Сигнал не соответсвует заданному значению')
                    exit()


"""Список значений для проверки"""
test_list = ['Красный', 'Желтый', 'Зеленый']

t = TrafficLight()
t.running(test=test_list)
