def zero(var_1, var_2):
    """Добавляем обработку ситуации, в которой пользователь пытается поделить на ноль."""
    try:
        var_1 / var_2
    except ZeroDivisionError:
        return print('нельзя делить на ноль')


a = int(input('Первое число: '))
b = int(input('Второе число: '))
zero(a, b)
if a % b != 0:
    print(a / b)
else:
    print(a // b)
