time = int(input('введите число: '))

hours = time // 3600
if hours < 10:
    hours = f'0{hours}'
minutes = time % 3600 // 60
if minutes < 10:
    minutes = f'0{minutes}'
seconds = time % 3600 % 60
if seconds < 10:
    seconds = f'0{seconds}'

print(f'{hours}:{minutes}:{seconds}')
