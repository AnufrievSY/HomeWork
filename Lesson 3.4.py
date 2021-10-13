def func(x, y):
    z = x
    for i in range(y - 1):
        z *= x
    z = 1 / z
    return z


var_x = float(input('Ваше число: '))
var_y = int(input('Ваша отрицательная степень: '))
var_z = func(x=var_x, y=abs(var_y))
print(f'{var_x} в степени {var_y} = {var_z}')
