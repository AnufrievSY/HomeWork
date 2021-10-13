def var_func(*args):
    print(sum(args)-min(args))


var_1 = int(input('Введите первое число: '))
var_2 = int(input('Введите второе число: '))
var_3 = int(input('Введите третье число: '))
var_func(var_1, var_2, var_3)
