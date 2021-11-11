from random import randint


class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


result = [Pen(), Pencil(), Handle()]
for i in range(6):
    result[randint(0, 2)].draw()
