from random import randint


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{(self.a * other.a) - (self.b * other.b)} + {(self.a * other.b) + (other.a * self.b)}i'


z_1 = ComplexNumber(randint(-10, 10), randint(-10, 10))
z_2 = ComplexNumber(randint(-10, 10), randint(-10, 10))

print(f'z_1 = {z_1}\n'
      f'z_2 = {z_2}\n'
      f'Сумма: z_1 + z_2 = {z_1 + z_2}\n'
      f'Произведение: z_1 * z_2 = {z_1 * z_2}')
