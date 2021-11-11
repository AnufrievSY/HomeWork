from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def result(self):
        pass


class Coat (Clothes):
    @property
    def result(self):
        return self.args / 6.5 + 0.5


class Suit(Clothes):
    @property
    def result(self):
        return 2 * self.args + 0.3


coat = round(Coat(int(input('Размер пальто: '))).result, 2)
suit = round(Suit(int(input('Рост костюма: '))).result, 2)
print(f'Для пальто понадобиться {coat} ткани.')
print(f'Для костюма понадобиться {suit} ткани.')
print(f'------\n'
      f'Всего понадобиться {round(coat+suit)} ткани.')

