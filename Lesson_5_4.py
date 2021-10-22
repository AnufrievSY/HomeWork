translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

"""Получаем старые данные из документа"""
with open('L_5_4.txt', 'r') as my_file:
    print(f'Старый текст:\n{my_file.read()}')
    my_file.seek(0)
    file_list = [i for i in my_file.read().split('\n')]

"""Меняем данные"""
old_dict = {x.split(' - ')[0]: y.split(' - ')[1] for x in file_list for y in file_list}
new_dict = {}
for key in old_dict.keys():
    new_dict.update({translate_dict.get(key): old_dict.get(key)})

"""Записываем новые данные в документ"""
with open('L_5_4.txt', 'w+') as my_file:
    for key, value in new_dict.items():
        my_file.write(f'{key} - {value}\n')
    my_file.seek(0)
    print(f'Новый текст:\n{my_file.read()}')
