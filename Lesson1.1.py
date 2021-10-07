name = input('Введите ваше имя: ')
year = int(input('Какого вы года рождения? '))

age = 2021 - year
answer = input('У вас было день рождение в этом году? (Y or N): ')
if answer == 'Y':
    last_answer = input(f'{name}, вам сейчас {age}? (Y or N): ')
    if last_answer == 'Y':
        print('Хорошо. Значит код работает!')
    else:
        print('Значит, что-то сломалось...')

else:
    age = age - 1
    last_answer = input(f'{name}, вам сейчас {age}? (Y or N): ')
    if last_answer == 'Y':
        print('Хорошо. Значит код работает!')
    else:
        print('Значит, что-то сломалось...')
