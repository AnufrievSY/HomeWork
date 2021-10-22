with open('L_5_5.txt', 'w+') as my_file:
    my_file.writelines(input('Введите цифры через пробел \n'))
    my_file.seek(0)
    my_list = my_file.read().split()
my_list = [int(x) for x in my_list]
print(f'Сумма {my_list} = {sum(my_list)}')