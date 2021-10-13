"""создаем функцию base, которая будет печатать нам результат ввода"""
def base(name, surname, year, city, email, phone):
    print(f'{name}, {surname}, {year}, {city}, {email}, {phone}')


base_list = ['имя', 'фамилию', 'год рождения', 'город проживания', 'email', 'телефон']
var_list = []

"""создаем цикл, который поочереди будет спрашивать данные, указанные в base_list 
и записывать их в новый список var_list"""
for i in base_list:
    var_list.append(input(f'Введите {i}: '))

"""передаем полученные и записанные данные из списка var_list в аргументы функции base"""
base(name=var_list.pop(0),
     surname=var_list.pop(0),
     year=var_list.pop(0),
     city=var_list.pop(0),
     email=var_list.pop(0),
     phone=var_list.pop(0))
