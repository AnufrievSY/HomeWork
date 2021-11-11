from random import randint


class Date:
    @classmethod
    def my_method(cls, value):
        return list(map(int, [x for x in value.split('-')]))

    @staticmethod
    def valid(day, month, year):
        if 31 >= day > 0:
            if 12 >= month > 0:
                if 2021 >= year >= 0:
                    return 'Ok'
                else:
                    return f'year: Error ({year})'
            else:
                return f'month: Error ({month})'
        else:
            return f'day: Error ({day})'


my_list = ['day', 'month', 'year']
result = Date.my_method(f"{randint(1, 50)}-{randint(1, 20)}-{randint(2000, 2050)}")
valid = Date.valid(result[0], result[1], result[2])

if valid == 'Ok':
    for i in range(3):
        print(f'{my_list[i]} - '
              f'{result[i]} - '
              f'{type(result[i])}')
else:
    print(valid)
