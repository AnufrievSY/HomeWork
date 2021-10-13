def update(var_list):
    """Функция меняет строчные значения полученные инпутом на цифры"""
    for value in var_list:
        new_value = int(value)
        new_var_list.append(new_value)
    return sum(new_var_list)


def up_list(var):
    """Функция преобразовывает строку к верхнему регистру и возвращает ее в виде списка"""
    new_var = var.upper()
    return list(new_var.split())


new_var_list = []
while True:
    print('Чтобы выйти введите - Q')
    my_list = up_list(var=input())
    if my_list.count('Q') > 0:
        my_list.remove('Q')
        print(update(var_list=my_list))
        break
    else:
        print(update(var_list=my_list))
