from random import randint


class Car:
    def __call__(self, color, name, is_police):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Движется'

    def stop(self):
        return 'Остановился'

    def turn(self, direction):
        return f'Повернул {direction}'

    def show_speed(self, speed):
        return f'Скорость автомобиля: {speed} км/ч'


class TownCar(Car):
    name = 'Toyota'
    color = 'Grey'
    is_police = False


    def show_speed(self, speed):
        limit = 60
        if speed > limit:
            return (f'ПРЕВЫШЕНИЕ СКОРОСТИ\n'
                    f'На {speed - limit} разрешеных {limit} км/ч')
        else:
            return f'Скорость автомобиля: {speed} км/ч'


class SportCar(Car):
    color = 'Black'
    name = 'Bugatti'
    is_police = False


class WorkCar(Car):
    color = 'Yellow'
    name = 'CAT'
    is_police = False

    def show_speed(self, speed):
        limit = 40
        if speed > limit:
            return (f'ПРЕВЫШЕНИЕ СКОРОСТИ\n'
                    f'На {speed - limit} разрешеных {limit} км/ч')
        else:
            return f'Скорость автомобиля: {speed} км/ч'


class PoliceCar(Car):
    color = 'Blue'
    name = 'Lada Vesta'
    is_police = True


result = {'ГОРОДСКАЯ': TownCar(), 'РАБОЧАЯ': WorkCar(), 'СПОРТИВНАЯ': SportCar(), 'ПОЛИЦЕЙСКАЯ': PoliceCar()}
turn = ['налево', 'направо']
condition = [Car().go(), Car().stop(), Car().turn(turn[randint(0, 1)])]
i = randint(0, 3)
status = condition[randint(0, 2)]

print(f'----{list(result.keys())[i]} МАШИНА----\n'
      f'Наименование: {list(result.values())[i].name}\n'
      f'Цвет: {list(result.values())[i].color}\n'
      f'{"Полицейская машина" if list(result.values())[i].is_police else "Не полицейская" }\n'
      f'{list(result.values())[i].show_speed(randint(10, 180)) if status == "Движется" else status}')


