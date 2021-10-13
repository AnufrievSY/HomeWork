def check_lng(value):
    """Функция проверяет введены ли латинские символы,
    если нет, то выдает предупреждение о том, что не обходимо вводить именно их"""
    for i in list(value):
        if 97 <= ord(i) <= 122:
            return True
        else:
            return False


def check_rgs(value):
    """Функция проверяет в каком регистре полученные символы
    и если в верхнем, то меняет на нижний"""
    if value.islower():
        return value
    else:
        return value.lower()


def int_func(value):
    """Функция делает так, чтобы каждое введенное слово начиналось с заглавной буквы"""
    return value.title()


print('Чтобы выйти введите - Q')
while True:
    var = input('Ваше слово: ')
    if var == 'q':
        break
    else:
        """проверка регистра"""
        var = check_rgs(value=var)
        """проверка языка ввода"""
        if check_lng(value=var):
            """результат"""
            print(int_func(value=var))
        else:
            """предупреждение"""
            print('Слово должно состоять из латинский букв!')
            continue
