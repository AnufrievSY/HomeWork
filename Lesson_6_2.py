class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length
        self.__weight = 25
        self.__thickness = 5

    def calculate(self):
        result = round((self._length * self._width * self.__weight * self.__thickness)/1000)
        return f'Длинна дороги - {self._width} м.\n' \
               f'Ширина дороги - {self._length} м.\n' \
               f'Масса асфальта для покрытия одного кв. м. дороги толщиной в 1 см. - {self.__weight} кг\n' \
               f'Толщина полотна {self.__thickness} см\n' \
               f'В результате необходимо {result} тонн асфальта'


road = Road(int(input('Длинна дороги: ')), int(input('Ширина дороги: ')))
print(road.calculate())
