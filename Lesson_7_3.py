class Cell:
    def __init__(self, value):
        try:
            self.param = round(float(value))
            self.result = f'param = {self.param}'
        except ValueError:
            self.result = f'Введите число'

    def elf(self):
        return self.result

    def __add__(self, other):
        return f'слияние клетки: {self.param} + {other.param} = {self.param + other.param}'

    def __sub__(self, other):
        result = self.param - other.param
        return f'вычитание из клетки: {self.param} - {other.param} = {result}' if result > 0 else 'клетки нет'

    def __mul__(self, other):
        return f'слияние клетки: {self.param} * {other.param} = {self.param * other.param}'

    def __truediv__(self, other):
        return f'вычитание из клетки: {self.param} / {other.param} = {self.param / other.param}'

    def make_order(self, row):
        result = ''
        for _ in range(int(self.param / row)):
            result += '0' * row + '\n'
        result += '0' * (self.param % row) + '\n'
        return result


while True:
    for i in range(50):
        print('-', end='')
    print('\n"q" чтобы выйти\n'
          '"+" чтобы сложить\n'
          '"-" чтобы вычесть\n'
          '"*" чтобы перемножить\n'
          '"/" чтобы разделить\n'
          '"=" чтобы вывести колличество ячеек\n')
    x = input()
    if x == 'q':
        break
    elif x == '+':
        print(Cell(input()) + Cell(input()))
    elif x == '-':
        print(Cell(input()) - Cell(input()))
    elif x == '*':
        print(Cell(input()) * Cell(input()))
    elif x == '/':
        print(Cell(input()) / Cell(input()))
    elif x == '=':
        cell = Cell(round(float(input('масса клетки: '))))
        print(cell.make_order(5))
    else:
        print(Cell(x).elf())
