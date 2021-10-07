start = int(input('Ваш текущий результат: '))
result = int(input('Результат, к которому вы стремитесь: '))
day = 1


while result > start:
    if start == 0:
        print('Простите, но вы сейчас слишком слабы...')
        start = int(input('Введите другой результат: '))
    else:
        day += 1
        start += start * 0.1

if day == 1:
    print('Вы уже достигли результата')
else:
    print(f'Вы достигните результата через {day} дней.')
