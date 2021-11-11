from statistics import mean

with open('L_5_3.txt', 'r') as my_file:
    salary_list = []
    my_dict = {}
    for i in my_file.read().split('\n'):
        b_list = i.split(' - ')
        salary_list.append(int(b_list[1]))
        if int(b_list[1]) < 20000:
            my_dict.update({b_list[0]: b_list[1]})

print(f'Средняя величина дохода сотрудников - {round(mean(salary_list))}')
print('Сотрудники с наименьшим окладом:')
for key, value in my_dict.items():
    print(f'{key} - {value}')
