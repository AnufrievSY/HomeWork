from itertools import count
from itertools import cycle

start = round(float(input('Введите стартовое число: ')))
end = start + 10
for i in count(start):
    if i > end:
        break
    else:
        print(f'count: {i}')

a_list = input('Введите слово: ')
a = 1
for i in cycle(list(a_list)):
    if a > len(a_list)*2:
        break
    else:
        print(f'cycle: {i}')
        a += 1
