class Err(Exception):
    @staticmethod
    def value():
        return 'Error: деление на ноль'


while True:
    a = input('Выйти - "q"\n')
    if a == 'q':
        break
    else:
        a = int(a)
        b = int(input())
        try:
            if b == 0:
                raise Err
        except Err:
            print(Err.value())
        else:
            print(a / b)
