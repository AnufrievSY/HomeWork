class Worker:
    def __init__(self, name, surname,  wage, bonus):
        self.name = name
        self.surname = surname
        self.position = None
        self._income = {'Оклад': wage, 'Премия': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


a = Position(name=input('Имя: '),
             surname=input('Фамилия: '),
             wage=int(input('Оклад: ')),
             bonus=int(input('Премия: ')))
print(f'-----ВЫВОД-----\n'
      f'Полное имя сотрудника: {a.get_full_name()}\n'
      f'Доход с учетом премии: {a.get_total_income()}')
