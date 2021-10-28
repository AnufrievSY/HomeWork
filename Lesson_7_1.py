from random import randint


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for x in self.my_list:
            for y in x:
                print(f"{y:4}", end="")
            print()
        return ''

    def __add__(self, add_list):
        new_list = [[sum(a) for a in list(zip(self.my_list[i], add_list[i]))] for i in range(3)]
        return Matrix(new_list)


a_list = [[randint(-10, 0) for x in range(3)] for y in range(3)]
print(f'Первый список: {a_list}')
b_list = [[randint(0, 10) for z in range(3)] for w in range(3)]
print(f'Второй список: {b_list}')
print(Matrix(a_list).__add__(b_list))


