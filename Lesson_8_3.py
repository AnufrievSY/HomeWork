class Err(Exception):
    @staticmethod
    def error():
        return 'вы ввели недопустимое значение\n' \
               'оно не был добавлен в итоговый список'


my_list = []
while True:
    x = input('"q" - выйти\n'
              '"s" - печать списка\n')
    if x == 'q':
        break
    elif x == 's':
        for i in my_list:
            print(i, end=' ')
        break
    else:
        try:
            int(x)
        except:
            print(Err.error())
            print(''.join(['-' for x in range(100)]))
        else:
            my_list.append(x)

