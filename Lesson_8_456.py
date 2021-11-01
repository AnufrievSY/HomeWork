class Warehouse:
    def __init__(self, item):
        self.base = dict(item)

    def accepted(self, name, value):
        try:
            int(value[0])
        except ValueError:
            Error.not_number()
        else:
            base = {name: value}
            self.base.update(base)
            return self.base

    def sent(self, name, value):
        try:
            int(value)
        except ValueError:
            Error.not_number()
        else:
            update = self.base.pop(name)
            old_value = int(update[0])
            new_value = int(value)
            if old_value > 1:
                old_value -= new_value
                self.base.update({name: [old_value, update[1]]})
                return self.base
            else:
                return self.base


class OfficeEquipment:
    def __init__(self, old, name, value):
        self.old_item = old
        self.name = name
        self.value = value

    def accepted(self):
        return Warehouse(self.old_item).accepted(self.name, self.value)

    def sent(self):
        return Warehouse(self.old_item).sent(self.name, self.value)


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass


class Error(Exception):
    @staticmethod
    def unknown_command():
        print('неизвестная команда')

    @staticmethod
    def not_number():
        print('вы ввелли не число')

    @staticmethod
    def unknown_category():
        print('такой категории не существует')


printer = {}
scanner = {}
copier = {}

while True:
    command = input('"q" - выйти\n'
                    '"a" - добавить\n'
                    '"s" - отправить\n')
    if command == 'q':
        break
    elif command == 'a':
        x = input('категория, название, колличество, уникальное значение 1, уникальное значение 2\n')
        x = x.split(', ')
        try:
            if x[0] == 'printer':
                printer = Printer(printer, x[1], [x[2], x[3: 5]]).accepted()
                print(printer)
            elif x[0] == 'scanner':
                scanner = Scanner(scanner, x[1], [x[2], x[3: 5]]).accepted()
                print(scanner)
            elif x[0] == 'copier':
                copier = Copier(copier, x[1], [x[2], x[3: 5]]).accepted()
                print(copier)
            else:
                raise Error.unknown_category()
        except TypeError:
            raise Error.unknown_command()
    elif command == 's':
        x = input('категория, название, колличество\n')
        x = x.split(', ')
        try:
            if x[0] == 'printer':
                printer = Printer(printer, x[1], x[2]).sent()
                print(printer)
            elif x[0] == 'scanner':
                scanner = Scanner(scanner, x[1], x[2]).sent()
                print(scanner)
            elif x[0] == 'copier':
                copier = Copier(copier, x[1], x[2]).sent()
                print(copier)
            else:
                raise Error.unknown_category()
        except TypeError:
            raise Error.unknown_command()
    else:
        raise Error.unknown_command()
