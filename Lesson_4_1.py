from sys import argv

name, output, rate, prize = argv

salary = (int(output) * int(rate)) + int(prize)

print(f'Зарплата сотрудника составила - {salary}:')
print(f'- Сотрудник отработал {output} часов.')
print(f'- Ставка сотрудника в час - {rate}.')
print(f'- Премия сотрудника - {prize}.')

