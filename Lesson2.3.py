a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [10, 11, 12]
my_dict = {'зима': a, 'весна': b, 'лето': c, 'осень': d}

command = int(input())

for key, value in my_dict.items():
    if value.count(command) == 1:
        print(f'Ваш месяц - {key}')
